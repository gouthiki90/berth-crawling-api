from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from .no_connection_test import postToHangman

now = datetime.now()
before = now - timedelta(days=1)
after = before + timedelta(days=8)

incheon_SNCT_url = 'https://snct.sun-kwang.co.kr/infoservice/webpage/vessel/vslScheduleText.jsp?startDate={}&endDate={}'.format(
    before.strftime('%Y-%m-%d'), after.strftime('%Y-%m-%d'))

# incheon SNCT


def incheon_SNCT_download():
    data_check_list = []
    try:
        response = requests.request("GET", incheon_SNCT_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get table
        table = soup.select_one("#goosl_table")

        # table parse
        get_tables = parser_functions.make2d(table)

        for index, get in enumerate(get_tables, 1):
            # print('{}번째 {}데이터'.format(index, get))

            if index == 1:
                continue

            oid = get[2]
            berth_code = get[1]  # 선석
            trminl_voyg = get[2]  # 모선항차
            ship_rute = get[4]  # 항로
            trminl_shipnm = get[5]  # 모선명
            csdhp_prarnde = get[6]  # 접안일시
            carry_fin_day = get[7]  # 반입마감
            tkoff_prarnde = get[8]  # 출항일시
            wtorcmp_code = get[9]  # 선사
            landng_qy = get[10]  # 양하
            shipng_qy = get[11]  # 적하
            shifting = get[12]  # S/H

            # dict로 만들기
            result = {
                "oid": oid,
                "trminlCode": "SNCT",
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
                "shipRute": ship_rute,
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
