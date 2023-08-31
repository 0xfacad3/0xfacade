import io
import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

        driver.implicitly_wait(15)

        # スクリーンショットを連続して撮影
        screenshots = []
        action = ActionChains(driver)
        for i in range(60):  # 6秒間、0.1秒ごとにスクリーンショットを撮影
            # ズームアウト
            action.send_keys(Keys.COMMAND, Keys.SUBTRACT).perform()  # これはMacの場合です。Windowsの場合は、Keys.CONTROLを使用してください。
            screenshot = driver.get_screenshot_as_png()
            screenshots.append(screenshot)
            time.sleep(0.05)

        # 連続したスクリーンショットからGIFを作成
        images = [Image.open(io.BytesIO(screenshot)) for screenshot in screenshots]
        images[0].save('screenshot.gif', save_all=True, append_images=images[1:], loop=0, duration=100)

    finally:
        driver.quit()

if __name__ == "__main__":
    take_screenshot()
