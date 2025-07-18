from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rpg_api.domain.models.base import Base


class GameState(Base):
    __tablename__ = 'game_states'
    id_game_state: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_current_room: Mapped[int | None] = mapped_column(
        Integer, ForeignKey('room.id_room'), nullable=True
    )
    current_day: Mapped[int] = mapped_column(Integer, nullable=False)
    current_hour: Mapped[int] = mapped_column(Integer, nullable=False)

    current_room = relationship('Room')
