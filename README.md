Room Escape Reservation Macro

방탈출 예약 사이트의 예약 과정을 자동화하기 위한 Python 프로젝트입니다.

Playwright를 이용하여 방탈출 사이트에 접속하고, 원하는 날짜와 테마의 예약 가능 시간을 확인한 뒤 예약 정보를 입력하여 예약하는 기능을 구현합니다.

Features
예약 사이트 접속
원하는 날짜 선택
테마 선택 및 검색
예약 가능 시간 조회
원하는 시간대 필터링
예약자 정보 입력
예약 인원 선택
이용약관 동의
예약 진행
예약 가능한 시간이 없을 경우 주기적으로 확인하는 기능 (개발 예정)
여러 방탈출 사이트 지원 (개발 예정)
Tech Stack
Python
Playwright
Git / GitHub
Project Structure
room_escape_macro/
├── main.py
├── config.py
├── config_local.py
├── browser.py
├── reservation.py
├── notifier.py
├── .gitignore
└── README.md
주요 파일
main.py

프로그램의 전체 실행 흐름을 관리합니다.

reservation.py

방탈출 예약 사이트의 페이지 조작 및 예약 기능을 담당합니다.

날짜 선택
예약 가능 시간 검색
예약 정보 입력
인원 선택
약관 동의
예약 진행
browser.py

Playwright 브라우저의 생성 및 초기 설정을 담당합니다.

config.py

예약 날짜, 테마, 시간대 등 Git에 공유해도 되는 설정을 관리합니다.

config_local.py

이름, 전화번호, 이메일 등 개인 정보를 관리합니다.

config_local.py는 개인정보 보호를 위해 Git에 포함하지 않습니다.

notifier.py

예약 가능 여부 등의 결과를 사용자에게 알리는 기능을 담당합니다.

Configuration
config.py
DATE = "2026-10-10"
THEME_NAME = "꼬치 진다"
START_TIME = "1400"
END_TIME = "1700"
PLAYER = 4
config_local.py
NAME = "홍길동"
PHONE_NUMBER = "1012345678"
EMAIL = "example@email.com"

config_local.py는 .gitignore에 등록하여 Git에 업로드하지 않습니다.

Installation

Python 가상환경을 생성한 후 필요한 패키지를 설치합니다.

python -m venv .venv

가상환경을 활성화합니다.

Windows PowerShell:

.venv\Scripts\Activate.ps1

Playwright를 설치합니다.

pip install playwright

필요한 브라우저를 설치합니다.

playwright install
Usage

설정을 완료한 후 다음 명령으로 실행합니다.

python main.py

프로그램은 설정된 날짜와 테마를 기준으로 예약 가능 시간을 확인하고 예약 과정을 진행합니다.

Supported Sites

현재:

Showroom404

지원 예정:

추가 방탈출 예약 사이트

사이트마다 HTML 구조와 예약 방식이 다르기 때문에 사이트별 예약 객체를 분리하여 구현할 예정입니다.

Development Roadmap
Completed

Playwright 기반 브라우저 자동화

날짜 선택

테마 조회

예약 가능 시간 검색

시간대 필터링

예약자 정보 입력

예약 인원 선택

약관 동의

예약 실행

TODO

예약 가능한 시간이 없을 경우 반복 조회

예약 가능 시간 발견 시 자동 예약

예약 실패 및 예외 처리

예약 결과 알림 개선

여러 방탈출 사이트 지원

사이트별 예약 로직 분리 및 공통 인터페이스 설계

Security

개인정보 및 민감한 설정은 Git 저장소에 업로드하지 않습니다.

다음 파일은 .gitignore에 포함되어야 합니다.

config_local.py

GitHub에 업로드하기 전에 개인정보가 포함된 파일이 commit 대상에 포함되어 있지 않은지 확인합니다.

Disclaimer

본 프로젝트는 개인적인 학습 및 자동화 구현을 목적으로 개발되었습니다.

각 예약 사이트의 이용약관 및 자동화 정책을 확인하고 적절하게 사용해야 합니다.
