import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import no_connection_test
import my_sql_connection
import data_check_all

# 날짜 세팅
now = datetime.now()
print(now)

after = now + timedelta(days=7)
print(after)

data_check_list = []


def incheon_download():
    def html_parse(tds):
        count = 1
        get_table_text = []
        table_page_list = []
        for text in tds:
            count = count + 1
            # print(text)
            to_string = str(text)
            get_remove_td_right = to_string.replace('<td>', '')
            get_remove_td_left = get_remove_td_right.replace('</td>', '')
            get_remove_class = get_remove_td_left.replace(
                '<td class="red">', '')
            get_remove_p_class = get_remove_class.replace(
                '<td class="blue">', '')
            get_remove_p_tag_left = get_remove_p_class.replace(
                '<p class="sub_txt">', ' ')
            get_remove_p_tag_right = get_remove_p_tag_left.replace('</p>', '')
            done_to_parse = get_remove_p_tag_right.replace('<br/>', '')

            get_table_text.append(done_to_parse)  # append

            if count == 19:  # 칼럼 수만큼
                print(get_table_text)

                # if get_table_text[2] == "한진":
                #     get_table_text[2] = "HJIT"
                # elif get_table_text[2] == "선광":
                #     get_table_text[2] = "SNCT"
                # elif get_table_text[2] == "E1":
                #     get_table_text[2] = "E1CT"
                # elif get_table_text[2] == "인천":
                #     get_table_text[2] = "ICT"

                # oid = get_table_text[4]  # oid
                # trminl_code = get_table_text[2]  # 터미널코드
                # berth_code = get_table_text[3]  # 선석코드
                # trminl_voyg = get_table_text[4]  # 모선-항차
                # trminl_shipnm = get_table_text[6]  # 선명
                # csdhp_prarnde = get_table_text[7]  # 접안 (예정) 일시
                # carry_fin_day = get_table_text[8]  # 반입 마감 시간
                # tkoff_prarnde = get_table_text[9]  # 출항 (예정) 일시
                # wtorcmp_code = get_table_text[10]  # 선사
                # landng_qy = get_table_text[11]  # 양하
                # shipng_qy = get_table_text[12]  # 적하
                # shifting = get_table_text[13]  # shift

                # # dict로 만들기
                # result = {
                #     "oid": oid,
                #     "trminlCode": trminl_code,
                #     "berthCode": berth_code,
                #     "trminlVoyg": trminl_voyg,
                #     "trminlShipnm": trminl_shipnm,
                #     "wtorcmpCode": wtorcmp_code,
                #     "carryFiniDay": carry_fin_day,
                #     "csdhpPrarnde": csdhp_prarnde,
                #     "tkoffPrarnde": tkoff_prarnde,
                #     "landngQy": landng_qy,
                #     "shipngQy": shipng_qy,
                #     "shifting": shifting,
                # }

                # print(result)
                count = 1
                get_table_text.clear()

    page_no = 1
    while True:
        # incheon req url
        req_url_IC = 'https://scon.icpa.or.kr/vescall/list.do'
        query_date_IC = '?searchStartDt={}&searchEndDt={}'.format(
            now.strftime("%Y-%m-%d"), after.strftime("%Y-%m-%d"))
        paging_number_IC = '&currentPageNo={}'.format(page_no)

        # 페이지 넘버, 1씩 증가
        page_no = page_no + 1

        # get html bs4
        data = requests.get(req_url_IC + query_date_IC + paging_number_IC)
        html = BeautifulSoup(data.text, 'html.parser')

        # html in td parsing
        tds = html.find_all('td')
        html_parse(tds)
        # table_page_list.append(get_table_text)  # 2차원 배열 생성

        if page_no == 5:
            break

    # print(table_page_list)

    # for text in table_page_list:
    #     print(text)
        # if text[6] == "한진":
        #     text[6] = "HJIT"
        # elif text[6] == "선광":
        #     text[6] = "SNCT"
        # elif text[6] == "E1":
        #     text[6] = "E1CT"
        # elif text[6] == "인천":
        #     text[6] = "ICT"

        # oid = text[8]  # oid
        # trminl_code = text[6]  # 터미널코드
        # berth_code = text[7]  # 선석코드
        # trminl_voyg = text[8]  # 모선-항차
        # trminl_shipnm = text[10]  # 선명
        # csdhp_prarnde = text[11]  # 접안 (예정) 일시
        # carry_fin_day = text[12]  # 반입 마감 시간
        # tkoff_prarnde = text[13]  # 출항 (예정) 일시
        # wtorcmp_code = text[14]  # 선사
        # landng_qy = text[15]  # 양하
        # shipng_qy = text[16]  # 적하
        # shifting = text[17]  # shift

        # # print(oid)

        # # dict로 만들기
        # result = {
        #     "oid": oid,
        #     "trminlCode": trminl_code,
        #     "berthCode": berth_code,
        #     "trminlVoyg": trminl_voyg,
        #     "trminlShipnm": trminl_shipnm,
        #     "wtorcmpCode": wtorcmp_code,
        #     "carryFiniDay": carry_fin_day,
        #     "csdhpPrarnde": csdhp_prarnde,
        #     "tkoffPrarnde": tkoff_prarnde,
        #     "landngQy": landng_qy,
        #     "shipngQy": shipng_qy,
        #     "shifting": shifting,
        # }

        # print(result)
        # data_check_list.append(result)

    # now_data = my_sql_connection.select_incheon_all(
    #     "HJIT", "SNCT", "E1CT", "ICT")
    # checked_data = data_check_all.data_check(data_check_list, now_data)
    # no_connection_test.post(checked_data)
    # no_connection_test.postJan(checked_data)
    # no_connection_test.postToHangman(checked_data)


incheon_download()
