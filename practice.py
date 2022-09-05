# def good_enough(x,guess):
#     return abs((guess*guess) -x)< 0.00000000001

# def improve_guess(x,guess):
#     return (guess + x/guess)/2

# print(good_enough(12,1))
# print(improve_guess(9,3))


# from re import A


# my_list=[value for value in range(10) ]
# my_list.insert(2,34)
# print(len(my_list))
# my_list.pop(7)
# print(my_list)
# print(len(my_list))

# my_dict={key:value for key,value in [['apple',12],['banana',12],['orange','pink']]}
# print(my_dict)
# print(my_dict['apple'])
# print(my_dict['banana'])
# print(my_dict['orange'])

# addd=my_dict['apple']+my_dict['banana']
# print(addd)
# my_dict['peach']=44 #adding new item in the dict
# print(my_dict)


# def is_even(number):
#     if number % 2==0:
#         return True
#     else:
#         return False

# print(is_even(2))
# print(is_even(3))

# def adding(num1,num2):
#     number=num1+num2
#     print(number)

# adding(2,3)
# adding(23,3)
# adding(3,3)
# adding(5,3)
# adding(25,3)


# list_=['apple','banana','orange']
# def list_parse(num):
#     for i in list_:
#         print(i)
#     list_.append(num)
#     print(list_)
#     print(f"new item {num} is added into the list")

# list_parse(23)

# d={1:'one',2:"two",3:"three"}
# print(d.items())
# for k,v in d.items():
#     print(k,":", v)


# list1=[1,2,3,4,5]
# list2=[6,7,8,9,0]
# merged=list(zip(list1,list2))
# print(merged)

# a=["id","name"]
# b=[12,"usman"]
# print(dict(zip(a,b)))
# print(list(zip(a,b)))




# class point:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y

#     def __str__(self):
#         return "["+str(self.x)+","+str(self.y)+"]"

# p1=point()
# print("p1= ",p1.x)
# print("p1= ",p1)

# p2=point(2,4)
# print("p2= ",p2.x)
# print("p2= ",p2)

try:
    print(4/2)
    print(3/0)
    print("everything completed")

except ZeroDivisionError:
    print("Donot ask me to divide by zero")

print("done")