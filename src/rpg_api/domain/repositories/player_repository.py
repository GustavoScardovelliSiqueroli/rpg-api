from typing import Protocol

from rpg_api.domain.schemas.player_schemas import PlayerCreateRequest


class PlayerRepository(Protocol):
    def get_by_name(self, name: str): ...
    def create(self, player: PlayerCreateRequest): ...
