# secure-notes/app/services.py

from sqlalchemy.orm import Session
from app import models
from datetime import datetime

class NoteService:
    def __init__(self, db: Session):
        self.db = db

    def create_note(self, title: str, content: str):
        note = models.Note(title=title, content=content, timestamp=datetime.utcnow())
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)  # Refresh to get the DB-assigned id
        return note

    def get_note(self, note_id: int):
        return self.db.query(models.Note).filter(models.Note.id == note_id).first()

    def update_note(self, note_id: int, title: str = None, content: str = None):
        note = self.db.query(models.Note).filter(models.Note.id == note_id).first()
        if not note:
            return None
        if title:
            note.title = title
        if content:
            note.content = content
        self.db.commit()
        self.db.refresh(note)
        return note

    def delete_note(self, note_id: int):
        note = self.db.query(models.Note).filter(models.Note.id == note_id).first()
        if not note:
            return None
        self.db.delete(note)
        self.db.commit()
        return note
