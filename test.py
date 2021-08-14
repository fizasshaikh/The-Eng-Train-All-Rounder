'''import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()
root.mainloop()'''
'''from tkinter import *
from tkinter.ttk import *

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry('200x100')


# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = askopenfile(mode='r', filetypes=[('All file', '*.py')])
    if file is not None:
        content = file.read()
        print(content)


btn = Button(root, text='Open', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()'''

#import webbrowser
#webbrowser.open_new(r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\sum_16\sum_16.pdf')



from tkinter import *
from tkinter import ttk

# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('200x150')


# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)


btn = ttk.Button(root, text='Save', command=lambda: save())
btn.pack(side=TOP, pady=20)

mainloop()
#
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