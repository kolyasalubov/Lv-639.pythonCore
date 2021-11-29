from tkinter import *
from random import randrange as rnd, choice
import time
import datetime
import pygame
from pygame.mixer import pause
import re
import sqlite3
from tkinter import ttk

# занулюємо необхідні для подальшої роботи параметри
before_pause_time = 0
all_pause_time=0
points = 0
# ініціалізуємо музику
pygame.mixer.init()
m = 'select.mp3'
w = 'win.wav'
pygame.mixer.music.load(m)
pygame.mixer.music.play(-1, 0.0)
hit_sound = pygame.mixer.Sound("tic.mp3")
fail_hit = pygame.mixer.Sound("fail.mp3")
pause_music=False

CONST_NEGATIVE = -1000
colors = ['red','orange','yellow','green','blue', 'LightSkyBlue1']
# створюємо вікно
root = Tk()
# центруємо вікно
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# робимо вікно незмінним
root.resizable(False, False)
root.title("The Magic Balls")

# створюємо холст, на якому зможемо малювати кульки, текст та ін.
canv = Canvas(root,bg='LightSkyBlue1')
canv.pack(fill=BOTH, expand=1)
# занулюємо(ініціалізуємо) текстові віджети, які викор. далі
text = canv.create_text(55,30,text='')
pause_banner=canv.create_text(200,400, text='')
# додаємо малюнок-заставку
img=PhotoImage(file="giphy.gif")
logo=canv.create_image(160, 10, anchor=NW, image=img)

def new_ball():
    """
    функція створює випадкові кульки, а також змінює музику в залежності від рівня гри
    """
    global x,y,r,ball,color,points,b2,b3,b4,m

    canv.delete(ball)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(20,50)
    color = choice(colors)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = color, width=0.1)
        
    if points >= 30:
        if m!='stage3.mp3':
            m = 'stage3.mp3'
            pygame.mixer.music.load(m)
            pygame.mixer.music.play(-1, 0.0)
        b2=root.after(650,new_ball)
    elif points >= 20:
        if m!='stage2.mp3':
            m='stage2.mp3'
            pygame.mixer.music.load(m)
            pygame.mixer.music.play(-1, 0.0)
        b3=root.after(800,new_ball)
    else:
        b4=root.after(1000,new_ball)
     
def click(event):
    """
    функція обробляє влучання в кульку, рахує очки, та завершує гру або програшем або перемогою,
    також функція створює базу даних і записує туди дані
    """
    global points, x, text, timer, before_pause_time,all_pause_time,user_name, date_game
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        hit_sound.play()
        if color == 'LightSkyBlue1':
            points -= 5
        elif r <= 22:
            points += 7
        elif r <= 30:
            points += 5
        elif r<=40:
            points += 2
        else:
            points += 1

        x = CONST_NEGATIVE
        #видалення круга при кліку
        canv.delete(text)
        canv.delete(ball)
        text = canv.create_text(55,30,text=f"{user_name}\nScore: " + str(points), font = 'Arial 20')

        if points >= 35:
            canv.delete(text)
            canv.delete(ball)
            root.after_cancel(b2)
            pygame.mixer.music.load(w)
            pygame.mixer.music.play()
            finish_time = time.time()
            timer = finish_time-start_time+all_pause_time
            text = canv.create_text(650,50, text=f"C O N G R A T U L A T I O N!!!\n{user_name}\nyou win with score: {points}\nTime: {round(timer)} sec", font = 'Arial 20')
            date_game = (datetime.date.today()).strftime("%b-%d-%Y")
            data_base()
            points = 0
            all_pause_time = 0
            timer = 0
            pre_start()
        
    else:
        fail_hit.play()
        canv.delete(text)
        canv.delete(ball)
        if points >=30:
            root.after_cancel(b2)
        elif points >=20:
            root.after_cancel(b3)
        else:
            root.after_cancel(b4)
        pygame.mixer.music.stop()
        finish_time = time.time()
        timer = finish_time-start_time+all_pause_time
        text = canv.create_text(730,40, text=f"{user_name}\nScore: {points}\nTime: {round(timer)} sec", font = 'Arial 20')
        date_game = (datetime.date.today()).strftime("%b-%d-%Y")
        data_base()
        points = 0
        all_pause_time = 0
        timer = 0
        pre_start()

def paused(e):
    """
    функція паузи у грі
    """
    global pause_banner, pause_music, before_pause_time
    pause_banner=canv.create_text(400,300,text="PAUSE", fill='red', font = 'Arial 60')
    pygame.mixer.music.pause()
    pause_music=True
    canv.unbind('<Button-1>')
    before_pause_time=time.time()
    canv.delete(ball)
    if points >=30:
        root.after_cancel(b2)
    elif points >=20:
        root.after_cancel(b3)
    else:
        root.after_cancel(b4)
    canv.bind_all('<space>', start_game)

def start_game(event=None):
    """
    функція запускає гру з першого рівня з відповідною музикою,
    передає роботу функції new_ball(),
    запускає обробник події - натискання ЛКМ, та Пробіл
    """
    global ball, text, points, start_time, logo, m, pause_banner,pause_music,before_pause_time, all_pause_time,user_name
    canv.delete(pause_banner)
    if pause_music == True:
        pygame.mixer.music.unpause()
        pause_music=False
        after_pause_time=time.time()
        all_pause_time+=after_pause_time-before_pause_time
    else:     
        m = 'stage1.mp3'
        pygame.mixer.music.stop()
        pygame.mixer.music.load(m)
        pygame.mixer.music.play(-1, 0.0)
        start_time = time.time()
    canv.delete(text)
    canv.delete(logo)
    button1.destroy()
    button2.destroy()
    ball = canv.create_oval(-100,0,0,0)
    text = canv.create_text(55,30,text=f"{user_name}\nScore: " + str(points), font = 'Arial 20')
    new_ball()
    canv.bind('<Button-1>', click)
    canv.bind_all('<space>', paused)

def pre_start():
    """
    функція створює кнопки Старта гри та Виходу
    """
    global button1, button2
    canv.unbind('<Button-1>')
    canv.unbind_all('<space>')
    canv.delete(id1,id2,id3)
    button1 = Button(canv, text="Start", bg="LightSkyBlue1", command=start_game)
    button1.pack(side=LEFT, anchor=E, expand=1)
    button2 = Button(canv, text="Qiut", bg="LightSkyBlue1", command=root.destroy)
    button2.pack(side=LEFT, anchor=W, expand=1)

def nick():
    """
    функція валідує введене ім'я гравця
    """
    global user_name
    user_name=a.get()
    pattern = re.compile(r"[A-Za-z0-9_-]{1,10}$")
    if not pattern.match(user_name):
        canv.delete(id1,id2,id3)   
        login()     
    else:
        pre_start()

def login():
    """
    функція запитує імя гравця і передає на валідацію функції nick()
    """
    global nickname,a,b,c,id1,id2,id3
    nickname=StringVar()
    a=Entry(root, textvariable=nickname)
    b=Label(root, text="Enter your nickname:")
    c=Button(root, text="Login", command=nick)
    id1 = canv.create_window(430, 297, window=a)
    id2 = canv.create_window(263, 297, window=b)
    id3 = canv.create_window(563, 297, window=c)

def data_base():
    """
    функція створю базу даних database.db, а також виводить у нове вікно 10 накращих результатів
    """
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """CREATE TABLE IF NOT EXISTS achivements(name TEXT, score INTEGER, time INTEGER, date TEXT)"""
        cursor.execute(query)
        db.commit()
        query="SELECT COUNT(*) FROM achivements"
        cursor.execute(query)
        count=cursor.fetchone()[0]
        if count == 100:
            query="DELETE FROM achivements WHERE ROWID in(SELECT ROWID FROM achivements ORDER BY score ASC, time DESC LIMIT 1)"
            cursor.execute(query)
            db.commit()
        query = f"INSERT INTO achivements (name, score, time, date) VALUES('{user_name}', {points}, {round(timer)}, '{date_game}')"
        cursor.execute(query)
        db.commit()
        query ="SELECT * FROM achivements ORDER BY score DESC, time ASC LIMIT 10"
        root2 = Tk()
        root2.title('achivements')
        root2.geometry('380x210+260+140')
        root2.resizable(False, False)
        columns = ('rating', 'name', 'score', 'time', 'date')
        tree = ttk.Treeview(root2, columns=columns, show='headings')
        tree.heading('rating', text='rating')
        tree.heading('name', text='nickname')
        tree.heading('score', text='score')
        tree.heading('time', text='time')
        tree.heading('date', text='date')
        tree.column('rating', width=40, anchor=CENTER)
        tree.column('name', width=100)
        tree.column('score', width=40, anchor=CENTER)
        tree.column('time', width=80, anchor=CENTER)
        tree.column('date', width=120, anchor=CENTER)
        players=cursor.execute(query)
        i=1
        for player in players:
            tree.insert('', END, values=(i,player[0],player[1],f"{player[2]} sec",player[3]))
            i+=1
        tree.grid(row=0, column=0, sticky='nsew')

login()

mainloop()
