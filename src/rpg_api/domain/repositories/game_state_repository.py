from typing import Protocol

from rpg_api.domain.models.game_state import GameState


class GameStateRepository(Protocol):
    def get_by_id(self, id_game_state: int) -> GameState: ...
    def create(self, data: GameState) -> GameState: ...
