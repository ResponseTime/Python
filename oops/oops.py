import random
# class emp:
#     comp = "Google"
#     def __init__(slef,comp,name):
#         emp.comp = comp;
#         print(f"The comp name is: {comp} name is {name}")
    
#     def getSalary(self):
#         print(f"the comp is {self.comp} sal is {self.sal}")

#     @staticmethod    
# #     def greet():
# #         print("Hello world")    

# # emp = emp("Facebook","aayush")
# # # emp.comp = "Meta"
# # emp.sal = "120k"
# # emp.getSalary()
# # emp.greet()

# #Practice set



# class microsoft:
#     salary = 0
#     department = ""
#     shift = ""

#     def takeInfo(self):
#         print(''' Enter the details->
#                   Department
#                   shift
#                   salary ''')

#         self.department = str(input(": "))
#         self.shift = str(input(": "))
#         self.salary = int(input(": "))           

# #     def infoGiven(self):
# #         print(f'''Department {self.department}
# #                   Shift {self.shift} 
# #                   Salary {self.salary}''')
    

# # Emp1 = microsoft()

# # Emp1.takeInfo()
# # Emp1.infoGiven()

# # class math:
# #     def squareCube(self,a):
# #         return a*a*a

# #     def squareRoot(self,a):
# #         return a*a


# # math = math()
# # a = math.squareCube(9)
# # b = math.squareRoot(9)

# # print(a,b)

# # class test:
# #     a = 9
# #     def tes(self):
# #         print(self.a)

# # te = test()
# # te.tes()
# # te.a = 69
# # te.tes()

# # class static:
# #     @staticmethod
# #     def test():
# #         print("this is a static method doesnt take any args")

# # st = static()
# # st.test()        

# class train:
#     seats = 9000
#     book = 0
#     trains = ['delhi','luckhnow','odisha','kolkata','punjab','kerala']
#     def getSeats(self):
#         print(f"The no of seats rn: {self.seats}")

#     def bookTicket(self):
#         try:
#             self.book = int(input("How many seats r to be booked: "))
#             self.seats = self.seats - self.book
#         except:
#             print("Only put seats in integers")

#     def whereIsMyTrain(self): 
#         r = random.randint(0,(len(self.trains)-1))
#         print(f"Your train is in {self.trains[r]}")       

# train = train()

# train.getSeats()
# train.bookTicket()
# train.getSeats()
# train.whereIsMyTrain()
# train.whereIsMyTrain()
# train.whereIsMyTrain()

# class mistake:
#     def mis(aayush):
#         print(f"hello + {aayush}")

# mistake.mis("aayush")
