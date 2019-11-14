import requests
import time
import json
import random

CONFIG = {
    'granularity': 1,
    'metric': 1000,
    'start': 1514736000,
    'total': 1000000
}

count = 0
success = 0
failed = 0


def send_json(json, s):
    r = s.post("http://localhost:4242/api/put?details", json=json)
    return r.text


def generate_point(metric, ts, value, ty):
    """

    :param metric: str
    :param ts: int
    :param value: float
    :param ty: str
    :return: dict
    """
    point = {
        "metric": metric,
        "timestamp": ts,
        "value": value,
        "tags": {
            "host": "web01",
            "type": ty
        }
    }
    return point


def post_one_metric(metric):
    s = requests.Session()
    global count
    global success
    global failed
    for ty in ['1', '2', '3']:
        result = []
        end_time = CONFIG['start'] + CONFIG['total'] * CONFIG['granularity'] // CONFIG['metric']
        current_time = CONFIG['start']
        while current_time < end_time:
            result.append(generate_point(metric, current_time, random.randint(0, 100), ty))
            current_time += CONFIG['granularity']
            count += 1
            if len(result) == 1000:
                temp = send_json(result, s)
                temp = json.loads(temp)
                success += temp['success']
                failed += temp['failed']
                result = []
            if count % 10000 == 0:
                print(count)


def post_all_metric():
    for i in range(CONFIG['metric']):
        metric = 'test.metric%d' % i
        post_one_metric(metric)


def main():
    post_all_metric()


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    print("%d record time used: %f" % (count, t2 - t1))
    print("success: %d" % success)
    print("failed: %d" % failed)
