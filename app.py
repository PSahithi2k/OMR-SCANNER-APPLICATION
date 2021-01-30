from views.AuthView import AuthView 
# from views.DetectionView import DetectionView
from controllers.OMR import OMR
from views.AnswersView import AnswersView
from views.DetailsImageView import DetailsImageView

class MyApp:
    
    def run(self):
        av = AuthView()
        av.transfer_control = self.start_key_sheet
        av.load()
        

    # def detection(self):
    #     dv = DetectionView()
    #     dv.load()

    def start_key_sheet(self):
        ansv = AnswersView()
        ansv.transfer_Control = self.upload_image
        ansv.load()

    def upload_image(self):
        dmv = DetailsImageView()
        dmv.load()



    def start_evaluating(self):
        omr = OMR()
        omr.evaluate('test_01.png')



ma = MyApp()
ma.run()
    