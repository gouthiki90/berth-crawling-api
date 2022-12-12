import requests
from my_sql_connection import select_container
from no_connection_test import putToHangman


def download_etrans(url):
    # 조회할 컨테이너 select
    container_list = select_container()

    if len(container_list) == 0:
        return []

    # list를 토대로 요청
    for index, result in enumerate(container_list, 1):
        print(result)

        default_data = {
            "dma_search": {
                "KLNET_ID": "{}".format(result['CNTR_NO']),
                "SEARCH_DATA": "FSCU5909470",
                "NOTICE_CNT": 25
            }
        }

        # eTrans 요청
        response = requests.post(url, json=default_data)
        container_response_data = response.json()

        # nest.js로 전송
        putToHangman(container_response_data)
