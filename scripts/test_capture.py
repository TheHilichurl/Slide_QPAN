import asyncio
import os
import sys
from playwright.async_api import async_playwright
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            headless=True
        )
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            device_scale_factor=2560 / 1920
        )
        page = await context.new_page()
        await page.goto('http://localhost:8000/index.html')
        await page.wait_for_timeout(1000)

        # Apply exporting-2k class
        await page.evaluate("document.body.classList.add('exporting-2k')")
        await page.wait_for_timeout(300)

        # Screenshot slide-1
        slide_el = page.locator('#slide-1')
        await slide_el.screenshot(path='slide_1_test.png')
        await browser.close()

    im = Image.open('slide_1_test.png')
    print(f'Captured slide 1 test: size={im.size}')

asyncio.run(main())
