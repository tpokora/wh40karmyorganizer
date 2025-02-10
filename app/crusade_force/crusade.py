import logging

from app.crusade_force.model import Crusade, CrusadeFieldValidationException
from app.crusade_force.models import CrusadeForce
from app.database import db


class CrusadeExistException(CrusadeFieldValidationException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class CrusadeService:

    def save(self, crusade: Crusade) -> Crusade:
        self.__crusade_exists(crusade)
        new_crusade_force = CrusadeForce(
            name=crusade.crusade_force,
            faction=crusade.faction,
            supply_limit=crusade.supply_limit
        )
        db.session.add(new_crusade_force)
        db.session.commit()

        crusade.crusade_id = new_crusade_force.id
        logging.info(f'Saved {crusade.crusade_force}')
        return crusade

    def get_all(self) -> list[Crusade]:
        logging.info('Get all Crusade forces...')
        crusade_forces = CrusadeForce.query.all()
        return [self.__convert_to_crusade(_) for _ in crusade_forces]

    def get_by_id(self, _id: str) -> Crusade:
        logging.info(f'Get crusade force by id {_id}...')
        crusade_force = CrusadeForce.query.get(_id)
        if not crusade_force:
            raise ValueError(f"Crusade force with id '{_id}' does not exist")
        return self.__convert_to_crusade(crusade_force)

    def find_all_by_name(self, name) -> list[Crusade]:
        crusade_forces = CrusadeForce.query.filter(CrusadeForce.name.ilike(f'%{name}%')).all()
        return [self.__convert_to_crusade(_) for _ in crusade_forces]

    @staticmethod
    def __crusade_exists(crusade: Crusade):
        existing_crusade = CrusadeForce.query.filter_by(name=crusade.crusade_force).first()
        if existing_crusade:
            raise CrusadeExistException(f"Crusade force '{crusade.crusade_force}' exists")

    @staticmethod
    def __convert_to_crusade(crusade_force: CrusadeForce) -> Crusade:
        return Crusade(
            crusade_force=crusade_force.name,
            faction=crusade_force.faction,
            supply_limit=crusade_force.supply_limit,
            crusade_id=crusade_force.id
        )
