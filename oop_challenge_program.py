# student report card generator
class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.__marks = marks

    def add_marks(self, sub, marks):
        self.__marks[sub] = marks

    def avg_marks(self):
        total = sum(self.__marks.values())
        avg = total / len(self.__marks)
        print(f"{self.name}'s Avg is {avg}")

    def is_pass(self):
        for sub, mark in self.__marks.items():
            if mark < 35:
                print(f"{self.name} failed in {sub}")
                return False
        print(f"{self.name} passed")
        return True
    
    
s1 = Student("11", 'Ajay', {"hindi":35})
s1.add_marks("english", 30)
s1.avg_marks()
print("Result: ", s1.is_pass())

print()

s2 = Student("12", 'Ram', {"hindi": 90})
s2.add_marks("kannada", 92)
s2.avg_marks()
print("Result: ", s2.is_pass())

