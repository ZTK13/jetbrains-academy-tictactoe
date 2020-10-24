triangle_height = int(input())

triangle_width = 2 * triangle_height - 1

for i in range(triangle_height):
    n_hashes = 2 * (i + 1) - 1
    n_spaces = triangle_width - n_hashes
    print((' ' * int(n_spaces / 2)) + ('#' * n_hashes) + (' ' * int(n_spaces / 2)))
