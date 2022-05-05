import pygame


class Input:
    def __init__(self, game):
        self.game = game

        self.click = False
        self.select = ""

        self.jump = False

    def _get_mouse_pos(self):
        window_mouse_pos = pygame.mouse.get_pos()
        display_mouse_pos = (window_mouse_pos[0] * self.game.window.DISPLAY_SIZE[0] / self.game.window.WINDOW_SIZE[0],
                             window_mouse_pos[1] * self.game.window.DISPLAY_SIZE[1] / self.game.window.WINDOW_SIZE[1])
        return display_mouse_pos

    def _get_ui_buttons(self):
        return self.game.renderer.get_ui().buttons

    def update(self):
        mouse_pos = self._get_mouse_pos()

        self.select = ""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button_name, button in list(self._get_ui_buttons().items()):
                        button.is_pushed(mouse_pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for button_name, button in list(self._get_ui_buttons().items()):
                        if button.pushed:
                            self.select = button_name
                        button.push_up()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game.world.gameover:
                        self.jump = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.jump = False
