# 스케쥴 테스트
from internal_download import incheon_download
import aioschedule as schedule
import asyncio
import time


async def test():
    print("-"*50 + "스케쥴 시작" + "-"*50)
    incheon_download()
    print("-"*50 + "스케쥴 끝" + "-"*50)


schedule.every(20).seconds.do(test)
loop = asyncio.get_event_loop()

while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(1)
