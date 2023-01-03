import no_connection_test
import requests

# 울산


def ulsan_download(req_url):
    data_check_list = []

    try:
        response = requests.get(req_url)

        # JSON으로 파싱
        result = response.json()

        # body 데이터
        body = result['queryResult']

        # 데이터 확인
        for index, result in enumerate(body, 1):
            # print('{}번째 데이터 : {}'.format(index, result))

            data = {
                'oid': result['aa'],
                'trminlCode': 'UNCT',  # 터미널코드
                'berthCode': result['position'],  # 선석
                'trminlVoyg': result['aa'],  # 모선항차
                'trminlShipnm': result['cdvVslName'],  # 선명
                'wtorcmpCode': result['cdvVslOperator'],  # 선사
                'csdhpDrc': result['vsbVoyStartpos'],  # 접안위치
                'carryFiniDay': result['cct'],  # 반입 마감 시간
                'csdhpPrarnde': result['etb'],  # 접안 예정 일시
                'tkoffPrarnde': result['etd'],  # 출항 예정 일시
                'landngQy': result['vsbVoyDisvan'],  # 양하
                'shipngQy': result['vsbVoyLoadvan'],  # 적하
                'reshmtQy': result['vsbVoyTsvan'],  # 이적
            }

            print(data)

            data_check_list.append(data)

        if data_check_list == None:
            return []
        else:
            no_connection_test.postToHangman(data_check_list)

    except Exception as e:
        print(e)
    finally:
        response.close()
