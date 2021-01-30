from models.AnswersModel import AnswersModel


class AnswersController:


    def validateAnswerKey(self, subject, typeOfExam, className, answers):
        
        if(len(subject) == 0 or typeOfExam==0 or className==0 or answers==0):
            return "non of the areas should be empty"

        ansm = AnswersModel()
        result = ansm.createAnswer(subject, typeOfExam, className, answers)

        if result:
            message = "success"
            return message
        else:
            message = 'unsuccessful'
            return message
