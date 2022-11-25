new_data_arr_ch = []
now_data_arr_ch = []

compare_now_data_dict = []
compare_new_data_dict = []

checked_data = []


def data_check(new_data, now_data):
    try:
        for index, result in enumerate(new_data, 1):
            new_data_obj_checking = result['oid']

            new_data_arr_ch.append(new_data_obj_checking)
            compare_new_data_dict.append(result)

        for index, result in enumerate(now_data, 1):
            now_data_obj_checking = result["oid"]

            now_data_arr_ch.append(now_data_obj_checking)
            compare_now_data_dict.append(result)

        same_things = set(new_data_arr_ch) & set(now_data_arr_ch)
        same_check = set(new_data_arr_ch) - set(same_things)  # 새로 생긴 모선항차
        print("-"*50)
        print("새로 생긴 모선항차", same_check)
        print("-"*50)

        for checked in same_check:
            if same_check:
                # new data에 기존 데이터의 모선항차가 없을 시를 걸러서 데이터를 담기
                compare_data = compare_new_data_dict + \
                    compare_now_data_dict  # 기존, 최근 데이터 모두 합한 후
                for index, get in enumerate(compare_data, 1):
                    if get['oid'] == checked:  # oid를 통해 비교
                        checked_data.append(get)  # 비교한 것만 append

        return checked_data
    except Exception as e:
        print(e)
