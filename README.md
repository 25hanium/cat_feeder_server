# cat_feeder_server
# 프로젝트 구조 요약

cat_feeder_server-main/

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── README.md

├── app/

│   ├── main.py              ← FastAPI 실행 진입점

│   ├── database.py          ← DB 연결 설정

│   ├── models.py            ← SQLAlchemy 모델 정의

│   ├── schemas.py           ← Pydantic 스키마 정의

│   └── routers/

│       └── feeding.py       ← feeding 관련 API 라우터

├── rpi_sensor_post/

│   └── read_weight.py       ← 라즈베리파이 센서 데이터 전송 코드

# 의존성 설치

Docker 기반으로 실행되므로 다음 명령어를 사용하세요:

docker-compose up --build

> MySQL 8.0과 FastAPI 백엔드가 컨테이너로 실행됩니다.

# Docker 컨테이너 설명

- cat-feeder-db: MySQL DB 컨테이너 (DB명: cat_feeder)
- cat-feeder-api: FastAPI 애플리케이션 컨테이너 (포트: 8000)

# FastAPI 서버 사용

API가 정상 작동하면 브라우저에서 다음 주소로 접속하여 Swagger 문서를 확인할 수 있습니다:
http://localhost:8000/docs

# 라즈베리파이에서 센서 데이터 전송

rpi_sensor_post/read_weight.py는 측정한 무게 데이터를 FastAPI 서버로 전송하는 예제입니다.

사용법

pip install requests
python rpi_sensor_post/read_weight.py

해당 스크립트는 http://<서버주소>:8000/feeding/ 엔드포인트로 POST 요청을 보냅니다.

# 데이터베이스 수동 접속 (선택)

docker exec -it cat-feeder-db mysql -u root -p <br> # password: root

# 앞으로 수행 또는 해결해야할 점

현재 제 컴퓨터의 이상인지 아니면 또다른 문제인지 모르겠으나 데이터베이스에 접속이 안되는 중 추가적으로 진행할 예정
라즈베리파이의 스크립트가 정상적으로 전송되는지 확인 (수요일에 확인할 예정)
