import time
import asyncio
from pyppeteer import launch

# Headless control

# Launch webpage
async def launch_page():
	browser = await launch(headless=False, autoClose=False)
	page = await browser.newPage()
	await page.goto("https://www.youtube.com/watch?v=zVA1HfpksJ8", timeout=100000000000)
	return page

# Click play/stop button
async def click_button(page):
	await page.click(".ytp-play-button.ytp-button")