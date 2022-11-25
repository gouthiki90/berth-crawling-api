import requests
import my_sql_connection
import no_connection_test
import data_check_all


def pyeongtack_download(req_url, query_date, query_sort, query_page):
    data_check_list = []
    try:
        response = requests.get(req_url + query_date + query_sort + query_page)

        # JSON 파싱
        result = response.json()

        # content 접근
        data = result['content']

        for index, result in enumerate(data, 1):

            # dict 만들기
            send_data = {
                "oid": result['VOY_NO'],
                "trminlCode": "PCCT",  # 터미널코드
                "trminlVoyg": result['VOY_NO'],  # 모선항차
                "workStarDay": result['ATW'],  # 작업시작
                "shipment": result['LOAD_QTY'],  # 선적
                "csdhpPrarnde": result['ATA'],  # 입항일시
                "tkoffPrarnde": result['ATD'],  # 출항일시
                "landngQy": result['DIS_QTY'],  # 양하수량
                "shifting": result['SHIFT_QTY'],  # s/h
                "berthCode": result['BERTH_NO'],  # 선석코드
                "wtorcmpCode": result['PTNR_CODE'],  # 선사코드
                "shipRute": result['IN_LANE'],  # 항로
                "csdhpDrc": result['ALONGSIDE'],  # 접안/접안방향
                "workFiniDay": result['ATC'],  # 작업완료
                "predBerth": result['MOVE_TMNL'],  # 전배
                "carryFiniDay": result['YARD_CLOSE']  # 반입마감
            }
            data_check_list.append(send_data)

        now_data = my_sql_connection.select_all("PCCT")
        checked_data = data_check_all.data_check(data_check_list, now_data)
        # no_connection_test.post(checked_data)
        no_connection_test.postJan(checked_data)
        no_connection_test.postToHangman(data_check_list)

    except Exception as e:
        response.close()
        print(e)
