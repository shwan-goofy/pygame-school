"""
게임 1: 낙하 캐치 게임 - 스켈레톤 (학생용)
목표: 떨어지는 동전을 받으면 점수 +10, 장애물을 받으면 게임 오버

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
COIN_SPEED = 3
OBSTACLE_SPEED = 3

# 플레이어 설정
player = Actor('player')
# TODO 1: player의 x 좌표를 WIDTH // 2 로 설정해서 화면 중앙에 배치하세요
player.x = ___________________
player.y = HEIGHT - 50

# 동전 설정
coin = Actor('coin')
coin.x = random.randint(32, WIDTH - 32)
coin.y = 0
coin_speed = COIN_SPEED

# 장애물 설정
obstacle = Actor('obstacle')
obstacle.x = random.randint(32, WIDTH - 32)
obstacle.y = 0
obstacle_speed = OBSTACLE_SPEED

# 게임 상태
score = 0
game_over = False
difficulty_multiplier = 1.0

def draw():
    screen.clear()
    screen.fill((25, 25, 60))  # 어두운 파란색 배경
    
    if not game_over:
        player.draw()
        coin.draw()
        obstacle.draw()
        
        # 점수 표시
        screen.draw.text(f"Score: {score}", (20, 20), fontsize=30, color=(255, 255, 255))
        screen.draw.text(f"Difficulty: x{difficulty_multiplier:.1f}", (20, 60), fontsize=20, color=(200, 200, 200))
    else:
        screen.draw.text("GAME OVER!", (150, 150), fontsize=60, color=(255, 50, 50))
        screen.draw.text(f"Final Score: {score}", (150, 220), fontsize=40, color=(255, 255, 255))
        screen.draw.text("Press R to restart or Q to quit", (100, 300), fontsize=24, color=(200, 200, 200))

def update():
    global score, game_over, coin_speed, obstacle_speed, difficulty_multiplier
    
    if game_over:
        if keyboard.r:
            reset_game()
        if keyboard.q:
            exit()
        return
    
    # TODO 2: 좌측 방향키를 누르면 player.x를 SPEED만큼 감소시키세요
    if keyboard.left:
        player.x -= ___________________
    
    # TODO 3: 우측 방향키를 누르면 player.x를 SPEED만큼 증가시키세요
    if keyboard.right:
        player.x += ___________________
    
    # TODO 4: 플레이어가 왼쪽 경계(x < 32)를 넘어가면 player.x = 32로 설정하세요
    if player.x < 32:
        ___________________
    
    # TODO 5: 플레이어가 오른쪽 경계(x > WIDTH - 32)를 넘어가면 player.x = WIDTH - 32로 설정하세요
    if player.x > WIDTH - 32:
        ___________________
    
    # TODO 6: 동전의 y 좌표를 coin_speed만큼 증가시키세요
    coin.y += ___________________
    
    # TODO 7: 장애물의 y 좌표를 obstacle_speed만큼 증가시키세요
    obstacle.y += ___________________
    
    # TODO 8: player와 coin이 충돌했는지 확인하세요 (colliderect 사용)
    # 충돌했으면: score += 10, coin을 리셋 (coin.x = random.randint(...), coin.y = 0)
    if ___________________:
        score += 10
        coin.x = random.randint(32, WIDTH - 32)
        coin.y = 0
    
    # TODO 9: player와 obstacle이 충돌했는지 확인하세요
    # 충돌했으면: game_over = True로 설정
    if ___________________:
        game_over = True
        return
    
    # 동전이 화면 밖으로 나가면 리셋
    if coin.y > HEIGHT:
        coin.x = random.randint(32, WIDTH - 32)
        coin.y = 0
    
    # 장애물이 화면 밖으로 나가면 리셋
    if obstacle.y > HEIGHT:
        obstacle.x = random.randint(32, WIDTH - 32)
        obstacle.y = 0
    
    # 난이도 조정 (점수 50점 이상이면 난이도 증가)
    if score >= 50 and difficulty_multiplier == 1.0:
        difficulty_multiplier = 1.5
        coin_speed = int(COIN_SPEED * difficulty_multiplier)
        obstacle_speed = int(OBSTACLE_SPEED * difficulty_multiplier)
    
    if score >= 100 and difficulty_multiplier == 1.5:
        difficulty_multiplier = 2.0
        coin_speed = int(COIN_SPEED * difficulty_multiplier)
        obstacle_speed = int(OBSTACLE_SPEED * difficulty_multiplier)

def reset_game():
    global score, game_over, coin_speed, obstacle_speed, difficulty_multiplier
    score = 0
    game_over = False
    difficulty_multiplier = 1.0
    coin_speed = COIN_SPEED
    obstacle_speed = OBSTACLE_SPEED
    
    player.x = WIDTH // 2
    player.y = HEIGHT - 50
    
    coin.x = random.randint(32, WIDTH - 32)
    coin.y = 0
    
    obstacle.x = random.randint(32, WIDTH - 32)
    obstacle.y = 0

pgzrun.go()
