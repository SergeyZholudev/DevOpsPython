# Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде
# списка объектов `Student` также реализованного в виде соответствующего класса.
# В классах реализовать необходимый набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
# `grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.


class Group:
    def __init__(self, name):
        self.name = name
        self.gr_list = []

    def add(self, other):
        self.gr_list.append(other)

    def remove(self, other):
        self.gr_list.remove(other)

    def print_list(self):
        print(f'{self.name} ({len(self.gr_list)} members)')
        for item in self.gr_list:
            print(f'{item.name} : {item.age} : grades = {item.grades}')


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades


# creation of students
std_1 = Student('Alex', 25, [5, 2, 4, 5])
std_2 = Student('John', 23, [4, 1, 5, 4, 3])
std_3 = Student('Mike', 26, [3, 3, 4, 3, 5])
std_4 = Student('Jane', 22, 4)
std_5 = Student('Jeremy', 40, 5)
std_6 = Student('Alice', 32, [5, 3, 4, 5, 2, 1])
std_7 = Student('Alice', 28, [5, 5, 5, 5, 2, 4])
std_8 = Student('Egor', 28, [5, 5, 5, 5, 2, 4])

# add students to the group & print
group_1 = Group('Physicists')
group_1.add(std_1)
group_1.add(std_2)
group_1.add(std_3)
group_1.add(std_8)
print('+' * 50)
group_1.print_list()

group_2 = Group('Chemists')
group_2.add(std_4)
group_2.add(std_5)
group_2.add(std_6)
group_2.add(std_7)
print('+' * 50)
group_2.print_list()
print('+' * 50)

# remove student from the groups & print
group_1.remove(std_1)
group_1.print_list()
print('+' * 50)
group_2.remove(std_4)
group_2.remove(std_7)
group_2.print_list()
