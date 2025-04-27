# secure-notes/app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import services, database, models
from app.database import get_db

app = FastAPI()

# Create database tables (only runs once at startup)
models.Base.metadata.create_all(bind=database.engine)

@app.post("/notes")
def create_note(title: str, content: str, db: Session = Depends(get_db)):
    note_service = services.NoteService(db)
    note = note_service.create_note(title, content)
    return note

@app.get("/notes/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)):
    note_service = services.NoteService(db)
    note = note_service.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.put("/notes/{note_id}")
def update_note(note_id: int, title: str = None, content: str = None, db: Session = Depends(get_db)):
    note_service = services.NoteService(db)
    note = note_service.update_note(note_id, title, content)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note_service = services.NoteService(db)
    note = note_service.delete_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted"}
