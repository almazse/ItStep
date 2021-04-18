import pygame
import random
import sys

from pygame.locals import *

from constans import *


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    mouse_x = 0
    mouse_y = 0

    pygame.display.set_caption("Memory Game")
    main_board = get_randomized_board()
    revealed_boxes = generate_revealed_boxed_data(False)
    first_selection = None
    DISPLAYSURF.fill(BG_COLOR)
    start_game_animation(main_board)

    while True:
        mouse_clicked = False
        DISPLAYSURF.fill(BG_COLOR)
        draw_board(main_board, revealed_boxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                mouse_clicked = True

        box_x, box_y = get_box_at_pixel(mouse_x, mouse_y)
        if box_x is not None and box_y is not None:
            if not revealed_boxes[box_x][box_y]:
                draw_highlight_box(box_x, box_y)
            if not revealed_boxes[box_x][box_y] and mouse_clicked:
                reveal_boxes_animation(main_board, [(box_x, box_y)])
                revealed_boxes[box_x][box_y] = True
                if first_selection is None:
                    first_selection = (box_x, box_y)
                else:
                    icon_first_shape, icon_first_color = get_shape_and_color(main_board,
                                                                             first_selection[0],
                                                                             first_selection[1])
                    icon_second_shape, icon_second_color = get_shape_and_color(main_board,
                                                                             box_x,
                                                                             box_y)
                    if icon_first_shape != icon_second_shape or icon_first_color != icon_second_color:
                        pygame.time.wait(1000)
                        cover_boxes_animation(main_board, [(first_selection[0], first_selection[1]),
                                                           (box_x, box_y)])
                        revealed_boxes[first_selection[0]][first_selection[1]] = False
                        revealed_boxes[box_x][box_y] = False
                    if has_won(revealed_boxes):
                        game_won_animation(main_board)
                        pygame.time.wait(2000)
                        main_board = get_randomized_board()
                        revealed_boxes = generate_revealed_boxed_data(False)

                        draw_board(main_board, revealed_boxes)
                        pygame.display.update()
                        pygame.time.wait()
                        start_game_animation(main_board)
                    first_selection = None


def generate_revealed_boxed_data(val):
    revealed_boxes = []
    for i in range(BOARD_WIDTH):
        revealed_boxes.append([val] * BOARD_HEIGHT)
    return revealed_boxes


def get_randomized_board():
    icons = []
    board = []

    for color in ALL_COLORS:
        for shape in ALL_SHAPES:
            icons.append((shape, color))
    random.shuffle((icons))
    num_icons_used = int(BOARD_WIDTH * BOARD_HEIGHT / 2)
    icons = icons[:num_icons_used] * 2
    random.shuffle(icons)

    for x in range(BOARD_WIDTH):
        column = []
        for y in range(BOARD_HEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)

    return board


def split_into_groups(group_size, groups):
    result = []
    for i in range(0, len(groups), group_size):
        result.append(groups[i:i+group_size])
    return result


def left_coords_of_box(box_x, box_y):
    left = box_x * (BOX_SIZE + GAP_SIZE) + X_MARGIN
    top = box_y *  (BOX_SIZE + GAP_SIZE) + Y_MARGIN
    return (left, top)


def get_box_at_pixel(x, y):
    for box_x in range(BOARD_WIDTH):
        for box_y in range(BOARD_HEIGHT):
            left, top = left_coords_of_box(box_x, box_y)
            box_rect = pygame.Rect()
    return (None, None)


def draw_icon(shape, color, box_x, box_y):
    quarter = int(BOX_SIZE * 0.25)
    half = int(BOX_SIZE * 0.5)
    left, top = left_coords_of_box(box_x, box_y)
    if shape == DONNUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half -5)
        pygame.draw.circle(DISPLAYSURF, BG_COLOR, (left + half, top + half), quarter -5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter,
                                              BOX_SIZE - half, BOX_SIZE- half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOX_SIZE - 1,
                                                                      top * half),
                                                 (left + half, top + BOX_SIZE),
                                                 (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOX_SIZE, 4):
            pygame.draw.lines(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.lines(DISPLAYSURF, color, (left + i, top + BOX_SIZE - 1), (left + BOX_SIZE - 1, top + i))
    elif shape == OVAL:
        # pygame.draw.oval(DISPLAYSURF, color)
        pass


def get_shape_and_color(board, box_x, box_y):
    return board[box_x][box_y][0], board[box_x][box_y][1]


def draw_box_covers(board, boxes, coverage):
    for box in boxes:
        left, top = left_coords_of_box(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BG_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
        shape, color = get_shape_and_color(board, box[0], box[1])
        draw_icon(shape, color, box[0], box[1])
        if coverage > 0:
            pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, coverage, BOX_SIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def reveal_boxes_animation(board, boxes_to_reveal):
    for coverage in range(BOX_SIZE, (-REVEAL_SPEED) - 1, -REVEAL_SPEED):
        draw_box_covers(board, boxes_to_reveal, coverage)


def cover_boxes_animation(board, boxes_to_cover):
    for coverage in range(0, BOX_SIZE + REVEAL_SPEED, REVEAL_SPEED):
        draw_box_covers(board, boxes_to_cover, coverage)


def draw_board(board, revealed):
    for box_x in range(BOARD_WIDTH):
        for box_y in range(BOARD_HEIGHT):
            left, top = left_coords_of_box(box_x, box_y)
            if not revealed[box_x][box_y]:
                pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
            else:
                shape, color = get_shape_and_color(board, box_x, box_y)
                draw_icon(shape, color, box_x, box_y)


def draw_highlight_box(box_x, box_y):
    left, top = left_coords_of_box(box_x, box_y)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHT_COLOR, (left - 5, top - 5, BOX_SIZE + 10, BOX_SIZE + 10), 4)


def start_game_animation(board):
    covered_boxes = generate_revealed_boxed_data(False)
    boxes = []
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    box_groups = split_into_groups(8, boxes)

    draw_board(board, covered_boxes)
    for box_group in box_groups:
        reveal_boxes_animation(board, box_group)
        cover_boxes_animation(board, box_group)


def game_won_animation():
    covered_boxes = generate_revealed_boxed_data(True)
    color_first = LIGHT_BG_COLOR
    color_second = BG_COLOR

    for i in range(13):
        color_first, color_second = color_second, color_first
        DISPLAYSURF.fill(color_first)
        draw_board(board, covered_boxes)
        pygame.display.update()
        pygame.time.wait(300)


def has_won():
    pass


if __name__ == '__main__':
    main()