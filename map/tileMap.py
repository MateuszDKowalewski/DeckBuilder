from geometry.hexagonalPosition import HexagonalPosition


def prepare_hexagonal_net(side_length):
    points = []
    u = 0
    v = 0
    w = 0
    step = 0
    points.append(HexagonalPosition(0, 0, 0))
    for i in range(0, side_length):
        for j in range(0, 6):
            for k in range(0, step):
                points.append((HexagonalPosition(u, v, w)))
                new_positon = {
                    0: (u, v + 1, w),
                    1: (u - 1, v, w),
                    2: (u, v, w + 1),
                    3: (u, v - 1, w),
                    4: (u + 1, v, w),
                    5: (u, v, w - 1)
                }
                (u, v, w) = new_positon.get(j)
        step += 1
    return points