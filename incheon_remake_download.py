import requests
from bs4 import BeautifulSoup
import no_connection_test
from datetime import datetime, timedelta

# 날짜 세팅
now = datetime.now()

before = now - timedelta(days=1)
print(before, "-"*20 + "incheon before" + "-"*20)

after = before + timedelta(days=8)
print(after, "-"*20 + "incheon after" + "-"*20)


def incheon_download():
    index_cout = 0
    page_count = ['1', '2', '3']
    result_list = []

    try:
        for page in page_count:
            url = "https://scon.icpa.or.kr/vescall/list.do?menuKey=19&searchStartDt={}&searchEndDt={}&currentPageNo={}".format(
                before.strftime("%Y-%m-%d"), after.strftime("%Y-%m-%d"), page)
            print(url)
            payload = ""
            headers = {
                'Cookie': 'JSESSIONID=xbpnaLKVYkcPtOC9QceigazxVzbaWhWXMu3RfrT5.sin-was_1; SERVERID=WEB-1'
            }

            response = requests.request(
                "GET", url, headers=headers, data=payload)

            soup = BeautifulSoup(response.text, 'html.parser')

            # td 안에 있는 것을 다 가져옴
            result = soup.find_all("td")

            result_dict = {}

            for index, get in enumerate(result, 1):

                # string parse
                make_str = str(get)

                if make_str != '<td>조회된 데이터가 없습니다.</td>':
                    index_cout = index_cout + 1

                # print(index_cout)

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

                # 13번일 때 담아주기
                if index_cout == 13:
                    # heap point 때문에 깊은 복사를 해서 리스트에 담기
                    copy_result = result_dict.copy()
                    print(copy_result)
                    result_list.append(copy_result)
                    print('-'*50)
                    print(result_list)
                    print('-'*50)
                    index_cout = 0

        if result_list == None or len(result_list) == 0:
            return []
        else:
            no_connection_test.postToHangman(result_list)

    except Exception as e:
        print(e)


incheon_download()
