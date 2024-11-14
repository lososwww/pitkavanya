import ctypes
import requests
import os

def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("Изображение скачано:", file_path)
        return True
    else:
        print("Ошибка загрузки изображения")
        return False

def set_wallpaper(image_path):  
    if os.path.exists(image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Обои изменены на:", image_path)
    else:
        print("Файл для обоев не найден")

# Ссылка на изображение
image_url = "https://i.ibb.co.com/xm82j5P/1.jpg"

# Путь к папке Downloads для текущего пользователя
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
image_path = os.path.join(downloads_folder, "image.jpg")

if download_image(image_url, image_path):
    set_wallpaper(image_path)
