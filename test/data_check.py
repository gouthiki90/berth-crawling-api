import busan_download
import crud.my_sql_connection as my_sql_connection
import crud.no_connection_test as no_connection_test

# 모선항차 기준으로 data 중복 체크

# 터미널 코드
trminlCode = {
    "부산신항컨테이너": "BPTS",
    "현대부산신항": "HPNT",
    "부산신항다목적": "BNMT",
    "BPTG-감만": "BPTG",
    "BPTS-신선대": "BPTS",
    "동원부산컨테이너": "DPCT",
    "한진부산신항": "HJNC",
    "허치슨": "HKT",
    "현대부산신항": "HPNT",
    "부산신항": "PNC",
    "부산신항국제": "PNIT",
}

new_data_arr_ch = []
now_data_arr_ch = []

compare_now_data_dict = []
compare_new_data_dict = []


try:
    new_data = busan_download.download()  # 다운로드한 것
    now_data = my_sql_connection.select_all(
        trminlCode.get("부산신항컨테이너"))  # 기존에 있는 것

    for index, result in enumerate(new_data, 1):
        # print('{}번째 데이터 : {}'.format(index, result))
        new_data_obj_checking = result['trminlVoyg']

        new_data_arr_ch.append(new_data_obj_checking)
        compare_new_data_dict.append(result)

    for index, result in enumerate(now_data, 1):
        # print('{}번째 데이터 : {}'.format(index, result))
        now_data_obj_checking = result["trminlVoyg"]

        now_data_arr_ch.append(now_data_obj_checking)
        compare_now_data_dict.append(result)

    same_check = new_data_arr_ch = now_data_arr_ch
    if same_check == False:
        # new data에 기존 데이터의 모선항차가 없을 시를 걸러서 데이터를 담기
        compare_data = compare_new_data_dict + compare_now_data_dict
        checked_data = list(
            {result['trminlVoyg']: result for result in compare_data}.values())
        print(checked_data)
        no_connection_test.postBusan(checked_data)


except Exception as e:
    print(e)
