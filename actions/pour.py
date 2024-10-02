from entities import BOTTLE_SIZE, Bottle

def pour(source: Bottle, target: Bottle, test: bool = False) -> bool:

    '''
    Does not cover redundant partial pours to allow for pours when the top color
    can be spread across two bottles of capacity 1.
    '''

    def is_color_mismatch(source: Bottle, target: Bottle):
        return target.top_color and source.top_color != target.top_color

    def is_single_color_move(source: Bottle, target: Bottle):
        return target.is_empty and source.is_single_color

    def is_inefficient_pour(source: Bottle, target: Bottle):
        return all ([
            source.is_single_color,
            source.source_capacity > target.source_capacity,
            source.source_capacity + target.source_capacity == BOTTLE_SIZE
        ])

    if any([
        source.is_empty,
        target.is_full,
        source.is_complete,
        is_color_mismatch(source, target),
        is_single_color_move(source, target),
        is_inefficient_pour(source, target)
    ]):
        return False

    pour_volume = min(source.source_capacity, target.target_capacity)

    if not test:
        for _ in range(pour_volume):
            target.append(source.pop())

    return True
