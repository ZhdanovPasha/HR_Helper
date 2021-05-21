class CONFIG:
    DATA_FOLDER = 'data'
    URL_RABOTA_RU_CV = 'https://spb.rabota.ru/v3_searchResumeByParamsResults.html?action=search' +\
                       '&area=v3_searchResumeByParamsResults&p=-2005&w=&qk%5B0%5D=Web+developer&qot%5B0%5D=1' + \
                       '&qsa%5B0%5D%5B%5D=1&sf=&st=&cu=2&krl%5B%5D=4&krl%5B%5D=3&af=&at=&sex=' + \
                       '&eylo=&t2l=&la=&nex=true&id=30585906'
    CV_LINKS_NUM_SCROLLS = 1500
    CV_LINKS_TIME_SLEEP = 0.5
    URL_HH_VACANCIES = 'https://spb.hh.ru/search/vacancy?clusters=true&area=2&enable_snippets=true&salary=&' +\
                       'st=searchVacancy&text=Web+developer&from=suggest_post'
    MODELS_FOLDER = 'models'
    BINARY_VECTORIZER_NAME = 'binary_vectorizer.joblib'
    BINARY_CLASSIFER_NAME = 'binary_classifier.joblib'
    MULTI_VECTORIZER_NAME = 'multi_vectorizer.joblib'
    MULTI_CLASSIFIER_NAME = 'multi_classifier.joblib'
    