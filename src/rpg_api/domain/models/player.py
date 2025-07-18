from decimal import Decimal

from sqlalchemy import Float, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rpg_api.domain.models.base import Base


class Player(Base):
    __tablename__ = 'players'
    id_player: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_game_state: Mapped[int] = mapped_column(
        Integer, ForeignKey('game_state.id_game_state'), nullable=False
    )

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    productivity: Mapped[float] = mapped_column(Float, nullable=False)
    energy: Mapped[int] = mapped_column(Integer, nullable=False)

    money: Mapped[Decimal] = mapped_column(
        Numeric(precision=15, scale=2), nullable=False
    )
    network: Mapped[Decimal] = mapped_column(
        Numeric(precision=15, scale=2), nullable=False
    )

    game_state = relationship('GameState')
