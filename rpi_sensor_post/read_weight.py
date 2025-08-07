
import time
import requests
import datetime
from hx711 import HX711

load_dotenv()
SERVER_IP = os.getenv("FASTAPI_SERVER_IP", "localhost")    //fast_server api 설정해야 함
CAT_ID = int(os.getenv("CAT_ID", 1))

hx = HX711(dout_pin=5, pd_sck_pin=6)
hx.zero()
hx.set_scale_ratio(200)

def read_weight():
    try:
        weight = hx.get_weight_mean(20)
        print("측정 무게:", weight, "g")
        return weight
    except Exception as e:
        print("무게 측정 실패:", e)
        return None

def send_to_api(weight):
    url = f"http://{SERVER_IP}:8000/log"
    payload = {
        "cat_id": CAT_ID,
        "feeding_time": datetime.datetime.now().isoformat(),
        "food_amount": weight,
        "behavior_notes": "정상 급식"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("데이터 전송 성공")
            print("서버 응답:", response.json())
        else:
            print("전송 실패:", response.status_code, response.text)
    except Exception as e:
        print("API 전송 에러:", e)

if __name__ == "__main__":
    while True:
        weight = read_weight()
        if weight:
            send_to_api(weight)
        time.sleep(60)
