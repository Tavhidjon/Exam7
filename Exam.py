### 1 Question
# What is OOP and why is it important? Write about main principles of OOP.
# Чиро ООП мегуянд ва барои чӣ он лозим аст? Дар бораи принсипҳои асосии он нависед.

# OOP in yak paradigmai barnomasozi meboshad,yane yak rohi barnomasozi mebosad,
# principhoi OOP:
# in yane:
# 1)Abstraction-->ba vositai in mo teavonem ya classi xomush sozem va metodhoyashro inherit kunem
# 2)incapsulation--> in yane zashitai veriablo mo metavonem 1(private-shaxsi),2(protected-zashishoniy),3(Obshiy)
# 3)inheritence-->nasledstvie yane meros classi dochernoy az classi mother metodhoyashro inherit mekunad
# 4)Polimorfism-->pole -(gunogun,morfe-shakl,yane gunogun shakl)


### 2 Question
# What are getter and setter and how to use them? Write about properties in python.
# Getter ва setter чист ва чӣ тавр онҳоро истифода мебарем? Дар бораи хусусиятҳо(properties) дар python нависед.
# inho dar class istifoda meshavand asosan vazifai onho giriftani malumot ba vosiati 'getter' va ivaz kardani malumot ba vositai 'setter', 
# 'property' in yak metode meboshad ki bo yorii on mo metavonem ba atributhoyamon dastrasi paydo kunem in vazifai 'geter va seter'-ro ijro mekunad.
# in yak metodirohi behtari kor ki yane mo vaqqte bo getter va setter kor kunem dar vaqti object sozi qavshoyashro memonem vale dar metodi (property(@property))
# faqat barobari hamon qimmate ki mexohem monem.



### 3 Question
# Types of variables and methods in a class.
# Кадом намуди атрибутҳо ва методҳо дар клас мавҷуданд. 


# @classmethod
# @isinstance
# @staticmethod
# @isinstance


### 4 Question
# Write about constructor and destructor.
# Дар бораи конструктор ва деструктор нависед.

# constructor in yak metode meboshad ki bo yorii on mo object baroi class mesozem example(__init__,__new__)
# destructor in yak metode meboshad ki bo yorii on mo metavonem ki metodhoi daruni calss ro udalit kunem yo ki nest kunem, 
# asosan python xudash onro dorad ba mo lozim ast example(__del__)




### 5 Question
# Difference between global, local and nonlocal variables.
# Фарқият байни тағйирёбандаҳои global, local and nonlocal.
# global variable in yak namudi variable mevoshad ki obshedostupniy hast yane dastrasi hama 
# nonlocal variables in yak veriable meboshad ki agar mo du def  doshta boshem vaagar cxohem veriabli function asosiro girem aval onro
#  nonloacl mekunem va bad istifoda mebarem


# ### 1 
# Create a program that asks the user for a range of numbers (x, y) and displays the multiplication tables from x to y.
# Барномае созед ки аз консол 2 рақамро қабул мекунад. Барои ҳар як адади дар ин давр вуҷуддошта ҷадвали зарбашро нишон диҳад.
# ### EXAMPLE
# # INPUT
#     From = 2
#     To = 3
# # OUTPUT
#     2x1= 2
#     2x2= 4
#     2x3= 6
#     2x4= 8
#     2x5= 10
#     2x6= 12
#     2x7= 14
#     2x8= 16
#     2x9= 18
#     2x10= 20
    
#     3x1= 3
#     3x2= 6
#     3x3= 9
#     3x4= 12
#     3x5= 15
#     3x6= 18
#     3x7= 21
#     3x8= 24
#     3x9= 27
#     3x10= 30




# a=int(input('From= '))
# b=int(input('To= '))

# for i in range(1,10):
#     print(f'{a}*{i}={a*i}')
# print()
# for i in range(1,10):
#     print(f'{b}*{i}={b*i}')




### 2
# Create a class of Circle with instance variable like radius and class variable like PI(3.14). Then create a constructor which initializes the radius(radius comes as a parameter of constructor).
# Your class should have the following methods:
# Як класи Circle ки аз як тағйирёбандаи ба клас таалуқдошта PI = 3.14 ва як тағйирёбандаи ба обект тааллуқдошта radius ки қиммати он аз конструктор гузошта мешавад созед. Класи Шумо аз методҳои зерин бояд иборат бошад:

# 1. get_area();               // area = 2 * PI * R * R
# 2. get_diametr();           // diameter = 2 * R
# 3. get_circumference();      //  circumference  = 2 * PI * R
# 4. get_radius();             // radius  = R



# class Circle:
#     PI=3.14
#     def __init__(self,area,diameter,ircumference,radius):
#         self.area=area
#         self.diameter=diameter
#         self.ircumference=ircumference
#         self.radius=radius

#     def get_area(self):
#         print (f'{2*self.PI*self.radius*self.radius}')
    
#     def get_diametr(self):
#         print (f'{2*self.radius}')
    
#     def get_circumference(self):
#         print (f'{2*self.PI*self.radius}')
    
#     def get_radius(self):
#         print (f"{self.radius}")
    

# obj1=Circle(20,5,7,6)
# obj1.get_area()
# obj1.get_diametr()
# obj1.get_circumference()
# obj1.get_radius()
    



### 3
# Create a Calculator class with this static methods:
# Класи Калкуляторро бо методҳои статикии зерин созед:
# 1. factorial(n)
# 2. power(a, b)
# 3. sqrt(n)


# class Calculator:
#     def __init__(self,n,a,b):
#         self.n=n
#         self.a=a
#         self.b=b
    
#     def factorial(self):
#         cnt=1
#         for i in range(self.n):
#             cnt*=i
#         print (cnt)
#     def power(self):
#         print (self.a**self.b)
    
#     def sqrt(self):
#         print (self.n**(1/2))
    
# obj1=Calculator(4,3,4)
# obj1.factorial()
# obj1.power()
# obj1.sqrt()

    



### 4
# Write a program in Python that asks the user for two numbers and one operation (+, -, *, /) then calculate the operation and display the result on the screen.
# You should to follow this steps:
# Як класи Calculator созед ки дар конструктор атрибутҳои зеринро дорост. Рақами якум, амал(+, -, *, /) ва рақами дуюм. Калкулятори Шумо баяд 4 амали математикиро иҷро кунад.
#  Берун аз клас як даври беохир(infinite loop) созед. 
# Объекти класи Калкуляторро созед ва рақамҳо ва аломати дохил кардаатонро ба он гузоред. match case - ро барои  даъват кардани методиҳои клас вобаста ба аломати дохилкарда истифода баред.



# 1.	Create class Calculator 
# 2.	Create a constructor which initializes the first number, operation(+, -, *, /) and second number(first num, second num, operation comes as parameter of constructor).
# 3.	Create four instance methods like: 
#     Sum()
#     Subtract()
#     Multiplication()
#     Division()
# 4.	Create infinite loop outside Calculator class 
# 5.	Use the math case block for calling methods
# ### EXAMPLE
# # input 
#     The first number is: 3
#     The operation is: +
#     The second number is: 1
# # output
#     3 + 1 = 4


# ROHI YAKUM

# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
  

#     def Sum(self):
#         print(self.a+self.b)

#     def subtract(self):
#         print(self.a-self.b)
    
#     def multiply(self):
#         print(self.a*self.b)

#     def divid(self):
#         print(self.a/self.b)


#     def __str__(self):
#         return f"{self.Sum}{self.subtract}{self.multiply}{self.divid}"

# obj1=Calculator(3,4)
# obj1.multiply()
# obj1.Sum()
# obj1.subtract()
# obj1.multiply()
# obj1.divid()

# ROHI DUYUM

# while True:
#     a=int(input("The first number is: "))
#     b=int(input('The second number is: '))
#     client=input('The operation is: ')   
#     if client== '+':
#         print(a+b)
#     elif client =='-':
#         print(a-b)
#     elif client=='/':
#         print(a/b)
#     elif client == '*':
#         print(a*b)
#     elif client == 'stop':
#         break


### 5 Question
# Write a program to build a simple Student Management System using classes and containers (lists, dict). The system should perform the following operations:

#     1. Accept: Method to enter new student details
#     2. Display: Function to display student details
#     3. Search: search function for searching student by username
#     4. Delete: for deleting student by id
#     5. Update: update student by id

# Баронома Student Management System барои контроли донишҷуён созед бо истифодаи Класс ва Контейнерҳо(lists, dict). Баронома бояд вазифаҳои зеринро иҷро кунад.
#     1. Accept: Функсия барои сабт кардани донишҷуи нав ба базаи маълумотҳо
#     2. Display: Нишон додани маълумотҳои донишҷуён дар экран
#     3. Search: Барои кофтани донишҷу бо username
#     4. Delete: Барои нест кардани маълумотҳои донишҷуи додашуда аз база
#     5. Update: Барои иваз кардани маълумотҳои донишҷуи додашуда 



### 5 Question
# Write a program to build a simple Student Management System using classes and containers (lists, dict). The system should perform the following operations:

#     1. Accept: Method to enter new student details
#     2. Display: Function to display student details
#     3. Search: search function for searching student by username
#     4. Delete: for deleting student by id
#     5. Update: update student by id

# Баронома Student Management System барои контроли донишҷуён созед бо истифодаи Класс ва Контейнерҳо(lists, dict). Баронома бояд вазифаҳои зеринро иҷро кунад.
#     1. Accept: Функсия барои сабт кардани донишҷуи нав ба базаи маълумотҳо
#     2. Display: Нишон додани маълумотҳои донишҷуён дар экран
#     3. Search: Барои кофтани донишҷу бо username
#     4. Delete: Барои нест кардани маълумотҳои донишҷуи додашуда аз база
#     5. Update: Барои иваз кардани маълумотҳои донишҷуи додашуда 



