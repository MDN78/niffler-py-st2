## Фреймворк автоматизированного тестирования приложения Niffler. 

### Особенности фреймворка:  
<p  align="center">
  <code><img width="75%" title="main_page" src="/assets/main_page.PNG"></code>
</p>

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