from dis import dis


class Button:
    def __init__(self, image, pos):
        self.image = image
        self.pushed = False
    
        self.pos = pos

    @property
    def rect(self):
        return self.image.get_rect()
    
    def push_down(self):
        self.pushed = True
    
    def push_up(self):
        self.pushed = False
    
    def is_pushed(self, mouse_pos):
        if self.rect.collidepoint(*mouse_pos):
            self.push_down()
            return True
        else:
            self.push_up()
            return False
        

    def render(self, surf):
        if self.pushed:
            surf.blit(self.image, (self.pos[0], self.pos[1] + 3))
        else:
            surf.blit(self.image, self.pos)
