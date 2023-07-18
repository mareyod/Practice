import pygame
import random
import pygame_menu
import sys
pygame.init()

SIZE_BLOCK = 50
COUNT_BLOCKS = 10
FRAME_MARGIN = SIZE_BLOCK * 3
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_GREEN = (185, 232, 181)
GREEN = (200, 242, 196)
FRAME_COLOR = (10, 115, 0)
SNAKE_COLOR = (10, 115, 0)
MAX_TOTAL = 0


SIZE = [SIZE_BLOCK*COUNT_BLOCKS + SIZE_BLOCK * 2,
        SIZE_BLOCK*COUNT_BLOCKS + SIZE_BLOCK + FRAME_MARGIN]

apple_size = ((SIZE_BLOCK * 2) * 2000 // 2775, SIZE_BLOCK * 2)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Змейка')
fps = pygame.time.Clock()
font_size = SIZE_BLOCK // 4 * 3
font_main = pygame.font.SysFont('Segoe UI', font_size)
font_gameover = pygame.font.SysFont('Segoe UI', font_size // 2, bold=True)


def show_start_menu():
    start_menu = pygame_menu.Menu(width=SIZE[0], height=SIZE[1], title='Игра Змейка', theme=pygame_menu.themes.THEME_GREEN)
    start_menu.add.button("Играть", game)
    start_menu.add.button("Выход", pygame_menu.events.EXIT)
    start_menu.mainloop(screen)


def show_gameover_menu(total):
    while True:
        pygame.draw.rect(screen, LIGHT_GREEN, (SIZE_BLOCK, FRAME_MARGIN, COUNT_BLOCKS * SIZE_BLOCK, COUNT_BLOCKS * SIZE_BLOCK))
        text_gameover1 = font_gameover.render("Игра закончена", True, FRAME_COLOR)
        text_gameover2 = font_gameover.render("Нажмите Q для завершения сеанса", True, FRAME_COLOR)
        text_gameover3 = font_gameover.render("или N для запуска нового сеанса", True, FRAME_COLOR)
        gameover_rect1 = text_gameover1.get_rect()
        gameover_rect2 = text_gameover2.get_rect()
        gameover_rect3 = text_gameover3.get_rect()
        gameover_rect1.midtop = (SIZE[0] // 2, SIZE[1] // 2 - gameover_rect1.height)
        gameover_rect2.midtop = (SIZE[0] // 2, SIZE[1] // 2)
        gameover_rect3.midtop = (SIZE[0] // 2, SIZE[1] // 2 + gameover_rect2.height)
        screen.blit(text_gameover1, gameover_rect1)
        screen.blit(text_gameover2, gameover_rect2)
        screen.blit(text_gameover3, gameover_rect3)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_n:
                    game()


def show_statistics(total, speed):
    apple_image = pygame.image.load('apple.png')
    apple_image = pygame.transform.scale(apple_image, apple_size)

    text_total = font_main.render(f"{total}", 1, WHITE)
    text_speed = font_main.render(f"Скорость:{speed}", 1, WHITE)
    text_maxtotal = font_main.render(f"Рекорд:{MAX_TOTAL}", 1, WHITE)

    screen.blit(apple_image, (SIZE_BLOCK, FRAME_MARGIN - apple_size[1] - SIZE_BLOCK))
    screen.blit(text_total, (SIZE_BLOCK + apple_size[0], FRAME_MARGIN - text_total.get_height() - SIZE_BLOCK))
    screen.blit(text_speed, (SIZE[0] - SIZE_BLOCK * 2 - text_maxtotal.get_width() - text_speed.get_width(), FRAME_MARGIN - text_speed.get_height() - SIZE_BLOCK))
    screen.blit(text_maxtotal, (SIZE[0] - SIZE_BLOCK - text_maxtotal.get_width(), FRAME_MARGIN - text_maxtotal.get_height() - SIZE_BLOCK))


def draw_block(color, row, column, radius):
    pygame.draw.rect(screen, color,
                     (SIZE_BLOCK + column * SIZE_BLOCK,
                      FRAME_MARGIN + row * SIZE_BLOCK,
                      SIZE_BLOCK,
                      SIZE_BLOCK), border_radius=radius)


def draw_apple(row, column):
    apple_image = pygame.image.load('apple_mini.png')
    apple_image = pygame.transform.scale(apple_image, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(apple_image, (SIZE_BLOCK + column * SIZE_BLOCK, FRAME_MARGIN + row * SIZE_BLOCK))


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def game():
    global MAX_TOTAL

    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_body:
            empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
        return empty_block

    snake_body = [SnakeBlock(0, 0)]
    apple = get_random_empty_block()
    d_row = 0
    d_col = 1
    total = 0
    speed = 1

    while True:

        screen.fill(FRAME_COLOR)
        show_statistics(total, speed)

        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = GREEN
                else:
                    color = LIGHT_GREEN
                draw_block(color, row, column, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1

        head = snake_body[-1]

        if not head.is_inside():
            show_gameover_menu(total)

        draw_apple(apple.x, apple.y)

        for block in snake_body:
            draw_block(SNAKE_COLOR, block.x, block.y, 7)

        if apple == head and len(snake_body) < 60:
            total += 1
            if total > MAX_TOTAL:
                MAX_TOTAL = total
            speed = total // 3 + 1
            snake_body.append(apple)
            apple = get_random_empty_block()

        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_body:
            show_gameover_menu(total)

        snake_body.append(new_head)
        snake_body.pop(0)
        pygame.display.flip()
        fps.tick(3+speed)


show_start_menu()
