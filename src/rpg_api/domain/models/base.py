from typing import Any

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def as_dict(self) -> dict[str, Any]:
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }

    pass
