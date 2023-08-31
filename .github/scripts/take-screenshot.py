import os
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

        # スクリーンショットを撮影
        driver.save_screenshot('screenshot.png')
    finally:
        driver.quit()

if __name__ == "__main__":
    take_screenshot()
