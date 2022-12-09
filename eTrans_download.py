import requests

# common options
url = "https://etrans3.klnet.co.kr/main/searchTracking.do"
session = "JSESSIONID=zo2MfSaDmZwjAU8V18TABTycKHpc1gsSefkPuMDTChetrUR0b8d05cwZ4r8Ju4zG.amV1c19kb21haW4vTmV3LVdBUzFfc2VydmVyMw==; WMONID=jR8q99wHNdc"
default_data = {
    "dma_search": {
        "KLNET_ID": "",
        "SEARCH_DATA": "FSCU5909470",
        "NOTICE_CNT": 25
    }
}


def download_etrans():
    response = requests.post(url, json=default_data)
    print(response.json())

    get_data_json = response.json()
    get_info_list = get_data_json['dma_tracking']
    print(get_info_list)


download_etrans()
