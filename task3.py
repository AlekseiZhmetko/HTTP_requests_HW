import requests
from pprint import pprint
import time

epoch_time_now = int(time.time())
epoch_time_target = epoch_time_now - 172800
print(epoch_time_now)
print(epoch_time_target)
# epoch_time_now = 0
# epoch_time_target = 0

def get_from_stackoverflow(url, params):
    r = requests.get(url, params)
    python_q = r.json()
    python_q_title_list = []
    for i in python_q['items']:
        for k, v in i.items():
            if k == 'title':
                python_q_title_list.append(v)
    pprint(python_q_title_list)

if __name__ == '__main__':
    q_url = 'https://api.stackexchange.com/2.3/search/advanced'
    q_params = {'order': 'desc', 'tagged': 'python', 'site': 'stackoverflow',
              'fromdate': f'{epoch_time_target}', 'todate': f'{epoch_time_now}'}
    get_from_stackoverflow(url=q_url, params=q_params)