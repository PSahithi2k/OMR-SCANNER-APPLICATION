from models.DetailsImageModel import DetailsImageModel

class DetailsImageController:

    def getKey(self, subjectName, className, typeOfExam):
        dim = DetailsImageModel()
        key = dim.selectKey(subjectName, className, typeOfExam)

        key = key[0].split(',')
        d = {}
        for i in range(0, len(key)):
            d[i] = int(key[i])
        print(d)
        return d

    def studentDetails(self, subjectName, className, typeOfExam, studentName, score):
        dim = DetailsImageModel()
        result = dim.studentScore(studentName, subjectName, className, typeOfExam, score)
        if result==1:
                return "added record to database"
            
        else:
            return "User could not add record to database"
