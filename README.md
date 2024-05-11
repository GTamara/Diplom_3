# UI тесты
## Установка зависимостей
pip install -r requirements.txt 

## Генерация отчета
pytest --alluredir=allure_results 
allure serve allure_results

## Генерация актуального requirements.txt
pip freeze > requirements.txt 
