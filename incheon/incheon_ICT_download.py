
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

now = datetime.now()
before = now - timedelta(days=1)
after = before + timedelta(days=8)

incheon_ICT_url = 'https://service.psa-ict.co.kr/webpage/vessel/vslScheduleText.jsp?strdStDate={}&strdEdDate={}'.format(
    after.strftime('%Y-%m-%d'), before.strftime('%Y-%m-%d'))


def incheon_ICT_download():
    try:
        response = requests.request("GET", incheon_ICT_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        print(soup)
    except Exception as e:
        print(e)
    finally:
        response.close()


incheon_ICT_download()
