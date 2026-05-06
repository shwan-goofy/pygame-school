"""
Pygame Zero 게임용 PNG 에셋 자동 생성 스크립트
images/ 폴더에 3개의 PNG 파일을 생성합니다.
"""

from PIL import Image, ImageDraw
import os

# images 폴더 생성 (없으면)
images_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(images_dir, exist_ok=True)

print("PNG 에셋 생성 중...")

# 1. player.png - 64x64 파란 원 (캐릭터)
print("  - player.png 생성 중...")
player_img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
player_draw = ImageDraw.Draw(player_img)
# 파란 원 그리기
player_draw.ellipse([8, 8, 56, 56], fill=(50, 150, 255, 255), outline=(30, 100, 200, 255))
# 눈 그리기
player_draw.ellipse([20, 20, 26, 26], fill=(255, 255, 255, 255))
player_draw.ellipse([38, 20, 44, 26], fill=(255, 255, 255, 255))
player_img.save(os.path.join(images_dir, 'player.png'))

# 2. coin.png - 48x48 노란 원 (동전, 낙하 게임용)
print("  - coin.png 생성 중...")
coin_img = Image.new('RGBA', (48, 48), (0, 0, 0, 0))
coin_draw = ImageDraw.Draw(coin_img)
# 노란 원 그리기
coin_draw.ellipse([4, 4, 44, 44], fill=(255, 215, 0, 255), outline=(200, 170, 0, 255))
# 동전 무늬 (원)
coin_draw.ellipse([16, 16, 32, 32], outline=(200, 170, 0, 255), width=2)
coin_img.save(os.path.join(images_dir, 'coin.png'))

# 3. obstacle.png - 56x56 빨간 사각형 (장애물)
print("  - obstacle.png 생성 중...")
obstacle_img = Image.new('RGBA', (56, 56), (0, 0, 0, 0))
obstacle_draw = ImageDraw.Draw(obstacle_img)
# 빨간 사각형 그리기
obstacle_draw.rectangle([4, 4, 52, 52], fill=(255, 80, 80, 255), outline=(200, 50, 50, 255))
# 사각형 내부 무늬
obstacle_draw.line([10, 28, 46, 28], fill=(200, 50, 50, 255), width=2)
obstacle_draw.line([28, 10, 28, 46], fill=(200, 50, 50, 255), width=2)
obstacle_img.save(os.path.join(images_dir, 'obstacle.png'))

print(f"✓ 완료! 3개 이미지가 {images_dir}/ 폴더에 생성되었습니다.")
print("  - player.png (64x64)")
print("  - coin.png (48x48)")
print("  - obstacle.png (56x56)")
