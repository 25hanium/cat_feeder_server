import pymysql

# RDS 접속 정보 입력
host = "my-hanium-db.ct8466ykusoj.ap-southeast-2.rds.amazonaws.com"
user = "admin"
password = "hanium2025"  
port = 3306
db_name = "cat_feeder"

# RDS 접속 후 데이터베이스 생성
connection = pymysql.connect(host=host, user=user, password=password, port=port)
cursor = connection.cursor()

try:
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    print(f"✅ 데이터베이스 '{db_name}' 생성 완료 또는 이미 존재합니다.")
except Exception as e:
    print("❌ 데이터베이스 생성 중 오류 발생:", e)
finally:
    cursor.close()
    connection.close()
