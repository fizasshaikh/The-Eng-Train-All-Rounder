import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Frame,BOTH,YES,END
import webbrowser
from tkinter.filedialog import asksaveasfile
from os import *

#function of theroy

def theroy():

    global screen
    screen=tk.Toplevel(Acdemic)
    screen.title('THEROY')
    screen.geometry('1100x700')
    class Exa(Frame):

        def __init__(self, master, *pargs):

            Frame.__init__(self, master, *pargs)

            global t_comb
            global c_comb1
            global c_comb2

            self.image = Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\abc.gif')
            self.img_copy = self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background =tk.Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)
            year_lab = tk.Label(self.background, text="year", width=22, bg="deepskyblue4", fg="white", height=2,font=("Arial", 12)).place(x=170, y=100)
            t_comb = ttk.Combobox(self.background, width=15, height=2, font=("Arial", 15))
            t_comb["values"] = ("FE", "SE", "TE", "BE")
            t_comb.current()
            t_comb.place(x=440, y=100)
            sem_lab = tk.Label(self.background, text="Semester", width=22, height=2, bg="deepskyblue4", fg="white",
                               font=("Arial", 12)).place(x=170, y=200)
            c_comb1 = ttk.Combobox(self.background, width=15, height=2, font=('Arial', 15))
            c_comb1['values'] = ('Sem-I', 'Sem-II')
            c_comb1.current()
            c_comb1.place(x=440, y=200)
            sub_lab = tk.Label(self.background, text="SubjectName", width=22, height=2, bg="deepskyblue4", fg="white",
                               font=("Arial", 12)).place(x=170, y=300)
            c_comb2 = ttk.Combobox(self.background, width=15, height=2, font=("Arial", 15),postcommand=Exa.chk)
            # c_comb2['values']=()
            # c_comb2.current()
            c_comb2.place(x=440, y=300)

            # radio1=tk.Radiobutton(self.background,text="Notes",font=("Arial"),bg='deepskyblue4',value=1,fg="white").place(x=350,y=470)
            # radio2 = tk.Radiobutton(self.background, text="Assignment", font=("Arial"),bg='deepskyblue4',fg="white").place(x=530, y=470)

            practical_button = tk.Button(self.background, text='STORE', bg='deepskyblue4', fg='white', width=22, height=3,
                                         bd=10, font=("Arial", 10, "bold"),command=Exa.save).place(x=220, y=400)
            practical_button1 = tk.Button(self.background, text='VIEW', bg='deepskyblue4', fg='white', width=22, height=3,
                                          bd=10, font=("Arial", 10, "bold"),command=Exa.chkoption_view).place(x=500, y=400)
            lb1 = tk.Label(self.background, text="View And Store The Theory Data Select Your Option", width=50, font=( "Castellar", 15, "bold"),bg="deepskyblue4",fg="white")\
                .place(x=0,y=0)
            acadmic_entry3 = tk.Button(self.background, text='BACK', bg='deepskyblue4', fg='white',
                                       font=('helvetica', 9, 'bold'), width=12, height=2, bd=7,
                                       command=Exa.back1).place(x=990, y=5)

        @staticmethod
        def back1():
            screen.destroy()


        @staticmethod
        def chk():
            if t_comb.get() == "FE" and c_comb1.get() == "Sem-I":
                c_comb2['values'] = ("Physics-I", "Chemistry-I", "Maths-I", "Basic Electrical and elecronics",
                                       "Engineering Mechanics","Basic Mechanical Engineering","Communication Skills")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            elif t_comb.get() == "FE" and c_comb1.get() == "Sem-II":
                c_comb2['values'] = (
                    "Physics-II", "Chemistry-II", "Maths-II", "Graphics & Design", "Basic Civil Engineering",
                    "Programming for problem solving", "Professional Communication",
                    "Democracy , election and good governance")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            elif t_comb.get() == "SE" and c_comb1.get() == "Sem-I":
                c_comb2['values'] = (
                    "Applied Maths-I", "Discrete Mathematics Structure", "Data Communication", "Digital Techniques",
                    "Computer Graphics", "Advance C")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            elif t_comb.get() == "SE" and c_comb1.get() == "Sem-II":
                c_comb2['values'] = (
                    "Applied Maths-II", "Theory Of Computation", "Microprocessor", "Data Structure",
                    "Computer Networks", "C++")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            elif t_comb.get() == "TE" and c_comb1.get() == "Sem-I":
                c_comb2['values'] = (
                    "System Programming", "operating System-I", "Software Engineering", "Database Engineering",
                    "Design & Analysis of Alorithm", "Python Programming", "Java Programming")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            elif t_comb.get() == "TE" and c_comb1.get() == "Sem-II":
                c_comb2['values'] = (
                    "Compiler Construction", "Unix Operating System", "Computer organization & Architecture",
                    "Artificial Intelligence", "Mobile Application Development", "Elective-III")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            elif t_comb.get() == "BE" and c_comb1.get() == "Sem-I":
                c_comb2['values'] = ("A", "B", "C", "D")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            elif t_comb.get() == "BE" and c_comb1.get() == "Sem-II":
                c_comb2['values'] = ("A", "B", "C", "D")
                c_comb2.current()
                c_comb2.place(x=440, y=300)
            else:
                pass

        def _resize_image(self, event):


            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)

        @staticmethod
        def save():
            files = [('All Files', '*.*'),
                     ('Python Files', '*.py'),
                     ('Text Document', '*.txt')]
            file = asksaveasfile(filetypes=files, defaultextension=files)

        @staticmethod
        def chkoption_view():
                if t_comb.get() == 'FE' and c_comb1.get() == 'Sem-I':
                    Exa.FE_SEM1()
                elif t_comb.get() == 'FE' and c_comb1.get() == 'Sem-II':
                    Exa.FE_SEM2()
                elif t_comb.get() == 'SE' and c_comb1.get() == 'Sem-I':
                    Exa.SE_SEM1()
                elif t_comb.get() == 'SE' and c_comb1.get() == 'Sem-II':
                    Exa.SE_SEM2()
                elif t_comb.get() == 'TE' and c_comb1.get() == 'Sem-I':
                    Exa.TE_SEM1()
                elif t_comb.get() == 'TE' and c_comb1.get() == 'Sem-II':
                    Exa.TE_SEM2()
                else:
                    pass


        @staticmethod
        def FE_SEM1():
            if c_comb2.get() == 'Physics-I':
                pass
            elif c_comb2.get() == 'Chemistry-I':
                pass
            elif c_comb2.get() == 'Maths-I':
                pass
            elif c_comb2.get() == 'Basic Electrical and elecronics':
               pass
            elif c_comb2.get() == 'Engineering Mechanics':
               pass
            elif c_comb2.get() == 'Basic Mechanical Engineering':
                pass
            elif c_comb2.get()=='Basic Mechanical Engineering':
                pass
            elif c_comb2.get()=='Communication Skills':
                pass
            else:
                pass

        @staticmethod
        def FE_SEM2():
            if c_comb2.get() == 'Physics-II':
               pass
            elif c_comb2.get() == 'Chemistry-II':
                pass
            elif c_comb2.get() == 'Maths-II':
                pass
            elif c_comb2.get() == 'Graphics & Design':
               pass
            elif c_comb2.get() == 'Basic Civil Engineering':
                pass
            elif c_comb2.get() == 'Programming for problem solving':
                pass
            elif c_comb2.get()=='Professional Communication':
               pass
            elif c_comb2.get()=='Democracy , election and good governance':
                pass
            else:
                pass

        @staticmethod
        def SE_SEM1():
            if c_comb2.get() == 'Applied Maths-I':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_I\AMP 3\M3.pdf')
            elif c_comb2.get() == 'Discrete Mathematics Structure':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_I\DMS\DMS.pdf')
            elif c_comb2.get() == 'Data Communication':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_I\DC\DCOM.pdf')
            elif c_comb2.get() == 'Digital Techniques':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_I\DT\DTE.pdf')
            elif c_comb2.get() == 'Computer Graphics':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_I\CG\CG.pdf')
            elif c_comb2.get() == 'Advance C':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_I\ACC\ACC.pdf')
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_I\ACC\C.pdf')
            else:
                pass

        @staticmethod
        def SE_SEM2():
            if c_comb2.get() == 'Applied Maths-II':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_II\AMP 4\M4.pdf')
            elif c_comb2.get() == 'Theory Of Computation':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_II\TOC\TOC.pdf')
            elif c_comb2.get() == 'Microprocessor':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_II\MAP\MAP.pdf')
            elif c_comb2.get() == 'Data Structure':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_II\DS\DS.pdf')
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_II\DS\DS2.pdf')
            elif c_comb2.get() == 'Computer Networks':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_II\CN\CN.pdf')
            elif c_comb2.get() == 'C++':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\SE\Sem_II\CPP\CPP.pdf')
            else:
                pass

        @staticmethod
        def TE_SEM1():
            if c_comb2.get() == 'System Programming':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_I\SP\SP.pdf')
            elif c_comb2.get() == 'operating System-I':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_I\OS\OS.pdf')
            elif c_comb2.get() == 'Software Engineering':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_I\SE\SE.pdf')
            elif c_comb2.get() == 'Database Engineering':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_I\DBE\DBE.pdf')
            elif c_comb2.get() == 'Design & Analysis of Alorithm':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_I\DAA\DAA.pdf')
            elif c_comb2.get() == 'Python Programming':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_I\PP\PP.pdf')
            elif c_comb2.get() == 'Java Programming':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_I\JP\JP1.pdf')
            else:
                pass

        @staticmethod
        def TE_SEM2():
            if c_comb2.get() == 'Compiler Construction':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\CC\CC.pdf')
            elif c_comb2.get() == 'Unix Operating System':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\OS2\OS2.pdf')
            elif c_comb2.get() == 'Computer organization & Architecture':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\COA\COA.pdf')
            elif c_comb2.get() == 'Artificial Intelligence':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\AI\AI.pdf')
            elif c_comb2.get() == 'Mobile Application Development':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\MAD\AAD.pdf')
            elif c_comb2.get() == 'Elective-III':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\EL_I\ANN.pdf')
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\EL_I\DS.pdf')
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Theory_folder\TE\Sem_II\EL_I\OOM.pdf')
            else:
                pass
    global e
    e =Exa(screen)
    #e.chk()
    e.pack(fill=BOTH, expand=YES)

#function of examination

def Examination():
    global put
    put=tk.Toplevel(Acdemic)
    put.title('Examination')
    put.geometry('1100x700')

    class Exa(Frame):
        def __init__(self, master, *pargs):
            global E_comb
            global s_comb1
            global s_comb2
            Frame.__init__(self, master, *pargs)

            self.image = Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\abc.gif')
            self.img_copy = self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background = tk.Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)
            dept_name = tk.Label(self.background, text="Departement_Name", width=22, height=2, bg="deepskyblue4", fg="white", font=("Arial", 12)).place(x=170, y=120)
            dept_entry = tk.Entry(self.background, width=21, font=("Arial", 12),text='CSE').place(x=440, y=120)
            Exame_label = tk.Label(self.background, text="Examination", width=22, height=2, bg="deepskyblue4", fg="white",font=("Arial", 12)).place(x=170, y=190)
            E_comb = ttk.Combobox(self.background, width=15, height=2, font=("Arial", 15))
            E_comb['values'] = ("FE", "SE", "TE", "BE")
            E_comb.current()
            E_comb.place(x=440, y=190)
            year_label = tk.Label(self.background, text='YEAR', width=22, height=2, bg='deepskyblue4', fg='white', font=("Arial", 12)).place(x=170,y=260)
            sem_lab = tk.Label(self.background, text="Semester", width=22, height=2, bg="deepskyblue4", fg="white", font=("Arial", 12)).place(x=170,y=330)
            s_comb1 = ttk.Combobox(self.background, width=15, height=2, font=('Arial', 15))
            s_comb1['values'] = ('Sem-I', 'Sem-II')
            s_comb1.current()
            s_comb1.place(x=440, y=330)
            s_comb2 = ttk.Combobox(self.background, width=15, height=2, font=('Arial', 15))
            s_comb2['values'] = ('sum-16', 'win-17', 'sum-17', 'win-18', 'sum-18', 'win-19')
            s_comb2.current()
            s_comb2.place(x=440, y=260)
            E_btt = tk.Button(self.background, text="VIEW", width=22, height=3, bd=10, font=("Arial", 10,"bold"),
                         bg="deepskyblue4", fg="white",command=Exa.chkview).place(x=410, y=480)
            lb1 = tk.Label(self.background, text="To View The Question papers Enter The Below details", width=50,font=("Castellar", 15, "bold"), bg="deepskyblue4", fg="white").place(x=0, y=0)
            b= tk.Button(self.background, text='BACK', bg='deepskyblue4', fg='white', font=('helvetica', 9, 'bold'), width=12, height=2, bd=7, command=Exa.back1).place(x=990,y=5)

        def _resize_image(self, event):
            new_width = event.width
            new_height = event.height
            self.image = self.img_copy.resize((new_width, new_height))
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)
        @staticmethod
        def back1():
            put.destroy()

        @staticmethod
        def chkview():
            if E_comb.get()=='FE' and s_comb1.get()=='Sem-I':
                Exa.FE_SEM1()
            elif E_comb.get()=='FE' and s_comb1.get()=='Sem-II':
                Exa.FE_SEM2()
            elif E_comb.get()=='SE' and s_comb1.get()=='Sem-I':
                Exa.SE_SEM1()
            elif E_comb.get()=='SE' and s_comb1.get()=='Sem-II':
                Exa.SE_SEM2()
            elif E_comb.get()=='TE' and s_comb1.get()=='Sem-I':
                Exa.TE_SEM1()
            elif E_comb.get()=='TE' and s_comb1.get()=='Sem-II':
                Exa.TE_SEM2()
            else:
                pass

       #elif E_comb.get()=='FE' and s_comb1.get()=='Sem-I' and s_comb2.get()=='win-17':
       #webbrowser.open_new(r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\win_17\win_17.pdf')
        @staticmethod
        def FE_SEM1():
            if s_comb2.get() == 'sum-16':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\sum_16\sum_16.pdf')
            elif s_comb2.get() == 'win-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\win_17\win_17.pdf')
            elif s_comb2.get() == 'sum-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\sum_17\sum_17.pdf')
            elif s_comb2.get() == 'sum-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\sum_18\sum_18.pdf')
            elif s_comb2.get() == 'win-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\win_18\win_18.pdf')
            elif s_comb2.get() == 'win-19':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 1\win_19\win_19.pdf')
            else:
                pass

        @staticmethod
        def FE_SEM2():
            if s_comb2.get() == 'sum-16':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 2\sum_16\sum_16.pdf')
            elif s_comb2.get() == 'win-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 2\win_17\win_17.pdf')
            elif s_comb2.get() == 'sum-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 2\sum_17\sum_17.pdf')
            elif s_comb2.get() == 'sum-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 2\sum_18\sum_18.pdf')
            elif s_comb2.get() == 'win-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 2\win_18\win_18.pdf')
            elif s_comb2.get() == 'win-19':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\FE\SEM 2\win_19\win_19.pdf')
            else:
                pass

        @staticmethod
        def SE_SEM1():
            if s_comb2.get() == 'sum-16':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 1\sum_16\sum_16.pdf')
            elif s_comb2.get() == 'win-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 1\win_17\win_17.pdf')
            elif s_comb2.get() == 'sum-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 1\sum_17\sum_17.pdf')
            elif s_comb2.get() == 'sum-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 1\sum_18\sum_18.pdf')
            elif s_comb2.get() == 'win-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 1\win_18\win_18.pdf')
            elif s_comb2.get() == 'win-19':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 1\win_19\win_19.pdf')
            else:
                pass

        @staticmethod
        def SE_SEM2():
            if s_comb2.get() == 'sum-16':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 2\sum_16\sum_16.pdf')
            elif s_comb2.get() == 'win-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 2\win_17\win_17.pdf')
            elif s_comb2.get() == 'sum-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 2\sum_17\sum_17.pdf')
            elif s_comb2.get() == 'sum-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 2\sum_18\sum_18.pdf')
            elif s_comb2.get() == 'win-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 2\win_18\win_18.pdf')
            elif s_comb2.get() == 'win-19':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\SE\SEM 2\win_19\win_19.pdf')
            else:
                pass

        @staticmethod
        def TE_SEM1():
            if s_comb2.get() == 'sum-16':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 1\sum_16\sum_16.pdf')
            elif s_comb2.get() == 'win-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 1\win_17\win_17.pdf')
            elif s_comb2.get() == 'sum-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 1\sum_17\sum_17.pdf')
            elif s_comb2.get() == 'sum-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 1\sum_18\sum_18.pdf')
            elif s_comb2.get() == 'win-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 1\win_18\win_18.pdf')
            elif s_comb2.get() == 'win-19':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 1\win_19\win_19.pdf')
            else:
                pass

        @staticmethod
        def TE_SEM2():
            if s_comb2.get() == 'sum-16':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\sum_16\sum_16.pdf')
            elif s_comb2.get() == 'win-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\win_17\win_17.pdf')
            elif s_comb2.get() == 'sum-17':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\sum_17\sum_17.pdf')
            elif s_comb2.get() == 'sum-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\sum_18\sum_18.pdf')
            elif s_comb2.get() == 'win-18':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\win_1qweuueowwe2o8\win_18.pdf')
            elif s_comb2.get() == 'win-19':
                webbrowser.open_new(
                r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\win_19\win_19.pdf')
            else:
                pass
    e = Exa(put)
    e.pack(fill=BOTH, expand=YES)


def practical():
 global show
 show =tk.Toplevel(Acdemic)
 show.title('practical')
 show.geometry('1100x700')

 class Exa(Frame):
        def __init__(self, master, *pargs):

            global p_comb1
            global p_comb2
            global p_comb3
            global p_comb4

            Frame.__init__(self, master, *pargs)

            self.image = Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\abc.gif')
            self.img_copy = self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background =tk.Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)
            practical_label = tk.Label(self.background, text='YEAR', bg='deepskyblue4', fg='white', width=22, font=("Arial", 12),height=2).place(x=250, y=100)
            p_comb1 = ttk.Combobox(self.background, width=15, font=("Arial", 15), height=2)
            p_comb1['value'] = ('FE', 'SE', 'TE', 'BE')
            p_comb1.current()
            p_comb1.place(x=500, y=100)
            practical_label1 = tk.Label(self.background, text='SEMESTER', bg='deepskyblue4', fg='white', width=22, height=2,
                                        font=("Arial", 12)).place(x=250, y=170)
            p_comb2 = ttk.Combobox(self.background, width=15, font=("Arial", 15), height=2)
            p_comb2['value'] = ('Sem-I', 'Sem-II')
            p_comb2.current()
            p_comb2.place(x=500, y=170)
            practical_label2 = tk.Label(self.background, text="BATCH", bg="deepskyblue4", fg="white", width=22, height=2,font=("Arial", 12)).place(x=250, y=240)
            p_comb3 = ttk.Combobox(self.background, width=15, font=("Arial", 15), height=2)
            p_comb3['value'] = ('B1', 'B2', 'B3', 'B4')
            p_comb3.place(x=500, y=240)
            practical_label3 = tk.Label(self.background, text='SUBJECT NAME', bg='deepskyblue4', fg='white', width=22, height=2,font=("Arial", 12)).place(x=250, y=310)
            p_comb4 = ttk.Combobox(self.background, width=15, font=("Arial", 15), height=2, postcomman=Exa.chkprac)
            # p_comb4['value']=()
            # p_comb4.current()
            p_comb4.place(x=500, y=310)
            practical_label4 = tk.Label(self.background, text='FILE NAME', bg='deepskyblue4', fg='white', width=22, height=2,font=("Arial", 12)).place(x=250, y=380)
            p_comb = ttk.Combobox(self.background, width=15, height=2, font=("Arial", 15))
            p_comb['values'] = ('LabMannual')
            p_comb.current()
            p_comb.place(x=500, y=380)
            practical_button = tk.Button(self.background, text='UPLOAD', bg='deepskyblue4', fg='white', width=22, height=3,bd=10,font=("Arial", 10,"bold"),command=Exa.upload).place(x=300, y=550)
            practical_button1 = tk.Button(self.background, text='View', bg='deepskyblue4', fg='white', width=22, height=3, bd=10,font=("Arial", 10,"bold"),command=Exa.view).place(x=600, y=550)
            lb1 = tk.Label(self.background, text="To Upload and Download Practical Data Enter The Below Details", width=60,font=("Castellar", 15, "bold"), bg="deepskyblue4", fg="white").place(x=0, y=0)
            #chkbtn1 = tk.Checkbutton(self.background,text="Notes",font=("Arial"),bg="deepskyblue4",fg="white",onvalue=1).place(x=350,y=470)
            acadmic_entry3 = tk.Button(self.background, text='BACK', bg='deepskyblue4', fg='white',
                                       font=('helvetica', 9, 'bold'), width=12, height=2, bd=7, command=Exa.back1).place(x=990,y=5)
        @staticmethod
        def back1():
            show.destroy()



        def _resize_image(self, event):

            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)

        @staticmethod
        def chkprac():
            if p_comb1.get() == "FE" and p_comb2.get() == "Sem-I":
                p_comb4['values'] = ("Physics-I", "Chemistry-I", "Maths-Tutorial-I", "Basic Electrical and elecronics",
                                     "Engineering Mechanics", " Basic Mechanical Engineering", "Communication Skills")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            elif p_comb1.get() == "FE" and p_comb2.get() == "Sem-II":
                p_comb4['values'] = (
                "Physics-II", "Chemistry-II", "Maths-Tutorial-II", "Graphics & Design", "Basic Civil Engineering",
                "Programming for problem solving", "Professional Communication",
                "Democracy election and good governance")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            elif p_comb1.get() == "SE" and p_comb2.get() == "Sem-I":
                p_comb4['values'] = ("Data Communication", "Digital Techniques", "Computer Graphics", "Advance C")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            elif p_comb1.get() == "SE" and p_comb2.get() == "Sem-II":
                p_comb4['values'] = ("Microprocessor", "Data Structure", "Computer Networks", "C++")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            elif p_comb1.get() == "TE" and p_comb2.get() == "Sem-I":
                p_comb4['values'] = (
                "System Programming", "Database Engineering", "Design & Analysis of Alorithm", "Python Programming",
                "Java Programming")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            elif p_comb1.get() == "TE" and p_comb2.get() == "Sem-II":
                p_comb4['values'] = ("Compiler Construction", "Unix Operating System", "Artificial Intelligence",
                                     "Mobile Application Development", "Mini-project")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            elif p_comb1.get() == "BE" and p_comb2.get() == "Sem-I":
                p_comb4['values'] = ("A", "B", "C", "D")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            elif p_comb1.get() == "BE" and p_comb2.get() == "Sem-II":
                p_comb4['values'] = ("A", "B", "C", "D")
                p_comb4.current()
                p_comb4.place(x=500, y=310)
            else:
                pass

        @staticmethod
        def upload():
            files = [('All Files', '*.*'),
              ('Python Files', '*.py'),
              ('Text Document', '*.txt')]
            file = asksaveasfile(filetypes=files, defaultextension=files)

        @staticmethod
        def view():
            if p_comb1.get() == 'FE' and p_comb2.get() == 'Sem-I':
                Exa.FE_SEM1()
            elif p_comb1.get() == 'FE' and p_comb2.get() == 'Sem-II':
                Exa.FE_SEM2()
            elif p_comb1.get() == 'SE' and p_comb2.get() == 'Sem-I':
                Exa.SE_SEM1()
            elif p_comb1.get() == 'SE' and p_comb2.get() == 'Sem-II':
                Exa.SE_SEM2()
            elif p_comb1.get() == 'TE' and p_comb2.get() == 'Sem-I':
                Exa.TE_SEM1()
            elif p_comb1.get() == 'TE' and p_comb2.get() == 'Sem-II':
                Exa.TE_SEM2()
            else:
                pass

        @staticmethod
        def FE_SEM1():
            if p_comb4.get() == 'Physics-I':
                pass
            elif p_comb4.get() == 'Chemistry-I':
                pass
            elif p_comb4.get() == 'Maths-Tutorial-I':
                pass
            elif p_comb4.get() == 'Basic Electrical and elecronics':
                pass
            elif p_comb4.get() == 'Engineering Mechanics':
                pass
            elif p_comb4.get() == 'Basic Mechanical Engineering':
                pass
            elif p_comb4.get() == 'Basic Mechanical Engineering':
                pass
            elif p_comb4.get() == 'Communication Skills':
               pass
            else:
                pass

        @staticmethod
        def FE_SEM2():
            if p_comb4.get() == 'Physics-II':
                pass
            elif p_comb4.get() == 'Chemistry-II':
                pass
            elif p_comb4.get() == 'Maths-Tutorial-II':
                pass
            elif p_comb4.get() == 'Graphics & Design':
               pass
            elif p_comb4.get() == 'Basic Civil Engineering':
               pass
            elif p_comb4.get() == 'Programming for problem solving':
               pass
            elif p_comb4.get() == 'Professional Communication':
                pass
            else:
                pass

        @staticmethod
        def SE_SEM1():
            if p_comb4.get() == 'Data Communication':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_I\DC\DCOM.pdf')
            elif p_comb4.get() == 'Digital Techniques':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_I\DT\DT.pdf')
            elif p_comb4.get() == 'Computer Graphics':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_I\CG\CG.pdf')
            elif p_comb4.get() == 'Advance C':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_I\ACC\ACC.pdf')
            else:
                pass

        @staticmethod
        def SE_SEM2():
            if p_comb4.get() == 'Microprocessor':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_II\MAP\MP.pdf')
            elif p_comb4.get() == 'Data Structure':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_II\DS\DS.pdf')
            elif p_comb4.get() == 'Computer Networks':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_II\CN\CN.pdf')
            elif p_comb4.get() == 'C++':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\SE\Sem_II\CPP\C++.pdf')
            else:
                pass

        @staticmethod
        def TE_SEM1():
            if p_comb4.get() == 'System Programming':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\TE\Sem_I\SP\SP.pdf')
            elif p_comb4.get() == 'Database Engineering':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\TE\Sem_I\DBE\DBE.pdf')
            elif p_comb4.get() == 'Design & Analysis of Alorithm':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 1\win_18\win_18.pdf')
            elif p_comb4.get() == 'Python Programming':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\TE\Sem_I\PP\PP.pdf')
            elif p_comb4.get() == 'Java Programming':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\TE\Sem_I\JP\JP.pdf')
            else:
                pass

        @staticmethod
        def TE_SEM2():
            if p_comb4.get() == 'Compiler Construction':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\TE\Sem_II\CC\CC.pdf')
            elif p_comb4.get() == 'Unix Operating System':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\TE\Sem_II\OS2\UOS.pdf')
            elif p_comb4.get() == 'Artificial Intelligence':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\sum_18\sum_18.pdf')
            elif p_comb4.get() == 'Mobile Application Development':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Practical data\TE\Sem_II\MAD\MAD.pdf')
            elif p_comb4.get() == 'Mini-project':
                webbrowser.open_new(
                    r'C:\Users\HP Elite 820\PycharmProjects\Student Diary\Question paper\TE\SEM 2\win_19\win_19.pdf')
            else:
                pass
 e =Exa(show)
 e.pack(fill=BOTH, expand=YES)

#funcation of back
def back():
 Acdemic.destroy()

#function of quit

def quit():
 #Acdemic.destroy()
 pass

#main function

def Ac():
    global Acdemic
    Acdemic = tk.Toplevel()
    Acdemic.title("ACADEMIC")
    acadmic_entry=tk.Entry(Acdemic)
    Acdemic.geometry('1100x700')
    class Exa(Frame):
        def __init__(self, master, *pargs):

            Frame.__init__(self, master, *pargs)

            self.image = Image.open('C:\\Users\\HP Elite 820\\PycharmProjects\\Student Diary\\Images\\abc.gif')
            self.img_copy = self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background =tk.Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)
            theroy_button2 = tk.Button(self.background, text='THEORY', bg='deepskyblue4', fg='white', font=('helvetica', 11, 'bold'),width=20, height=8, bd=14, command=theroy).place(x=340, y=200)
            acadmic_entry1 = tk.Button(self.background, text='PRACTICAL', bg='deepskyblue4', fg='white', font=('helvetica', 11, 'bold'),width=20, bd=14, height=8, command=practical).place(x=590, y=200)
            acadmic_entry2 = tk.Button(self.background, text='EXAM', bg='deepskyblue4', fg='white', font=('helvetica', 11, 'bold'),width=20, height=8, bd=14, command=Examination).place(x=460, y=420)
            acadmic_entry3 = tk.Button(self.background, text='BACK', bg='deepskyblue4', fg='white', font=('helvetica', 9, 'bold'),width=12, height=2, bd=7, command=back).place(x=990, y=10)
            #acadmic_entry4 = tk.Button(self.background, text='QUAIT', bg='deepskyblue4', fg='white', font=('helvetica', 9, 'bold'),width=20, height=7, bd=12, command=quit).place(x=720, y=250)
            lbl = tk.Label(self.background, text="Select Your Academic Task", font=("Castellar", 15, "bold"), bg="deepskyblue4",fg="white", width=27).place(x=0, y=0)

        def _resize_image(self, event):

            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)

    e =Exa(Acdemic)
    e.pack(fill=BOTH, expand=YES)
    Acdemic.mainloop()
