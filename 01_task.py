# Question - 1
# number = 15
# if number%3 == 0 and number%5 == 0:
#     print("Consultadd - Python Training")
# elif number%3 == 0:
#     print("Consultadd") 
# elif number%5 == 0:
#     print("Python Training")
# else:
#     print(number)  


# Question -2
# # num1 = int (input("enter number : ")) 
# num2 = int (input("enter number : ")) 
# operation = input("""select your function :
# 1 - Addition
# 2 - Subtraction
# 3 - Division
# 4 - Multiplication
# 5 - Average \n""")

# answer = 0 
# if operation == "1":
#     answer = num1 + num2
#     print("The value of num1+num2 is :", answer)
# elif operation == "2":
#     answer = num1 - num2
#     print("The value of num1-num2 is :", answer)
# elif operation == "3":
#     answer = num1 / num2
#     print("The value of num1/num2 is :", answer)
# elif operation == "4":
#     answer = num1  * num2
#     print("The value of num1*num2 is :", answer)
# elif operation == "5":
#     answer = (num1 + num2)/2
#     print("The value of (num1+num2)/2 is :", answer)
# if answer < 0 :  
#     print("NEGATIVE") 


# Question - 3 
# a = 10
# b = 20
# c = 30
# avg = (a+b+c)/3
# print("avg =",avg)
# if avg>a and avg >b and avg >c :
#     print("avg is higherthan a,b,c")
# elif avg>a and avg >b :
#     print("avg is higher than a,b,c")
# elif avg>a and avg >c:
#     print("avg is higher than a,c")
# elif avg>b and avg >c :
#     print("avg is higher than b,c")
# elif avg>a :
#     print("avg is just higher than a")
# elif avg>b :
#     print("avg is just higher than b")
# elif avg>c :
#     print("avg is just higher than c")         


# Question - 4
count = 6
while count :
    number = int(input("enter number : "))
    if number > 0:
        print("good going")
    if number < 0:
        print("it's over")
        break


# Question - 5
# lower = int(input("enter the lower bound :"))
# upper = int(input("enter the upper bond :")) 
# for i in range (lower,upper+1):
#     if i%7==0:
#         print(i)

# Question - 6
# x = "123"
# for i in x:
#     print(i)


# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)  


# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# Question - 7
# for x in range(6):
#     if(x == 3 or x == 6):
#         continue
#     # print(x)
#     print(x,end=' ')
# print("\n") 


# Question - 8
# alpha, string = 0, "consul72"
# for i in string:
#     if(i.isalpha()):
#         alpha +=1
# print ("number of digit is", len(string)-alpha) 
# print ("number of alphabets is", alpha)  


# Question - 9
# guess_num = 6
# while (True):
#     answer = int(input("guess the true number : "))
#     print(answer)
#     if guess_num == answer:
#         print ("correct number")
#         break
#     else:
#         print("answer is incorrect" )  
#         user = input("\n do you want to guess again ? : ") 
#         if user == "no" :
#             break
#         continue  


# Question - 10
# num = int(input("enter the lucky number : "))
# luckynum = 6
# guess_count = 1
# guess_limit = 5
# while guess_count <= 5:
#     guess = int(input('Guess a number : '))
#     # guess_count += 1
#     if guess == luckynum :
#         print("Good guess ! ")
#     else:
#         if guess_count == 5:
#             break
#         print("Try again ! ")
#     guess_count += 1 
# print("Game over ! ") 


# Question - 11
# num = int(input("Enter the lucky number : "))
# luckynum = 6
# guess_count = 1
# guess_limit = 5
# while guess_count <= 5:
#     guess = int(input('Guess a number : '))
#     # guess_count += 1
#     if guess == luckynum :
#         print("Good guess!")
#         break
#     else:
#         if guess != luckynum:
#             print("Sorry but that was not very successful !")
#             guess_count += 1 