import requests
from html_table_parser import parser_functions
from bs4 import BeautifulSoup


def incheon_download():

    try:

        url = "https://scon.icpa.or.kr/vescall/list.do?menuKey=19&searchStartDt=2023-01-29&searchEndDt=2023-02-02&currentPageNo=1"
        payload = ""
        headers = {
            'Cookie': 'JSESSIONID=xbpnaLKVYkcPtOC9QceigazxVzbaWhWXMu3RfrT5.sin-was_1; SERVERID=WEB-1'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        soup = BeautifulSoup(response.text, 'html.parser')

        # 일단 td 안에 있는 것을 다 가져옴
        result = soup.find_all("td")

        index_cout = 1
        for index, get in enumerate(result, 1):
            # print('{}번째 {}데이터'.format(index, get))
            index_cout + 1

            # string parse
            make_str = str(get)

            print(make_str)

            # html parse
            remove_td_tags = make_str.strip(
                '<td></td><br><br/> class="red"> class="blue"></p')
            remove_all_tags = remove_td_tags.replace(
                '<br/><p class="sub_txt">', '')

            incheon_schedule_data = remove_all_tags

            # dict으로 만들기
            result = {
                "num": incheon_schedule_data,
            }

            # print(result)

            if index_cout == 13:
                continue

                # if index > 5:

                # print(remove_tds)

    except Exception as e:
        print(e)


incheon_download()
