import random
import pygame
#############################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz") # 게임 이름

#FPS
clock = pygame.time.Clock()
#############################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("C:/Users/user/Desktop/pythonworkspace/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/user/Desktop/pythonworkspace/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치(세로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(가로)

# 이동할 좌표
to_x = 0


# 이동 속도
character_speed = 0.3

# 적 캐릭터
enemy = pygame.image.load("C:/Users/user/Desktop/pythonworkspace/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로크기
enemy_height = enemy_size[1] # 캐릭터의 세로크기
enemy_x_pos = random.randint(0, screen_width - enemy_width) 
enemy_y_pos = 0 # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(가로)
enemy_speed = 10

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 결정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif  event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향기를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width) 
    

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    # 5. 화면에 그리기

    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 캐릭터 그리기
    pygame.display.update() # 게임 화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 
# pygame 종료
pygame.quit()

