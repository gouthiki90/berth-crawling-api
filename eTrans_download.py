import requests
from my_sql_connection import select_container
from no_connection_test import putToHangman


def download_etrans(url):
    # 조회할 컨테이너 select
    container_list = select_container()

    try:
        if container_list == None:
            return []
        else:
            # list를 토대로 요청
            for index, result in enumerate(container_list, 1):
                print(result)

                default_data = {
                    "dma_search": {
                        "KLNET_ID": "",
                        "SEARCH_DATA": "{}".format(result['CNTR_NO']),
                        "NOTICE_CNT": 25
                    }
                }

                # eTrans 요청
                response = requests.post(url, json=default_data)
                container_response_data = response.json()

                # nest.js로 전송
                putToHangman(container_response_data)

    except Exception as e:
        print(e)
