import requests, random

load_balancer_post: int = 1337

submit_url = f"http://127.0.0.1:{load_balancer_post}/submit"

while True:
    if random.random() > 0.1:
        _ = random.randint(1, 100)
        requests.post(submit_url, data={"main": _})
        print(f"Spammed load balancer with {_}")
