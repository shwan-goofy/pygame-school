---
marp: true
theme: default
paginate: true
---

# 내 코드로 움직이는 첫 번째 게임
## Pygame Zero로 배우는 파이썬 기초

---

## 오늘 배울 것

| 교시 | 파이썬 문법 | 게임 실습 |
|------|-------------|-----------|
| **도입** | 자료형, 연산자, print | 환경 설정 |
| **1교시** | 변수, f-string | 캐릭터 배치, 이동 |
| **2교시** | 조건문(if/else) | 키보드 입력, 충돌 |
| **2.5교시** | 함수(def), global | reset_game 작성 |
| **3교시** | 리스트, 반복문(for) | 여러 장애물 관리 |

---

## 오늘 만들 게임

### 게임 1: 낙하 캐치 게임
떨어지는 동전을 받아서 점수를 올리세요!  
장애물에 닿으면 게임 오버.

### 게임 2: 피하기 게임
쏟아지는 장애물을 피하며 최대한 오래 살아남으세요!  
생존 시간이 점수입니다.

---

## 환경 확인 (Windows CMD)

```cmd
:: Python 버전 확인 (3.11 이상이어야 합니다)
python --version

:: 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate.bat

:: 라이브러리 설치
python -m pip install pgzero Pillow

:: 게임 이미지 생성
python make_assets.py
```

프롬프트 앞에 `(venv)` 가 보이면 성공입니다!

---

# 도입: 파이썬 기초 문법

---

## 파이썬이란?

- 사람이 읽기 쉬운 프로그래밍 언어
- 한 줄씩 위에서 아래로 실행됨
- `#` 뒤는 **주석** — 컴퓨터가 무시함

```python
# 이것은 주석입니다 (실행 안 됨)
print("Hello!")   # Hello! 를 화면에 출력
```

> 파이썬 파일을 실행하면 위에서부터 한 줄씩 읽어 내려갑니다.

---

## 기본 자료형(Data Type)

파이썬은 값의 종류(자료형)를 자동으로 구분합니다.

```python
age = 17          # int   — 정수 (소수점 없는 숫자)
height = 173.5    # float — 실수 (소수점 있는 숫자)
name = "철수"     # str   — 문자열 (따옴표로 감쌈)
is_pass = True    # bool  — 참/거짓 (True 또는 False)
```

`type()` 함수로 자료형을 확인할 수 있습니다:

```python
print(type(age))      # <class 'int'>
print(type(name))     # <class 'str'>
print(type(is_pass))  # <class 'bool'>
```

---

## 실습 A — 자료형 확인

아래 코드를 Python IDLE 또는 메모장에서 작성하고 실행해 보세요.

```python
my_name = "홍길동"
my_age = 17
my_score = 99.5
is_winner = True

print(my_name, "나이:", my_age)
print(type(my_name))
print(type(my_age))
print(type(my_score))
```

**출력 결과 예시:**
```
홍길동 나이: 17
<class 'str'>
<class 'int'>
<class 'float'>
```

---

## 산술 연산자

```python
a = 10
b = 3

print(a + b)   # 13   덧셈
print(a - b)   # 7    뺄셈
print(a * b)   # 30   곱셈
print(a / b)   # 3.333...  나눗셈 (결과가 float)
print(a // b)  # 3    몫만 (정수 나눗셈)
print(a % b)   # 1    나머지
```

---

## 게임에서 연산자가 쓰이는 곳

```python
SPEED = 5
player_x = 300

# 방향키를 누르면
player_x = player_x - SPEED   # 왼쪽으로 5 이동
player_x = player_x + SPEED   # 오른쪽으로 5 이동

# 줄여서 쓸 수 있음
player_x -= SPEED   # 위와 같음
player_x += SPEED   # 위와 같음
```

**`+=` 와 `-=` 는 자주 사용하니 기억해 두세요!**

---

## 실습 B — 연산자 계산

빈칸을 채워서 이동 거리를 계산하세요.

```python
x = 300
speed = 5

# 왼쪽으로 2번 이동하면?
x = x - speed
x = x - speed
print("2번 왼쪽 이동 후 x:", x)   # 290이 출력되어야 함

# 오른쪽으로 3번 이동하면?
x ___ speed
x ___ speed
x ___ speed
print("3번 오른쪽 이동 후 x:", _____)  # 305가 출력되어야 함
```

---

## print()와 f-string

변수 값을 문자열에 넣는 방법:

```python
score = 42
name = "철수"

# 방법 1: 쉼표로 연결
print("이름:", name, "점수:", score)

# 방법 2: f-string (권장)
print(f"이름: {name}, 점수: {score}")
```

**출력:**
```
이름: 철수 점수: 42
이름: 철수, 점수: 42
```

f-string은 `f"..."` 처럼 `f` 를 앞에 붙이고, `{변수명}` 으로 값을 삽입합니다.

---

## 실습 C — f-string 출력

빈칸을 채워서 아래 출력이 나오도록 하세요.

```python
player = "나"
score = 0

# "나 의 현재 점수: 0점" 이 출력되어야 함
print(f"___ 의 현재 점수: ___점")
```

**정답:**
```python
print(f"{player} 의 현재 점수: {score}점")
```

---

# 1교시: 변수 — 값을 저장하는 상자

---

## 변수란?

프로그램이 값을 기억해야 할 때 사용합니다.

**비유:** 이름표가 붙은 상자에 물건을 넣으면 나중에 꺼낼 수 있습니다.

```python
name = "철수"        # name 상자에 "철수"를 넣음
score = 0            # score 상자에 0을 넣음
x = 300              # x 상자에 300을 넣음
```

나중에 값을 바꿀 수도 있습니다:

```python
score = score + 10   # score를 꺼내서 10을 더하고 다시 넣음
print(score)         # 10 출력
```

---

## Pygame Zero 기초: Actor(캐릭터)

게임에서 움직이는 물체를 `Actor` 로 만듭니다.

```python
import pgzrun

WIDTH = 600     # 화면 가로 크기
HEIGHT = 450    # 화면 세로 크기

# images/player.png 파일을 자동으로 불러옴
player = Actor('player')
player.x = 300    # x 좌표 (왼쪽 끝 = 0, 오른쪽 끝 = 600)
player.y = 400    # y 좌표 (위쪽 끝 = 0, 아래쪽 끝 = 450)

def draw():
    screen.clear()   # 매 프레임마다 화면을 지움
    player.draw()    # 캐릭터를 그림

def update():
    pass             # 게임 상태 변경 (나중에 채움)

pgzrun.go()
```

---

## Pygame Zero의 두 핵심 함수

### draw() — 화면에 뭘 그릴까?
매 프레임(1초에 60번) 자동으로 호출됩니다.

```python
def draw():
    screen.clear()
    player.draw()
    screen.draw.text(f"Score: {score}", (20, 20), fontsize=30, color=(255,255,255))
```

### update() — 게임 상태를 어떻게 바꿀까?
마찬가지로 매 프레임 자동으로 호출됩니다.

```python
def update():
    player.y += 5    # 매 프레임 y를 5씩 증가 → 아래로 이동
```

---

## 좌표 시스템

```
(0, 0)──────────────── x 증가 ──→ (600, 0)
  │
  │  y 증가
  │
  ↓
(0, 450)                          (600, 450)
```

- 왼쪽 위가 `(0, 0)`
- x가 클수록 오른쪽
- y가 클수록 아래쪽 ← **일반 수학과 반대!**

```python
player.x = 300   # 화면 가운데
player.y = 0     # 화면 맨 위
player.y = 450   # 화면 맨 아래
```

---

## 실습 1 — 플레이어 배치

`game1_skeleton.py` 를 열어서 **TODO 1** 을 채우세요.

```python
# TODO 1: player의 x 좌표를 WIDTH // 2 로 설정해서 화면 중앙에 배치하세요
player.x = ___________________
```

**힌트:** `WIDTH = 600` 이므로 `WIDTH // 2 = 300`

**정답:**
```python
player.x = WIDTH // 2
```

저장 후 실행해 보세요:
```cmd
python game1_skeleton.py
```

---

## 1교시 정리

| 개념 | 예시 |
|------|------|
| 변수 대입 | `score = 0` |
| 변수 변경 | `score += 10` |
| Actor 생성 | `player = Actor('player')` |
| 좌표 설정 | `player.x = 300` |
| 자동 호출 | `draw()`, `update()` |

다음 교시에서는 **"언제 움직이냐"** 를 결정하는 조건문을 배웁니다.

---

# 2교시: 조건문 — 상황에 따라 다르게

---

## 조건문이란?

**신호등:** 빨간불이면 멈추고, 파란불이면 가세요.

```python
if score >= 100:
    print("최고!")
elif score >= 50:
    print("잘 하고 있어!")
else:
    print("계속 해봐!")
```

## 조건문 구조

```python
if 조건:          # 조건이 참(True)이면
    실행할 코드
elif 다른 조건:   # 위 조건이 거짓이고, 이 조건이 참이면
    실행할 코드
else:             # 모든 조건이 거짓이면
    실행할 코드
```

> 들여쓰기(스페이스 4칸)가 필수입니다. 들여쓰기가 틀리면 오류 발생!

---

## 비교 연산자

```python
x > 5     # x가 5보다 크다
x < 5     # x가 5보다 작다
x == 5    # x가 5와 같다   (= 는 대입, == 는 비교!)
x != 5    # x가 5와 다르다
x >= 5    # x가 5 이상 (5 포함)
x <= 5    # x가 5 이하 (5 포함)
```

**자주 하는 실수:**

```python
score = 10       # 대입 (= 하나)
score == 10      # 비교 (= 두 개) → True
```

---

## 실습 2 — 조건문 작성

점수에 따라 다른 메시지를 출력하는 코드를 완성하세요.

```python
score = 75

if _____________________:
    print("대단해! 100점 이상!")
elif _____________________:
    print("잘 하고 있어! 50점 이상!")
else:
    print("아직 50점 미만, 계속 도전!")
```

**정답:**
```python
if score >= 100:
    print("대단해! 100점 이상!")
elif score >= 50:
    print("잘 하고 있어! 50점 이상!")
else:
    print("아직 50점 미만, 계속 도전!")
```

---

## Pygame Zero: 키보드 입력

`keyboard` 객체로 어떤 키가 눌렸는지 확인합니다.

```python
SPEED = 5

def update():
    if keyboard.left:         # 왼쪽 방향키가 눌린 동안
        player.x -= SPEED    # x를 줄임 (왼쪽으로 이동)
    
    if keyboard.right:        # 오른쪽 방향키가 눌린 동안
        player.x += SPEED    # x를 늘림 (오른쪽으로 이동)
```

> `update()` 는 1초에 60번 호출되므로, 키를 누르고 있으면 계속 이동합니다.

---

## 경계 체크(Boundary Check)

화면 밖으로 나가지 못하게 막습니다.

```python
WIDTH = 600

def update():
    if keyboard.left:
        player.x -= SPEED
    if keyboard.right:
        player.x += SPEED
    
    # 왼쪽 끝 이상 나가면 강제로 되돌림
    if player.x < 32:
        player.x = 32
    
    # 오른쪽 끝 이상 나가면 강제로 되돌림
    if player.x > WIDTH - 32:
        player.x = WIDTH - 32
```

> `32` 는 캐릭터 이미지 크기의 절반(64px / 2)입니다.

---

## 실습 3 — 키보드 이동 + 경계 체크

`game1_skeleton.py` 를 열어서 **TODO 2, 3, 4, 5** 를 채우세요.

```python
# TODO 2: 좌측 방향키를 누르면 player.x를 SPEED만큼 감소시키세요
if keyboard.left:
    player.x -= ___________________

# TODO 3: 우측 방향키를 누르면 player.x를 SPEED만큼 증가시키세요
if keyboard.right:
    player.x += ___________________

# TODO 4: 왼쪽 경계 체크
if player.x < 32:
    ___________________

# TODO 5: 오른쪽 경계 체크
if player.x > WIDTH - 32:
    ___________________
```

---

## 충돌 감지(Collision Detection)

두 Actor가 겹쳤는지 확인합니다.

```python
player = Actor('player')
coin = Actor('coin')

if player.colliderect(coin):
    print("동전을 잡았다!")
    score += 10
```

`colliderect()` 는 두 캐릭터의 사각형 영역이 겹치면 `True` 를 반환합니다.

---

## 실습 4 — 동전 충돌 + 게임 오버

`game1_skeleton.py` 에서 **TODO 6, 7, 8, 9** 를 채우세요.

```python
# TODO 6: 동전이 아래로 떨어지게
coin.y += ___________________

# TODO 7: 장애물이 아래로 떨어지게
obstacle.y += ___________________

# TODO 8: 동전과 충돌하면 점수 +10
if ___________________:
    score += 10
    coin.x = random.randint(32, WIDTH - 32)
    coin.y = 0

# TODO 9: 장애물과 충돌하면 게임 오버
if ___________________:
    game_over = True
    return
```

---

## 2교시 정리

| 개념 | 예시 |
|------|------|
| 조건문 | `if score >= 50:` |
| 비교 연산자 | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| 키보드 입력 | `if keyboard.left:` |
| 경계 체크 | `if player.x < 32: player.x = 32` |
| 충돌 감지 | `player.colliderect(coin)` |

게임 1 완성! 실행해서 동전을 잡아보세요.

```cmd
python game1_skeleton.py
```

---

# 2.5교시: 함수 — 코드를 묶어서 재사용하기

---

## 함수란?

같은 코드를 여러 번 쓰지 않고 묶어서 이름을 붙입니다.

```python
# 함수 없이
print("=====")
print("안녕!")
print("=====")

print("=====")   # 또 써야 함...
print("잘 가!")
print("=====")

# 함수로 묶으면
def 구분선():
    print("=====")

구분선()   # 함수 호출
print("안녕!")
구분선()

구분선()
print("잘 가!")
구분선()
```

---

## 함수 기본 구조

```python
def 함수이름():        # def + 함수이름 + () + 콜론
    실행할 코드        # 들여쓰기(4칸) 필수!
    실행할 코드
```

### 매개변수(Parameter) — 함수에 값 전달

```python
def greet(name):           # name이 매개변수
    print(f"안녕, {name}!")

greet("철수")    # "안녕, 철수!" 출력
greet("영희")    # "안녕, 영희!" 출력
```

### 반환값(return) — 함수에서 값 돌려받기

```python
def add(a, b):
    return a + b       # 결과를 반환

result = add(3, 5)
print(result)          # 8 출력
```

---

## global 키워드

함수 안에서 **함수 바깥의 변수**를 수정하려면 `global` 을 선언해야 합니다.

```python
score = 0       # 바깥 변수

def add_score():
    global score         # "바깥의 score를 사용하겠다" 선언
    score += 10

add_score()
print(score)    # 10
```

> `global` 없이 수정하면 오류가 발생합니다. 게임 코드에서 자주 등장하니 기억하세요!

---

## 게임에서 함수가 쓰이는 곳

`reset_game()` 함수 — R 키를 누르면 게임을 처음부터 다시 시작

```python
score = 0
game_over = False

def reset_game():
    global score, game_over    # 바깥 변수를 수정할 예정
    score = 0
    game_over = False
    player.x = WIDTH // 2
    player.y = HEIGHT - 50
    coin.x = random.randint(32, WIDTH - 32)
    coin.y = 0

def update():
    if game_over:
        if keyboard.r:
            reset_game()    # 함수 호출
```

---

## 실습 5 — 함수 작성

아래 함수를 완성하세요.

```python
# 두 수를 받아서 더 큰 수를 반환하는 함수
def max_value(a, b):
    if ___________________:
        return ___________________
    else:
        return ___________________

print(max_value(10, 20))   # 20 출력
print(max_value(99, 3))    # 99 출력
```

**정답:**
```python
def max_value(a, b):
    if a > b:
        return a
    else:
        return b
```

---

## 2.5교시 정리

| 개념 | 예시 |
|------|------|
| 함수 정의 | `def greet():` |
| 함수 호출 | `greet()` |
| 매개변수 | `def greet(name):` |
| 반환값 | `return result` |
| global | `global score` |

**Pygame Zero에서 `draw()`, `update()` 도 함수입니다!**  
Pygame Zero가 자동으로 호출해 주는 특별한 함수들입니다.

---

# 3교시: 리스트와 반복문 — 여러 개를 한꺼번에

---

## 리스트란?

여러 개의 값을 하나의 변수에 저장합니다.

**비유:** 바구니에 여러 과일을 담는 것처럼.

```python
fruits = ["사과", "바나나", "딸기"]

print(fruits[0])   # "사과"  (인덱스는 0부터 시작)
print(fruits[1])   # "바나나"
print(fruits[2])   # "딸기"
print(len(fruits)) # 3  (항목 개수)
```

### 리스트 수정

```python
obstacles = []              # 빈 리스트 생성
obstacles.append("장애물1") # 항목 추가
obstacles.remove("장애물1") # 항목 제거
print(len(obstacles))      # 0
```

---

## for 반복문

같은 작업을 여러 번 반복합니다.

### range() 사용

```python
for i in range(5):         # 0, 1, 2, 3, 4 순서로 반복
    print(i)

for i in range(1, 6):      # 1, 2, 3, 4, 5 순서로 반복
    print(i)
```

### 리스트 순회

```python
fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:       # 리스트의 각 항목을 순서대로
    print(fruit)
```

---

## 실습 6 — for 반복문

빈칸을 채워서 1부터 5까지의 합계를 계산하세요.

```python
total = 0

for i in range(_____________________):
    total ___ i

print("합계:", total)   # 합계: 15 가 출력되어야 함
```

**정답:**
```python
total = 0

for i in range(1, 6):
    total += i

print("합계:", total)
```

---

## 게임에서 리스트가 쓰이는 곳

장애물이 여러 개일 때 리스트로 관리합니다.

```python
obstacles = []   # 빈 리스트

# 장애물 3개 생성
for i in range(3):
    obs = Actor('obstacle')
    obs.x = random.randint(32, WIDTH - 32)
    obs.y = -50 - (i * 100)   # 서로 다른 y 위치
    obstacles.append(obs)

# 모든 장애물 이동
for obstacle in obstacles:
    obstacle.y += obstacle_speed
```

---

## 리스트에서 항목 제거하기

반복 중에 리스트를 바꾸면 오류가 납니다. **복사본** 을 순회하세요.

```python
# 화면 밖으로 나간 장애물 제거
obstacles_to_remove = []   # 제거할 목록

for obstacle in obstacles[:]:  # [:] 는 리스트 복사본
    if obstacle.y > HEIGHT:
        obstacles_to_remove.append(obstacle)

for obstacle in obstacles_to_remove:
    obstacles.remove(obstacle)
```

---

## 실습 7 — game2_skeleton.py 작업

`game2_skeleton.py` 를 열어서 **TODO 1~6** 을 채우세요.

```python
# TODO 1: 빈 리스트 생성
obstacles = ___________________

# TODO 2: 초기 장애물 3개 배치
for i in range(3):
    obs = Actor('obstacle')
    obs.x = ___________________
    obs.y = ___________________
    obstacles.append(obs)

# TODO 3: draw() 안에서 모든 장애물 그리기
for obstacle in ___________________:
    ___________________
```

---

## 실습 7 이어서 — TODO 4~6

```python
# TODO 4: 모든 장애물 아래로 이동
for obstacle in ___________________:
    obstacle.y += ___________________

# TODO 5: 화면 밖 장애물 제거
obstacles_to_remove = []
for obstacle in obstacles[:]:
    if obstacle.y > HEIGHT:
        ___________________
for obstacle in obstacles_to_remove:
    ___________________

# TODO 6: 충돌 감지 (모든 장애물과 확인)
for obstacle in ___________________:
    if ___________________:
        game_over = True
        return
```

---

## 난이도 점진적 상승

`frame_count` 를 이용해 시간이 지날수록 어렵게 만듭니다.

```python
frame_count = 0          # 게임이 시작되고 흐른 프레임 수
obstacle_speed = 3

def update():
    global frame_count, obstacle_speed
    frame_count += 1
    
    # 3초마다 새 장애물 추가 (60fps × 3초 = 180프레임)
    if frame_count % 180 == 0:
        new_obstacle = Actor('obstacle')
        new_obstacle.x = random.randint(32, WIDTH - 32)
        new_obstacle.y = 0
        obstacles.append(new_obstacle)
    
    # 10초마다 속도 증가 (60fps × 10초 = 600프레임)
    if frame_count % 600 == 0:
        obstacle_speed += 1
```

---

## 실습 8 — TODO 7, 8 완성

```python
# TODO 7: 3초마다 새 장애물 추가
if ___________________:
    new_obstacle = Actor('obstacle')
    new_obstacle.x = random.randint(32, WIDTH - 32)
    new_obstacle.y = 0
    obstacles.append(new_obstacle)

# TODO 8: 10초마다 속도 증가
if ___________________:
    obstacle_speed += ___________________
```

완성 후 실행:
```cmd
python game2_skeleton.py
```

---

## 생존 시간 점수 표시

```python
frame_count = 0

def draw():
    screen.clear()
    screen.fill((25, 25, 60))   # 어두운 파란색 배경
    
    for obstacle in obstacles:
        obstacle.draw()
    
    player.draw()
    
    # 초로 변환: 프레임 ÷ 60
    survival_time = frame_count // 60
    screen.draw.text(f"Survival: {survival_time}s", (20, 20), fontsize=30, color=(255,255,255))
    screen.draw.text(f"Speed: {obstacle_speed}", (20, 60), fontsize=20, color=(200,200,200))
```

---

## 3교시 정리

| 개념 | 예시 |
|------|------|
| 빈 리스트 | `obstacles = []` |
| 리스트 추가 | `obstacles.append(obs)` |
| 리스트 제거 | `obstacles.remove(obs)` |
| for + range | `for i in range(3):` |
| for + 리스트 | `for obstacle in obstacles:` |
| 시간 계산 | `frame_count // 60` |

---

# 마무리: 도전 과제

---

## 게임 1 도전 과제

완성 후 시도해 볼 것들:

1. **이동 속도 바꾸기:** `SPEED = 5` 를 `SPEED = 8` 로 바꿔보세요.
2. **낙하 속도 바꾸기:** `COIN_SPEED = 3` 을 더 크게 바꿔보세요.
3. **나쁜 동전 추가:** 검은 동전을 받으면 점수가 -5 되게 만들어보세요.
4. **Wrap-around:** 왼쪽 끝을 나가면 오른쪽에서 나타나게 해보세요.
   ```python
   if player.x < 0:
       player.x = WIDTH   # 왼쪽 끝 → 오른쪽 끝으로 순간이동
   ```

---

## 게임 2 도전 과제

1. **장애물 추가 주기 바꾸기:** `180` 을 `120` 으로 바꿔 더 빨리 추가되게 하세요.
2. **속도 증가 주기 바꾸기:** `600` 을 `300` 으로 바꿔 더 빨리 빨라지게 하세요.
3. **여러 방향 장애물:** 위에서만 아니라 옆에서도 오게 만들어보세요.
4. **생명(하트) 시스템:** 장애물에 3번까지 맞아도 괜찮게 만들어보세요.
   ```python
   lives = 3   # 생명 3개

   if player.colliderect(obstacle):
       lives -= 1
       if lives <= 0:
           game_over = True
   ```

---

## 오늘 배운 것 전체 정리

| 문법 | 핵심 |
|------|------|
| 자료형 | `int`, `str`, `float`, `bool` |
| 변수 | `score = 0`, `score += 10` |
| f-string | `f"점수: {score}"` |
| 조건문 | `if`, `elif`, `else` |
| 함수 | `def reset_game():` + `global` |
| 리스트 | `[]`, `.append()`, `.remove()` |
| 반복문 | `for i in range(3):` |
| Pygame Zero | `Actor`, `draw()`, `update()`, `keyboard`, `colliderect()` |

---

## 더 배우고 싶다면

- **Pygame Zero 공식 문서:** https://pygame-zero.readthedocs.io
- **파이썬 공식 튜토리얼(한국어):** https://docs.python.org/ko/3/tutorial/
- **더 많은 게임 아이디어:**
  - 슈팅 게임: 총알 리스트 + for 반복문
  - 퍼즐 게임: 2차원 리스트(리스트 안의 리스트)
  - RPG 게임: 딕셔너리(`{}`) + 함수

---

## 마지막 조언

프로그래밍을 잘 하는 방법:

- **작은 부분부터:** 한 번에 한 TODO씩 채우세요.
- **자주 실행:** 조금 수정할 때마다 `python game1_skeleton.py` 로 확인하세요.
- **오류를 두려워하지 말 것:** 오류 메시지를 읽으면 어디가 문제인지 알 수 있습니다.
- **창의력 발휘:** 규칙을 바꾸고 숫자를 바꿔서 나만의 게임을 만들어보세요.

**오늘 수업 수고하셨습니다!**
