from sqlalchemy.orm import Session

import models


def get_iin(db: Session):
    return db.query(models.Sadale).all()


def get_user_gads(db: Session, gads: str):
    return db.query(models.Sadale).filter(models.Sadale.gads == gads).all()
