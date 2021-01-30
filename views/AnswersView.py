from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.AnswersController import AnswersController
from views.DetailsImageView import DetailsImageView

class AnswersView:

        def load(self):
            self.window = Tk()
            self.window.title('Ket sheet Preparation')
            
            subject_lable = Label(self.window, text="Name of the subject")
            subject_lable.grid(row=0, column=0, columns=2, sticky='nesw')

            subject_entry = Entry(self.window, width=20)
            subject_entry.grid(row=0, column=2)

            type_lable = Label(self.window, text="Typer of exam")
            type_lable.grid(row=1, column=0, columns=2, sticky='nesw')

            type_entry = Entry(self.window, width=20)
            type_entry.grid(row=1, column=2)

            class_lable = Label(self.window, text="For which class")
            class_lable.grid(row=2, column=0, columns=2, sticky='nesw')

            class_entry = Entry(self.window, width=20)
            class_entry.grid(row=2, column=2)

            answers_lable = Label(self.window, text="Enter answers to all the questions separated with commas")
            answers_lable.grid(row=3, column=0, columns=2, sticky='nesw')

            instructions_lable = Label(self.window, text="Options start from 0 ends 4 eg:0,3,2,1,4")
            instructions_lable.grid(row=4, column=0, columns=2, sticky='nesw')

            answer_entry = Entry(self.window, width=20)
            answer_entry.grid(row=5, column=2)

            b1 = Button(self.window, text='Next', command= lambda: self.upload_page(subject_entry.get(), type_entry.get(), class_entry.get(), answer_entry.get()), pady = 15)
            b1.grid(row=6, column=2, sticky='nesw', pady = 10)

            self.window.mainloop()

        def upload_page(self, subject, typeOfExam, className, answers):
            ansc = AnswersController()
            message = ansc.validateAnswerKey(subject, typeOfExam, className, answers)
            if(message == 'success'):
                self.window.destroy()
                dmv = DetailsImageView()
                dmv.load()
            else:
                messagebox.showinfo('Information', message)

            

if __name__ == '__main__':
    qv=AnswersView()
    qv.load()