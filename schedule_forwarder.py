import asyncio
from phang_download import pohang_download
from ulsan_download import ulsan_download
from gwongyang_download import gwaongyang_download
from incheon_remake_download import incheon_download
from get_req_urls import req_url_PH, query_date_PH
from get_req_urls import req_url_US
from get_req_urls import req_url_GW
import asyncio
import aioschedule
import time


async def get_forwarder():
    # 터미널 크롤링
    print("::: start schedule... :::")
    await asyncio.sleep(3)
    pohang_download(req_url_PH, query_date_PH)
    print("::: pohang schedule... :::")
    await asyncio.sleep(3)
    ulsan_download(req_url_US)
    print("::: ulsan schedule... :::")
    await asyncio.sleep(3)
    gwaongyang_download(req_url_GW)
    print("::: gwang schedule... :::")
    # await asyncio.sleep(3)
    # busan_download(req_url_BS)
    # print("::: busan schedule... :::")
    await asyncio.sleep(3)
    incheon_download()
    print("::: incheon schedule... :::")
    await asyncio.sleep(3)
    print("::: end schedule... :::")

aioschedule.every(20).seconds.do(get_forwarder)
loop = asyncio.get_event_loop()

while True:
    try:
        loop.run_until_complete(aioschedule.run_pending())
        time.sleep(1)

    except Exception as e:
        print(e)
        print("::: erorr!! now closing... :::")
        loop.close()
