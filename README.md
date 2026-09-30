# Room Escape Macro

방탈출 예약 사이트의 예약 과정을 자동화하기 위한 Python 프로젝트입니다.

현재는 `showroom404.com`을 대상으로 개발하고 있으며, 향후 여러 방탈출 예약 사이트를 지원하는 것을 목표로 합니다.

## Features

* 브라우저 자동 실행
* 방탈출 예약 페이지 접속
* 예약 날짜 선택
* 테마별 예약 가능 시간 조회
* 원하는 시간대 검색
* 예약자 정보 입력
* 인원 수 선택
* 이용약관 동의
* 예약 실행
* 예약 가능한 시간이 없을 경우 주기적인 재조회
* 예약 가능 시간 발견 시 자동 예약
* 예약 결과 알림

> 현재 일부 기능은 개발 중입니다.

## Tech Stack

* Python
* Playwright
* Git / GitHub

## Project Structure

```text
room_escape_macro/
├── main.py
├── config.py
├── config_local.py
├── config_local_example.py
├── browser.py
├── reservation.py
├── notifier.py
├── .gitignore
└── README.md
```

### 주요 파일

| 파일                        | 설명                      |
| ------------------------- | ----------------------- |
| `main.py`                 | 프로그램 실행 및 전체 흐름 관리      |
| `config.py`               | 프로그램의 기본 설정             |
| `config_local.py`         | 개인 정보 및 로컬 설정           |
| `config_local_example.py` | 로컬 설정 파일 예시             |
| `browser.py`              | Playwright 브라우저 생성 및 관리 |
| `reservation.py`          | 방탈출 예약 사이트 동작 처리        |
| `notifier.py`             | 예약 결과 및 알림 처리           |

## Installation

### 1. Repository Clone

```bash
git clone https://github.com/tmdwns0907/room_escape_macro.git
cd room_escape_macro
```

### 2. Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install playwright
```

### 4. Install Browser

```bash
playwright install
```

## Configuration

개인 정보는 GitHub에 업로드하지 않도록 별도의 로컬 설정 파일을 사용합니다.

`config_local_example.py`를 복사하여 `config_local.py`를 생성합니다.

`config_local_example.py` → `config_local.py`

`config_local.py`에 개인 정보를 입력합니다.

```python
NAME = "홍길동"
PHONE_NUMBER = "10-0000-0000"
EMAIL = "example@example.com"
```

`config_local.py`는 `.gitignore`에 등록되어 있으므로 GitHub에 업로드하지 않습니다.

## Usage

설정을 완료한 후 다음 명령어로 프로그램을 실행합니다.

```bash
python main.py
```

프로그램이 실행되면 Playwright를 통해 Chrome 브라우저가 실행되고 예약 페이지에 접속합니다.

## Supported Sites

현재 지원하는 사이트:

* Showroom404

향후 다른 방탈출 예약 사이트도 추가할 예정입니다.

## Development Roadmap

* [x] 브라우저 자동 실행
* [x] 예약 페이지 접속
* [x] 날짜 선택
* [x] 테마별 시간 조회
* [x] 원하는 시간대 검색
* [x] 예약자 정보 입력
* [x] 인원 수 선택
* [x] 이용약관 동의
* [x] 예약 실행
* [ ] 예약 가능 여부 주기적 확인
* [ ] 예약 가능 시간 발견 시 자동 예약
* [ ] 예약 성공 / 실패 처리
* [ ] 예약 결과 알림
* [ ] 여러 방탈출 사이트 지원

## Security

개인 정보 및 민감한 설정은 `config_local.py`에 저장합니다.

`config_local.py`는 GitHub에 업로드하지 않으며 `.gitignore`에 등록해야 합니다.

```gitignore
config_local.py
```

실제 개인정보가 포함된 설정 파일을 GitHub에 커밋하지 않도록 주의하세요.

## Disclaimer

이 프로젝트는 개인적인 학습 및 자동화 구현을 목적으로 개발되었습니다.

예약 사이트의 이용약관 및 자동화 정책을 확인하고 적절한 범위에서 사용해야 합니다.
