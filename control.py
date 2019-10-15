import time
import asyncio
from pyppeteer import launch

import detect

async def main():
    browser = await launch(headless=False, autoClose=False)
    page = await browser.newPage()
    await page.goto("https://www.youtube.com/watch?v=zVA1HfpksJ8", timeout=10000)
    time.sleep(10)
    await page.click(".ytp-play-button.ytp-button")


asyncio.get_event_loop().run_until_complete(main())