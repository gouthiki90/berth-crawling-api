from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from no_connection_test import postToHangman

# 날짜 세팅
now = datetime.now()
before = now - timedelta(days=1)

incheon_HJIT = "http://59.17.254.10:9130/esvc/berth/BerthAction.do"

payload = {
    "cmd": "BerthScheduleList",
    "nowPage": "1",  # 페이지 수
    "scPeriod": "14",  # 2주
    "menuID": "01",  # 메뉴
    "subMenuID": "1",  # 서브 메뉴
    "pgID": "01",
    "scBaseDate": f"{before.strftime('%Y-%m-%d')}",  # 서치 날짜
    "rowPerPage": "50"  # row 수
}


def incheon_HJIT_download():
    data_check_list = []
    try:

        response = requests.request("POST", incheon_HJIT, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')

        select_table = soup.select('table')

        # table list 중 선석 테이블
        get_berth_table = select_table[19]

        # table parse
        get_tables = parser_functions.make2d(get_berth_table)

        for index, get in enumerate(get_tables, 1):
            if index == 2:
                continue

            if get[0] == '':
                break

            oid = get[0] + ' ' + get[2] + ' ' + get[3]
            trminl_voyg = get[0] + ' ' + get[2] + ' ' + get[3]  # 모선항차
            trminl_shipnm = get[1]  # 모선명
            wtorcmp_code = get[2]  # 선사
            carry_fin_day = get[5]  # 반입마감
            csdhp_prarnde = get[6]  # 접안일시
            tkoff_prarnde = get[7]  # 출항일시
            landng_qy = get[8]  # 양하
            shipng_qy = get[9]  # 적하
            shifting = get[10]  # S/H
            berth_code = get[11]  # 선석

            # dict로 만들기
            result = {
                "oid": oid,
                "trminlCode": "HJIT",
                "trminlShipnm": trminl_shipnm,
                "wtorcmpCode": wtorcmp_code,
                "berthCode": berth_code,
                "trminlVoyg": trminl_voyg,
                "carryFiniDay": carry_fin_day,
                "csdhpPrarnde": csdhp_prarnde,
                "tkoffPrarnde": tkoff_prarnde,
                "landngQy": landng_qy,
                "shipngQy": shipng_qy,
                "shifting": shifting,
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


incheon_HJIT_download()
