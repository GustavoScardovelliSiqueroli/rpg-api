from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from rpg_api.domain.models.base import Base


class Player(Base):
    id_player: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
