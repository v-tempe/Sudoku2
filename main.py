def main():
    import pygame

    import constants

    pygame.init()
    display = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption(constants.GAME_NAME)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((0, 0, 0))

        pygame.display.flip()

        clock.tick(constants.FPS)


if __name__ == "__main__":
    main()
