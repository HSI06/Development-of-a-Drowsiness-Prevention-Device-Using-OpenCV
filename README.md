# Development of a Drowsiness Prevention Device Using OpenCV
## OpenCV 졸음방지 디바이스 만들기

---

## 프로젝트 소개

OpenCV의 Haar Cascade 분류기를 활용하여 웹캠 영상에서 실시간으로 얼굴과 눈을 감지하고,
눈이 감기면 라즈베리파이 GPIO 16번 핀에 연결된 능동 부저로 경보음을 울리는 졸음방지 디바이스입니다.

---

## 준비물 및 회로 연결

| 부품 | 수량 |
|------|------|
| 브레드보드 | 1개 |
| 능동 부저 | 1개 |
| 암/수 점퍼케이블 | 2개 |

| 연결 | GPIO 핀 |
|------|---------|
| 능동 부저 (+) | GPIO 16 |
| 능동 부저 (-) | GND (34번) |

---

## 동작 흐름

카메라 실행 → 매 프레임 얼굴 감지 → 얼굴 영역 내 눈 탐지
→ 눈 2개 이상: 정상 → 부저 OFF
→ 눈 1개 이하: 졸음 → 부저 ON
→ q 키 입력 시 종료

---

## 파일 구성

project_34/
├── main34.py       # 얼굴·눈 인식 시각화 (부저 없음)
└── main34-1.py     # 졸음 감지 시 부저 작동 (최종 버전)

---

## 실행 방법

```bash
# 가상환경 활성화
source 나의가상환경/bin/activate

# 프로젝트 폴더 이동
cd 나의프로젝트폴더/myProjects/project_34

# 라이브러리 설치
pip install gpiozero

# 1단계: 얼굴·눈 시각화 확인
python main34.py

# 2단계: 졸음방지 부저 작동
python main34-1.py
```
