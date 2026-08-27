class Fail(Exception):
    def __init__(self, message):
        super().__init__(message)


class Student:
    def __init__(self, rollNo, name, marks):
        self.rollNo = rollNo
        self.name = name
        self.marks = marks

    def displayDetails(self):
        print('{} \t {} \t {}'.format(self.name, self.rollNo, self.marks))
        try:
            if self.marks < 40:
                raise Fail('Student {} has Scored {} marks and has Failed  '.format(
                    self.name, self.marks))

        except Fail as f:
            print(f)


myStudentList = []

num = int(input('Enter the number of Students : '))
for i in range(num):
    rollNo, name, marks = input(
        'Enter Roll-no,Name,Marks of Student {} : '.format(i+1)).split(',')
    print('----------------------------------------')
    marks = int(marks)
    myStudentList.append(Student(rollNo, name, marks))

print('DETAILS OF STUDENTS ARE : ')

for i in range(num):
    myStudentList[i].displayDetails()
