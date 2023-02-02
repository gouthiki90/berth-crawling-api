import requests
from html_table_parser import parser_functions
from bs4 import BeautifulSoup


def incheon_download():
    index_cout = 0
    result_dict = {}

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

        for index, get in enumerate(result, 1):
            # string parse
            make_str = str(get)

            if make_str != '<td>조회된 데이터가 없습니다.</td>':
                index_cout = index_cout + 1

            print(index_cout)

            # html parse
            remove_td_tags = make_str.strip(
                '<td></td><br><br/> class="red"> class="blue"></p')
            remove_all_tags = remove_td_tags.replace(
                '<br/><p class="sub_txt">', '')

            incheon_schedule_data = remove_all_tags

            if index_cout == 1:
                # dict으로 만들기
                result_dict['num'] = incheon_schedule_data
            elif index_cout == 2:
                result_dict['trminlCode'] = incheon_schedule_data
            elif index_cout == 3:
                result_dict['berthCode'] = incheon_schedule_data
            elif index_cout == 4:
                result_dict['oid'] = incheon_schedule_data
                result_dict['trminlVoyg'] = incheon_schedule_data
            elif index_cout == 5:
                result_dict['year'] = incheon_schedule_data
            elif index_cout == 6:
                result_dict['csdhpPrarnde'] = incheon_schedule_data
            elif index_cout == 7:
                result_dict['carryFiniDay'] = incheon_schedule_data
            elif index_cout == 8:
                result_dict['tkoffPrarnde'] = incheon_schedule_data
            elif index_cout == 9:
                result_dict['wtorcmpCode'] = incheon_schedule_data
            elif index_cout == 10:
                result_dict['landngQy'] = incheon_schedule_data
            elif index_cout == 11:
                result_dict['shipngQy'] = incheon_schedule_data
            elif index_cout == 12:
                result_dict['shifting'] = incheon_schedule_data

            # print(result_dict)
            # dict까지는 잘 만들어지는데, 이걸 어떻게 리스트로 담을 지 생각해봐야 될 듯
            if index_cout == 13:
                index_cout = 0
                print(result_dict)
                continue

    except Exception as e:
        print(e)


incheon_download()
