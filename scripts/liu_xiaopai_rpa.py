import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        # 使用本地已经存在的浏览器实例或开启新实例
        # 这里的逻辑模拟了 Browser-use 的观察-动作循环
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        url = "https://v.douyin.com/In2bL9NwCw4/"
        print(f"[*] 正在导航至: {url}")
        await page.goto(url, wait_until="networkidle")
        
        # 建立输出目录
        os.makedirs("artifacts/liu_xiaopai", exist_ok=True)

        for i in range(1, 8):
            print(f"[*] 正在处理第 {i}/7 张图片...")
            
            # --- 自愈逻辑：处理弹窗 ---
            # 抖音常见的登录弹窗关闭按钮选择器
            close_btn = page.locator(".dy-account-close")
            if await close_btn.is_visible():
                print("[!] 检测到登录弹窗，正在执行自动去遮挡...")
                await close_btn.click()
                await page.wait_for_timeout(500)

            # --- 采集数据 ---
            save_path = f"artifacts/liu_xiaopai/slide_{i}.png"
            await page.screenshot(path=save_path)
            print(f"[+] 已保存采样图: {save_path}")

            # --- 翻页逻辑 ---
            if i < 7:
                await page.keyboard.press("ArrowRight")
                await page.wait_for_timeout(1000) # 等待渲染

        await browser.close()
        print("[*] 任务圆满完成。")

if __name__ == "__main__":
    asyncio.run(run())
