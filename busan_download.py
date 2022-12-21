import requests
import my_sql_connection
import data_check_all
import no_connection_test

# 부산


def busan_download(req_url):
    data_check_list = []
    try:
        response = requests.get(req_url)

        # JSON 파싱
        result = response.json()

        # item까지 접근
        response_obj = result["response"]
        body = response_obj['body']
        items = body['items']
        item = items['item']

        for index, result in enumerate(item, 1):
            result['oid'] = result['trminlVoyg']
            data_check_list.append(result)

        now_data = my_sql_connection.select_busan_all()
        checked_data = data_check_all.data_check(data_check_list, now_data)

        # no_connection_test.post(checked_data)
        no_connection_test.postJan(data_check_list)
        no_connection_test.postToHangman(data_check_list)

    except Exception as e:
        print(e)
    finally:
        response.close()
