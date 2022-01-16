from gemeConsts import SCALE, X_OFFSET, Y_OFFSET


def game_to_screen_coordinates(points):
    new_points = []
    for point in points:
        new_points.append((game_to_screen_coordinate(point[0], point[1])))
    return new_points


def game_to_screen_coordinate(game_x, game_y):
    screen_x = game_x * SCALE + X_OFFSET
    screen_y = - game_y * SCALE + Y_OFFSET
    return screen_x, screen_y


def screen_to_game_coordinates(screen_x, screen_y):
    world_x = (screen_x - X_OFFSET) / SCALE
    world_y = - (screen_y - Y_OFFSET) / SCALE
    return world_x, world_y