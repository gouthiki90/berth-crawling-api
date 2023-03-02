import requests
import crud.no_connection_test as no_connection_test

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

            if result['trminlCode'] == "BPTG":
                result['oid'] = result['trminlVoyg'] + '-' + "BPTG"
            else:
                result['oid'] = result['trminlVoyg']

            data_check_list.append(result)

        if data_check_list == None:
            return []
        else:
            no_connection_test.postToHangman(data_check_list)

    except Exception as e:
        print(e)
    finally:
        response.close()
