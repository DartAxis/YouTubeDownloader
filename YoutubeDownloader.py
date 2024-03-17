# подключаем библиотеки

import pytube
from tkinter import messagebox, Tk, Label, StringVar, Entry, Button

ERROR_TITLE = "Ошибка"


# # механика кнопки Скачать
def download():
    # Проверяем адрес видео если не пустой пытаемся качать
    ytlink = link_video.get()
    ytplink = link_playlist.get()
    if len(ytlink) > 0 or len(ytplink) > 0:
        if len(ytlink) > 0:
            download_video(ytlink)
        if len(ytplink) > 0:
            download_playlist(ytplink)
    else:
        messagebox.showerror(ERROR_TITLE, "Ни одно поле с адресом незаполнено")


def download_playlist(url):
    """
    Функция скачивания всех видео из плейлиста на YouTube
    :param url: ссылка плейлиста на YouTube:
    :return:
    """
    try:
        playlist = pytube.Playlist(url)
        videos = list(playlist.videos)
        for idx in range(0, len(videos)):
            # получаем ссылку на видео с самым высоким качеством
            video = videos[idx].streams.get_highest_resolution()
            new_file_name = str(idx + 1) + "-" + video.default_filename
            # скачиваем видео
            video.download(filename=new_file_name)
        messagebox.showinfo("Готово", "Загрузка завершена")
    except:
        # выводим сообщение об ошибке
        messagebox.showerror(ERROR_TITLE, "Шота пашло не так")


def download_video(url):
    """
    Функция скачивания одного видео с YouTube
    :param url: ссылка на видео на YouTube:
    :return:
    """
    # пробуем скачать видео по ссылке
    try:
        # переводим его в нужный формат
        youtubelink = pytube.YouTube(url)
        # получаем ссылку на видео с самым высоким качеством
        video = youtubelink.streams.get_highest_resolution()
        # скачиваем видео
        video.download()
        # выводим результат
        messagebox.showinfo("Готово", "Загрузка завершена")
    # если скачать не получилось
    except:
        # выводим сообщение об ошибке
        messagebox.showerror(ERROR_TITLE, "Ссылка не работает")


# при нажатии на кнопку очистки очищаем строку с адресом видео
def reset():
    link_video.set("")
    link_playlist.set("")


# при нажатии на кнопку выхода — закрываем окно с интерфейсом
def quiting():
    root.destroy()


# рисуем главное окно
root = Tk()
root.geometry("720x350")
root.resizable(False, False)
# заголовок окна
root.title("Код")
# цвет фона
root.config(bg='#D3D3D3')
# заголовок формы
lb = Label(root, text="---Загрузка видео с YouTube---", font=('Arial', 10, 'bold'), bg='#D3D3D3')
lb.pack(pady=15)
# пояснительный текст для поля с адресом
lb1 = Label(root, text="Ссылка на видео :", font=('Arial', 10, 'bold'), bg='#D3D3D3')
lb1.place(x=10, y=60)
# пояснительный текст для поля с адресом плэйлиста
lb2 = Label(root, text="Ссылка на PlayList :", font=('Arial', 10, 'bold'), bg='#D3D3D3')
lb2.place(x=10, y=100)
# поле ввода адреса видео
link_video = StringVar()
en1 = Entry(root, textvariable=link_video, font=('Arial', 10, 'bold'), width=75)
en1.place(x=150, y=60)
# поле ввода адреса видео
link_playlist = StringVar()
en1 = Entry(root, textvariable=link_playlist, font=('Arial', 10, 'bold'), width=75)
en1.place(x=150, y=100)
# кнопка скачивания
btn1 = Button(root, text="Скачать", font=('Arial', 10, 'bold'), bd=4, command=download)
btn1.place(x=590, y=130)
# кнопки очистки и выхода
btn2 = Button(root, text="Очистить", font=('Arial', 10, 'bold'), bd=4, command=reset)
btn2.place(x=450, y=130)
btn3 = Button(root, text=" Выход ", font=('Arial', 10, 'bold'), bd=4, command=quiting)
btn3.place(x=250, y=190)
# запускаем окно
root.mainloop()
