class Task:
    def __init__(self, number):
        self.number = number
    def form(self):
    def check(self):
    def approval(task: int) -> bool:
        if task == 1:
            return True
        else:
            return False
class Student(Task):
    def __init__(self, name):
        self.name = name
    def form(self):
        super().form()

    # def task_solve(self, number):
    #     super().task_solve(number)
    #     return Task.number
class Teacher(Task):
    def __init__(self, name):
        super().__init__(name)
    def form(self):
        super().form()
    def check(self):
        super().check()





# t1 = Task('oop')
# print(t1.name, t1.approval())
# st1 = Student('Ivan')
# print(st1.name)
# st2 = Student('Oksana')
# print(st2.name)
# tc1 = Teacher('Vladislav')
# tc1.task_give('1')
# print(tc1.task_give('1'))
