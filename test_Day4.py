# How to use  Random Module
# pseudo- random number generators in python by Mersenne Twister for more knowledge go for wikipedia 
# Also available free video the KhanAcademy.org website for that more knowledge  \
#algorithm to get the things that we want,like the air speed velocity of a laden sw
# Use askpython.com

#import random
# random_int = random.randint(20,30)
# print(random_int)

# When different people working on different modules like that
# let take new module name my_module , create a new python file 
# let say we want to store value pi 
# import my_module
# print(my_module.py)

#Generationg Random floating point numbers 

#random.random()- next floating point number between(0.0 to 1.0 )
#random.uniform(a,b)- a random floating point N a<=N<=b if a<=b and b<=N<=a if b<a
#random.expovariate(lambda)- returns a num corresponding to an exponential distribution 
#random.gauss(mu,sigma)- returns a num corresponding to a gaussian distribution.

# random_float = random.random()
# print(random_float)
# random_float* 5 
# randomF = random. random()*10
# print(randomF)
# love_score = random.randint(1,50)
# print(f"your love score is {love_score}")

# auditorium problem solution 
# import random 
# random_toss = random.randint(0,1) #use function inside the random module call randint 
# if random_toss == 1:
#     print("Heads ")
# else:
#     print(" Tails")

# How use list in python 
#books =[item1, item2, item3] doesn't matter datatpye integer float or string colud store 
# state1 = "Delhi\n"
# state2 = "Mumbai\n"
# state3 = "Kanpur\n"
# state_comb = state1+state2+state3
# print(state_comb)

# state_comb1 = ["Delhi","Mumbai","Kanpur"]
# print(state_comb1)

#understanding the offset and appending items to lists

#state_comb2 = ["Bombay","Sind","Madras","Bengal","Burma","Punjab","Assam","Bihar", "Orissa", "Bengal", "Bihar"]
# print(state_comb2[8]) # use index forward 
# print(state_comb2[-8])  #use index backward
# state_comb2.append("Chennai")
# print(state_comb2)

# go to website docs.python.org/tutorial/stractures.html more on list 
# list.append(x) - add an item the end of the list 
# list.extend(iteration)- Extend the list by appending all the iterable .Equivalent to a[len(a):]= iterable 
# list.insert(i,x)- inset an item at a given position.
# list.remove()- Remove the first item from the list whose the value is equal to x
# list.pop([i])- Remove the  item at the given position in the list. if no index specified, a.pop() return
# remove and returns the last item in the list 
# list.clear()- Return a shallow copy of the list Equivalent to a[:]
# list.index(x[,start,[,end]])- return zero-based index in the list of the first item whose value is equal to x. Raise a valueerror if there is no such item 
# list.count(x)- return the number of times x appearing 
#state_comb2.extend(["Agra", "G B Nagar"])
# print(state_comb2)
# st =state_comb2.count('Bombay')
# state_comb2.count('Bombay')
# state_comb2.reverse()
# print(state_comb2)
# print(st)

# at1 = state_comb2.index('Bihar',2) # find next bihar same list 
# print(at1)

# sort_list = state_comb2.sort() 
# print(sort_list)
# names_string = [("Ganesh","Mohan", "Khan","Sochna","Ginni", "Munni")]
# names = names_string.split("Ganesh,Mohan, Khan, Sochna, Ginni, Munni")
# print(names)

# names_string = ("Ganesh", "Mohan", "Khan", "Sochna", "Ginni", "Munni")
# names = list(names_string[0].split(","))
# import random
# num_items = len(names)
# #print(names)
# random_choice = random.randint(1, num_items-1)# generate random numbers bet 0 and last index
# person_payee_bill = names[random_choice]
# print(person_payee_bill + "will go to buy the meel toaday!")

# north_food = ["kadhi pakoda","karela bharta","halwa","kheer"]
# south_food = ["Naan","pakhala","palak paneer","missi roti"]
# mixed_food = [north_food , south_food]
# #print(mixed_food)
# print(mixed_food[1][1])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
#print(dirty_dozen[1][1])
#print(dirty_dozen[0])  # for fruits index 0 
#print(dirty_dozen[1])  # for vegetables index 1 
#print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
#create treasure list three 
line1 = [" ", " "," "]
line2 = [" ", " "," "]
line3 = [" ", " "," "]

map = [line1, line2,line3]

position = input()
marks = position[0]
print(marks)

print(f"{line1}\n{line2}\n{line3}")
