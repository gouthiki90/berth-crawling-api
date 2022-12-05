import requests
from bs4 import BeautifulSoup
import no_connection_test
import my_sql_connection
import data_check_all


def incheon_download():

    try:
        response_IC = requests.get(
            'https://scon.icpa.or.kr/vescall/list.do?menuKey=19')
        # print(response_IC.text)
        get_json = response_IC.text
        print(get_json)
        # get_result = BeautifulSoup(response_IC.text, 'html.parser')
        # # print(get_result)
        # found = get_result.find_all()
        # print(found)

    except Exception as e:
        print(e)


incheon_download()
