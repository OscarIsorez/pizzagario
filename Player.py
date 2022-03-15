import pygame
import time

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/pizza.png").convert_alpha()
        self.x = 0
        self.y = 0
        self.size = 100

    def update(self, x_screen, y_screen, bots):
        x, y = pygame.mouse.get_pos()
        print(x, y)
        x += x_screen - self.x
        y += y_screen - self.y
        print(x, y)
        if abs(x) > 1 or abs(y) > 1:
            l = (x**2+y**2)**0.5
            x = x/l
            y = y/l
            self.x += x
            self.y += y
        for bot in bots:
            x = bot.x - self.x
            y = bot.y - self.y
            l = (x**2+y**2)**0.5
            if l < self.size/2:
                self.size += bot.size
                bots.remove(bot)

        self.render()


    def render(self):
        image = pygame.transform.scale(self.image, (self.size, self.size))
        self.screen.blit(image, (self.x - self.size/2, self.y - self.size/2))

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption('pizzagario')

    screen = pygame.display.set_mode((640, 920))
    player = Player(screen)

    while True:
        time.sleep(0.01)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 1000, 1000))
        player.update(0, 0)
        pygame.display.flip()