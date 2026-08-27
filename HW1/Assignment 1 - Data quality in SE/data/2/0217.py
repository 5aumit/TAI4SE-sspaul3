import pygame

class MenuManager():
    def __init__(self, manager):
        print "Menu manager created. Continue? [y/n]"
        self.manager = manager
        self.paused = False
        self.intro_done = False
        self.menus = []
        self.menus.append(Pause_menu(self))
        self.menus.append(Start_screen(self))

    def get_paused(self):
        return self.paused

    def set_paused(self, pause):
        self.paused = pause

    def set_intro_done(self, startup):
        self.intro_done = startup

    def get_intro_done(self):
        return self.intro_done

    def set_active(self, menu_index):
        self.menus[menu_index].set_active()

    def unset_active(self, menu_index):
        self.menus[menu_index].unset_active()

    def exit_game(self):
        self.manager.exit_game()

    def pass_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.unset_active(1)
                self.paused = not self.paused

    def draw(self, screen):
        if self.paused and self.menus[1].is_active() == False:
            self.set_active(0)
        else:
            self.unset_active(0)

        for menu in self.menus:
            if menu.is_active():
                menu.draw(screen)


class Button():
    def __init__(self, pos, size, color, font, font_size, font_color, image=None, text=None):
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(self.pos, self.size)
        self.color = color
        self.d_color = 40
        if self.color[0]>235 or self.color[1]>235 or self.color[2]>235:
            self.hover_color = (self.color[0]-self.d_color, self.color[1]-self.d_color, self.color[2]-self.d_color)
        else:
            self.hover_color = (self.color[0]+self.d_color, self.color[1]+self.d_color, self.color[2]+self.d_color)
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.font.set_bold(True)
        if image != None: self.image = pygame.image.load("Sprites/"+image+".png")
        else: self.image = None
        if text != None:
            self.text = self.font.render(text, True, self.font_color)

    def draw(self, screen):
        draw_pos = (screen.get_width()/2+self.pos[0]-self.size[0]/2, screen.get_height()/2+self.pos[1])
        if self.image != None:
            screen.blit(self.image, draw_pos)
        else:
            self.rect = pygame.Rect(draw_pos, self.size)
            if self.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                draw_color = self.hover_color
            else:
                draw_color = self.color
            pygame.draw.rect(screen, draw_color, self.rect)
            screen.blit(self.text, (self.rect.x+self.rect.w/2-self.text.get_width()/2, self.rect.y+self.rect.h/2-self.text.get_height()/2))
            pygame.draw.rect(screen, (0,0,0), self.rect, 1)

    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False



class Pause_menu():
    def __init__(self, manager):
        self.manager = manager
        self.buttons = []
        self.buttons.append(Button((-100, 30), (100,50), (255,255,255), "Arial", 20, (255,0,0), text="Continue"))
        self.buttons.append(Button((100, 30), (120,50), (255,255,255), "Arial", 20, (255,0,0), text="Exit game"))
        self.active = False

    def draw(self, screen):
        for button in self.buttons:
            self.check_clicked()
            button.draw(screen)

    def is_active(self):
        return self.active

    def set_active(self):
        self.active = True

    def unset_active(self):
        self.active = False

    def check_clicked(self):
        for button_i in range(len(self.buttons)):
            if pygame.mouse.get_pressed()[0] == True and self.buttons[button_i].is_clicked():
                if button_i == 0:
                    self.manager.set_paused(False)
                    self.manager.unset_active(1)
                elif button_i == 1:
                    print "Exit button pressed. Goodbye"
                    self.manager.exit_game()


class Start_screen():
    def __init__(self, manager):
        self.manager = manager
        self.active = False
        self.image = pygame.image.load("Files/Start_screen.png")
        self.buttons = []
        self.buttons.append(Button((-100, 150), (130,50), (255,255,255), "Arial", 20, (255,0,0), text="Start"))
        self.buttons.append(Button((100, 150), (190,50), (255,255,255), "Arial", 20, (255,0,0), text="Exit game [ESC]"))

    def draw(self, screen):
        draw_pos = (screen.get_width()/2-self.image.get_width()/2, 20)
        self.check_clicked()
        for button in self.buttons:
            button.draw(screen)
        screen.blit(self.image, draw_pos)

    def is_active(self):
        return self.active

    def set_active(self):
        self.active = True

    def unset_active(self):
        self.active = False

    def check_clicked(self):
        for button_i in range(len(self.buttons)):
            if pygame.mouse.get_pressed()[0] == True: 
                if self.buttons[button_i].is_clicked():
                    if button_i == 0:
                        self.manager.set_intro_done(True)
                        self.manager.unset_active(1)
                        self.manager.manager.get_universe().set_can_shoot(True)
                    elif button_i == 1:
                        print "Exit button pressed. Goodbye"
                        self.manager.exit_game()