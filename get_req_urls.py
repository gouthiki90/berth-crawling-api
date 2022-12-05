from datetime import datetime, timedelta

# 날짜 세팅
now = datetime.now()
print(now)

after = now + timedelta(days=7)
print(after)

service_key = 'eCazEq%2FCP4iBdrQDcQQrLr3rgUrV%2ByZOFRdwxGTrcfeZbe3FqDvkQ6iMAWgeXRDOa%2FABNLYI3Dhz7hzxyUuI4A%3D%3D'

# pohang req url
req_url_PH = 'http://www.pohangport.com/info/ShipBerthT.pict'
query_date_PH = '?STARTDATE={}&ENDDATE={}'.format(
    now.strftime("%Y%m%d"), after.strftime("%Y%m%d"))

# ulsan req url
req_url_US = 'http://www.unct.co.kr/json/comm/commonSelect.do?sqlId=es010_100Qry.selectBerthScheduleList&from={}&to={}'.format(
    now.strftime("%Y%m%d"), after.strftime("%Y%m%d"))

# pyeong req url
req_url_PT = 'http://www.pctc21.com/esvc/vessel/berthScheduleT/data'
query_date_PT = '?startDate={}&endDate={}'.format(
    now.strftime("%Y-%m-%d"), after.strftime("%Y-%m-%d"))
query_sort_PT = '&sort=ETB'
query_page_PT = '&page=1'

# incheon req url
req_url_IC = 'https://opendata.icpa.or.kr/OpenAPI/service/ipaBerthUse/getBerthUse?ServiceKey={}'.format(
    service_key)
query_date_IC = '&endRow={}&skipRow={}&numOfRows={}&pageSize={}'.format(
    '1', '0', '1', '1')

# gwaongyang req url
main_req_url_GW = 'http://www.gwct.co.kr/e-service2/?m=B&s=2'
query_date_GW = '&v_time=term&fromY={}&fromM={}&fromD={}&toY={}&toM={}&toD={}'.format(
    now.year, now.month, now.day, after.year, after.month, after.day)

req_url_GW = main_req_url_GW + query_date_GW

# busan url
main_url = 'http://apis.data.go.kr/B551220/vsslBerthStatService/getVsslBerthStatList?'
service_key = 'serviceKey=9tYWVSjyoaIk2zT%2F0sJB81RO1McEvujAkH4lc9bKcT55hdcJAEiCt78hs40eByd3KlX5DyVcXBO0qYht01W5eA%3D%3D'
query_type = '&dataType=JSON'
query_page = "&pageNo=1"
query_rows = '&numOfRows=3000'
query_date = '&startDate={}&endDate={}'.format(
    now.strftime("%Y%m%d"), after.strftime("%Y%m%d"))

req_url_BS = main_url + service_key + query_type + \
    query_page + query_rows + query_date
