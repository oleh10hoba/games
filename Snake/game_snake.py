import pygame
####################################################
class Gui:
    def __init__(self):
        self.level = [
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,    
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        ]
        
        self.gui_image = pygame.image.load("./images/gui.png")
        self.win = pygame.image.load("./images/win.png")
        self.lose = pygame.image.load("./images/lose.png")
        self.pause = pygame.image.load("./images/pause.png")
        self.barier = []
        self.field = []
        self.indecator = [[12,12]]
        self.game = "GAME"

    def create_image(self):
        screen = pygame.Surface((441,441),pygame.SRCALPHA,32)
        x = 1
        y = 1
        for i in self.level:
            if i == 0:
                pygame.draw.rect(screen,pygame.Color("Grey"),pygame.Rect(x,y,10,10))
            x += 11
            if x == 441:
                y += 11
                x = 1
        pygame.image.save(screen,"images/gui.png")

    def draw_level(self,window):
        """draw level game"""
        window.blit(self.gui_image,(0,0))

    def init_field(self):
        """fill list coordinate"""
        x = 1
        y = 1
        for i in self.level:
            if i == 0:
                self.barier.append([x,y])
            elif i == 1 and y!= 12:
                self.field.append([x,y])
            x += 11
            if x == 441:
                y += 11
                x = 1

    def get_new_indecator(self):
        self.indecator.append([self.indecator[-1][0] + 11, 12])

    def draw_indecator(self,window):
        for i in self.indecator:
            pygame.draw.rect(window,pygame.Color("Green"),pygame.Rect(i[0],i[1],10,10))

    def draw_win(self,window):
        window.blit(self.win,(110,110))

    def draw_pause(self,window):
        window.blit(self.pause,(110,110))

    def draw_lose(self,window):
        window.blit(self.lose,(110,110))

    def check_win_or_lose(self):
        if len(self.indecator) == 0:
            self.game = "LOSE"
        elif len(self.indecator) == 37:
            self.game = "WIN"
##################################################################
from  pygame.locals import *
class Control:
    def __init__(self):
        self.flag_game = True
        self.flag_direction = "RIGHT"
        self.flag_pause = True
    def control(self):
        """Direction according flag"""
        #for close window after click exit
        for event in pygame.event.get():
            if event.type == QUIT:
                self.flag_game = False
            #knopka nazata
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.flag_direction != "LEFT":
                    self.flag_direction = "RIGHT"
                elif event.key == K_LEFT and self.flag_direction != "RIGHT":
                    self.flag_direction = "LEFT"
                elif event.key == K_UP and self.flag_direction != "DOWN":
                    self.flag_direction = "UP"
                elif event.key == K_DOWN and self.flag_direction != "UP":
                    self.flag_direction = "DOWN"
                elif event.key == K_ESCAPE:
                    self.flag_game = False
                elif event.key == K_SPACE:
                    if self.flag_pause:
                        self.flag_pause = False
                    elif self.flag_pause == False:
                        self.flag_pause = True
                        pygame.mixer.music.unpause()
                else:
                    pass
##################################################################
import random
class Food:
    def __init_(self):
        self.food_position = []

    def get_food_position(self,gui):
        """get random coordinate for fod"""
        self.food_position = random.choice(gui.field)

    def draw_food(self,window):
        pygame.draw.rect(window,pygame.Color("red"),pygame.Rect(self.food_position[0],self.food_position[1],10,10)) 
##################################################################
class Snake:
    def __init__(self):
        self.head = [45,45]
        self.body = [[45,45], [34,45], [23,45]]

    def move(self,control):
        "Mooving snake according direction"
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        elif control.flag_direction == "LEFT":
            self.head[0] -= 11
        elif control.flag_direction == "UP":
            self.head[1] -= 11
        elif control.flag_direction == "DOWN":
            self.head[1] += 11

    def animation(self):
        #add in begin list head and delete tail
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        """draw snake on window"""
        for segment in self.body:
            pygame.draw.rect(window,pygame.Color("Green"),pygame.Rect(segment[0],segment[1],10,10))

    def check_end_window(self):
        if self.head[0] >= 419:
            self.head[0] = 23
        elif self.head[0] <= 12:
            self.head[0] = 419
        elif self.head[1] <= 23:
            self.head[1] = 419
        elif self.head[1] >= 419:
            self.head[1] = 34


    def eat(self,food,gui):
        """snake eat food"""
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui)
            gui.get_new_indecator()

    def check_barier(self,gui):
        if self.head in gui.barier:
            self.body.pop()
            gui.indecator.pop()
        if self.head in self.body[1:]:
            self.body.pop()
            gui.indecator.pop()

##################################################################
#x - head[0]       y - head[1]
pygame.init()
#make window
window = pygame.display.set_mode((441,441))
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
MY_GREEN = (28, 249, 0)
pygame.mixer.music.load('serceedka.mp3')
pygame.mixer.music.set_volume(0.3)

FONT = pygame.font.Font("pinpong.ttf", 50)
def click_play():
    control = Control()
    snake = Snake()
    gui = Gui()
    food = Food()
    gui.init_field()
    food.get_food_position(gui)
    var_speed = 0
    pygame.mixer.music.play(-1)
    while control.flag_game:
        gui.check_win_or_lose()
        control.control()
        window.fill(pygame.Color("Black"))
        if  gui.game == "GAME":
            snake.draw_snake(window)
            food.draw_food(window)
        elif gui.game == "WIN":
            pygame.mixer.music.pause()
            
            gui.draw_win(window)
            button_sound = pygame.mixer.Sound("loss.wav")
        elif gui.game == "LOSE":
            pygame.mixer.music.pause()
            button_sound = pygame.mixer.Sound("loss.wav")
            pygame.mixer.Sound.play(button_sound)
            pygame.time.delay(1)
            gui.draw_lose(window)
        if control.flag_pause == False:
            pygame.mixer.music.pause()
            gui.draw_pause(window)
        gui.draw_indecator(window)
        gui.draw_level(window)
        if var_speed % 50 == 0 and control.flag_pause and  gui.game == "GAME":
            snake.move(control)
            snake.check_barier(gui)
            snake.check_end_window()
            snake.eat(food,gui)
            snake.animation()
        var_speed += 1
        pygame.display.flip()

def button(width,height,x,y,message,color_1,color_2):
    # The button is just a rect.
    button = pygame.Rect(width, height, x, y)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # 'event.pos' is the mouse position.
                    if button.collidepoint(event.pos):
                        # Increment the number.
                        button_sound = pygame.mixer.Sound("button.wav")
                        pygame.mixer.Sound.play(button_sound)
                        pygame.time.delay(300)
                        click_play()
                        pygame.quit()
        window.fill((199,201,110))
        pygame.draw.rect(window, color_2, button)
        text_surf = FONT.render(message,True,color_1)
        text_rect = text_surf.get_rect(center = (441/2,300))
        window.blit(text_surf,text_rect)
        # You can pass the center directly to the 'get_rect' method.
        pygame.display.update()
button(145.5,275,150,50,"PLAY",MY_GREEN,BLACK)