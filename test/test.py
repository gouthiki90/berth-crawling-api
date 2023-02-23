# 스케쥴 테스트
from temp.eTrans_download import download_etrans
from get_req_urls import eTrans_url
import aioschedule as schedule
import asyncio
import time


async def test():
    print("-"*50 + "스케쥴 시작" + "-"*50)
    download_etrans(eTrans_url)
    print("-"*50 + "스케쥴 끝" + "-"*50)

schedule.every(20).seconds.do(test)
loop = asyncio.get_event_loop()

while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(1)
