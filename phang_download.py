from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import requests
import data_check_all
import my_sql_connection
import no_connection_test


def pohang_download(req_url, query_date):
    print(req_url + query_date)
    data_check_list = []

    try:
        response_PH = requests.get(req_url + query_date)
        html = response_PH.text
        soup = BeautifulSoup(html, 'html.parser')  # get html
        table = soup.select_one(".info_board")
        # print(table)

        get_tables = parser_functions.make2d(table)
        # print(get_tables)

        for index, get in enumerate(get_tables, 1):
            # print('{}번째 {}데이터'.format(index, get))

            oid = get[2]  # oid
            trminl_shipnm = get[1]  # 모선명
            trminl_voyg = get[2]  # 모선-항차
            wtorcmp_code = get[4]  # 선사
            ship_rute = get[5]  # 항로
            csdhp_drc = get[6]  # 접안방향
            csdhp_prarnde = get[7]  # 접안 (예정) 일시
            tkoff_prarnde = get[8]  # 출항 (예정) 일시
            berth_code = get[9]  # 선석
            carry_fin_day = get[10]  # 반입마감일시
            landng_qy = get[11]  # 양하
            shipng_qy = get[12]  # 적하
            shifting = get[13]  # shift

            # dict로 만들기
            result = {
                "oid": oid,
                "trminlCode": "KPOL",
                "berthCode": berth_code,
                "trminlVoyg": trminl_voyg,
                "shipRute": ship_rute,
                "csdhpDrc": csdhp_drc,
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
        response_PH.close()
