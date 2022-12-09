import requests

# requests 기본 데이터
post_url = 'http://localhost:3001/api/v1/berthStatPy/'
post_busan_url = 'http://localhost:3001/api/v1/berthStatPy/busan'
post_jan_url = 'http://54.180.73.195/receive'
post_hangman_url = 'http://localhost:3040/berth-py'

headers = {
    'Content-Type': 'application/json; charset=utf-8'
}


# post
def post(result):
    respone = requests.post(post_url, json=result, headers=headers)
    respone.close()


def postToHangman(result):
    respone = requests.post(post_hangman_url, json=result, headers=headers)
    respone.close()


def postBusan(result):
    respone = requests.post(post_busan_url, json=result, headers=headers)
    respone.close()


def postJan(result):
    response = requests.post(post_jan_url, json=result, headers=headers)
    response.close()


def put(result, key):
    send = [result, {"key": key}]
    response = requests.put(post_url, json=send, headers=headers)
    response.close()
