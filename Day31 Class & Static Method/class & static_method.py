'''
# class method:------>>
it is used to perform operations on class level data.
first parameter of class method is cls ---> class
apply ---> decorator ---> @classmethod
class ---> class name
syntax :

        class Cls_name:
            ca = value1
            def __init__(self):
                self.ia = vallue2

            @classmethod
            def m12(cls):
                ans = ca**2
                return ans
'''
 
class Student:
    #class attributes
    course = "Python"
    trainer = "vaibhav patil"
    fees = 40000
    def __init__(self,rll,nm,ag):
        #instance attributes
        self.roll = rll
        self.name = nm
        self.age =ag
        self.marks = {}
 
    # instance method 1 - student chi details print karayla
    def show_details(self):
        details = f'''
        Roll   : {self.roll}
        Name   : {self.name}
        Age    : {self.age}
        Course : {Student.course}
        Trainer: {Student.trainer}
        '''
        print(details)
 
    # instance method 2 - navin marks add karayla (dictionary madhe store karte)
    def add_marks(self,testname,mk):
        self.marks[testname] = mk
        return "done"
 
    # instance method 3 - total marks var percentage calculate karayla
    def cal_percentage(self):
        obt = 0
        for mk in self.marks.values():
            obt = obt+mk
        total = 100*len(self.marks)
        per = obt/total *100
        return per
 
    # instance method 4 - percentage cha base var pass/fail decide karayla
    def show_result(self):
        per = self.cal_percentage()
        if per>40:
            return "Pass"
        else:
            return "Fail"
 
    # class method 1 - discount apply karun fees calculate karayla
    @classmethod
    def apply_discount(cls,dis):
        dp = cls.fees*dis/100
        sp = cls.fees - dp
        return sp
 
    # class method 2 - trainer change karayla
    @classmethod
    def change_trainer(cls,trainer):
        cls.trainer = trainer
        return "done"
 
    # static method 1 - passing marks display karayla
    @staticmethod
    def passing_marks():
        print("Passing Marks 40")
 
    # static method 2 - percentage calculate karayla (class/instance data shivay)
    @staticmethod
    def percentage(obt,total):
        per = obt/total *100
        return per
 
 
s1=Student(1,"kunal",23)
print(s1.apply_discount(15))
print(Student.apply_discount(10))
print(s1.change_trainer("pavan"))
print(Student.trainer)
 
# static method calls
Student.passing_marks()
s1.passing_marks()
print(Student.percentage(80,100))
print(s1.percentage(45,50))
'''
# static method:----->>
static method is a method that belongs to a class but does not use instance (self) or class (cls)
it is defined using @staticmethod decorator. 
does not take self or cls as a parameter. we can call class method by using class name or object method. it is used for utility or helper function related to the class.
'''
#-----------------------------------------------------------------------------------------------------