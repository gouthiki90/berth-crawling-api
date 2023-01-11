import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import no_connection_test
from datetime import datetime, timedelta

# 날짜 세팅
now = datetime.now()
print(now)

after = now + timedelta(days=7)
print(after)


def incheon_download():
    data_check_list = []
    get_table_text = []
    page_no = 1

    try:
        while True:
            # incheon req url
            req_url_IC = 'https://scon.icpa.or.kr/vescall/list.do'
            query_date_IC = '?searchStartDt={}&searchEndDt={}'.format(
                now.strftime("%Y-%m-%d"), after.strftime("%Y-%m-%d"))
            paging_number_IC = '&currentPageNo={}'.format(page_no)
            print(req_url_IC + query_date_IC + paging_number_IC)
            # 페이지 넘버, 1씩 증가
            page_no = page_no + 1
            response_IC = requests.get(
                req_url_IC + query_date_IC + paging_number_IC)
            html = response_IC.text
            soup = BeautifulSoup(html, 'html.parser')  # get html
            get_tables = parser_functions.make2d(soup)
            print(get_tables)

            get_table_text.append(get_tables)

            if page_no == 5:
                break

        # 2차원 len
        total = len(get_table_text)

        for i in range(0, total):
            for index, get in enumerate(get_table_text[i], 1):
                print('{}번째 {}데이터'.format(index, get))

                if get[1] == "한진인천컨테이너터미널":
                    get[1] = "HJIT"
                elif get[1] == "선광신컨테이너터미널":
                    get[1] = "SNCT"
                elif get[1] == "E1컨테이너터미널":
                    get[1] = "E1CT"
                elif get[1] == "인천컨테이너터미널":
                    get[1] = "ICT"

                oid = get[3]  # oid
                trminl_code = get[1]  # 터미널코드
                berth_code = get[2]  # 선석코드
                trminl_voyg = get[3]  # 모선-항차
                trminl_shipnm = get[5]  # 선명
                csdhp_prarnde = get[6]  # 접안 (예정) 일시
                carry_fin_day = get[7]  # 반입 마감 시간
                tkoff_prarnde = get[8]  # 출항 (예정) 일시
                wtorcmp_code = get[9]  # 선사
                landng_qy = get[10]  # 양하
                shipng_qy = get[11]  # 적하
                shifting = get[12]  # shift

                # dict로 만들기
                result = {
                    "oid": oid,
                    "trminlCode": trminl_code,
                    "berthCode": berth_code,
                    "trminlVoyg": trminl_voyg,
                    "trminlShipnm": trminl_shipnm,
                    "wtorcmpCode": wtorcmp_code,
                    "carryFiniDay": carry_fin_day,
                    "csdhpPrarnde": csdhp_prarnde,
                    "tkoffPrarnde": tkoff_prarnde,
                    "landngQy": landng_qy,
                    "shipngQy": shipng_qy,
                    "shifting": shifting,
                }

                # print(result)
                data_check_list.append(result)

        if data_check_list == None:
            return []
        else:
            no_connection_test.postToHangman(data_check_list)

    except Exception as e:
        print(e)
    finally:
        response_IC.close()
