import copy
import pygame

SIZE = 470, 470


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width, self.height, self.left, self.top, self.cell_size = width, height, 0, 0, 0
        self.board = [[0] * width for _ in range(height)]
        self.set_view(left, top, cell_size)

    def set_view(self, left, top, cell_size):
        self.left, self.top, self.cell_size = left, top, cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, "white", (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def on_click(self, cell):
        pass

    def get_cell(self, mpos):
        cell_x = (mpos[0] - self.left) // self.cell_size
        cell_y = (mpos[1] - self.left) // self.cell_size
        if not self.width > cell_x >= 0 or not self.height > cell_y >= 0:
            return None
        return cell_x, cell_y

    def get_click(self, mpos):
        cell = self.get_cell(mpos)
        if cell:
            self.on_click(cell)


class Life(Board):
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height, left, top, cell_size)

    def on_click(self, cell):
        self.board[cell[1]][cell[0]] = (self.board[cell[1]][cell[0]] + 1) % 2

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    pygame.draw.rect(screen, "green", (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size, self.cell_size))
                    pygame.draw.rect(screen, "white", (
                        x * self.cell_size + self.left, y * self.cell_size + self.top,
                        self.cell_size,
                        self.cell_size), 1)

    def next_move(self):
        tmp_board = copy.deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                s = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                            continue
                        s += self.board[y + dy][x + dx]
                s -= self.board[y][x]
                if s == 3:
                    tmp_board[y][x] = 1
                elif s < 2 or s > 3:
                    tmp_board[y][x] = 0
        self.board = copy.deepcopy(tmp_board)


def main():
    pygame.init()
    size = SIZE
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Life")
    board = Life(30, 30, 10, 10, 15)
    time_on = False
    ticks = 0
    speed = 10
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or \
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT:
                time_on = not time_on
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_WHEELUP:
                speed += 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_WHEELDOWN:
                speed += -1
        screen.fill((255, 255, 255))
        board.render(screen)
        if ticks >= speed:
            if time_on:
                board.next_move()
            ticks = 0
        pygame.display.flip()
        clock.tick(100)
        ticks += 1
    pygame.quit()


if __name__ == "__main__":
    main()
