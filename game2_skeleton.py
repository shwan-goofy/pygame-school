"""
게임 2: 피하기 게임 - 완성본
목표: 장애물을 피하면서 최대한 오래 생존하기
점수 = 생존 시간(초)
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
obstacles = []

# 게임 상태
frame_count = 0
game_over = False
obstacle_speed = OBSTACLE_SPEED

# 초기 장애물 3개 생성
for i in range(3):
    obs = Actor('obstacle')
    obs.x = random.randint(32, WIDTH - 32)
    obs.y = -50 - (i * 100)  # 위쪽에서 순서대로 배치
    obstacles.append(obs)

def draw():
    screen.clear()
    screen.fill((25, 25, 60))  # 어두운 파란색 배경

    if not game_over:
        # 모든 장애물 그리기
        for obstacle in obstacles:
            obstacle.draw()

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

    # 모든 장애물 업데이트
    for obstacle in obstacles:
        obstacle.y += obstacle_speed

    # 화면 밖 장애물 제거
    obstacles_to_remove = []
    for obstacle in obstacles:
        if obstacle.y > HEIGHT:
            obstacles_to_remove.append(obstacle)

    for obstacle in obstacles_to_remove:
        obstacles.remove(obstacle)

    # 충돌 감지
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            game_over = True
            return

    # 일정 시간마다 새 장애물 추가 (3초마다 = 180프레임)
    if frame_count % 180 == 0:
        new_obstacle = Actor('obstacle')
        new_obstacle.x = random.randint(32, WIDTH - 32)
        new_obstacle.y = 0
        obstacles.append(new_obstacle)

    # 난이도 증가 (10초마다 속도 +1)
    if frame_count % 600 == 0:  # 600프레임 = 10초
        obstacle_speed += 1

def reset_game():
    global frame_count, game_over, obstacle_speed, obstacles
    frame_count = 0
    game_over = False
    obstacle_speed = OBSTACLE_SPEED

    player.x = WIDTH // 2
    player.y = HEIGHT - 50

    obstacles = []
    # 초기 장애물 3개 생성
    for i in range(3):
        obs = Actor('obstacle')
        obs.x = random.randint(32, WIDTH - 32)
        obs.y = -50 - (i * 100)
        obstacles.append(obs)

pgzrun.go()
