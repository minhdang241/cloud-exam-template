from typing import List, Optional

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from app.db.postgres import models
from .crud_base import CRUDBase


class Song(BaseModel):
    name: str

class SingerCreate(BaseModel):
    name: str
    nick_name: str
    birth_day: str
    address: str
    songs: Optional[List[Song]]

class SingerUpdate(BaseModel):
    name: str
    nick_name: str
    birth_day: str
    address: str
    songs: Optional[List[Song]]


class CRUDSinger(CRUDBase[models.Singer, SingerCreate, SingerUpdate]):
    pass

singer = CRUDSinger(models.Singer)
