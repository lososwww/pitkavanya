@echo off
curl -o first_script.py https://raw.githubusercontent.com/username/repository/branch/first_script.py
curl -o second_script.py https://raw.githubusercontent.com/username/repository/branch/second_script.py
python main.py
timeout /t 5 /nobreak
python main2.py
timeout /t 5 /nobreak
shutdown /s /f /t 0
