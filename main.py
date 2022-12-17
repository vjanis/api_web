import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "api_web darbojas"}


@app.get("/api/iin_sadale/", response_model=list[schemas.Sadale])
def read_users(db: Session = Depends(get_db)):
    iin_sadale = crud.get_iin(db)
    return iin_sadale


@app.get("/api/iin_sadale/{gads}", response_model=list[schemas.Sadale])
def read_user(gads: str, db: Session = Depends(get_db)):
    gadss = crud.get_user_gads(db, gads=gads)
    if gadss is None:
        raise HTTPException(status_code=404, detail="Gads nav atrasts")
    return gadss


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

