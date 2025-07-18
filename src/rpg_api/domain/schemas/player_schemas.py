from decimal import Decimal

from pydantic import BaseModel


class PlayerCreateRequest(BaseModel):
    name: str


class PlayerCreateResponse(BaseModel):
    name: str
    energy: int
    productivity: float
    money: Decimal
    network: Decimal
