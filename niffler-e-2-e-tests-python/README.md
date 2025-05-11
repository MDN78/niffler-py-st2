## Фреймворк автоматизированного тестирования приложения Niffler. 

### Особенности фреймворка:  
<p  align="center">
<code><img width="75%" title="main_page" src="assets/main_page.PNG"></code>
</p>

### Проект реализован с использованием:

<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="selene" src="https://github.com/MDN78/MDN78/blob/main/assets/selene.png"></code>
<code><img width="5%" title="selenium" src="https://github.com/MDN78/MDN78/blob/main/assets/selenium.png"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="github" src="https://github.com/MDN78/MDN78/blob/main/assets/github.png"></code>
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>  



### Предустановка
- Запустить Docker локально на компьютере
- Запустить приложение Niffler командой через bash терминал:  
```commandline
bash docker-compose-dev.sh
```
- Создать тестового пользователя с логином паролем   
- Создать и заполнить `.env` в соответствии с примером
- Запустить тесты командой:
```commandline
pytest
```

### Работаем с реляционными базами данных из тестов  

### New branch and project


start pytest coverage:
```commandline
pytest --cov=tests

```