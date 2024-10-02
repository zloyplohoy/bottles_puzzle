from collections import deque
from .constants import BOTTLE_SIZE
from .color import Color

class Bottle(deque):

    @property
    def is_empty(self) -> bool:
        return len(self) == 0

    @property
    def is_full(self) -> bool:
        return len(self) == BOTTLE_SIZE

    @property
    def is_single_color(self) -> bool:
        return len(set(self)) == 1

    @property
    def is_complete(self) -> bool:
        return self.is_full and self.is_single_color

    @property
    def top_color(self) -> Color:
        return self[-1] if self else None

    @property
    def source_capacity(self) -> int:
        if self.is_empty:
            return 0

        capacity = 0

        for color in reversed(self):
            if color == self.top_color:
                capacity += 1
            else:
                break
        return capacity

    @property
    def target_capacity(self) -> int:
        return BOTTLE_SIZE - len(self)

    def __repr__(self) -> str:
        return f'Bottle({', '.join(map(str, self))})'
