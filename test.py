# 스케쥴 테스트
from busan_download import busan_download
from get_req_urls import req_url_BS
import aioschedule as schedule
import asyncio
import time


async def test():
    print("-"*50 + "스케쥴 시작" + "-"*50)
    busan_download(req_url_BS)
    print("-"*50 + "스케쥴 끝" + "-"*50)

schedule.every(40).seconds.do(test)
loop = asyncio.get_event_loop()

while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(1)
