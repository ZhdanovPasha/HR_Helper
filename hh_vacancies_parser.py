import json
from tqdm import tqdm
from config import CONFIG
from selenium import webdriver
from bs4 import BeautifulSoup


def parse_vacancy(vacancy):
    vac = dict()
    name = vacancy.find('h1', {'data-qa': 'vacancy-title'})
    if name is not None:
        vac['name'] = name.text
    salary = vacancy.find('p', {'class': 'vacancy-salary'})
    if salary is not None:
        vac['salary'] = salary.text
    company = vacancy.find('div', {'class': 'vacancy-company__details'})
    if company is not None:
        vac['company'] = company.text

    address = vacancy.find('span', {'data-qa': 'vacancy-view-raw-address'})
    if address is not None:
        vac['address'] = address.text

    exp = vacancy.find('span', {'data-qa': 'vacancy-experience'})
    if exp is not None:
        vac['experience'] = exp.text

    employment_mode = vacancy.find('p', {'data-qa': 'vacancy-view-employment-mode'})
    if employment_mode is not None:
        vac['employment_mode'] = employment_mode.text

    description = vacancy.find('div', {'data-qa': 'vacancy-description'})
    if description is not None:
        vac['description'] = description.text

    return vac


def main():
    vacancies = []
    driver = webdriver.Chrome()

    with open(f'{CONFIG.DATA_FOLDER}/hh_vacancy_links.txt', 'r', encoding='utf-8') as f:
        vacancy_links = f.read().split('\n')

    for vacancy_link in tqdm(vacancy_links):
        driver.get(vacancy_link)
        page = driver.page_source
        vacancy_soup = BeautifulSoup(page)
        vacancies.append(parse_vacancy(vacancy_soup))

    with open(f'{CONFIG.DATA_FOLDER}/hh_vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()