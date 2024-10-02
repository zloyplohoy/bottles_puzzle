from .bottle import Bottle


class Board(list[Bottle]):

    @property
    def is_complete(self):
        return all(bottle.is_empty or bottle.is_complete for bottle in self)

    @property
    def as_hashable(self):
        return tuple(tuple(bottle) for bottle in self)
