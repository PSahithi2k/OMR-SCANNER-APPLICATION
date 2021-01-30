from tkinter import *
from tkinter import filedialog
from controllers.OMR import OMR
from controllers.DetailsImageController import DetailsImageController

class DetailsImageView:

    def load(self):
        self.window = Tk()
        self.window.title('Input Details')

        subject_lable = Label(self.window, text="Name of the subject")
        subject_lable.grid(row=0, column=0, columns=2, sticky='nesw')

        subject_entry = Entry(self.window, width=20)
        subject_entry.grid(row=0, column=2)

        class_lable = Label(self.window, text="Name of the class")
        class_lable.grid(row=1, column=0, columns=2, sticky='nesw')

        class_entry = Entry(self.window, width=20)
        class_entry.grid(row=1, column=2)

        typeOfExam_lable = Label(self.window, text="Type Of Exam")
        typeOfExam_lable.grid(row=2, column=0, columns=2, sticky='nesw')

        typeOfExam_entry = Entry(self.window, width=20)
        typeOfExam_entry.grid(row=2, column=2)

        student_lable = Label(self.window, text="Name of the student")
        student_lable.grid(row=3, column=0, columns=2, sticky='nesw')

        student_entry = Entry(self.window, width=20)
        student_entry.grid(row=3, column=2)


        button = Button(self.window, text='browse image', width=30, command= lambda: self.mfileopen(subject_entry.get(), class_entry.get(), typeOfExam_entry.get(), student_entry.get()))
        button.grid(row=4, column=2, sticky='nesw', pady = 10)
        self.window.mainloop()

    def mfileopen(self, subjectName, className, typeOfExam, studentName):
        omr = OMR()
        file1 = filedialog.askopenfile(initialdir='/', title='select a file', filetype=(("jpeg", "*.png"),("All Files", "*.*")))
        path = file1.name

        dic = DetailsImageController()
        ANSWER_KEY = dic.getKey(subjectName, className, typeOfExam)

        
        score = omr.evaluate(path, ANSWER_KEY)

        result = dic.studentDetails(subjectName, className, typeOfExam, studentName, score)

        label = Label(self.window, text=result)
        label.grid(row=4, column=0, pady=10)

        label = Label(self.window, text=score)
        label.grid(row=5, column=0, pady=10)

if __name__ =='__main__':
    div = DetailsImageView()
    div.load()