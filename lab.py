
mus_ID = 1
orc_ID = 1


class Orchestra:
    def __init__(self, name):
        global orc_ID
        self.name = name
        self.orc_ID = orc_ID

        orc_ID += 1

class Musician:
    def __init__(self, name, salary, orc_ID):
        global mus_ID
        self.name = name
        self.salary = salary
        self.mus_ID = mus_ID
        self.orc_ID = orc_ID
        mus_ID += 1


class Mus_In_Orc:
    def __init__(self, mus_ID, orc_ID):
        self.mus_ID = mus_ID
        self.orc_ID = orc_ID

mus = []
orc = []
m_o = []


with open("musician.txt", "r", encoding='utf8') as file:
    for line in file:
        data = line.split()
        mus1 = Musician(data[0], int(data[1]), int(data[2]))
        mus.append(mus1)


with open("Orchestra.txt", "r", encoding='utf8') as file:
    for line in file:
        data = line.split()
        orc1 = Orchestra(data[0])
        orc.append(orc1)


for i in orc:
    for j in mus:
        if i.orc_ID == j.orc_ID:
            m_o1 = Mus_In_Orc(j.mus_ID, i.orc_ID)
            m_o.append(m_o1)





#Задание 1
print("Задание 1")
for i in orc:
    if i.name[0] == 'A':
        print(i.name)
        print("Сотрудники:")
        for j in mus:
            if i.orc_ID == j.orc_ID:
                print(j.name)


def task1(orc, mus):
    ans = []
    for i in orc:
        if i.name[0] == 'A':
            print(i.name)
            print("Сотрудники:")
            for j in mus:
                if i.orc_ID == j.orc_ID:
                    ans.append(j.name)
    return ans



print('\n', '\n')
print("Задание 2")
#Задание 2

sp = []
for i in orc:
    max_sal = 0
    for j in mus:
        if j.orc_ID == i.orc_ID and j.salary > max_sal:
            max_sal = j.salary

    sp.append([i.name, max_sal])

sp.sort(key=lambda arr: arr[1])
sp = sp
for i in sp:
    print(i[0], "максимальная зарплата:", i[1])

print("Отсортировано по возрастанию")


def task2(orc, mus):
    ans = []
    sp = []
    for i in orc:
        max_sal = 0
        for j in mus:
            if j.orc_ID == i.orc_ID and j.salary > max_sal:
                max_sal = j.salary

        sp.append([i.name, max_sal])

    sp.sort(key=lambda arr: arr[1])
    sp = sp
    for i in sp:
        ans.append([i[0], "максимальная зарплата:", i[1]])

    return ans




#Задание 3
print('\n', '\n')
print("Задание 3")

for i in orc:
    print("Сотрудники, работающие в оркестре", i.name, ':')
    for j in mus:
        if j.orc_ID == i.orc_ID:
            print(j.name)
    print('')


def task3(orc, mus):
    ans = []
    for i in orc:
        elem = []
        for j in mus:
            if j.orc_ID == i.orc_ID:
                elem.append(j.name)
        if len(elem) != 0:
            ans.append(elem)
    return ans
