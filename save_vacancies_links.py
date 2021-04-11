from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from config import CONFIG


def main():
    vacancy_links = []
    driver = webdriver.Chrome()
    driver.get(CONFIG.URL_HH_VACANCIES)
    while True:
        page = driver.page_source
        soup = BeautifulSoup(page)
        vacancies = (
            soup
            .find_all('div', {'class': 'vacancy-serp-item'})
        )

        links = [vac.find('a', href=True) for vac in vacancies]
        links = [link['href'] for link in links]
        vacancy_links.extend([link for link in links if 'vacancy' in link])
        next_page = driver.find_elements_by_xpath('//a[text()="дальше"]')
        if not next_page:
            break
        next_page[0].click()

    vacancy_links = list(set(vacancy_links))

    with open(f'{CONFIG.DATA_FOLDER}/hh_vacancy_links.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(vacancy_links))


if __name__ == '__main__':
    main()
