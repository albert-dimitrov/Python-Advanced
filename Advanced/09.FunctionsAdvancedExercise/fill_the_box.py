from collections import deque


def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    cubes = deque(args)

    while cubes[0] != 'Finish':
        box_volume -= cubes.popleft()

        if box_volume < 0:
            cubes_left = sum(c for c in cubes if c != 'Finish')
            return f"No more free space! You have {cubes_left + abs(box_volume)} more cubes."

    return f"There is free space in the box. You could put {box_volume} more cubes."



# def fill_the_box(height, length, width, *args):
#     box_volume = height * length * width
#     filled_cubes = 0
#     cubes_cannot_go_in = 0
#
#     for el in args:
#         if el == 'Finish':
#             break
#
#         cubes_space = el * 1
#
#         if box_volume - cubes_space >= 0:
#             box_volume -= cubes_space
#             filled_cubes += cubes_space
#         else:
#             cubes_that_can_fit = box_volume
#             box_volume -= cubes_that_can_fit
#             cubes_space -= cubes_that_can_fit
#             cubes_cannot_go_in += cubes_space
#
#     if cubes_cannot_go_in:
#         return f"No more free space! You have {cubes_cannot_go_in} more cubes."
#     else:
#         return f"There is free space in the box. You could put {box_volume} more cubes."
