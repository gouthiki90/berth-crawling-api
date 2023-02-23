from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import re
from no_connection_test import postToHangman

now = datetime.now()
before = now - timedelta(days=1)
after = before + timedelta(days=8)

incheon_E1_url = 'http://www.e1ct.co.kr/info/terminal/berthText?searchStartDt={}&searchEndDt={}'.format(
    before.strftime("%Y-%m-%d"), after.strftime("%Y-%m-%d"))

# 인천 E1 터미널 스케줄


def incheon_E1_dowonload():
    data_check_list = []
    try:
        response = requests.request("GET", incheon_E1_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get table
        table = soup.select_one('table')

        # table parse
        get_tables = parser_functions.make2d(table)

        for index, get in enumerate(get_tables, 1):
            if index == 1:
                continue

            # 출항일 문자열 가공
            get_tkoff_prarnde = str(get[7])  # make str
            remove = get_tkoff_prarnde.split('\n')  # remove
            new_tkoff_prarnde = re.sub(r"[A-Z]", "", remove[0])  # eng remove

            if index == 2:
                get_tkoff_prarnde = new_tkoff_prarnde[:-3]  # slice
            else:
                get_tkoff_prarnde = new_tkoff_prarnde[:-1]  # slice

            oid = get[2]
            berth_code = get[1]  # 선석
            trminl_voyg = get[2]  # 모선항차
            trminl_shipnm = get[4]  # 모선명
            csdhp_prarnde = get[5]  # 접안일시
            carry_fin_day = get[6]  # 반입마감
            tkoff_prarnde = get_tkoff_prarnde  # 출항일시

            # dict로 만들기
            result = {
                "oid": oid,
                "trminlCode": "E1",
                "berthCode": berth_code,
                "trminlVoyg": trminl_voyg,
                "trminl_shipnm": trminl_shipnm,
                "carryFiniDay": carry_fin_day,
                "csdhpPrarnde": csdhp_prarnde,
                "tkoffPrarnde": tkoff_prarnde,
            }

            data_check_list.append(result)

        if data_check_list == None:
            return []
        else:
            postToHangman(data_check_list)

    except Exception as e:
        print(e)
    finally:
        response.close()
