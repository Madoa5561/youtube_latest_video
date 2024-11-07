from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def get_latest_video(id):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--log-level=200')
    user_ag = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    options.add_argument(f'user-agent={user_ag}')
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.youtube.com/{id}/videos")
    try:
        background = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a/yt-image/img"))
        )
        titleAndhref = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[2]/h3/a"))
        )
        title = titleAndhref.get_attribute("title")
        href = titleAndhref.get_attribute("href")
        Theme = background.get_attribute("src")
        return [Theme, title, href]

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
    finally:
        driver.quit()

print(get_latest_video("@パトパトチャンネル"))
