from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

# 날짜 세팅
now = datetime.now()
before = now - timedelta(days=1)

incheon_HJIT = "http://59.17.254.10:9130/esvc/berth/BerthAction.do"


def incheon_HJIT_download():
    try:
        payload = {
            "cmd": "BerthScheduleList",
            "nowPage": "1",
            "scPeriod": "14",
            "menuID": "01",
            "subMenuID": "1",
            "pgID": "01",
            "scBaseDate": f"{before.strftime('%Y-%m-%d')}",
            "rowPerPage": "50"
        }
        response = requests.request("POST", incheon_HJIT, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

        find_tables = soup.find('table', attrs={'class': 'not_exist'})
        get_text = find_tables.find_all_next(string=True)
        print(get_text)

    except Exception as e:
        print(e)

    finally:
        response.close()


incheon_HJIT_download()
