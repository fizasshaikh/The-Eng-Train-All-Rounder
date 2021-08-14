#!/usr/bin/env python

import tkinter as tk
import json
import random
import tkinter.messagebox
import pkg_resources
import os

QUESTIONS_FILE = pkg_resources.resource_filename('py_quiz','questions.json')
QUESTIONS_FILE1 = pkg_resources.resource_filename('py_quiz','Amazonquestion.json')

def TCS(args=None):
    top = tk.Toplevel()
    top.title("Quiz")

    top.geometry('1100x700')

    class Application(tk.Frame):

        def __init__(self,master,*pargs):
            '''Call to the constructor when the object is created.Variables initialized and set the grid as per need.'''

            tkinter.messagebox.showinfo('Welcome!','Welcome to PyQuiz!\nA quiz built in Python to test your general knowledge.')
            tk.Frame.__init__(self,master,*pargs)
            # declaring variables to store question and answer
            tk.Frame.configure(self,bg="turquoise4")
            self.optionA = tk.StringVar() # control variable for# option A
            self.optionB = tk.StringVar() # control variable for option B
            self.optionC = tk.StringVar() # control variable for option C
            self.optionD = tk.StringVar() # control variable for option D
            self.selected_answer = tk.StringVar() # variable to get the selected answer
            self.correct_answer = "" # to store the correct answer before randomizing options
            self.question = tk.StringVar() # control variable for the question to be loaded
            self.file = open(QUESTIONS_FILE,"r")
            self.questions = json.loads(self.file.read())
            self.question_index = []
            self.score = tk.IntVar() # to hold the score
            #top = self.winfo_toplevel()
            self.createWidgets(top) # call to create the necessary widgets
            self.load_question(top) # load the first question



        def confirm_quit(self):
            '''Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.'''

            choice = tkinter.messagebox.askyesno('Quit Application','Are you sure you wish to stop playing PyQuiz! ?')
            if choice == True:
                self.quit()
            elif choice == False:
                pass

        def set_ans(self,answer):
            '''Function to set the 'selected_answer' variable to the selected option label to compare with correct answer later.Args: answer - gets the option number which calls this function.'''

            if answer==1:
                self.selected_answer = self.optionA.get()
            elif answer==2:
                self.selected_answer = self.optionB.get()
            elif answer == 3:
                self.selected_answer = self.optionC.get()
            elif answer == 4:
                self.selected_answer = self.optionD.get()

        def validate_ans(self):
            '''Function to validate the selected answer with the correct answer. If they match, increase the score by 5.'''

            print("In Validate answer:")
            print ("selected:",self.selected_answer)
            print ("Correct:",self.correct_answer)
            self.py_var = ["PY_VAR1","PY_VAR2","PY_VAR3","PY_VAR4"]
            if str(self.selected_answer) == str(self.correct_answer):
                self.score.set(int(self.score.get()) + 5)
                print("Correct!")
            elif str(self.selected_answer) in self.py_var :
                print("IN py var if")
                pass
            else:
                self.score.set(int(self.score.get()) - 5)
                print("Incorrect!")
	   
	

        def load_question(self,top):
            '''Function to load a new question set with options. The question is randomly picked from the JSON file for questions.The options to that questions are also randomized and loaded.'''

            self.validate_ans() # call to check the answer before loading the next question
            randomindex = random.randint(0,len(self.questions["results"])-1) # generate random index to be picked from list
            if randomindex not in self.question_index: # only proceed if the question has not already been picked up.
                self.question_index.append(randomindex) # keep a track of the question indices.
                pass
            else:
                randomindex = random.randint(0,len(self.questions["results"])-1)
                self.question_index.append(randomindex)
                print ("Debug:")
                print (self.questions["results"][randomindex]["question"] )
            self.correct_answer = self.questions["results"][randomindex]["correct_answer"] # parse the correct answer from JSON file and store it.
            #print self.correct_answer
            self.answers = self.questions["results"][randomindex]["incorrect_answers"] # parse the other incorrect answers
            self.answers.append(self.correct_answer) # add all the answers to the list.
            self.question.set(self.questions["results"][randomindex]["question"]) # set the question label
            length=len(self.question.get())  # get the length of the question
            width=str(100+10*length)
            #top.geometry(width+"x180")	# change the width of the window according to the length of the question
            self.optionA.set(self.answers.pop(random.randrange(len(self.answers)))) # randomly set the option label from the answers list and then remove from that list to avoid repetition
            self.optionB.set(self.answers.pop(random.randrange(len(self.answers))))
            self.optionC.set(self.answers.pop(random.randrange(len(self.answers))))
            self.optionD.set(self.answers.pop(random.randrange(len(self.answers))))
            self.radioButtonA.deselect()
            self.radioButtonB.deselect()
            self.radioButtonC.deselect()
            self.radioButtonD.deselect()
        def createWidgets(self,top):
            '''Function that creates all the necessary Tkinter widgets. All the widgets are specified here while creation.'''


            self.optionA.set('Hello A!')
            self.optionB.set('Hello B!')
            self.optionC.set('Hello C!')
            self.optionD.set('Hello D!')
            self.question.set('Demo Question')
            #Creating the buttons

            self.quitButton = tk.Button(self, text='Quit', command=self.confirm_quit,font=('Castellar',10,'bold'),bd=10,width=20,height=2)
            self.nextButton = tk.Button(self, text='Next', command=lambda: self.load_question(top),font=('Castellar',10,'bold'),bd=10,width=20,height=2)

        #Creating Radio buttons for options

            self.radioButtonA = tk.Radiobutton(self,anchor='w',
                            textvariable=self.optionA, 
                            variable = self.selected_answer, 
                            value = 'A',
                            command = lambda: self.set_ans(1),font=('Castellar',10,'bold')) # the radio button call 'set_ans()' with the number to set the 'selected_answer' variable
            self.radioButtonB = tk.Radiobutton(self,anchor='w',
                            textvariable=self.optionB, 
                            variable = self.selected_answer,
                            value = 'B', 
                            command = lambda: self.set_ans(2),font=('Castellar',10,'bold'))
            self.radioButtonC = tk.Radiobutton(self,anchor='w',
                            textvariable=self.optionC, 
                            variable = self.selected_answer, 
                            value = 'C', 
                            command = lambda: self.set_ans(3),font=('Castellar',10,'bold'))
            self.radioButtonD = tk.Radiobutton(self,anchor='w',
                            textvariable=self.optionD,
                            variable = self.selected_answer,
                            value = 'D', 
                            command = lambda: self.set_ans(4),font=('Castellar',10,'bold'))

            
            #Creating the labels for options and questions
            
            self.label_question = tk.Label(self,font=('Castellar',10,'bold'),width=99,height=6,textvariable=self.question,wraplength=700)
            #print(type(self.question))
            #self.label_question.insert(tk.END,self.question)
            #self.label_question.config(state='disabled')
            self.label_score = tk.Label(self,text='Score:',font=('Castellar',10,'bold'),width=7,height=1)
            self.label_score_value = tk.Label(self,textvariable=self.score,anchor='e',font=('Castellar',10,'bold'),width=2)

            #Packing the widgets in the grid

            self.label_question.place(x=3,y= 100)
            self.label_score.place(x=990,y= 5)
            self.label_score_value.place(x=1010,y =30)
            self.radioButtonA.place(x=250,y = 250)
            self.radioButtonB.place(x=580,y = 250)
            self.radioButtonC.place(x=250,y= 330)
            self.radioButtonD.place(x=580,y=330)
            
            self.quitButton.place(x=250 ,y=450)
            self.nextButton.place(x=550,y=450)

    e = Application(top)
    e.pack(fill=tk.BOTH, expand=tk.YES)
    top.mainloop()


print(__name__)


def mainAmazon(args=None):
    top = tk.Toplevel()
    top.title("Quiz")

    top.geometry('1100x700')

    class Application(tk.Frame):

        def __init__(self, master, *pargs):
            '''Call to the constructor when the object is created.Variables initialized and set the grid as per need.'''

            tkinter.messagebox.showinfo('Welcome!',
                                        'Welcome to PyQuiz!\nA quiz built in Python to test your general knowledge.')
            tk.Frame.__init__(self, master, *pargs)
            # declaring variables to store question and answer
            tk.Frame.configure(self, bg="turquoise4")
            self.optionA = tk.StringVar()  # control variable for# option A
            self.optionB = tk.StringVar()  # control variable for option B
            self.optionC = tk.StringVar()  # control variable for option C
            self.optionD = tk.StringVar()  # control variable for option D
            self.selected_answer = tk.StringVar()  # variable to get the selected answer
            self.correct_answer = ""  # to store the correct answer before randomizing options
            self.question = tk.StringVar()  # control variable for the question to be loaded
            self.file = open(QUESTIONS_FILE1, "r")
            self.questions = json.loads(self.file.read())
            self.question_index = []
            self.score = tk.IntVar()  # to hold the score
            # top = self.winfo_toplevel()
            self.createWidgets(top)  # call to create the necessary widgets
            self.load_question(top)  # load the first question

        def confirm_quit(self):
            '''Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.'''

            choice = tkinter.messagebox.askyesno('Quit Application', 'Are you sure you wish to stop playing PyQuiz! ?')
            if choice == True:
                self.quit()
            elif choice == False:
                pass

        def set_ans(self, answer):
            '''Function to set the 'selected_answer' variable to the selected option label to compare with correct answer later.Args: answer - gets the option number which calls this function.'''

            if answer == 1:
                self.selected_answer = self.optionA.get()
            elif answer == 2:
                self.selected_answer = self.optionB.get()
            elif answer == 3:
                self.selected_answer = self.optionC.get()
            elif answer == 4:
                self.selected_answer = self.optionD.get()

        def validate_ans(self):
            '''Function to validate the selected answer with the correct answer. If they match, increase the score by 5.'''

            print("In Validate answer:")
            print("selected:", self.selected_answer)
            print("Correct:", self.correct_answer)
            self.py_var = ["PY_VAR1", "PY_VAR2", "PY_VAR3", "PY_VAR4"]
            if str(self.selected_answer) == str(self.correct_answer):
                self.score.set(int(self.score.get()) + 5)
                print("Correct!")
            elif str(self.selected_answer) in self.py_var:
                print("IN py var if")
                pass
            else:
                self.score.set(int(self.score.get()) - 5)
                print("Incorrect!")

        def load_question(self, top):
            '''Function to load a new question set with options. The question is randomly picked from the JSON file for questions.The options to that questions are also randomized and loaded.'''

            self.validate_ans()  # call to check the answer before loading the next question
            randomindex = random.randint(0, len(
                self.questions["results"]) - 1)  # generate random index to be picked from list
            if randomindex not in self.question_index:  # only proceed if the question has not already been picked up.
                self.question_index.append(randomindex)  # keep a track of the question indices.
                pass
            else:
                randomindex = random.randint(0, len(self.questions["results"]) - 1)
                self.question_index.append(randomindex)
                print("Debug:")
                print(self.questions["results"][randomindex]["question"])
            self.correct_answer = self.questions["results"][randomindex][
                "correct_answer"]  # parse the correct answer from JSON file and store it.
            # print self.correct_answer
            self.answers = self.questions["results"][randomindex][
                "incorrect_answers"]  # parse the other incorrect answers
            self.answers.append(self.correct_answer)  # add all the answers to the list.
            self.question.set(self.questions["results"][randomindex]["question"])  # set the question label
            length = len(self.question.get())  # get the length of the question
            width = str(100 + 10 * length)
            # top.geometry(width+"x180")	# change the width of the window according to the length of the question
            self.optionA.set(self.answers.pop(random.randrange(len(
                self.answers))))  # randomly set the option label from the answers list and then remove from that list to avoid repetition
            self.optionB.set(self.answers.pop(random.randrange(len(self.answers))))
            self.optionC.set(self.answers.pop(random.randrange(len(self.answers))))
            self.optionD.set(self.answers.pop(random.randrange(len(self.answers))))
            self.radioButtonA.deselect()
            self.radioButtonB.deselect()
            self.radioButtonC.deselect()
            self.radioButtonD.deselect()

        def createWidgets(self, top):
            '''Function that creates all the necessary Tkinter widgets. All the widgets are specified here while creation.'''

            self.optionA.set('Hello A!')
            self.optionB.set('Hello B!')
            self.optionC.set('Hello C!')
            self.optionD.set('Hello D!')
            self.question.set('Demo Question')
            # Creating the buttons

            self.quitButton = tk.Button(self, text='Quit', command=self.confirm_quit, font=('Castellar', 10, 'bold'),
                                        bd=10, width=20, height=2)
            self.nextButton = tk.Button(self, text='Next', command=lambda: self.load_question(top),
                                        font=('Castellar', 10, 'bold'), bd=10, width=20, height=2)

            # Creating Radio buttons for options

            self.radioButtonA = tk.Radiobutton(self, anchor='w',
                                               textvariable=self.optionA,
                                               variable=self.selected_answer,
                                               value='A',
                                               command=lambda: self.set_ans(1), font=('Castellar', 10,
                                                                                      'bold'))  # the radio button call 'set_ans()' with the number to set the 'selected_answer' variable
            self.radioButtonB = tk.Radiobutton(self, anchor='w',
                                               textvariable=self.optionB,
                                               variable=self.selected_answer,
                                               value='B',
                                               command=lambda: self.set_ans(2), font=('Castellar', 10, 'bold'))
            self.radioButtonC = tk.Radiobutton(self, anchor='w',
                                               textvariable=self.optionC,
                                               variable=self.selected_answer,
                                               value='C',
                                               command=lambda: self.set_ans(3), font=('Castellar', 10, 'bold'))
            self.radioButtonD = tk.Radiobutton(self, anchor='w',
                                               textvariable=self.optionD,
                                               variable=self.selected_answer,
                                               value='D',
                                               command=lambda: self.set_ans(4), font=('Castellar', 10, 'bold'))

            # Creating the labels for options and questions

            self.label_question = tk.Label(self, font=('Castellar', 10, 'bold'), width=99, height=8,
                                           textvariable=self.question, wraplength=700)
            # print(type(self.question))
            # self.label_question.insert(tk.END,self.question)
            # self.label_question.config(state='disabled')
            self.label_score = tk.Label(self, text='Score:', font=('Castellar', 10, 'bold'),width=7,height=1)
            self.label_score_value = tk.Label(self, textvariable=self.score, anchor='e', font=('Castellar', 10, 'bold'),
                                             width=2 )

            # Packing the widgets in the grid

            self.label_question.place(x=3, y=100)
            self.label_score.place(x=990, y=5)
            self.label_score_value.place(x=10, y=30)
            self.radioButtonA.place(x=250, y=250)
            self.radioButtonB.place(x=580, y=250)
            self.radioButtonC.place(x=250, y=330)
            self.radioButtonD.place(x=580, y=330)

            self.quitButton.place(x=250, y=450)
            self.nextButton.place(x=550, y=450)

    e = Application(top)
    e.pack(fill=tk.BOTH, expand=tk.YES)
    top.mainloop()


print(__name__)