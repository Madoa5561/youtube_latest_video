from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

def get_latest_video(id):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--log-level=200')
    user_ag='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; '+'CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    options.add_argument('user-agent=%s'%user_ag)
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.youtube.com/{id}/videos")
    background = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a/yt-image/img")
    titleAndhref = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/h3")
    ignore = titleAndhref.find_element(By.TAG_NAME,"a")
    Theme = background.get_attribute("src")
    title = ignore.get_attribute("title")
    href = ignore.get_attribute("href")
    return [Theme,title,href] #[サムネURL,タイトル,動画URL]

print(get_latest_video("@user-ez4ul2lf7g"))
