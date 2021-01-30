from lib.db import *


class AnswersModel:
    def __init__(self):
        self.conn = connect('app.db')

    def createAnswer(self, subject, typeOfExam, className, answerskey):
        query = f"INSERT INTO keysheet (subject, typeOfExam, answerskey, className) VALUES ('{subject}','{typeOfExam}','{answerskey}', '{className}')"

        try:
            insert(self.conn,query)
            print("done")
            return 1
        except:
            print("Some database error")
            return 0