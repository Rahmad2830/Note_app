from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, login_user, logout_user, current_user
from app.models.Db_models import *
from app.forms.Forms import NoteForm, EditForm

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
  user_active = current_user
  data = Crud(session)
  user = data.read_by_id(User, 'id', user_active.id)
  notes = user.notes if user else []
  return render_template('index.html', user=user, notes=notes)
  
@main.route('/add_note', methods=['GET', 'POST'])
@login_required
def add_note():
  form=NoteForm()
  if form.validate_on_submit():
    content = form.note.data
    data = Crud(session)
    note = Notes(
        notes = content,
        user_id = current_user.id
      )
    add = data.add(note)
    if add > 0:
      flash('Catatan Berhasil Ditambahkan', 'success')
    else:
      flash('Catatan Gagal Ditambahkan', 'danger')
  return render_template('add.html', form=form)
  
@main.route('/note/<int:note_id>')
@login_required
def view_note(note_id):
  data = Crud(session)
  note = data.read_by_id(Notes, 'id', note_id)
  if note and note.user.id == current_user.id:
    return render_template('view.html', note=note)
  else:
    flash("Catatan tidak ditemukan", "danger")
    return redirect(url_for('main.index'))
    
@main.route('/delete/<int:note_id>', methods=['POST'])
@login_required
def delete(note_id):
  if request.method == 'POST':
    data = Crud(session)
    note = data.read_by_id(Notes, 'id', note_id)
    if note.user_id != current_user.id:
      abort(403)
    delete = data.delete(note)
    if delete > 0:
      flash('Catatan Berhasil Dihapus', 'success')
      return redirect(url_for('main.index'))
    else:
      flash('Gagal Menghapus Catatan', 'danger')
      return redirect(url_for('main.index'))
      
@main.route('/update/<int:note_id>', methods=['GET', 'POST'])
@login_required
def update(note_id):
  data = Crud(session)
  note = data.read_by_id(Notes, 'id', note_id)
  if note.user_id != current_user.id:
    abort(403)
  form = EditForm(obj=note)
  if form.validate_on_submit():
    note_edited = form.notes.data
    if note:
      note.notes = note_edited
      if data.update(note) > 0:
        flash("Sukses Edit Catatan", "success")
        return redirect(url_for('main.index'))
      else:
        flash("Gagal Edit Catatan", "danger")
        return redirect(url_for('main.index'))
  return render_template('edit.html', form=form)