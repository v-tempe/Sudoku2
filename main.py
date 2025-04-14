def main():
    import pygame

    pygame.init()
    display = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((0, 0, 0))

        pygame.display.flip()

        clock.tick(30)


if __name__ == "__main__":
    main()
