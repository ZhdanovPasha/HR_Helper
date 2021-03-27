import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from bs4 import BeautifulSoup


def main():
    driver = webdriver.Chrome()
    url = 'https://spb.rabota.ru/v3_searchResumeByParamsResults.html?action=search&area=v3_searchResumeByParamsResults&p=-2005&w=&qk%5B0%5D=Web+developer&qot%5B0%5D=1&qsa%5B0%5D%5B%5D=1&sf=&st=&cu=2&krl%5B%5D=4&krl%5B%5D=3&af=&at=&sex=&eylo=&t2l=&la=&nex=true&id=30585906'
    driver.get(url)
    NUM_SCROLLS = 1500
    html = driver.find_element_by_tag_name('html')
    for i in tqdm(range(NUM_SCROLLS)):
        time.sleep(0.5)
        html.send_keys(Keys.END)

    page = driver.page_source

    soup = BeautifulSoup(page)

    html = (
        soup
        .find_all('span', {'class': 'search-title'})
    )

    result = [item.find('a', href=True) for item in html]
    links = [item['href'] for item in result]

    with open('links.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(links))
    
if __name__ == "__main__":
    main()