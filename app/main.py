from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, auth, database


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Notes Management API")



@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    try:
        db_user = db.query(models.User).filter(models.User.email == user.email).first()

        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_pwd = auth.get_password_hash(user.password)

        new_user = models.User(
            email=user.email,
            hashed_password=hashed_pwd
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login", response_model=schemas.Token)
def login(user_credentials: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user or not auth.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}



@app.post("/notes", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    new_note = models.Note(**note.dict(), owner_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@app.get("/notes", response_model=List[schemas.NoteResponse])
def get_notes(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Note).filter(models.Note.owner_id == current_user.id).all()

@app.put("/notes/{note_id}", response_model=schemas.NoteResponse)
def update_note(note_id: int, updated_note: schemas.NoteCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    note_query = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id)
    note = note_query.first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_query.update(updated_note.dict(), synchronize_session=False)
    db.commit()
    return note_query.first()

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    note_query = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id)
    if not note_query.first():
        raise HTTPException(status_code=404, detail="Note not found")
    note_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Note deleted successfully"}