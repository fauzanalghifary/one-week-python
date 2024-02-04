class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"Student {self.name} has an average grade of {self.average_grade()}"

    def __repr__(self):
        return f"<Student {self.name}, grades: {self.grades}>"

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


john = Student("John", [90, 95, 88, 100, 78])
print(john)
