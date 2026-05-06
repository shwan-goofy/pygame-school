# Pygame Zero 3시간 수업 - 학생용 가이드

## 수업 목표

파이썬 기초 문법(변수, 조건문, 반복문, 함수)을 게임 제작으로 배우는 3시간 커리큘럼.  
스켈레톤 코드의 빈칸을 직접 채우며 2개의 게임을 완성합니다.

---

## 빠른 시작 (Windows)

### PowerShell 사용자

PowerShell을 열고 아래 명령어를 **순서대로** 입력하세요.

```powershell
# 1. 이 프로젝트 폴더로 이동
cd C:\경로\pgzero

# 2. 가상환경 생성
python -m venv venv

# 3. 가상환경 활성화
.\venv\Scripts\Activate.ps1

# 4. pip 최신화
python -m pip install --upgrade pip

# 5. 라이브러리 설치
python -m pip install pgzero Pillow

# 6. 게임 이미지 생성
python make_assets.py

# 7. 게임 실행
python game1_skeleton.py
```

> **PowerShell 오류: "이 시스템에서 스크립트를 실행할 수 없습니다"**  
> 관리자 권한으로 PowerShell을 열고 아래 명령어를 실행한 뒤 다시 시도하세요.
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

---

### 명령 프롬프트(CMD) 사용자

```cmd
:: 1. 이 프로젝트 폴더로 이동
cd C:\경로\pgzero

:: 2. 가상환경 생성
python -m venv venv

:: 3. 가상환경 활성화  (CMD는 .bat 파일 사용)
venv\Scripts\activate.bat

:: 4. pip 최신화
python -m pip install --upgrade pip

:: 5. 라이브러리 설치
python -m pip install pgzero Pillow

:: 6. 게임 이미지 생성
python make_assets.py

:: 7. 게임 실행
python game1_skeleton.py
```

> **가상환경이 활성화되면** 프롬프트 앞에 `(venv)` 가 붙습니다.  
> 예: `(venv) C:\pgzero>`

---

## 폴더 구조

```
pgzero/
├── README.md                      ← 이 파일
├── requirements.txt               ← 라이브러리 목록
├── lesson_slides.md               ← Marp 강의 자료
├── make_assets.py                 ← 이미지 자동 생성 스크립트
├── images/                        ← 게임 이미지 폴더 (자동 생성됨)
│   ├── player.png
│   ├── coin.png
│   └── obstacle.png
├── game1_skeleton.py              ← 학생용: 낙하 게임 (빈칸 채우기)
└── game2_skeleton.py              ← 학생용: 피하기 게임 (빈칸 채우기)
```

---

## 스켈레톤 코드 작업 방법

### 기본 규칙

스켈레톤 파일 안에 `___________________` 로 표시된 빈칸을 채우면 됩니다.  
`# TODO N:` 주석이 무엇을 작성해야 하는지 힌트를 줍니다.

```python
# TODO 1: player의 x 좌표를 WIDTH // 2 로 설정해서 화면 중앙에 배치하세요
player.x = ___________________   ← 여기를 채우세요
```

에디터(메모장, VS Code, IDLE 등)로 파일을 열고 `___________________` 를 찾아 값을 입력한 뒤 저장하면 됩니다.

---

### game1_skeleton.py — 낙하 캐치 게임 (TODO 1~9)

| TODO | 설명 | 힌트 |
|------|------|------|
| TODO 1 | 플레이어를 화면 중앙에 배치 | `WIDTH // 2` |
| TODO 2 | 왼쪽 방향키를 누르면 플레이어 이동 | `SPEED` |
| TODO 3 | 오른쪽 방향키를 누르면 플레이어 이동 | `SPEED` |
| TODO 4 | 왼쪽 화면 경계 넘지 않게 제한 | `player.x = 32` |
| TODO 5 | 오른쪽 화면 경계 넘지 않게 제한 | `player.x = WIDTH - 32` |
| TODO 6 | 동전이 아래로 떨어지게 이동 | `coin_speed` |
| TODO 7 | 장애물이 아래로 떨어지게 이동 | `obstacle_speed` |
| TODO 8 | 플레이어가 동전과 충돌 시 점수 증가 | `player.colliderect(coin)` |
| TODO 9 | 플레이어가 장애물과 충돌 시 게임 오버 | `player.colliderect(obstacle)` |

**실행 방법:**
```cmd
python game1_skeleton.py
```

---

### game2_skeleton.py — 피하기 게임 (TODO 1~8)

| TODO | 설명 | 힌트 |
|------|------|------|
| TODO 1 | 빈 장애물 리스트 만들기 | `[]` |
| TODO 2 | 초기 장애물 3개를 랜덤 위치에 배치 | `random.randint(32, WIDTH - 32)` |
| TODO 3 | 모든 장애물을 화면에 그리기 | `for obstacle in obstacles:` |
| TODO 4 | 모든 장애물을 아래로 이동 | `obstacle_speed` |
| TODO 5 | 화면 밖으로 나간 장애물 제거 | `obstacles_to_remove.append(obstacle)` |
| TODO 6 | 모든 장애물과의 충돌 확인 | `player.colliderect(obstacle)` |
| TODO 7 | 3초마다 새 장애물 추가 | `frame_count % 180 == 0` |
| TODO 8 | 10초마다 장애물 속도 증가 | `frame_count % 600 == 0` |

**실행 방법:**
```cmd
python game2_skeleton.py
```

---

## 수업 진행 순서

### 1교시 (0~60분): 변수와 좌표

1. 강의 자료 열기: `lesson_slides.md` (1교시 섹션)
2. 강의 (15분): 변수, 자료형, 산술 연산자 개념 설명
3. 실습 (35분):
   - `game1_skeleton.py` 열기
   - **TODO 1, 2, 3** 채우기 (플레이어 배치, 이동)
   - 실행: `python game1_skeleton.py`
4. 확인 (10분): 캐릭터가 좌우로 움직이는지 확인

### 2교시 (60~120분): 조건문과 경계 처리

1. 강의 (15분): 조건문(if/else), 비교 연산자 개념 설명
2. 실습 (35분):
   - `game1_skeleton.py` 이어서
   - **TODO 4, 5, 6, 7, 8, 9** 채우기 (경계 체크, 충돌, 점수)
   - 실행: `python game1_skeleton.py`
3. 확인 (10분): 동전 획득, 장애물 충돌, 게임 오버 동작 확인

### 3교시 (120~180분): 반복문과 리스트

1. 강의 (15분): 리스트, for 반복문, 함수(def) 개념 설명
2. 실습 (45분):
   - `game2_skeleton.py` 열기
   - **TODO 1~8** 모두 채우기
   - 실행: `python game2_skeleton.py`
3. 마무리 (10분): 최고 생존 시간 경쟁

---

## 게임 조작 방법

| 키 | 동작 |
|----|------|
| ← 왼쪽 방향키 | 플레이어 왼쪽 이동 |
| → 오른쪽 방향키 | 플레이어 오른쪽 이동 |
| R | 게임 재시작 |
| Q | 게임 종료 |

---

## 게임 설명

### 게임 1: 낙하 캐치 게임

- **목표:** 위에서 떨어지는 동전(노란 원)을 받으면 +10점
- **피해야 할 것:** 빨간 장애물에 닿으면 게임 오버
- **난이도:** 50점 달성 시 속도 1.5배, 100점 달성 시 속도 2배

### 게임 2: 피하기 게임

- **목표:** 장애물을 피하면서 최대한 오래 생존
- **점수:** 생존 시간(초)이 점수
- **난이도:** 3초마다 장애물 추가, 10초마다 속도 증가

---

## 난이도 튜닝 방법

각 스켈레톤 파일 상단에 있는 상수 값을 바꾸면 게임 난이도를 조절할 수 있습니다.

### game1_skeleton.py 상단 상수

```python
SPEED = 5          # 플레이어 이동 속도 (높일수록 빠르게 반응)
COIN_SPEED = 3     # 동전 낙하 속도 (높일수록 어려움)
OBSTACLE_SPEED = 3 # 장애물 낙하 속도 (높일수록 어려움)
```

난이도 상승 타이밍(점수 기준)도 코드 안에서 수정 가능합니다:

```python
# 현재: 50점에서 1.5배, 100점에서 2배
if score >= 50 and difficulty_multiplier == 1.0:    # ← 50을 바꾸면 타이밍 변경
if score >= 100 and difficulty_multiplier == 1.5:   # ← 100을 바꾸면 타이밍 변경
```

### game2_skeleton.py 상단 상수

```python
SPEED = 5          # 플레이어 이동 속도
OBSTACLE_SPEED = 3 # 장애물 낙하 초기 속도
```

장애물 추가/속도 증가 주기도 수정 가능합니다:

```python
# 현재: 3초(180프레임)마다 장애물 추가
if frame_count % 180 == 0:   # ← 작게 바꾸면 더 자주 추가됨

# 현재: 10초(600프레임)마다 속도 증가
if frame_count % 600 == 0:   # ← 작게 바꾸면 더 빨리 빨라짐
```

---

## 문제 해결

### python 명령어를 찾을 수 없다는 오류

```
'python'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.
```

→ `python` 대신 `py` 로 시도하세요.

```cmd
py --version
py -m venv venv
```

→ 그래도 안 되면 [python.org](https://www.python.org/downloads/)에서 Python 3.11 이상 재설치.  
  설치 시 **"Add Python to PATH"** 체크박스를 반드시 체크하세요.

---

### 라이브러리를 찾을 수 없다는 오류

```
ModuleNotFoundError: No module named 'pgzero'
```

→ 가상환경이 활성화된 상태에서 다시 설치하세요. 프롬프트에 `(venv)` 가 보여야 합니다.

```cmd
venv\Scripts\activate.bat
python -m pip install pgzero Pillow
```

---

### 이미지를 찾을 수 없다는 오류

```
FileNotFoundError: images/player.png
```

→ `make_assets.py` 를 먼저 실행하세요.

```cmd
python make_assets.py
```

---

### 게임 창이 뜨지 않음

→ `pgzero` 폴더로 이동했는지 확인하세요.

```cmd
cd C:\경로\pgzero
python game1_skeleton.py
```

---

## 추가 학습 자료

- Pygame Zero 공식 문서: https://pygame-zero.readthedocs.io
- 파이썬 공식 튜토리얼: https://docs.python.org/ko/3/tutorial/
