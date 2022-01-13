from hexagonalPosition import HexagonalPosition


hex_pos_1 = HexagonalPosition(0, 2, 0)
hex_pos_2 = HexagonalPosition(-2, 0, -2)

print("First point position {}".format(hex_pos_1.to_cartesian_position()))
print("Second point position {}".format(hex_pos_2.to_cartesian_position()))

print("Are positions equal: {}".format(hex_pos_1 == hex_pos_2))


