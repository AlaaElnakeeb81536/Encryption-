'''if i told you that Aya was absent because she was broken during her sport training .she was granted permission to attend this exam 
another day simulate this scenairo by using oop'''

class student:
    def __init__(self,name,sport_training,exam):
        self.sport_training=sport_training
        self.exam=exam
    def is_absent(self):
        if self.sport_training=='broken':
            return True
        else:
            return False
    def permission(self):
        
        if self.is_absent():
            self.exam='another day'
            return True
        else:
            return False
Aya=student('aya','broken','today')
Aya.permission()