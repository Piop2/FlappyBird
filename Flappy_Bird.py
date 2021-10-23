import pygame, time, sys, random, json


pygame.init()
screen_width = 432
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy_Bird")
icon = pygame.image.load('resorce/icon.ico')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# 타이머 : 여러 애니메이션 상황에 필요
class Timer:

    def __init__(self, time_interval):
        self.time_interval = time_interval
    
    def reset(self):
        del self.end_time
        del self.start_time

    def is_time_up(self):
        try:
            self.end_time = time.time()
            if self.end_time - self.start_time >= self.time_interval and self.time_interval != 0:
                self.start_time = time.time()
                return True
            else: return False
        except:
            self.start_time = time.time()
            self.end_time = time.time()
            return False

# 게임 : 메인 담당
class Game():
    def __init__(self):
        # 세이브 파일 불러오기
        ## data.json
        # self.player_name
        # self.best_score
        with open('resorce/data.json', 'r') as f:
            data = json.load(f)

        # 게임 화면
        self.game_info = ""
        self.score = 0
        self.best_score = data["BestScore"]

        # Test
        self.TESTMODE = data["TestMode"]


        # 바닥
        self.floor_count = 0
        
        # 새
        self.bird_speed = 2.3

        # 버튼
        self.menu_button_list = [start_button, score_button]
        self.game_button_list = [ok_button, share_button]

        # fadeIN
        self.alpha_Out = 0
        self.fadeOut = False
        self.alpha_In = 0
        self.fadeIn = False

        # 파이프
        self.pipe_reset()
        self.last_pipe = self.pipe_list[-1][0] # 첫번째 파이프를 인식하여 점수를 내기 때문에 마지막 파이프를 임의로 설정

    def pipe_reset(self):
        self.pipe_list = []
        pipe_x_pos = screen_width
        self.pipe_interval = 78 + 165  # 파이프당 간격 100
        for i in range(3):
            self.add_pipe(pipe_x_pos)
            pipe_x_pos += self.pipe_interval

    def add_pipe(self, x_pos):
        pipe_pass_interval = 175 #아니면 170 설정
        pipe_y_pos = random.randint(-320, -50)

        pipe_up = Pipe(pipes[0], (x_pos, pipe_y_pos), self.bird_speed)
        pipe_down = Pipe(pipes[1], (x_pos, pipe_y_pos + 405 + pipe_pass_interval), self.bird_speed)
        
        self.pipe_list.append([pipe_up, pipe_down])

    ## 페이드 인 아웃
    def ready_to_fade(self):
        self.fadeIn = True
        self.alpha_In = 255

        self.fadeOut = True
        self.alpha_Out = 0
    
    def fade_out(self):
        
        if self.fadeOut:
            if self.alpha_Out >= 255:
                self.fadeOut = False
            fadeout = pygame.Surface((screen_width, screen_height))
            fadeout = fadeout.convert()
            fadeout.fill((0, 0, 0))
            
            self.alpha_Out += 4

            fadeout.set_alpha(self.alpha_Out)
            screen.blit(fadeout, (0, 0))

    def fade_in(self):

        if self.fadeIn:
            if self.alpha_In <= 0:
                self.fadeIn = False

            fadein = pygame.Surface((screen_width, screen_height))
            fadein = fadein.convert()
            fadein.fill((255, 255, 255))

            self.alpha_In -= 6

            fadein.set_alpha(self.alpha_In)
            screen.blit(fadein, (0, 0))

    def save_data(self):
        data = {"BestScore" : self.best_score, "TestMode" : self.TESTMODE}
        with open('resorce/data.json', 'w') as f:
            json.dump(data, f)

    ## 게임상황당 화면
    # 게임 메뉴
    def game_menu(self):

        bird.flip_timer = Timer(0.15)
        bird.rotate_degree = 0

        self.game_info = 'game_menu'

        self.ready_to_fade()

        running = True
        while running:
            dt = clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_data()
                    pygame.quit()
                    sys.exit()
                

                # 마우스 누르기
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # 버튼을 눌렀는가?
                    for button in self.menu_button_list:
                        if button.position[0] <= event.pos[0] <= button.position[0] + button.size[0]:
                            if button.position[1] <= event.pos[1] <= button.position[1] + button.size[1]:
                                button.down = True
                
                # 마우스 업`
                if event.type == pygame.MOUSEBUTTONUP:

                    # 버튼을 땟는가?
                    for button in self.menu_button_list:
                        if button.down == True:
                            button.down = False
                            self.game_info = button.action


            
            # 바닥 위치 계산
            self.floor_count -= self.bird_speed
            floor_x = self.floor_count % 462


            ### 화면 출력 ###

            # 배경
            screen.blit(background, (0, 0))
            

            # 바닥 애니메이션
            screen.blit(floor, (floor_x, 600))
            screen.blit(floor, (floor_x - 462, 600))
            
            # 버튼
            for button in self.menu_button_list:
                button.update()
            
            # 큰 텍스트
            text_flappy_bird.update(repeat=True, fade=False)

            # copyright
            screen.blit(copyright_text, ((screen_width/2) - 138, 625))
            
            bird.position = [text_flappy_bird.position[0] + text_flappy_bird.img.get_rect().size[0] + 17, text_flappy_bird.position[1] + 10]
            bird.update(gravity=False)
            
            if self.game_info == 'game_start':
                self.fade_out()
                if self.fadeOut == False:
                    running = False


            pygame.display.update()



    # 게임 시작
    def game_run(self):
        

        # 게임시작을 위한 새 위치 설정
        bird.flip_timer = Timer(0.15)
        bird.position = [80, 300]
        bird.rotate_degree = 0

        # 파이프 리셋
        self.pipe_reset()

        # 점수 리셋
        self.score = 0
        score_animation_number = 0
        score_board_speed = 32
        score_board_position = [(screen_width / 2) - (339 / 2), screen_height + 174]
        new_best_score = False
        best_score_animation_number = self.best_score

        # 게임 상황 설정 : 대기
        self.game_info = 'game_wait'


        # 게임에서 페이드인은 죽을때 한 번 일어나니 반복적으로 일어나지 않게 미리 세팅
        self.ready_to_fade()

        # tip
        tip_alpha = 0
        tip_fade_in_out = 1

        # ready
        ready_alpha = 0
        ready_fade_in_out = 1

        game_over_flappy_bird.alpha = 0
        game_over_flappy_bird.round_one = False

        # computer
        computer = False
        jump_y = -5
        next_pipe_x = 72

        for button in self.game_button_list:
            button.is_button_visible = False
        

        running = True
        while running:
            dt = clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_data()
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if self.game_info == 'game_start' or self.game_info == 'game_wait':
                        if event.key == pygame.K_SPACE:
                            if self.game_info == 'game_wait':
                                self.game_info = 'game_start'
                                bird.flip_timer = Timer(0.05)
                            bird.bird_jump()
                    
                    if event.key == pygame.K_a and self.TESTMODE:
                        if computer:
                            computer = False
                        else:
                            computer = True
                        
                # 마우스 누르기
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # 버튼을 눌렀는가?
                    if event.button == 1:
                        for button in self.game_button_list:
                            if button.is_button_visible:
                                if button.position[0] <= event.pos[0] <= button.position[0] + button.size[0]:
                                    if button.position[1] <= event.pos[1] <= button.position[1] + button.size[1]:
                                        button.down = True
                
                # 마우스 업
                if event.type == pygame.MOUSEBUTTONUP:

                    # 버튼을 떗는가?
                    if event.button == 1:
                        for button in self.game_button_list:
                            if button.is_button_visible:
                                if button.down == True:
                                    button.down = False
                                    self.game_info = button.action
            
            

            if not (self.game_info == 'game_over' or self.game_info == 'game_menu' or self.game_info == 'game_restart'):

                # 바닥 위치 계산
                self.floor_count -= self.bird_speed
                floor_x = self.floor_count % 462

            
            # 파이프가 새 위치로 왔을 때 점수 계산
            if self.pipe_list[0][0].position[0] <= bird.position[0]:
                if not self.pipe_list[0][0] == self.last_pipe:
                    self.last_pipe = self.pipe_list[0][0]
                    self.score += 1

            # 파이프 끝까지 갔을때 / 파이프당 간격 100
            if self.pipe_list[0][0].position[0] <= - 78:
                del self.pipe_list[0]
                end_pipe_x_pos = self.pipe_list[-1][0].position[0]
                self.add_pipe(end_pipe_x_pos + self.pipe_interval)


            # computer
            if computer:
                if self.game_info == 'game_start':
                    if self.pipe_list[0][0] == self.last_pipe:
                        if bird.position[0] - self.pipe_list[0][1].position[0] <= next_pipe_x:
                            if self.pipe_list[0][1].position[1] - bird.position[1] <= 60:
                                jump_y = self.pipe_list[0][1].position[1] - 60 + bird.size[1]
                                bird.bird_jump()
                        else:
                            if self.pipe_list[1][1].position[1] - bird.position[1] <= 60:
                                jump_y = self.pipe_list[1][1].position[1] - 60 + bird.size[1]
                                bird.bird_jump()
                    else:
                        if self.pipe_list[0][1].position[1] - bird.position[1] <= 60:
                            jump_y = self.pipe_list[0][1].position[1] - 60 + bird.size[1]
                            bird.bird_jump()




            ### 화면 출력 ###

            # 배경
            screen.blit(background, (0, 0))


            if self.game_info == 'game_wait' or self.game_info == 'game_over' or self.game_info == 'game_stop' or self.game_info == 'game_menu' or self.game_info == 'game_restart':
                pipe_move = False
            else: pipe_move = True
                
            for pipe_updown in self.pipe_list:
                for pipe in pipe_updown:
                    pipe.update(pipe_move)

            # 바닥 애니메이션
            screen.blit(floor, (floor_x, 600))
            screen.blit(floor, (floor_x - 462, 600))


            # 대기 화면일 떄 중력 설정
            if self.game_info == 'game_wait' or self.game_info == 'game_stop' or self.game_info == 'game_menu' or self.game_info == 'game_restart':
                gravity = False
            else: gravity = True

            bird.update(gravity=gravity)
            
            # 대기 화면일 때 팁창
            if self.game_info == 'game_wait':
                tip_alpha += tip_fade_in_out * 4
                if tip_alpha >= 255:
                    tip_alpha = 255
                    tip_fade_in_out *= -1
                elif tip_alpha <= 0:
                    tip_alpha = 0
                    tip_fade_in_out *= -1
                
                tip.set_alpha(tip_alpha)
                screen.blit(tip, ((screen_width / 2) - (114 / 2), 300))

                ready_alpha += ready_fade_in_out * 4
                if ready_alpha >= 255:
                    ready_alpha = 255
                    ready_fade_in_out *= -1
                elif ready_alpha <= 0:
                    ready_alpha = 0
                    ready_fade_in_out *= -1
                
                ready_flappy_bird.set_alpha(ready_alpha)
                screen.blit(ready_flappy_bird, ((screen_width / 2) - (288 / 2), 130))

            if self.game_info == 'game_wait' or self.game_info == 'game_start':
                big_number_score.update(score = self.score)

            if self.game_info == 'game_over' or self.game_info == 'game_menu' or self.game_info == 'game_restart':
                
                self.fade_in()
                if self.fadeIn == False:
                    game_over_flappy_bird.update(repeat=False, fade=True)
                    
                    score_board_surface = pygame.Surface((339, 174))
                    score_board_surface.blit(score_board, (0, 0))
                    score_board_score.update(screen = score_board_surface, score = int(score_animation_number), center = False)
                    score_board_best_score.update(score = int(best_score_animation_number), screen = score_board_surface, center = False)
                    if new_best_score: score_board_surface.blit(new_score, (201, 87))


                    if self.score >= 100:
                        score_board_surface.blit(medals[0], (39, 64))
                    elif self.score >= 70:
                        score_board_surface.blit(medals[1], (39, 64))
                    elif self.score >= 40:
                        score_board_surface.blit(medals[2], (39, 64))
                    elif self.score >= 20:
                        score_board_surface.blit(medals[3], (39, 64))



                    if score_board_position[1] > 200:
                        score_board_position[1] -= score_board_speed
                        score_board_speed -= 0.7

                    else:
                        if self.best_score < self.score:
                            self.best_score = self.score

                        score_animation_number += self.score / 50
                        if score_animation_number >= self.score:
                            score_animation_number = self.score
                            
                        if int(score_animation_number) > int(best_score_animation_number):
                            new_best_score = True
                            best_score_animation_number = score_animation_number

                        score_board_position[1] = 200

                        ok_button.update(fade_in=True)
                        share_button.update(fade_in=True)
                        
                    screen.blit(score_board_surface, score_board_position)
            else:
                pause_button.update()

            if computer:
                if self.game_info == 'game_start':
                    pygame.draw.line(screen, (0, 255, 0), [0, bird.position[1] + (bird.size[1] / 2)], [screen_width, bird.position[1] + (bird.size[1] / 2)], bird.size[1])

                    pygame.draw.line(screen, (255, 0, 0), [0, jump_y], [screen_width, jump_y], 5)

                    pygame.draw.line(screen, (0, 0, 255), [self.pipe_list[0][0].position[0] + next_pipe_x, 0], [self.pipe_list[0][0].position[0] + next_pipe_x, screen_height], 5)



            if self.game_info == 'game_menu' or self.game_info == 'game_restart':
                self.fade_out()
                if self.fadeOut == False:

                    if self.game_info == 'game_restart': self.game_info = 'game_start'
                    running = False
            
            

            pygame.display.update()

# 버튼
class Button:
    def __init__(self, img, position, press_lenth, action):
        self.img = img
        self.size = self.img.get_rect().size
        self.position = list(position)

        self.is_button_visible = False
        self.action = str(action)
        
        self.press_lenth = press_lenth

        self.down = False

        self.fade_in_alpha = 0
    
    def update(self, fade_in = False):
        if fade_in:
            if self.fade_in_alpha <= 255:
                self.fade_in_alpha += 10
            else:
                self.fade_in_alpha = 255
            self.img.set_alpha(self.fade_in_alpha)

        self.is_button_visible = True

        if self.down:
            screen.blit(self.img, (self.position[0], self.position[1] - self.press_lenth))
        else:
            screen.blit(self.img, self.position)

# 오브젝트
class Text_img:
    def __init__(self, img, position, move_y, move_speed):
        self.img = img
        self.max_range = position[1] + move_y
        self.min_range = position[1] - move_y
        self.position = list(position)
        self.origin_position = list(position)
        self.move_speed = move_speed
        self.direction = 1

        self.repeat = True
        self.round_one = False

        self.fade = False
        self.alpha = 0
    
    def update(self, repeat = True, fade = False):
        self.repeat = repeat
        self.fade = fade

        if self.min_range > self.position[1] or self.max_range < self.position[1]:
            self.direction *= -1
            self.round_one = True
        self.position[1] += self.move_speed * self.direction

        if self.repeat == False and self.round_one and self.position[1] >= self.origin_position[1]:
            self.position[1] = self.origin_position[1]
            
            
        
        if self.fade:
            if self.alpha >= 255:
                self.alpha = 255
            else: self.alpha += 10
            self.img.set_alpha(self.alpha)

        screen.blit(self.img, self.position)


class Int_img:
    def __init__(self, number_imgs, position):
        self.score = 0
        self.imgs = list(number_imgs)
        self.position = list(position)

    def update(self, score, screen = screen, center = True):
        score_string = str(score)

        surface_x = 0
        for number_string in score_string:
            number_int = int(number_string)
            if number_int == 1:
                surface_x += 15
            else: surface_x += 21
        
        board = pygame.Surface((surface_x, 30))
        

        blit_x = 0
        for number_string in score_string:
            number_int = int(number_string)
            
            board.blit(self.imgs[number_int], (blit_x, 0))

            if number_int == 1:
                blit_x += 15
            else: blit_x += 21
        if center:
            screen.blit(board, (self.position[0] - (surface_x / 2), self.position[1]))
        else:
            screen.blit(board, (self.position[0] - (surface_x), self.position[1]))
    

class Pipe:
    def __init__(self, img, position, speed):
        self.img = img
        self.position = list(position)
        self.speed = speed
    
    def update(self, move=True):
        if move:
            self.position[0] -= self.speed

        bird_rect = bird.img[0].get_rect()
        bird_rect.left = bird.position[0]
        bird_rect.top = bird.position[1]


        pipe_rect = self.img.get_rect()
        pipe_rect.left = self.position[0]
        pipe_rect.top = self.position[1]

        if pipe_rect.colliderect(bird_rect) and not game.game_info == 'game_menu' and not game.game_info == 'game_restart':
            game.game_info = 'game_over'


        screen.blit(self.img, self.position)

class Bird:
    def __init__(self, imgs, position, flip_speed):
        self.img = imgs
        self.animation_number = 0
        self.flip_timer = Timer(flip_speed)

        self.size = imgs[0].get_rect().size

        self.position = list(position)

        self.gravity = 0.5
        self.jump_energy = 10
        self.to_y = 0

        self.rotate_speed = 0
        self.rotate_acceleration = 0.06
        self.rotate_degree = 0

    
    def bird_jump(self):
        self.to_y = - self.jump_energy
        self.rotate_degree = 40

        self.rotate_speed = 0

    def update(self, gravity = True):
        if self.flip_timer.is_time_up():
            self.animation_number += 1
        img = self.img[int(self.animation_number % len(self.img))]
        
        if gravity:
            self.to_y += self.gravity
            if self.position[1] >= 600 - self.size[1]:
                self.position[1] = 600 - self.size[1]
                self.to_y = 0
                game.game_info = 'game_over'
                self.flip_timer = Timer(0)
            else:
                self.rotate_speed += self.rotate_acceleration
                self.rotate_degree -= self.rotate_speed

            if self.position[1] <= 0:
                self.position[1] = 0

            self.position[1] += self.to_y

        if self.rotate_degree <= -90: self.rotate_degree = -90
        img = blitRotate(img, (self.size[0] / 2, self.size[1] / 2), self.position, self.rotate_degree)


        screen.blit(img, self.position)

def blitRotate(image, pos, originPos, angle): 
 
    #calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size() 
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]] 
    box_rotate = [p.rotate(angle) for p in box] 
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1]) 
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1]) 
 
    #calculate the translation of the pivot  
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1]) 
    pivot_rotate = pivot.rotate(angle) 
    pivot_move   = pivot_rotate - pivot 
 
    #calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1]) 
 
    #get a rotated image
    rotated_image = pygame.transform.rotate(image, angle) 
    return rotated_image

# 스트립 나누기
def seperate_strip(img, start_xy, seperate_tuple, count, scale):
    images = []

    width = seperate_tuple[0]
    height = seperate_tuple[1]

    x_ = start_xy[0]
    for i in range(count):
        x_ = start_xy[0] + width * i

        image_rect = pygame.Surface((width, height))
        image_rect.blit(img, (0, 0), pygame.Rect(x_, start_xy[1], width, height))
        
        image_rect = pygame.transform.scale(image_rect, (width * scale, height * scale))
        image_rect.set_colorkey((0, 0, 0))
        images.append(image_rect)

    return images




resorce_strip = pygame.image.load('resorce/sprites.png')


background = seperate_strip(resorce_strip, (0, 0), (144, 256), 1, 3)[0]

floor = seperate_strip(resorce_strip, (0, 256), (154, 56), 1, 3)[0]

bird = Bird(
    seperate_strip(resorce_strip, (144, 147), (17, 12), 3, 3),
    (0, 0),
    0.1
)

pipes = seperate_strip(resorce_strip, (296, 53), (26, 135), 2, 3)


buttons = seperate_strip(resorce_strip, (144, 39), (40, 14), 6, 3)
start_button = Button(buttons[0], (60, 480), -8, 'game_start')
score_button = Button(buttons[1], (screen_width - 120 - 60, 480), -8, 'score')
ok_button = Button(buttons[5], (60, 480), -8, 'game_menu')
share_button = Button(buttons[4], (screen_width - 120 - 60, 480), -8, 'game_over')

small_buttons = seperate_strip(resorce_strip, (144, 53), (13, 14), 2, 3)
pause_button = Button(small_buttons[0], (10, 70), -8, 'game_stop')

big_text = seperate_strip(resorce_strip, (144, 0), (96, 22), 3, 3)
text_flappy_bird = Text_img(big_text[0], (30, 160), 7, 0.7)
ready_flappy_bird = big_text[2]
game_over_flappy_bird = Text_img(big_text[1], ((screen_width / 2) - (288 / 2), 120), 10, 0.7)

big_numbers = seperate_strip(resorce_strip, (144, 22), (7, 10), 10, 3)
number_one = pygame.Surface((15, 30))
number_one.blit(big_numbers[1], (0, 0))
big_numbers[1] = number_one
big_number_score = Int_img(big_numbers, (screen_width / 2, 70))

score_board = seperate_strip(resorce_strip, (144, 67), (113, 58), 1, 3)[0]
score_board_position = [(screen_width / 2) - (339 / 2), screen_height + 174]
score_board_score = Int_img(big_numbers, (303, 48))
score_board_best_score = Int_img(big_numbers, (303, 111))
new_score = seperate_strip(resorce_strip, (232, 125), (16, 7), 1, 3)[0]
medals = seperate_strip(resorce_strip, (144, 125), (22, 22), 4, 3)

copyright_text = seperate_strip(resorce_strip, (0, 312), (92, 7), 1, 3)[0]

tip = seperate_strip(resorce_strip, (257, 67), (39, 49), 1, 3)[0]


# 메인 루프
if __name__ == '__main__':
    game = Game()
    game.game_menu()
    while True:
        if game.game_info == 'game_start':
            game.game_run()
        elif game.game_info == 'game_menu':
            game.game_menu()
        else:
            game.game_menu()
