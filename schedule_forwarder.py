import asyncio
from phang_download import pohang_download
from ulsan_download import ulsan_download
from gwongyang_download import gwaongyang_download
from busan_download import busan_download
from get_req_urls import req_url_PH, query_date_PH
from get_req_urls import req_url_US
from get_req_urls import req_url_GW
from get_req_urls import req_url_BS
import asyncio
import aioschedule
import time


async def get_forwarder():
    # 터미널 크롤링
    print("::: start schedule... :::")
    await asyncio.sleep(3)
    pohang_download(req_url_PH, query_date_PH)
    await asyncio.sleep(3)
    ulsan_download(req_url_US)
    await asyncio.sleep(3)
    gwaongyang_download(req_url_GW)
    await asyncio.sleep(3)
    busan_download(req_url_BS)
    await asyncio.sleep(3)
    print("::: end schedule... :::")

aioschedule.every(10).minutes.do(get_forwarder)
loop = asyncio.get_event_loop()

while True:
    try:
        loop.run_until_complete(aioschedule.run_pending())
        time.sleep(1)

    except Exception as e:
        print(e)
        print("::: erorr!! now closing... :::")
        loop.close()
