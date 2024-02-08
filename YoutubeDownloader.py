# подключаем библиотеки
from tkinter import *
import pytube
from tkinter import messagebox

# рисуем главное окно
root = Tk()
root.geometry("500x250")
root.resizable(False, False)
# заголовок окна
root.title("Код")
# цвет фона
root.config(bg='#D3D3D3')


# механика кнопки Скачать
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
        messagebox.showerror("Ошибка", "Ни одно поле с адресом незаполнено")


def download_playlist(url):
    try:
        playlist = pytube.Playlist(url)
        # print('Number of videos in playlist: %s' % len(playlist.video_urls))
        # playlist.download_all()
        for video in playlist.videos:
            # получаем ссылку на видео с самым высоким качеством
            video = video.streams.get_highest_resolution()
            # скачиваем видео
            video.download()
        messagebox.showinfo("Готово", "Загрузка завершена")
    except:
        # выводим сообщение об ошибке
        messagebox.showerror("Ошибка", "Шота пашло не так")


def download_video(url):
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
        messagebox.showerror("Ошибка", "Ссылка не работает")


# при нажатии на кнопку очистки очищаем строку с адресом видео
def reset():
    link_video.set("")


# при нажатии на кнопку выхода — закрываем окно с интерфейсом
def quit():
    root.destroy()


# заголовок формы
lb = Label(root, text="---Загрузка видео с YouTube---", font=('Arial,15,bold'), bg='#D3D3D3')
lb.pack(pady=15)
# пояснительный текст для поля с адресом
lb1 = Label(root, text="Ссылка на видео :", font=('Arial,15,bold'), bg='#D3D3D3')
lb1.place(x=10, y=80)

# пояснительный текст для поля с адресом плэйлиста
lb2 = Label(root, text="Ссылка на PlayList :", font=('Arial,15,bold'), bg='#D3D3D3')
lb2.place(x=10, y=100)

# поле ввода адреса видео
link_video = StringVar()
En1 = Entry(root, textvariable=link_video, font=('Arial,15,bold'))
En1.place(x=230, y=80)

# поле ввода адреса видео
link_playlist = StringVar()
En1 = Entry(root, textvariable=link_playlist, font=('Arial,15,bold'))
En1.place(x=230, y=100)

# кнопка скачивания
btn1 = Button(root, text="Скачать", font=('Arial,10,bold'), bd=4, command=download)
btn1.place(x=330, y=130)

# кнопки очистки и выхода
btn2 = Button(root, text="Очистить", font=('Arial,10,bold'), bd=4, command=reset)
btn2.place(x=120, y=190)
btn3 = Button(root, text=" Выход ", font=('Arial,10,bold'), bd=4, command=quit)
btn3.place(x=250, y=190)

# запускаем окно
root.mainloop()
