'''
Method --->function ---->operations on data
3 types:
1.instance method
2.class method
3.static method
'''
# 1.instance method: it is used to perform operation on instant attributes>
class Student:
    #class attributes
    course = "Python"
    trainer = "vaibhav patil"
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

