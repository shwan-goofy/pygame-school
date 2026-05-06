"""
게임 2: 피하기 게임 - 스켈레톤 (학생용)
목표: 장애물을 피하면서 최대한 오래 생존하기
점수 = 생존 시간(초)

아래의 TODO 부분을 완성해서 게임을 만들어보세요!
"""

import pgzrun
import random
from pgzero.builtins import *

# 화면 설정
WIDTH = 600
HEIGHT = 450

# 게임 설정
SPEED = 5
OBSTACLE_SPEED = 3

# 플레이어 설정
player = Actor('player')
player.x = WIDTH // 2
player.y = HEIGHT - 50

# 장애물 리스트
# TODO 1: obstacles라는 빈 리스트를 만드세요
obstacles = ___________________

# 게임 상태
frame_count = 0
game_over = False
obstacle_speed = OBSTACLE_SPEED

# 초기 장애물 생성
# TODO 2: for 반복문을 사용해서 obstacles 리스트에 장애물 3개를 추가하세요
# (각 장애물은 Actor('obstacle')이고, x는 랜덤, y는 음수로 위쪽에 배치)
for i in range(3):
    obs = Actor('obstacle')
    obs.x = ___________________
    obs.y = ___________________
    obstacles.append(obs)

def draw():
    screen.clear()
    screen.fill((25, 25, 60))  # 어두운 파란색 배경
    
    if not game_over:
        # TODO 3: for 반복문으로 모든 장애물을 그리세요 (obstacle.draw())
        for obstacle in ___________________:
            ___________________
        
        player.draw()
        
        # 생존 시간 표시
        survival_time = frame_count // 60  # 프레임을 초로 변환
        screen.draw.text(f"Survival: {survival_time}s", (20, 20), fontsize=30, color=(255, 255, 255))
        screen.draw.text(f"Speed: {obstacle_speed}", (20, 60), fontsize=20, color=(200, 200, 200))
    else:
        # 게임 오버 화면
        survival_time = frame_count // 60
        screen.draw.text("GAME OVER!", (150, 150), fontsize=60, color=(255, 50, 50))
        screen.draw.text(f"Survival: {survival_time}s", (150, 220), fontsize=40, color=(255, 255, 255))
        screen.draw.text("Press R to restart or Q to quit", (100, 300), fontsize=24, color=(200, 200, 200))

def update():
    global frame_count, game_over, obstacle_speed
    
    if game_over:
        if keyboard.r:
            reset_game()
        if keyboard.q:
            exit()
        return
    
    frame_count += 1
    
    # 플레이어 이동 (좌)
    if keyboard.left:
        player.x -= SPEED
    
    # 플레이어 이동 (우)
    if keyboard.right:
        player.x += SPEED
    
    # 플레이어 경계 체크
    if player.x < 32:
        player.x = 32
    if player.x > WIDTH - 32:
        player.x = WIDTH - 32
    
    # TODO 4: for 반복문으로 모든 장애물의 y 좌표를 obstacle_speed만큼 증가시키세요
    for obstacle in ___________________:
        obstacle.y += ___________________
    
    # TODO 5: 화면 밖으로 나간 장애물을 obstacles 리스트에서 제거하세요
    # (먼저 리스트 복사본을 순회해야 안전함: for obstacle in obstacles[:])
    obstacles_to_remove = []
    for obstacle in obstacles[:]:
        if obstacle.y > HEIGHT:
            ___________________
    
    for obstacle in obstacles_to_remove:
        ___________________
    
    # TODO 6: player와 모든 장애물의 충돌을 확인하세요
    # (for 반복문 사용, colliderect 사용, 충돌하면 game_over = True)
    for obstacle in ___________________:
        if ___________________:
            game_over = True
            return
    
    # TODO 7: frame_count가 180의 배수일 때마다 새 장애물을 추가하세요
    # (3초마다 = 60fps × 3초 = 180프레임)
    if ___________________:
        new_obstacle = Actor('obstacle')
        new_obstacle.x = random.randint(32, WIDTH - 32)
        new_obstacle.y = 0
        obstacles.append(new_obstacle)
    
    # TODO 8: frame_count가 600의 배수일 때마다 obstacle_speed를 1 증가시키세요
    # (10초마다 = 60fps × 10초 = 600프레임)
    if ___________________:
        obstacle_speed += ___________________

def reset_game():
    global frame_count, game_over, obstacle_speed, obstacles
    frame_count = 0
    game_over = False
    obstacle_speed = OBSTACLE_SPEED
    
    player.x = WIDTH // 2
    player.y = HEIGHT - 50
    
    obstacles = []
    for i in range(3):
        obs = Actor('obstacle')
        obs.x = random.randint(32, WIDTH - 32)
        obs.y = -50 - (i * 100)
        obstacles.append(obs)

pgzrun.go()
