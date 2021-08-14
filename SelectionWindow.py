
import tkinter as tk
from functools import *
from datetime import datetime
import time
import random
from PIL import Image, ImageTk
from tkinter import ttk,Frame,BOTH,YES
import webbrowser
from mainpage import *
global root
class Exa(Frame):

    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        global c_en1
        global c_en2
        global c_comb

        self.image = Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\KNOLSKAPE_GAFAM_blog_web_banner.gif')
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = tk.Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        c_name = tk.Label(self.background, text="Company Name", font=("Arial", 12,"bold"),bg="light slate gray",fg="black").place(x=330, y=300)
        c_en1 = ttk.Combobox(self.background, font=("Arial", 12))
        c_en1['values']=('TCS','AMAZON')
        c_en1.current()
        c_en1.place(x=500, y=300)
        c_round = tk.Label(self.background, text="Round Type", font=("Arial", 12,"bold"),bg="light slate gray",fg="black").place(x=330, y=400)
        c_comb = ttk.Combobox(self.background, font=("Arial", 12))
        c_comb["values"] = ('Round 1', 'Round 2', 'Round 3')
        c_comb.current()
        c_comb.place(x=500, y=400)
        c_year = tk.Label(self.background, text="Year", font=("Arial", 12,"bold"),bg="light slate gray",fg="black").place(x=330, y=350)
        c_en2 = ttk.Combobox(self.background, font=("Arial", 12))
        c_en2['values']=('2018','2019','2020')
        c_en2.current()
        c_en2.place(x=500, y=350)
        c_search = tk.Button(self.background, text="SEARCH", font=("Arial", 12,"bold"), width=15, height=2, bd=10,bg="light slate gray",fg="black",command=Exa.chk).place(x=350,
                                                                                                                 y=500)
        c_quiz = tk.Button(self.background, text="QUIZ", font=("Arial", 12,"bold"), width=15, height=2, bd=10,bg="light slate gray",fg="black",
                               command=quiz).place(x=600, y=500)
        bck=tk.Button(self.background,text="Back",font=('Arialblack', 9,"bold"), width=14, height=2, bd=9,bg="light slate gray",fg="Black",command=Exa.ch).place(x=970,y=0)
    @staticmethod
    def mainwin():
        if c_en1.get()=='TCS' and c_comb.get()=='Round 1':
            TCS()
        elif c_en1.get()=='AMAZON' and c_comb.get()=='Round 1':
            mainAmazon()
        else:
            pass

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
    @staticmethod
    def ch():
        Frame.destroy()
    @staticmethod
    def chk():
        print(type(c_en1))
        print(type(c_comb))
        if c_en1.get()=='TCS' and c_en2.get()=='2018':
            Exa.rnd1()
        elif c_en1.get()=='TCS' and c_en2.get()=='2019':
            Exa.rnd2()
        elif c_en1.get()=='TCS' and c_en2.get()=='2020':
            Exa.rnd3()
        elif c_en1.get()=='AMAZON' and c_en2.get()=='2018':
            Exa.rnd4()
        elif c_en1.get()=='AMZAON' and c_en2.get()=='2019':
            Exa.rnd5()
        elif c_en1.get()=='AMZAON' and c_en2.get()=='2020':
            Exa.rnd6()
        else:
            pass
    @staticmethod
    def rnd1():
        if c_comb.get()=='Round 1':
            webbrowser.open_new(
            r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2018\ROUND1\2018.pdf')
        elif c_comb.get()=='Round 2':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2018\ROUND2\2019.pdf')
        elif c_comb.get()=='Round 3':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2018\ROUND3\R3.pdf')
        else:
            pass

    @staticmethod
    def rnd2():
        if c_comb.get() == 'Round 1':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2019\ROUND1\2018.pdf')
        elif c_comb.get() == 'Round 2':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2019\ROUND2\2019.pdf')
        elif c_comb.get() == 'Round 3':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2019\ROUND3\R3.pdf')
        else:
            pass

    @staticmethod
    def rnd3():
        if c_comb.get() == 'Round 1':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2020\ROUND1\2018.pdf')
        elif c_comb.get() == 'Round 2':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2020\ROUND2\2019.pdf')
        elif c_comb.get() == 'Round 3':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\TCS\2020\ROUND3\R3.pdf')
        else:
            pass

    @staticmethod
    def rnd4():
        if c_comb.get() == 'Round 1':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2018\ROUND1\2018.pdf')
        elif c_comb.get() == 'Round 2':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2018\ROUND2\2019.pdf')
        elif c_comb.get() == 'Round 3':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2018\ROUND3\R3.pdf')
        else:
            pass
    @staticmethod
    def rnd5():
        if c_comb.get() == 'Round 1':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2019\ROUND1\2018.pdf')
        elif c_comb.get() == 'Round 2':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2019\ROUND2\2019.pdf')
        elif c_comb.get() == 'Round 3':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2019\ROUND3\R3.pdf')
        else:
                pass
    @staticmethod
    def rnd6():
        if c_comb.get() == 'Round 1':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2020\ROUND1\2018.pdf')
        elif c_comb.get() == 'Round 2':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2020\ROUND2\2019.pdf')
        elif c_comb.get() == 'Round 3':
            webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\PLACEMENT\AMAZON\2020\ROUND3\R3.pdf')
        else:
            pass
def quiz():
    Exa.mainwin()


def place():
    searchquiz=tk.Toplevel(root)
    searchquiz.geometry('1100x700')
    searchquiz.title("CAMPUS PREPARATION")
    global e
    e = Exa(searchquiz)
    e.pack(fill=BOTH, expand=YES)
def log():
    root.destroy()
def abt_us():
    about=tk.Toplevel(root)
    about.geometry('1100x700')
    about.title('Developers')

    class Exa(Frame):
        def __init__(self, master, *pargs):
            Frame.__init__(self, master, *pargs)

            self.image = Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\about.gif')
            self.img_copy = self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background = tk.Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)
            #self.img=Image.open("abc.gif")
            #self.im=ImageTk.PhotoImage(file="C:\Users\HP Elite 820\PycharmProjects\Student Diary_abc.gif")
            #lb1=tk.Label(self.background,width=22,height=6).place(x=500,y=10)
            self.img=ImageTk.PhotoImage(Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\my-passport-photo.jpg'))
            lbl=tk.Label(self.background,image=self.img,width=150,height=150).place(x=550,y=70)


        def _resize_image(self, event):
            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)

    e = Exa(about)
    e.pack(fill=BOTH, expand=YES)

def start():

    global root
    #main_account_screen()
    root=tk.Toplevel()
    root.geometry('1100x700')
    root.title("Selection window")

    class Exa(Frame):
        def __init__(self, master, *pargs):

            Frame.__init__(self, master, *pargs)

            self.image = Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\wp5426303.gif')
            self.img_copy = self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background =tk.Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)
            Academic = tk.Button(self.background, text="ACADEMIC", width=25, height=8, font=("Helvetica",12,"bold"), command=Ac,
                                 bd=15,bg="turquoise",fg="black").place(x=250, y=200)
            placement = tk.Button(self.background, text="PLACEMENT", width=25, height=8, font=("Helvetica",12,"bold"),
                                  command=place,bd=15,bg="turquoise",fg="black").place(x=600, y=200)
            logout = tk.Button(self.background, text="LOGOUT", font=('Arial', 12), command=log, bd=6,bg="turquoise",fg="black").place(x=1020, y=0)
            about = tk.Button(self.background, text="ABOUT US", width=25, height=8, font=("Helvetica",12,"bold"), bd=15,bg="turquoise",fg="black",command=abt_us).place(x=420, y=430)
            Tdate = tk.Label(self.background, text=time.asctime(time.localtime(time.time())), font=('Arial', 12,"bold"),bg="black",fg="turquoise").place(x=780, y=3)
            lbl=tk.Label(self.background,text="Select your choice",font=("Castellar",15,"bold"),bg="Black",fg="turquoise",width=20).place(x=100,y=0)

        def _resize_image(self, event):

            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)

    e =Exa(root)
    e.pack(fill=BOTH, expand=YES)
    root.mainloop()
