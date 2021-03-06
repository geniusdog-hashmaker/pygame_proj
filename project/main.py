import pygame

# Задаём необходимые константы
CELLS_COUNT = 4
CELL_SIZE = 100
MARGIN = 2
WIDTH, HEIGHT = 410, 410

# Это наше поле в виде списка
mapa = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


# Это наше клетчатое поле, в котором всё будет происходить
class CheckedField:

    # Инициализируем наше поле
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_size = 100

    # Отрисовываем поле
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):

                # Отрисовываем наши клеточки
                pygame.draw.rect(screen, (255, 229, 180),
                                 (MARGIN * (x + 1) + self.cell_size * x,
                                  MARGIN * (y + 1) + self.cell_size * y,
                                  self.cell_size, self.cell_size))


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

# Эта функция отвечает за стартовый экран,
# где будет написано привествие и обучение
def main_screen():

    # Список с фразами обучения управлению
    tutor = ['"W": to move up;', '"S": to move down;', '"A": to move left;',
             '"D": to move right', 'Press "Space" to start']

    # Заливаем эран, задаём шрифт и здороваемся
    screen.fill((255, 229, 180))
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


if __name__ == '__main__':\

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
                if event.key == pygame.K_SPACE:
                    screen.fill((100, 100, 100))
                    field = CheckedField(WIDTH, HEIGHT)
                    field.render(screen)
                    started = True if started is None or False else False
                if started:

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
