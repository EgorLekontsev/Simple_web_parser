import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def parse_website(url):
    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга содержимого HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим интересующие нас элементы на странице
        headlines = soup.find_all('p')

        # Возвращаем список
        return [headline.text.strip() for headline in headlines]

def on_button_click():
    # Получаем URL из текстового поля
    url = url_entry.get()

    try:
        # Парсим веб-сайт
        headlines = parse_website(url)

        # Очищаем текстовое поле вывода и выводим полученный текст
        output_text.delete('1.0', tk.END)
        for headline in headlines:
            output_text.insert(tk.END, headline + '\n')
    except:
        messagebox.showerror("Ошибка", "Такой ссылки не существует, либо сайт недоступен!")

# Создаем графический интерфейс
root = tk.Tk()
root.title("Простой веб-парсер")
root.geometry('600x500')
root.resizable(False, False)
root.configure(bg='#605A99')

# Создаем и размещаем элементы управления
url_label = tk.Label(root, text="Введите URL:", bg='#605A99', fg='#CAB2E3', font="Inter 16")
url_label.place(x=18, y=30)

url_entry = tk.Entry(root, width=50, font="Inter 14")
url_entry.place(x=18, y=73, width=563, height=33)

url_label2 = tk.Label(root, text="Результат:", bg='#605A99', fg='#CAB2E3', font="Inter 16")
url_label2.place(x=220, y=118)

parse_button = tk.Button(root, text="Парсить", command=on_button_click, bg='#7D70B2', fg='#D9D9D9', font="Inter 16")
parse_button.place(x=272, y=24, width=309, height=35)

output_text = tk.Text(root)
output_text.place(x=18, y=154, width=563, height=326)

root.mainloop()
