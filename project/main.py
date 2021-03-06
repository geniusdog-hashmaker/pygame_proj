import pygame


class CheckedField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 2
        self.top = 2
        self.cell_size = 100

    def set_view(self, left, top, cell_size):
        global screen
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.render(screen)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (255, 229, 180),
                                 (self.left * (x + 1) + self.cell_size * x,
                                  self.top * (y + 1) + self.cell_size * y,
                                  self.cell_size, self.cell_size))


def main_screen():
    tutor = ['"W": to move up;', '"S": to move down;', '"A": to move left;',
             '"D": to move right', 'Press "Space" to start']
    screen.fill((255, 229, 180))
    font = pygame.font.Font(None, 50)
    text = font.render("Welcome to 2048", True, (0, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() * 3
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 10,
                                         text_w + 20, text_h + 20), 1)
    font1 = pygame.font.Font(None, 30)
    for elem in range(len(tutor)):
        text1 = font1.render(tutor[elem],
                             True, (0, 0, 0))
        text_x1 = width // 2 - text1.get_width() // 2
        text_y1 = height // 2 + text.get_height() * elem
        if elem < 4:
            screen.blit(text1, (text_x1, text_y1))
        else:
            screen.blit(text1, (text_x1, text_y1 + 30))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 410, 410
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    main_screen()
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill((100, 100, 100))
                    field = CheckedField(width, height)
                    field.render(screen)
        clock.tick(60)
        pygame.display.flip()
