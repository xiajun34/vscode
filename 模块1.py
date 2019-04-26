class Person(object):
    address="earth"
    def __init__(self,name,gender,birth,addr):
        self.name=name
        self.gender=gender
        self.birth=birth
        self.addr=addr
class Teacher(object):
     def __init__(self,score):
         self.score=score
        
class tom(Teacher,Person):
    def __init__(self,gender,birth,score,addr):
        super(tom,self).__init__(gender,birth,addr,score)
s=tom("xxx",'man','1998','china',67)        

print(s.addr)

       
