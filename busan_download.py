import requests
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

        if data_check_list == None:
            return []
        else:
            print("busan" + "-"*30)
            print(data_check_list)
            no_connection_test.postToHangman(data_check_list)
            print("busan" + "-"*30)

    except Exception as e:
        print(e)
    finally:
        response.close()
