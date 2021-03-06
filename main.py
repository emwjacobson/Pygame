import pygame
import settings
import time
from worlds import dirtworld

# Initialization
pygame.init()
flags = (pygame.FULLSCREEN | pygame.SCALED | pygame.HWSURFACE | pygame.ASYNCBLIT | pygame.DOUBLEBUF) if settings.FULLSCREEN else (pygame.HWSURFACE | pygame.ASYNCBLIT | pygame.DOUBLEBUF)
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), flags)

clock = pygame.time.Clock()

cur_map = dirtworld.DirtWorld(settings.WIDTH * 2, settings.HEIGHT * 2, [-settings.WIDTH // 2, -settings.HEIGHT // 2])

while True:
    # This is here to make sure that movement is the same regardless of FPS
    micro = clock.tick(settings.FPS) / 1000

    event: pygame.event.Event
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

    screen.fill((0, 0, 0))

    cur_map.handle_events(events)
    cur_map.update(micro)
    cur_map.render(screen)

    pygame.display.flip()
    print(int(clock.get_fps()))
