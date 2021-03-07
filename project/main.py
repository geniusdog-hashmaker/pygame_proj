import pygame
import random

# Задаём необходимые константы
CELLS_COUNT = 4
CELL_SIZE = 100
MARGIN = 5
WIDTH, HEIGHT = 425, 425

# Константы цветов
COLORS = {2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46)}

SCREEN_COLOR = (215, 189, 140)

# Это наше поле в виде списка
mapa = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


# Функция для отрисовки поля
def render(screen):
    for i in range(HEIGHT):
        for j in range(WIDTH):

            # Отрисовываем наши клеточки
            pygame.draw.rect(screen, (170, 170, 170),
                             (MARGIN * (j + 1) + CELL_SIZE * j,
                              MARGIN * (i + 1) + CELL_SIZE * i,
                              CELL_SIZE, CELL_SIZE))


# Функция для заливки наших клеточек цветом и записи чисел
def filling_cells(screen, mapa, x, y, place):

    # Закрашиваем клеточки
    if cell_number(x, y) not in place:
        pygame.draw.rect(screen, COLORS.get(mapa[x][y]),
                         (MARGIN * (y + 1) + CELL_SIZE * y,
                          MARGIN * (x + 1) + CELL_SIZE * x,
                          CELL_SIZE, CELL_SIZE))
    else:
        pygame.draw.rect(screen, (170, 170, 170),
                         (MARGIN * (y + 1) + CELL_SIZE * y,
                          MARGIN * (x + 1) + CELL_SIZE * x,
                          CELL_SIZE, CELL_SIZE))


# Функции для болеее удобного вывода в консоль:
# Эта - выводит состояние карты
def pprint(mapa):
    print('-' * 10)
    for line in mapa:
        print(*line)
    print('-' * 10)


# Эта - ищет на карте свободное место
def get_free_place(mapa):
    place = []
    for x in range(CELLS_COUNT):
        for y in range(CELLS_COUNT):
            if mapa[x][y] == 0:
                number = cell_number(x, y)
                place.append(number)
    return place


# Здесь мы осуществляем более удобную для человека индексацию
def cell_number(x, y):
    return x * 4 + y + 1


def cell_index(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def getting_start_nums(mapa, x, y):
    val = random.choice([2, 2, 2, 2, 2, 2, 2, 4, 4, 4])
    mapa[x][y] = val
    return mapa


# Эта функция отвечает за стартовый экран,
# где будет написано привествие и обучение
def main_screen():

    # Список с фразами обучения управлению
    tutor = ['"W": to move up;', '"S": to move down;', '"A": to move left;',
             '"D": to move right', 'Press "Space" to start']

    # Заливаем эран, задаём шрифт и здороваемся
    screen.fill(SCREEN_COLOR)
    font = pygame.font.Font(None, 50)
    text = font.render("Welcome to 2048", True, (0, 0, 0))
    text_x = WIDTH // 2 - text.get_width() // 2
    text_y = HEIGHT // 2 - text.get_height() * 3
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 10,
                                         text_w + 20, text_h + 20), 1)

    # Выводим на экран обучение
    font1 = pygame.font.Font(None, 30)
    for elem in range(len(tutor)):
        text1 = font1.render(tutor[elem],
                             True, (0, 0, 0))
        text_x1 = WIDTH // 2 - text1.get_width() // 2
        text_y1 = HEIGHT // 2 + text.get_height() * elem
        if elem < 4:
            screen.blit(text1, (text_x1, text_y1))
        else:
            screen.blit(text1, (text_x1, text_y1 + 30))


if __name__ == '__main__':

    # Инициализируем пайгейм, создаём окно и пишем заголовок
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('2048')
    clock = pygame.time.Clock()
    running = True

    # Эта переменная нужно, чтобы понять, надо ли изменять поле
    started = None

    # Вызываем функцию для отрисовки начального экрана
    main_screen()
    pygame.display.flip()

    # Начинаем игровой цикл
    while running:
        for event in pygame.event.get():

            # Проверяем, чем является наше действие
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not started:

                    # Отрисовываем наше поле
                    screen.fill(SCREEN_COLOR)
                    render(screen)
                if event.key == pygame.K_SPACE:
                    started = True
                if started:

                    # Узнаём, какие клеки пустые
                    place = get_free_place(mapa)

                    # Перемешиваем информацию в place,
                    # чтобы числа появлялись на рандомных местах
                    random.shuffle(place)

                    # Присваиваем переменной рандомное число и
                    # удаляем этот порядковый номер из свободного места
                    rand_num = place.pop()

                    # Находим индекс в нашел списке,
                    # по которому будет располагаться наше число
                    x, y = cell_index(rand_num)

                    # Помещаем наше число на поле
                    mapa = getting_start_nums(mapa, x, y)
                    pprint(mapa)

                    filling_cells(screen, mapa, x, y, place)
                # Для удобства изначально я выводил всё в консоль,
                # Это останется, чтобы искать ошибки
                if event.key == pygame.K_w:
                    pprint(mapa)
                    print(get_free_place(mapa))
                elif event.key == pygame.K_s:
                    pprint(mapa)
                    print(get_free_place(mapa))
                elif event.key == pygame.K_a:
                    pprint(mapa)
                    print(get_free_place(mapa))
                elif event.key == pygame.K_d:
                    pprint(mapa)
                    print(get_free_place(mapa))
        clock.tick(60)
        pygame.display.flip()
