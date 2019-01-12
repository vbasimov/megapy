### Инструкция по установке и запуску на локальной машине ###

1. 
Устанавливаем git (если не установлен). 

2. 
Переходим в папку, где будет находиться проект, и выкачиваем его с помощью команды ```git clone https://vabsoluter@bitbucket.org/vabsoluter/megapy.git```

3. 
Устанавливаем [Python](https://www.python.org).

4. 
Устанавливаем пакет python3-venv 

5. 
В папке с проектом(или в любой другой) создаем виртуальное окружение командой ```python3 -m venv virtualenv/megapy```

5. 
Далее  необходимо активировать окружение. Для этого выполняем команду ```source /path_to_your_project/virtualenv/megapy/bin/activate```. Подробнее можно почитать [это](https://docs.python.org/3/tutorial/venv.html)
в резулате перед приглашением командной строки(bash) появится название виртуального окружения, например: ``` (megapy) user@host:~$```

6. 
Находясь в папке проекта, устанавливаем зависимости, прописанные в файле requirements.txt: ```pip install -r requirements.txt```

7. 
Выполняем миграции в БД командой ```pyhon3 manage.py migrate```

8. 
Запускаем виртуальный сервер ```pyhton3 manage.py runserver``` и переходим по [localhost:8000](http://localhost:8000). Готово!