import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from bs4 import BeautifulSoup
from config import CONFIG


def main():
    driver = webdriver.Chrome()
    driver.get(CONFIG.URL_RABOTA_RU_CV)
    html = driver.find_element_by_tag_name('html')
    for _ in tqdm(range(CONFIG.CV_LINKS_NUM_SCROLLS)):
        time.sleep(CONFIG.CV_LINKS_TIME_SLEEP)
        html.send_keys(Keys.END)

    page = driver.page_source
    soup = BeautifulSoup(page)
    html = soup.find_all('span', {'class': 'search-title'})
    result = [item.find('a', href=True) for item in html]
    links = [item['href'] for item in result]

    with open(f'{CONFIG.DATA_FOLDER}/rabota_cv_links.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(links))


if __name__ == "__main__":
    main()
