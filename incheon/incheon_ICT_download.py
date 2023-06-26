from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
from .no_connection_test import postToHangman


def incheon_ICT_download():
    now = datetime.now()
    before = now - timedelta(days=1)
    after = before + timedelta(days=8)

    incheon_ICT_url = 'https://service.psa-ict.co.kr/webpage/vessel/vslScheduleText.jsp?strdStDate={}&strdEdDate={}'.format(
        before.strftime('%Y-%m-%d'), after.strftime('%Y-%m-%d'))
    data_check_list = []
    try:
        response = requests.request("GET", incheon_ICT_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # print(soup)

        # talbe list 중 스케줄 테이블 찾기
        get_tables = soup.select('table.defualt')
        berth_talbe = get_tables[14]

        # table parse
        get_tables = parser_functions.make2d(berth_talbe)

        for index, get in enumerate(get_tables, 1):
            # print('{}번째 {}데이터'.format(index, get))

            if index == 1:
                continue

            # 양하, 적하, SH 문자열 가공
            get_texts = str(get[7])
            split_text = get_texts.split("/")

            # 모선항차 문자열 가공
            get_oid = str(get[2])
            remove_n = get_oid.replace("\n", "")
            remove_t = remove_n.replace("\t", "")
            oid_and_tr = remove_t.replace("\r", "")

            oid = oid_and_tr
            berth_code = get[1]  # 선석
            trminl_voyg = oid_and_tr  # 모선항차
            trminl_shipnm = get[3]  # 모선명
            carry_fin_day = get[5]  # 반입마감
            csdhp_prarnde = get[4]  # 접안일시
            tkoff_prarnde = get[6]  # 출항일시
            landng_qy = split_text[0].strip()  # 양하
            shipng_qy = split_text[1].strip()  # 적하
            shifting = split_text[2].strip()  # S/H

            # dict로 만들기
            result = {
                "oid": oid,
                "trminlCode": "ICT",
                "trminlShipnm": trminl_shipnm,
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
