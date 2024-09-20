## Демо проект автоматизации тестирования сайта [The code](https://thecode.media/)

---
### Проект представляет собой набор UI-тестов покрывающих следующий функционал:
1. Авторизация
2. Работа функции поиска
3. Переключение контента на странице
4. Проверка корректного перехода между страницами

---
## Используемый стек:
<p align="left">
<img src="media/python-original-wordmark.svg" width="50" height="50"/>
<img src="media/pytest-original-wordmark.svg" width="50" height="50"/>
<img src="media/Selenium.png" width="50" height="50"/>
<img src="media/jenkins-original.svg" width="50" height="50"/>
<img src="media/AllureReport.png" width="50" height="50"/>
<img src="media/Selenoid.png" width="50" height="50"/>

</p>

Проект написан на языке программирования Python, с использованием фреймворков Pytest, Selene. 

Реализована удаленная сборка тестов в Jenkins 

Запуск тестов в Selenoid

После прохождения тестов система отправляет краткий отчет в [Telegram](https://t.me/demo_project_notifications) 

Так же в Jenkins будет доступен подробный отчет Allure

---
## Инструкция по удаленному запуску тестов:
1. Перейти по ссылке в [сборку](https://jenkins.autotests.cloud/job/qa_guru_14_quick_project_hw14/)
2. Нажать Build Now
<img src="media/Jenkins_Build_Now.png"/>

## Инструкция по локальному запуску тестов:
1. Запустить команду Pytest
2. Заупстить команду allure serve tests/allure-results - для генерации Allure отчета
3. Запустить команду allure generate --clean tests/allure-results для генерации allure report
4. Запустить команду java "-DconfigFile=notifications/telegram.json" -jar allure-notifications-4.7.0.jar для получения отчета от телеграм бота
---
## Allure отчет о прохождении тестов
### Общий результат прохождения тестов
<img src="media/allure_general_report.png"/>

### Графики
<img src="media/allure_grafics.png"/>


### Подробный отчет о прохождении
<img src="media/allure_detailed_report.png"/>

### Видео прохождения теста
<img src="media/selenoid_file.gif"/>

---
## Telegram отчет
<img src="media/telegram_allure_report.png"/>


