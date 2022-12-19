import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import no_connection_test
import data_check_all
import my_sql_connection


def gwaongyang_download(req_url):
    data_check_list = []
    try:
        response_GW = requests.get(req_url)
        html = response_GW.text
        soup = BeautifulSoup(html, 'html.parser')  # get html
        table = soup.select_one(".AA_list")
        get_tables = parser_functions.make2d(table)
        print(get_tables)

        for index, get in enumerate(get_tables, 1):
            # print('{}번째 {}데이터'.format(index, get))

            oid = get[1]  # oid
            berth_code = get[0]  # 선석
            trminl_voyg = get[1]  # 모선-항차
            csdhp_drc = get[3]  # 접안방향
            wtorcmp_code = get[4]  # 선사
            csdhp_prarnde = get[5]  # 입항일시
            tkoff_prarnde = get[6]  # 출항 (예정) 일시
            work_star_day = get[7]  # 작업시작
            work_fini_day = get[8]  # 작업 끝
            carry_fin_day = get[9]  # 반입마감일시
            landng_qy = get[10]  # 양하
            shipment = get[11]  # 선적
            shifting = get[12]  # sh
            pred_berth = get[13]  # 전배
            ship_rute = get[14]  # 항로

            # dict로 만들기
            result = {
                "oid": oid,
                "trminlCode": "GWCT",
                "wtorcmpCode": wtorcmp_code,
                "berthCode": berth_code,
                "trminlVoyg": trminl_voyg,
                "shipRute": ship_rute,
                "csdhpDrc": csdhp_drc,
                "workStarDay": work_star_day,
                "workFiniDay": work_fini_day,
                "carryFiniDay": carry_fin_day,
                "csdhpPrarnde": csdhp_prarnde,
                "tkoffPrarnde": tkoff_prarnde,
                "landngQy": landng_qy,
                "shipment": shipment,
                "shifting": shifting,
                "predBerth": pred_berth,
                "shipRute": ship_rute,
            }

            data_check_list.append(result)

        now_data = my_sql_connection.select_all("GWCT")
        checked_data = data_check_all.data_check(data_check_list, now_data)
        # no_connection_test.post(checked_data)
        no_connection_test.postJan(checked_data)
        no_connection_test.postToHangman(checked_data)
    except Exception as e:
        print(e)
