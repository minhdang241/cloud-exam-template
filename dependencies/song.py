from sqlalchemy.orm import Session

from crud.crud_singer import singer


def get_singer_by_id(db: Session, id: int):
    return singer.get_by_id(db, id)
