# HR_Helper

Данный проект предназначен для помощи специалисту по найму персонала в поиске релевантных резюме.   
Этот проект выполняет следующие задачи:
1. Определяет является ли неструктурированный текст резюме или нет.
2. Разделяет абзацы на категории:
    * опыт работы
    * образование
    * навыки, умения
    * общая информация о себе
    * желаемая позиция
    * зарплатные и другие ожидания
    * прочее
3. Определяет названия организаций из категорий "образование" и "опыт работы".

<br>

### Структура проекта  

* /models - папка с обученными моделями
* binary_classification.ipynb - построение моделей для определения того, является ли текст резюме или нет
* categories_multiclass_classification.ipynb - построение моделей для разделения абзацев резюме на различные категории
* config.py - конфигурационный файл
* convert_parsed_json_files_to_csv.ipynb - трансформация структурированных резюме в неструктурированные тексты
* cv_hh_crawler.ipynb - парсинг резюме с hh.ru
* cv_remote_jobs_crawler.ipynb - парсинг резюме с remote-job.ru
* example.ipynb - пример работы модели
* hh_vacancies_parser.py - парсинг вакансий с hh.ru
* rabota_cv_parser.py - парсинг резюме с rabota.ru
* save_hh_vacancies_links.py - скачивание ссылок на вакансии с hh.ru
* save_rabota_cv_links.py - скачивание ссылок на резюме с rabota.ru
* utils.py - вспомогательные функции
