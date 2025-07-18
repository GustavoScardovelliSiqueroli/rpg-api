from rpg_api.config import get_settings
from rpg_api.domain.models.game_state import GameState
from rpg_api.domain.models.player import Player
from rpg_api.domain.repositories.game_state_repository import (
    GameStateRepository,
)
from rpg_api.domain.repositories.player_repository import PlayerRepository
from rpg_api.domain.schemas.player_schemas import (
    PlayerCreateRequest,
    PlayerCreateResponse,
)


class PlayerService:
    def __init__(
        self,
        player_repository: PlayerRepository,
        game_state_repository: GameStateRepository,
    ) -> None:
        self.player_repository = player_repository
        self.game_state_repository = game_state_repository

    def create_player(
        self, player_data: PlayerCreateRequest
    ) -> PlayerCreateResponse:
        settings = get_settings()
        game_state = GameState(
            id_currente_room=None,
            current_day=settings.START_DAY,
            current_hour=settings.START_HOUR,
        )
        game_state = self.game_state_repository.create(game_state)

        player = Player(
            id_game_state=game_state.id_game_state,
            name=player_data.name,
            productivity=settings.START_PRODUCTIVITY,
            energy=settings.START_ENERGY,
            money=settings.START_MONEY,
            network=settings.START_NETWORK,
        )
        player = self.player_repository.create(player)
        return PlayerCreateResponse(
            name=player.name,
            energy=player.energy,
            productivity=player.productivity,
            money=player.money,
            network=player.network,
        )
