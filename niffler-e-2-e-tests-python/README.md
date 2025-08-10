## Проект автоматизированного тестирования приложения Niffler.

<p  align="center">
<code><img width="75%" title="main_page" src="assets/main_page.PNG"></code>
</p>  

### Проект реализован с использованием:

<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="selene" src="https://github.com/MDN78/MDN78/blob/main/assets/selene.png"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="github" src="https://github.com/MDN78/MDN78/blob/main/assets/github.png"></code>
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>  
<code><img width="5%" title="requests" src="assets/Requests_Logo.png"></code>  
<code><img width="5%" title="kafka" src="assets/kafka.svg"></code>  
<code><img width="5%" title="git" src="assets/Git.svg"></code>  
<code><img width="5%" title="postgres" src="assets/PostgresSQL.svg"></code> 
</p>

### <img width="3%" title="pc" src="assets/tools.jpg"> Особенности проекта:

* Созданы UI тесты с использованием PageObject и ООП на фреймворке `Selene`
* Созданы UI тесты + DB с использованием передачи данных REST API
* Созданы тесты проверяющие передачу данных REST API + DB
* Созданы Е2Е тесты проверяющие очередь событий KAFKA -> DB -> API
* Для создания отчетов тестирования применен Allure Reports
* Для повышения читаемости отчетов тестирования используется шаблонизатор `Jinja2`
* Для валидации и трансформации данных используется библиотека `Pydantic`
* Для запуска тестов и управлением тестовыми данными созданы специальные фикстуры
* Для управления и вщзаимодействия с БД используется `SQLAlchemy`

### <img width="3%" title="pc" src="assets/pc.jpg"> Локальный запуск тестов

- Скопировать проект на локальную машину
- Запустить Docker локально на компьютере
- Запустить `Niffler` согласно README основного проекта
- Настроить виртуальное окружение проекта

```commandline
python -m venv .venv
source .venv/bin/activate
```

- Установить зависимости проекта из файла `requirements.txt`
- В соответствии с инструкцией установить
  Allure [https://allurereport.org/docs/install/](https://allurereport.org/docs/install/)
- Запустить приложение `Niffler` командой через `bash` терминал:

```commandline
bash docker-compose-dev.sh
```

- Создать тестового пользователя с логином паролем
- Создать и заполнить `.env` в соответствии с примером, добавив созданного тестового пользователя
- Открыть в браузере приложение `Niffler`  - [http://frontend.niffler.dc/](http://frontend.niffler.dc/)
- Зарегистрировать в приложении созданного тестового пользователя
- Запустить тесты командой:

```commandline
pytest --cov=tests
```

<details><summary>Результат прохождения тестов</summary>
<br>
<img src="assets/tests_run.PNG">
</details>

### <img width="3%" title="Allure" src="assets/allure_report.png"> Allure отчет

- Выполнить запрос на формирование отчета  
  note: команда для Windows

```commandline
allure serve
```  

Результат: откроется страница с отчетом Allure Report

<details><summary>Allure report</summary>
<br>
<img src="assets/allure_report_1.PNG">
<img src="assets/allure_report_2.PNG">
<img src="assets/allure_report_3.PNG">
</details>
