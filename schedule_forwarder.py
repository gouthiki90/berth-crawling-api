import aioschedule
import asyncio
import time
from phang_download import pohang_download
from ulsan_download import ulsan_download
from pyeongtack_download import pyeongtack_download
from incheon_download import incheon_download
from gwongyang_download import gwaongyang_download
from busan_download import busan_download
from get_req_urls import req_url_PT, query_date_PT, query_page_PT, query_sort_PT
from get_req_urls import req_url_PH, query_date_PH
from get_req_urls import req_url_US
from get_req_urls import req_url_GW
from get_req_urls import req_url_BS


async def get_forwarder():
    pohang_download(req_url_PH, query_date_PH)
    await asyncio.sleep(1)
    ulsan_download(req_url_US)
    await asyncio.sleep(1)
    pyeongtack_download(req_url_PT, query_date_PT,
                        query_sort_PT, query_page_PT)
    await asyncio.sleep(1)
    # incheon_download()
    # await asyncio.sleep(1)
    gwaongyang_download(req_url_GW)
    await asyncio.sleep(1)
    busan_download(req_url_BS)
    await asyncio.sleep(1)

aioschedule.every(3).minutes.do(get_forwarder)
loop = asyncio.get_event_loop()

while True:
    loop.run_until_complete(aioschedule.run_pending())
    time.sleep(1)
