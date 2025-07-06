
import time
import requests
import datetime
from hx711 import HX711

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
    url = "http://<FASTAPI_SERVER_IP>:8000/log"
    payload = {
        "cat_id": 1,
        "feeding_time": datetime.datetime.now().isoformat(),
        "food_amount": weight,
        "behavior_notes": "정상 급식"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("데이터 전송 성공")
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
