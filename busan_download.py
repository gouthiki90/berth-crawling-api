import requests
import crud.no_connection_test as no_connection_test
from datetime import datetime, timedelta

# 부산


def busan_download():
    data_check_list = []
    # 날짜 세팅
    now = datetime.now()

    before = now - timedelta(days=1)
    after = before + timedelta(days=8)

    # busan url
    main_url = 'http://apis.data.go.kr/B551220/vsslBerthStatService/getVsslBerthStatList?'
    service_key = 'serviceKey=9tYWVSjyoaIk2zT%2F0sJB81RO1McEvujAkH4lc9bKcT55hdcJAEiCt78hs40eByd3KlX5DyVcXBO0qYht01W5eA%3D%3D'
    query_type = '&dataType=JSON'
    query_page = "&pageNo=1"
    query_rows = '&numOfRows=3000'
    query_date = '&startDate={}&endDate={}'.format(
        before.strftime("%Y%m%d"), after.strftime("%Y%m%d"))

    req_url_BS = main_url + service_key + query_type + \
        query_page + query_rows + query_date

    print(req_url_BS)

    try:
        response = requests.get(req_url_BS)

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

            result['csdhpPrarnde'] = result['csdhpPrarnde'][0:-3]
            data_check_list.append(result)

        if data_check_list == None:
            return []
        else:
            no_connection_test.postToHangman(data_check_list)

    except Exception as e:
        print(e)
    finally:
        response.close()
