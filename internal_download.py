import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import no_connection_test
import my_sql_connection
import data_check_all

# 날짜 세팅
now = datetime.now()
print(now)

after = now + timedelta(days=7)
print(after)

data_check_list = []
table_list = []
making_list = []


def html_parse(tds):
    count = 1
    get_table_text = []
    for index, text in enumerate(tds, 0):
        count = count + 1
        to_string = str(text)
        get_remove_td_right = to_string.replace('<td>', '')
        get_remove_td_left = get_remove_td_right.replace('</td>', '')
        get_remove_class = get_remove_td_left.replace(
            '<td class="red">', '')
        get_remove_p_class = get_remove_class.replace(
            '<td class="blue">', '')
        get_remove_p_tag_left = get_remove_p_class.replace(
            '<p class="sub_txt">', ' ')
        get_remove_p_tag_right = get_remove_p_tag_left.replace('</p>', '')
        done_to_parse = get_remove_p_tag_right.replace('<br/>', '')
        test = list(done_to_parse)
        # print(test)
        get_table_text.append(done_to_parse)  # append

        if count == 12:
            gets = list(done_to_parse)
            print(str(gets))
            count = 1

    return get_table_text


def get_lists():
    page_no = 1
    while True:
        # incheon req url
        req_url_IC = 'https://scon.icpa.or.kr/vescall/list.do'
        query_date_IC = '?searchStartDt={}&searchEndDt={}'.format(
            now.strftime("%Y-%m-%d"), after.strftime("%Y-%m-%d"))
        paging_number_IC = '&currentPageNo={}'.format(page_no)

        # 페이지 넘버, 1씩 증가
        page_no = page_no + 1

        # get html bs4
        data = requests.get(req_url_IC + query_date_IC + paging_number_IC)
        html = BeautifulSoup(data.text, 'html.parser')

        # html in td parsing
        tds = html.find_all('td')

        get_list = html_parse(tds)
        table_list.append(get_list)

        if page_no == 5:
            return table_list


get_tables_list = get_lists()
print(get_tables_list)
# total = len(get_tables_list)
# result_list = []

# for i in range(0, total):
#     print(i)
#     for index, get in enumerate(get_tables_list, 0):

#         print(get[i])
