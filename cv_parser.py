import json
import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
from config import CONFIG


def delete_spaces(word):
    return ' '.join(word.split())


def parse_experience(soup):
    company_names = soup.find_all('p', {'class': 'company-name'})
    company_types = soup.find_all('p', {'class': 'company-type'})
    work_periods = soup.find_all('div', {'class': 'b-work-period'})
    last_position_names = soup.find_all('p', {'class': 'last-position-name'})
    res_exps = soup.find_all('p', {'class': 'p-res-exp'})
    base_work_dict = {
        'company_name': '',
        'company_type': '',
        'work_period': '',
        'last_position_name': '',
        'res_exp': '',
    }
    work_list_size = max(list(
        map(len, [company_names, company_types, work_periods, last_position_names, res_exps])
    ))
    work_list = [base_work_dict.copy() for _ in range(work_list_size)]
    for i, company_name in enumerate(company_names):
        work_list[i]['company_name'] = delete_spaces(company_name.text)
    for i, company_type in enumerate(company_types):
        work_list[i]['company_type'] = delete_spaces(company_type.text)
    for i, work_period in enumerate(work_periods):
        work_list[i]['work_period'] = delete_spaces(work_period.text)
    for i, last_position_name in enumerate(last_position_names):
        work_list[i]['last_position_name'] = delete_spaces(last_position_name.text)
    for i, res_exp in enumerate(res_exps):
        work_list[i]['res_exp'] = delete_spaces(res_exp.text)

    return work_list


def parse_education(soup):
    edu_years = soup.find_all('div', {'class': 'edu-year'})
    edu_types = soup.find_all('p', {'class': 'edu-type-ttl'})
    school_names = soup.find_all('p', {'class': 'school-name'})
    profes_infos = soup.find_all('div', {'class': 'profes-info'})

    edu_work_dict = {
        'edu_year': '',
        'edu_type': '',
        'school_name': '',
        'profes_info': '',
    }
    edu_list_size = max(list(
        map(len, (edu_years, edu_types, school_names, profes_infos))
    ))
    education_list = [edu_work_dict.copy() for _ in range(edu_list_size)]

    for i, edu_year in enumerate(edu_years):
        education_list[i]['edu_year'] = delete_spaces(edu_year.text)
    for i, edu_type in enumerate(edu_types):
        education_list[i]['edu_type'] = delete_spaces(edu_type.text)
    for i, school_name in enumerate(school_names):
        education_list[i]['school_name'] = delete_spaces(school_name.text)
    for i, profes_info in enumerate(profes_infos):
        education_list[i]['profes_info'] = delete_spaces(profes_info.text)

    return education_list


def parse_cv(request):
    candidate = dict()
    soup = BeautifulSoup(request.text)

    tmp = soup.find('span', {'class': 'position-name'})
    if tmp is not None:
        candidate['position_name'] = delete_spaces(tmp.text)

    tmp = soup.find('span', {'class': 'salary'})
    if tmp is not None:
        candidate['salary'] = delete_spaces(tmp.text)
    
    tmp = soup.find_all('div', {'class': 'b-skills-desrc'})
    if tmp is not None:
        candidate['skills'] = ''
        for skill in tmp: 
            candidate['skills'] += delete_spaces(skill.text) + '.'

    tmp = soup.find_all('span', {'class': 'resume_leaving_region_block'})
    if tmp is not None:
        cities = []
        for city in tmp:
            cities.append(delete_spaces(city.text))
        candidate['desired_places_of_work'] = cities

    tmp = soup.find('p', {'class': 'b-sex-age'})
    sexes = {'мужчина', 'женщина'}
    if tmp is not None:
        arr = delete_spaces(tmp.text).split(',')
        arr = [delete_spaces(item) for item in arr]
        age, sex = '', ''
        if len(arr) > 0:
            if arr[0] in sexes:
                sex = arr[0]
            else:
                age = arr[0]
        if len(arr) > 1:
            if arr[1] in sexes and not sex:
                sex = arr[1]
            elif not age:
                age = arr[1]
        candidate['age'] = delete_spaces(age)
        candidate['sex'] = delete_spaces(sex)

    tmp = soup.find('p', {'class': 'b-city-info'})
    if tmp is not None:
        candidate['city'] = delete_spaces(tmp.text)

    tmp = soup.find('p', {'class': 'b-citizenship-info'})
    if tmp is not None:
        candidate['citizenship'] = delete_spaces(tmp.text).split()[1]
    
    tmp = soup.find('p', {'class': 'bus-skill-txt'})
    if tmp is not None:
        candidate['bus_skill'] = delete_spaces(tmp.text)

    tmp = soup.find('p', {'class': 'drive-info'})
    if tmp is not None:
        candidate['drive_info'] = delete_spaces(tmp.text)

    tmp = soup.find('p', {'class': 'marriage-info'})
    if tmp is not None:
        candidate['marriage_info'] = delete_spaces(tmp.text)

    tmp = soup.find('p', {'class': 'aboutme-info'})
    if tmp is not None:
        candidate['aboutme_info'] = delete_spaces(tmp.text)

    candidate['experience_list'] = parse_experience(soup)

    candidate['education_list'] = parse_education(soup)

    return candidate


def main():
    with open(f'{CONFIG.DATA_FOLDER}/rabota_cv_links.txt', 'r', encoding='utf-8') as f:
        links = f.read().split('\n')

    cvs = []
    for link in tqdm(links):
        request = requests.get(link)
        cvs.append(parse_cv(request))
        time.sleep(1)
        
    with open(f'{CONFIG.DATA_FOLDER}/rabota_cvs.json', 'w', encoding='utf-8') as f:
        json.dump(cvs, f, ensure_ascii=False, indent=4)
        
        
if __name__ == "__main__":
    main()