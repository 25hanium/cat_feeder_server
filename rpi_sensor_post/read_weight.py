import time, os, json, requests, datetime
from dotenv import load_dotenv
from hx711 import HX711

load_dotenv()
SERVER_IP = os.getenv("3.27.174.25")
CAT_ID = int(os.getenv("CAT_ID", 1))
LOG_PATH = os.getenv("RPI_LOG_PATH", "/home/pi/feeding_logs")
os.makedirs(LOG_PATH, exist_ok=True)

hx = HX711(dout_pin=5, pd_sck_pin=6)
hx.zero()
hx.set_scale_ratio(200)

def read_weight():
    try:
        return hx.get_weight_mean(20)
    except Exception as e:
        print("Weight read error:", e)
        return None

def send_to_api(payload):
    try:
        res = requests.post(f"http://3.27.174.25:8000/log", json=payload)
        print("API Response:", res.status_code, res.text)
        return res.status_code == 200
    except Exception as e:
        print("Send error:", e)
        return False

def log_to_file(payload):
    filepath = os.path.join(LOG_PATH, f"log_{datetime.date.today()}.jsonl")
    with open(filepath, "a") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    while True:
        weight = read_weight()
        if weight is not None:
            payload = {
                "cat_id": CAT_ID,
                "feeding_time": datetime.datetime.now().isoformat(),
                "food_amount": weight,
                "behavior_notes": "정상 급식"
            }
            if not send_to_api(payload):
                log_to_file(payload)
        time.sleep(60)
