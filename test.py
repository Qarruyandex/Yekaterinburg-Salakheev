import pygame

WINDOW = 1050, 1050


class Board:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 20
        self.color = color

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        colors = ["black", "white"]
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    pygame.draw.rect(screen, self.color,
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, self.color,
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size), 1)

    def get_click(self, mpos):
        cell = self.get_cell(mpos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        for y in range(self.width):
            self.board[cell[1]][y] = (self.board[cell[1]][y] + 1) % 2
        for x in range(self.height):
            if x == cell[1]:
                continue
            self.board[x][cell[0]] = (self.board[x][cell[0]] + 1) % 2

    def get_cell(self, mpos):
        x = (mpos[0] - self.left) // self.cell_size
        y = (mpos[1] - self.top) // self.cell_size
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        print(x, y)
        return x, y


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WINDOW)
    running = True
    clock = pygame.time.Clock()
    board = Board(50, 50, "red")
    while running:
        screen.fill("white")
        board.render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.MOUSEMOTION:
                board.get_click(event.pos)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
