# secure-notes/tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes", params={"title": "Test Note", "content": "This is a test."})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test."
    assert "id" in data

def test_get_note():
    # First, create a note
    create_response = client.post("/notes", params={"title": "Another Note", "content": "More content"})
    note_id = create_response.json()["id"]

    # Then, retrieve it
    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == note_id
    assert data["title"] == "Another Note"
    assert data["content"] == "More content"

def test_update_note():
    # First, create a note
    create_response = client.post("/notes", params={"title": "Old Title", "content": "Old content"})
    note_id = create_response.json()["id"]

    # Update the note
    update_response = client.put(f"/notes/{note_id}", params={"title": "New Title", "content": "New content"})
    assert update_response.status_code == 200
    updated_note = update_response.json()
    assert updated_note["title"] == "New Title"
    assert updated_note["content"] == "New content"

def test_delete_note():
    # Create a note to delete
    create_response = client.post("/notes", params={"title": "Temp Note", "content": "Temp content"})
    note_id = create_response.json()["id"]

    # Delete the note
    delete_response = client.delete(f"/notes/{note_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"detail": "Note deleted"}

    # Confirm it's gone
    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 404
