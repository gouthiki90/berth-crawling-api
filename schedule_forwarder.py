import asyncio
from phang_download import pohang_download
from ulsan_download import ulsan_download
from pyeongtack_download import pyeongtack_download
from eTrans_download import download_etrans
from incheon_download import incheon_download
from gwongyang_download import gwaongyang_download
from busan_download import busan_download
from get_req_urls import req_url_PT, query_date_PT, query_page_PT, query_sort_PT
from get_req_urls import req_url_PH, query_date_PH
from get_req_urls import req_url_US
from get_req_urls import req_url_GW
from get_req_urls import req_url_BS
from get_req_urls import eTrans_url
import aioschedule
import time


async def get_forwarder():
    # 터미널 크롤링
    pohang_download(req_url_PH, query_date_PH)
    await asyncio.sleep(3)
    ulsan_download(req_url_US)
    await asyncio.sleep(3)
    pyeongtack_download(req_url_PT, query_date_PT,
                        query_sort_PT, query_page_PT)
    await asyncio.sleep(3)
    # incheon_download()
    # await asyncio.sleep(1)
    gwaongyang_download(req_url_GW)
    await asyncio.sleep(3)
    busan_download(req_url_BS)
    await asyncio.sleep(3)

    # 컨테이너 크롤링
    download_etrans(eTrans_url)
    await asyncio.sleep(3)

aioschedule.every(10).minutes.do(get_forwarder)
loop = asyncio.get_event_loop()

while True:
    try:
        print("::: start schedule... :::")
        loop.run_until_complete(aioschedule.run_pending())
        time.sleep(1)
        print("::: end schedule... :::")
    except Exception as e:
        print(e)
        print("::: erorr!! now closing... :::")
        loop.close()
