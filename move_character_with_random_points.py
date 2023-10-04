from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()


def draw_big_point(p):
    mouse.draw(x,y)
    pass

def draw_point(p):
    frame = 0
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8


def move_character(p1, p2):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

        draw_big_point(p1)
        draw_big_point(p2)

        a = (y2 - y1) / (x2 - x1)
        b = y1 - x1 * a
        for j in range(0, 100+1, 4):
            t = j / 100
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2
            draw_point((x,y))

        draw_point(p2)
        draw_point((x2,y2))
        pass



points = [[random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)] for i in range(10)]

for i in range(0,len(points)-1):
    move_character(points[i], points[i+1])
move_character(points[-1],points[0])

close_canvas()