from sqlalchemy import (Column, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship

from .setup_postgres import Base


class Singer(Base):
    name = Column(String)
    nick_name = Column(String)
    birthday = Column(String)
    address = Column(String)
    songs = relationship("Song", cascade="delete", backref="singer")


class Song(Base):
    name = Column(String)
    singer_id = Column(Integer, ForeignKey("Singers.singer_id", ondelete="CASCADE"))
