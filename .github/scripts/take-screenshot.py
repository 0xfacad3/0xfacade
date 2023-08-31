import io
import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot():
    # Chromeのオプション設定
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # ChromeのWebDriverオブジェクトを作成する
    driver = webdriver.Chrome(options=options)

    try:
        # ウェブサイトにアクセス
        driver.get('https://honzaap.github.io/GithubCity/?name=Once-a-deadcat&year=2023')

        # ウェブサイトがロードされるまで待つ
        driver.implicitly_wait(10)

        # スクリーンショットを連続して撮影
        screenshots = []
        for _ in range(100):  # 6秒間、0.05秒ごとにスクリーンショットを撮影
            screenshot = driver.get_screenshot_as_png()
            screenshots.append(screenshot)
            time.sleep(0.05)

        # 連続したスクリーンショットからGIFを作成
        images = [Image.open(io.BytesIO(screenshot)) for screenshot in screenshots]
        images[0].save('screenshot.gif', save_all=True, append_images=images[1:], loop=0, duration=200)

    finally:
        driver.quit()

if __name__ == "__main__":
    take_screenshot()