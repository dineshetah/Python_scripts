# # question_data = [
# # {"text": "A slug's blood is green.", "answer": "True"},
# # {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# # {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# # {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# # {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# # {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# # {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# # {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# # {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# # {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# # {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# # {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# # ]


# d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}    
# # print(d)

# # Accesing value using keys  

# # print("1st name is"+" "+d[1])
# # print("1st name is"+" "+d[4])

# # print(d.keys())
# # print(d.values())

# # Creating Empty set  
# # set1 = set()  
  
# # set2 = {'James', 2, 3,'Python'}  
# # print(set2)

# # # Adding element to the set  
  
# # set2.add(10)  
# # print(set2)  

# # #Removing element from the set  
# # set2.remove(2)  
# # print(set2)  

# # Code to show how we use docstrings in Python  
  
# # def add(x, y):  
# #     """This function adds the values of x and y"""  
# #     return x + y  
   
# # # Displaying the docstring of the add function  
# # print( add.__doc__ )  

# # Simple Python program to understand the if statement  

# # num = int(input("enter the number"))
# # if num%2==0:
# #     print("The Given number is an even number.")
# # else:
# #     print("The Given number is an odd number.")




# # Python program to show how the for loop works  

# # Creating a sequence which is a tuple of numbers  

# #numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]  

# # variable to store the square of the number  
# # square = 0  

# # # Creating an empty list  
# # squares = []  

# # # Creating a for loop 

# # for value in numbers:
# #     square = value**2

# #     squares.append(square)
# # print("This is list of squares is", squares)

# ## Using else Statement with for Loop
# # Python program to show how if-else statements work  
  
# # string = "Python Loop"  
# # for s in string:
# #     if s=="o":
# #         print("if-else")
# #     else:
# #         print("printed remaining letter", s)


# # The range() Function
# # With the help of the range() function, we may produce a series of numbers. range(10) will produce values between 0 and 9. (10 numbers).

# # We can give specific start, stop, and step size values in the manner range(start, stop, step size).
        
# # Python program to show the working of range() function  
        
# # print(range(15))
# # print(list(range(15)))  
# # print(list(range(4, 9)))  
# # print(list(range(5, 25, 4)))  

# # Python program to iterate over a sequence with the help of indexing  

  
# # tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")  

# # # iterating over tuple_ using range() function 
# # for item in range(len(tuple_)):
# #     print(tuple_[item].upper())


# # Code to find the sum of squares of each element of the list using for loop  

# # creating the list of numbers  

# # numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]  
# # sum = 0 
# # for num in numbers:
# #     sum = sum + num**2
# #     print("Print the sum of all squares", sum)


# ##################### The range() Function ##########################
# """Since the "range" capability shows up so habitually in for circles, we could erroneously accept the reach as a part of the punctuation of for circle. It's not: It is a built-in 
# Python method that fulfills the requirement of providing a series for the for expression to run over by following a particular pattern (typically serial integers)"""

# # my_list = [3, 5, 6, 8, 4]  

# # for iter_val in range(len(my_list)):
# #     my_list.append(my_list[iter_val]+2)
# # print(my_list)

# ##############Iterating by Using Index of Sequence##############
# "Another method of iterating through every item is to use an index offset within the sequence. Here's a simple illustration"

# # Code to find the sum of squares of each element of the list using for loop  
  
# # creating the list of numbers  
# # numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]  
# # sum = 0
# # for num in range(len(numbers)):
# #     sum = sum + numbers[num]**2 
# #     print("The sum of squares", sum)


# #################### Using else Statement with for Loop ########################
# # code to print marks of a student from the record  
# # student_name_1 = 'Itika'  
# # student_name_2 = 'Parker'  

# # # Creating a dictionary of records of the students  
# # records = {'Itika': 90, 'Arshia': 92, 'Peter': 46}  

# # def marks(self):
# #     for a_student in self.record:
# #         if a_student == self.student_name:
# #             return records[a_student]
# #         break
# #     else:
# #          return f'There is no student of name {self.student_name} in the records'

# # # giving the function marks() name of two students  
# # print( f"Marks of {student_name_1} are: ", marks( student_name_1 ))    



# # student_name_1 = 'Itika'
# # student_name_2 = 'Parker'

# # # Dictionary of records of the students  
# # records = {'Itika': 90, 'Arshia': 92, 'Peter': 46}

# # # Function to get the marks of a student
# # def marks(student_name):
# #     if student_name in records:
# #         return records[student_name]
# #     else:
# #         return f'There is no student of name {student_name} in the records'

# # # Giving the function marks() the names of two students  
# # print(f"Marks of {student_name_1} are: ", marks(student_name_1))
# # print(f"Marks of {student_name_2} are: ", marks(student_name_2))


# #####   Nested Loops  ###########
# """If we have a piece of content that we need to run various times and, afterward, one more piece of content inside that script that we need to run B several times, 
# we utilize a "settled circle." While working with an iterable in the rundowns, Python broadly uses these."""

# # import random # this is module library

# # numbers = []
# # for val in range(0,11):
# #     numbers.append(random.randint(0,11))
# #     print(numbers)
# # for num in range(0,11):
# #     for i in numbers:
# #         if num==i:
# #             print(num,end="")


# ### Python While Loops ############

# #Program code 1:Now we give code examples of while loops in Python for printing numbers from 1 to 10. The code is given below -
# #Method1:
# # i = 1
# # while i<=10:
# #     print(i,end='')
# #     i = i + 1
# # output: 12345678910

# # #Method2:
# # i = 1
# # while i<=10:
# #     i = i + 1
# #     print(i,end='')
# # output: 234567891011


# # Program Code 2:
# # Now we give code examples of while loops in Python 
# # for Printing those numbers divisible by either 5 or 7 within 1 to 50 using a while loop. The code is given below -

# # i = 1
# # while i<51:
# #     if i%5==0 or i%7 ==0: 
# #         print(i,end=" ")
# #     i = i + 1 

# # Program Code:

# # Now we give code examples of while loops in Python, the sum of squares of the first 15 natural numbers using a while loop. The code is given below -

# # num = 15
# # sum = 0
# # count = 1
# # while count<=num:
# #     sum = sum + count**2
# #     count+=1   # incrementing the count
# # print("The sum of squares is:", sum)


# # Program Code:

# # Now we give code examples of while loops in Python for a number is Prime number or not. The code is given below -
# # num = [34, 12, 54, 23, 75, 34, 11] 
# # def prime_number(number):
# #     situation = 0
# #     iteration = 2

# #     while iteration<= number/2:
# #         if number%iteration==0:
# #             situation=1
# #             break
# #         iteration = iteration + 1
# #     if situation == 0:  
# #         print(f"{number} is a PRIME number")  
# #     else:
# #         print(f"{number} is not a PRIME number")  
# # for i in num:
# #     prime_number(i)



# # ## 2. Armstrong and Python While Loop
# ## We will construct a Python program using a while loop to verify whether the given integer is an Armstrong number.


# # Input number to check
# # num = int(input("Enter a number: "))
# # # Copy of original number for checking
# # original_num = num
# # # Variable to store sum of digits raised to power
# # sum_of_digits = 0
# # # Calculate the number of digits
# # num_digits = len(str(num))

# # # While loop to process each digit
# # while num > 0:
# #     digit = num % 10
# #     sum_of_digits += digit ** num_digits
# #     num = num // 10

# # # Check if sum of digits equals original number
# # if sum_of_digits == original_num:
# #     print(f"{original_num} is an Armstrong number.")
# # else:
# #     print(f"{original_num} is not an Armstrong number.")


# # Multiplication Table using While Loop
# # In this example, we will use the while loop for printing the multiplication table of a given number.

# # Program Code:

# # In this example, we will use the while loop for printing the multiplication table of a given number. The code is given below -


# # num = 21
# # counter = 1
# # # we will use a while loop for iterating 10 times for the multiplication table  
# # print("The multiplication of: ", num)
# # while counter <= 10:
# #     ans=num*counter
# #     print(num, 'X', counter,'=', ans)
# #     counter+=1

# ####################### Python While Loop with List ######################
# # Program Code 1:

# # Now we give code examples of while loops in Python for square every number of a list. The code is given below -

# # Python program to square every number of a list    
# # initializing a list    
# # list_ = [3, 5, 1, 4, 6]    
# # squares = []
# # # programing a while loop     
# # while list_:      # until list is not empty this expression will give boolean True after that False  
# #     squares.append(list_.pop()**2)
# #     print(squares)


# # Program Code 2:

# # Now we give code examples of while loops in Python for determine odd and even number from every number of a list. The code is given below -
    
# # list_ = [3, 4, 8, 10, 34, 45, 67,80]        # Initialize the list  
# # index = 0  
# # while index<len(list_):
# #     element = list_[index]
# #     if element % 2 == 0:
# #         print("This is an even element")
# #     else:
# #         print("This is an odd element")
# #     index+=1


# # Program Code 3:

# # Now we give code examples of while loops in Python for determine the number letters of every word from the given list. The code is given below -

# # List_= ['Priya', 'Neha', 'Cow', 'To']  
# # index = 0  
# # while index < len(List_):
# #     element = List_[index]
# #     print(len(element))
# #     index+=1

# ############### Python While Loop Multiple Conditions ##########
    
# # num1 = 17
# # num2 = -12
# # while num1>5 and num2<-5:  # multiple conditions in a single while loop  
# #     num1 -=2
# #     num2 +=2
# #     print((num1, num2))

# # We can also group multiple logical expressions in the while loop, as shown in this example.

# # Code

# # num1 = 9
# # num2 = 14
# # maximum_value = 10
# # counter = 0
# # while (counter<num1 or counter<num2) and not counter >= maximum_value: #grouping multiple conditions
# #     print(f"number of iterations: {counter}")
# #     counter+=1


# # Single Statement While Loop
#     # Python program to show how to create a single statement while loop  
# # counter = 1  
# # while counter: print('Python While Loops')  


# # ############   Loop Control Statements ####################

# # Python program to show how to use continue loop control  
  
# # Initiating the loop  

# # for string in "While Loop":
# #     if string=="o" or string=="i" or string=="e":
# #         continue
# #     print("Current Letter:", string)


# ########### Break Statement ##################
# # Python program to show how to use the break statement  
# # for string in "Python Loops":
# #     if string == "n":
# #         break
# #     print("Current Letter:", string)

# ############ Pass Statement #########################
# # Pass statements are used to create empty loops. Pass statement is also employed for classes, functions, and empty control statements.

# # for  string in "Python Loops":    
# #     pass    
# # print( 'The Last Letter of given string is:', string)     

# # ################## Python break statement #########################
# # Example 1 : break statement with for loop
# # my_list = [1, 2, 3, 4]  
# # count = 0
# # for item in my_list:
# #     if item == 4:
# #         print("Item has been matched")
# #         count+=1
# #         break
# #     print("Found at location", count)


# # break statement example  
# # my_list = [1, 2, 3, 4]  
# # count = 1  
# # for item in my_list:  
# #     if item == 4:  
# #         print("Item matched")  
# #         count += 1  
# #         break  
# # print("Found at location", count)  # it is line out of break loop

# # Example 2 : Breaking out of a loop early

# # break statement example  
# # my_str = "python"  
# # for char in my_str:  
# #     if char == 'o':  
# #         break  
# #     print(char)    

# ###  Example 3: break statement with while loop 
    
# # break statement example  

# # i = 0
# # while 1:
# #     print(i," ",end="")
# #     i = i +1
# #     if i==10:
# #         break;
# # print("came out of while loop");

# ##### Example 4 : break statement with nested loops##########
# # n=2
# # while True:
# #     i = 1
# #     while i<=10:
# #         print("%d X %d =%d\n"%(n,i,n*i))
# #         i+=1
# #     choice = int(input("Do you want to continue printing the table? Press 0 for no:"))
# #     if choice ==0:
# #         print("Exiting the program...")
# #         break
# #     n+=1
# # print("Program finished Successfully")


# ############ Python Continue Statements in for Loop ##############

# # Python code to show example of continue statement  
# # looping from 10 to 20  
# # for iterator in range(10, 21):  
# #      # If iterator is equals to 15, loop will continue to the next iteration  
# #     if iterator == 15: 
# #              continue  
# #     # otherwise printing the value of iterator  
# #     print(iterator)


# ######## Python Continue Statements in while Loop  #############

# # # Creating a string  
# # string = "JavaTpoint"  
# # # initializing an iterator  
# # iterator = 0  

# # while iterator < len(string):
# #        # if loop is at letter a it will skip the remaining code and go to next iteration  
# #     if string[iterator]=='a':
# #      continue
# # # otherwise it will print the letter
# # print(string[iterator])
# # iterator+=1


# ###### Python Continue statement in list comprehension ########
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # using a list comprehension with countinue 

# # sq_num = [num**2 for num in numbers if num%2==0]
# # print(sq_num)

# ##   An Illustration of the Pass Statement

# # Python program to show how to use a pass statement in a for loop  
# '''''pass acts as a placeholder. We can fill this place later on'''  

# # sequence = {"Python", "Pass", "Statement", "Placeholder"}  
# # for value in sequence:  
# #     if value == "Pass":  
# #         pass # leaving an empty if block using the pass keyword  
# #     else:  
# #         print("Not reached pass keyword: ", value)  


# # ############## Python List #######################
# """ 
#  the sequence of various data types is stored in a list, A list is a collection of different kinds of values or items,
#  Python lists are mutable, we can change their elements after forming
# """

# # list example in detail  
# emp = [ "John", 102, "USA"]       
# Dep1 = [ "CS",10]    
# Dep2 = [ "IT",11]      
# HOD_CS = [ 10,"Mr. Holding"]      
# HOD_IT = [11, "Mr. Bewon"]      
# #print("printing employee data ...")      
# #print(" Name : %s, ID: %d, Country: %s" %(emp[0], emp[1], emp[2]))    
  
# # print("printing departments ...")     
# # print("""Department 1:\nName: %s, ID: %d\n Department 2:\n Name: %s, ID: %s
# #       """%( Dep1[0], Dep2[1], Dep2[0], Dep2[1]))      

# # print("HOD Details ....")      
# # print("CS HOD Name:%s, Id:%s" %(HOD_CS[1], HOD_CS[0]))
# # print("CS HOD Name: %s, Id: %d" %(HOD_CS[1], HOD_CS[0]))      
# # print("IT HOD Name: %s, Id: %d" %(HOD_IT[1], HOD_IT[0]))      
# # print(type(emp), type(Dep1), type(Dep2), type(HOD_CS), type(HOD_IT))    

# #######    Updating List Values ################
# # updating list values  
# list = [1, 2, 3, 4, 5, 6]       
# print(list)       
# # It will assign value to the value to the second index     
# list[2] = 10     
# print(list)      
# # Adding multiple-element     
# list[1:3] = [89, 78]       
# print(list)     
# # It will add value at the end of the list    
# list[-1] = 25    
# print(list)    


# #############  Python List Operations  #####################
# """The concatenation (+) and repetition (*) operators work in the same way as they were working with the strings. The different operations of list are
# 1.Repetition 2.Concatenation 3.Length 4.Iteration 5.Membership"""

# # 5. Membership
# # It returns true if a particular item exists in a particular list otherwise false.


# # membership of the list  
# # # declaring the list  
# # list1 = [100, 200, 300, 400, 500]  
# # # true will be printed if value exists  
# # # and false if not  
  
# # print(600 in list1)  
# # print(700 in list1)  
# # print(1040 in list1)  
  
# # print(300 in list1)  
# # print(100 in list1)  
# # print(500 in list1)  


# ####### Adding Elements to the List  ###################
# # The append() function in Python can add a new item to the List. In any case, the annex() capability can enhance the finish of the rundown.

# # Declaring the empty list 
# I =[]

# n = int(input("Enter the number of elements in the list: "))
# # for loop to take the input 

# for i in range(0, n):
#     I.append(input("Enter the item:"))
# print("printing the list items..")
# print(I)
# # traversal loop to print the list items   

# for i in I:
#     print(i,end="")

# ########### Removing Elements from the List ##########
# The remove() function in Python can remove an element from the List. To comprehend this idea, look at the example that follows.

# list = [0,1,2,3,4,5]
# print("printing original list:");
# for i in list:
#     print(i,end=" ")
# list.remove(2)
# print("\nprinting the list after the removal of first element...");
# for i in list:
#     print(i,end=" ")

# ########### Python List Built-in Functions ###############
# Python provides the following built-in functions, which can be used with the lists.
   #  len(), max(), min()
# declaring the list  
# list1 = [12, 16, 18, 20, 39, 40]  
# len(list1)
# max(list1)
    
# Example: 1- Create a program to eliminate the List's duplicate items.
# list1 = [1,2,2,3,55,98,65,65,13,29]    
# list2 =[] # an empty list that will store unique values 
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# Example:2- Compose a program to track down the amount of the component in the rundown.
# list1 = [3,4,5,9,10,12,24]    
# sum = 0    
# for i in list1:    
#     sum = sum+i        
# print("The sum is:",sum)  

#Example: 3- Compose the program to find the rundowns comprise of somewhere around one normal component.
# list1 = [1,2,3,4,5,6]    
# list2 = [7,8,9,2,10]    
# for x in list1:    
#     for y in list2:    
#         if x == y:    
#             print("The common element is:",x)   


# ######### Python Tuples ######################
# A comma-separated group of items is called a Python triple. The ordering, settled items, and reiterations of a tuple are to some degree like those of a rundown, 
# but in contrast to a rundown, a tuple is unchanging. 
            
# Tuples are an immutable data type, meaning their elements cannot be changed after they are generated.
# Each element in a tuple has a specific order that will never change because tuples are ordered sequences.

# Python program to show how to create a tuple    
# Creating an empty tuple    
# empty_tuple = ()    
# print("Empty tuple: ", empty_tuple)    
    
# # Creating tuple having integers    
# int_tuple = (4, 6, 8, 10, 12, 14)    
# print("Tuple with integers: ", int_tuple)    
    
# # Creating a tuple having objects of different data types    
# mixed_tuple = (4, "Python", 9.3)    
# print("Tuple with different data types: ", mixed_tuple)    
    
# # Creating a nested tuple    
# nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))    
# print("A nested tuple: ", nested_tuple)    

## Prentheses are not necessary for the construction of multiples. This is known as triple pressing.###
# tuple_list = 4, 5.7,"Tuples", ["Python", "Tuples"]
# print(tuple_list) # Displaying the tuple created

# checking the data type of object tuple_list
#print(type(tuple_list));

# trying to modify tuple_list
# try:
#     tuple_list[1] = 4.67
# except:
#     print(TypeError)

############### Accessing Tuple Elements ###############
# A tuple's objects can be accessed in a variety of ways.

#Indexing

# Indexing We can use the index operator [] to access an object in a tuple, where the index starts at 0.

# Python program to show how to access tuple elements    
# Creating a tuple    
# tuple_ = ("Python", "Tuple", "Ordered", "Collection")    
# print(tuple_[0])
# print(tuple_[1])

# trying to access element index more than the length of a tuple 
# try:
#     print(tuple_[5])
# except Exception as e:
#     print(e)

# # trying to access elements through the index of floating data type    

# try:
#     print(tuple_[1.0])
# except Exception as e:
#     print(e)

# # Creating a nested tuple
#     nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7)) 

# # Accessing the index of a nested tuple     
# print(nested_tuple[1][0]);

############# Slicing ################
# Python program to show how slicing works in Python tuples    
# Creating a tuple    
# tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")    
# # Using slicing to access elements of the tuple    
# print("Elements between indices 1 and 3: ", tuple_[1:3])    
# # Using negative indexing in slicing    
# print("Elements between indices 0 and -4: ", tuple_[:-4])    
# # Printing the entire tuple by using the default start and end values.     
# print("Entire tuple: ", tuple_[:]) 

############## Deleting a Tuple #######################
# Python program to show how to delete elements of a Python tuple    
# Creating a tuple    
# tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")    
# # Deleting a particular element of the tuple    
# try:     
#     del tuple_[3]    
#     print(tuple_)    
# except Exception as e:    
#     print(e)
# del tuple_[3]    
# # Trying accessing the tuple after deleting it    
# try:
#     print(tuple_)
# except Exception as e:
#     print(e)


############# Tuple Methods #################
# Like the list, Python Tuples is a collection of immutable objects. There are a few ways to work with tuples in Python
######### $$$$$$$$$ Count () Method $$$$$$$$$$$$$$$$
# Creating tuples  
# T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)  
# T2 = ('python', 'java', 'python', 'Tpoint', 'python', 'java')

# # counting the appearance of 2

# result = T1.count(2)
# print('Count of 2 in T1 is:', result)

# # counting the appearance of java
# result = T2.count('java')
# print('Count of Java in T2 is:', result)

# ###################  Index() Method #################
# The Index() function returns the first instance of the requested element from the Tuple.'


# Creating tuples  
# Tuple_data = (0, 1, 2, 3, 2, 3, 1, 3, 2)  
# # getting the index of 3  
# res = Tuple_data.index(4)  
# print('First occurrence of 1 is', res)  
# # getting the index of 3 after 4th  
# # index  
# res = Tuple_data.index(3, 4)  
# print('First occurrence of 1 after 4th index is:', res)  

##########  Tuple Membership Test ############################
############# Utilizing the watchword, we can decide whether a thing is available in the given Tuple.

# Python program to show how to perform membership test for tuples    
# Creating a tuple    
# tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")    

# # In operator
# print('Tuple' in tuple_)
# print('Items' in tuple_)

# # Not in operator    
# print('Immutable' not in tuple_)    
# print('Items' not in tuple_) 


############### Iterating Through a Tuple ##################
# A for loop can be used to iterate through each tuple element.
# Python program to show how to iterate over tuple elements    
# Creating a tuple    
# tuple_ = ("Python", "Tuple", "Ordered", "Immutable")    
# # Iterating over tuple elements using a for loop    

# for item in tuple_:
#     print(item)


############### Changing a Tuple #####################
   # Tuples, instead of records, are permanent articles.
    # Multiple values can be assigned to a tuple through reassignment.
# Python program to show that Python tuples are immutable objects    
    
# Creating a tuple    
# tuple_ = ("Python", "Tuple", "Ordered", "Immutable", [1,2,3,4])    
# # Trying to change the element at index 2 
# try: 
#     tuple_[2]="Items"
#     print(tuple_)
# except Exception as e:
#     print(e)
# # But inside a tuple, we can change elements of a mutable object
# tuple_[-1][2] = 10
# print(tuple_)

# # Changing the whole tuple
# tuple_ = ("Python", "Items")
# print(tuple_)

##################///////////  Python Set\\\\\\\\\\\\\ ##################

# A Python set is the collection of the unordered items. 
# Each element in the set must be unique, immutable, and the sets remove the duplicate elements

# Example 1: Using curly braces
# Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
# print(Days)    
# print(type(Days))    
# print("looping through the set elements ... ")    
# for i in Days:    
#     print(i)    

# The set can be created by enclosing the comma-separated immutable items with the curly braces {}. Python also provides the set() method, 
# which can be used to create the set by the passed sequence.
    
# Example 2: Using set() method
    
# Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
# print(Days)    
# print(type(Days))    
# print("looping through the set elements ... ")    
# for i in Days:    
#     print(i)    


# Creating a set which have immutable elements  
set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
print(type(set1))  
#Creating a set which have mutable element  
# set2 = {1,2,3,["Javatpoint",4]}  
# print(type(set2))  

# Example: 1 - Using add() method
# Months = set(["January","February", "March", "April", "May", "June"])    
# print("\nprinting the original set ... ")    
# print(Months)    
# print("\nAdding other months to the set...");    
# Months.add("July");    
# Months.add ("August");    
# print("\nPrinting the modified set...");    
# print(Months)    
# print("\nlooping through the set elements ... ")    
# for i in Months:    
#     print(i)    

# Example - 2 Using update() function
    
# Months = set(["January","February", "March", "April", "May", "June"])    
# print("\nprinting the original set ... ")    
# print(Months)    
# print("\nupdating the original set ... ")    
# Months.update(["July","August","September","October"]);    
# print("\nprinting the modified set ... ")     
# print(Months);  

# Removing items from the set
# Python provides the discard() method and remove() method which can be used to remove the items from the set. 
# The difference between these function, using discard() function if the item does not exist in 
# the set then the set remain unchanged whereas remove() method will through an error.

# months = set(["January","February", "March", "April", "May", "June"])    
# print("\nprinting the original set ... ")    
# print(months)    
# print("\nRemoving some months from the set...");    
# months.discard("January");    

################ Python Dictionary ########################

# The data is stored as key-value pairs using a Python dictionary.
# This data structure is mutable
# The components of dictionary were made using keys and values.
# Keys must only have one component.
# Values can be of any type, including integer, list, and tuple.

# Creating an empty Dictionary       
Dict = {}       
# print("Empty Dictionary: ")       
#print(Dict)    

# Creating a Dictionary       
# with dict() method       
Dict = dict({1: 'Hcl', 2: 'WIPRO', 3:'Facebook'})       
# print("\nCreate Dictionary by using  dict(): ")       
#print(Dict)      

# Creating a Dictionary       
# with each item as a Pair       
Dict = dict([(4, 'Rinku'), (2, 'Singh')])       
# print("\nDictionary with each item as a pair: ")       
# print(Dict)     

################ Accessing the dictionary values #############

Employee = {"Name": "Dev", "Age": 20, "salary":45000,"Company":"WIPRO"}      
#print(type(Employee))
# print("Name:%s" %Employee["Name"], "Age:%d" %Employee["Age"])

############## Adding Dictionary Values  ################# 

# Adding elements to dictionary one at a time       
Dict[0] = 'Peter'      
Dict[2] = 'Joseph'      
Dict[3] = 'Ricky'      
# print("\nDictionary after adding 3 elements: ")       
# print(Dict)  

# Adding set of values        
# with a single Key       
# The Emp_ages doesn't exist to dictionary      
Dict['Emp_ages'] = 20, 33, 24      
# print("\nDictionary after adding 3 elements: ")       
# print(Dict)       

#################### Deleting Elements using pop() Method ################## 
# Creating a Dictionary       
Dict1 = {1: 'JavaTpoint', 2: 'Educational', 3: 'Website'}       
# Deleting a key        
# using pop() method       
pop_key = Dict1.pop(1)       
# print(Dict1)      

############# Iterating Dictionary #################
# Example 1
# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}     
# for x in Employee:
    # print(x) # it will get output keys
    # print(Employee[x]) # here will get values 



# Example 2
#for loop to print the values of the dictionary by using values() method.    
# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}        
# for x in Employee.values():        
#     print(x)       



# Example 3
#for loop to print the items of the dictionary by using items() method    
# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}       
# for x in Employee.items():        
#     print(x)      


############ Properties of Dictionary Keys ##################
    
# 1. In the dictionary, we cannot store multiple values for the same keys. If we pass more than one value for a single key
# Employee={"Name":"John","Age":29,"Salary":25000,"Company":"WIPRO","Name": "John"}   
# for x, y in Employee.items():
#     print(x,y)


def square(num):
    """
    This function computes the square of the number.
    """
    return num**2
sq = square(6)
# print("The square of the given number is:", sq)

############## Calling a Function ##################
# Calling a Function To define a function, use the def keyword to give it a name, 
# specify the arguments it must receive, and organize the code block.

# Example Python Code for calling a function  
# Defining a function    
# def a_function( string ):    
#     "This prints the value of length of string"    
#     return len(string)    
# Calling the function we defined  
# print("Lenght of the string Functions is:", a_function("Functions"))

########### Pass by Reference vs. Pass by Value ##########

# Example Python Code for Pass by Reference vs. Value  
# defining the function    

# def square(item_list):
    # """This function will find the square of items in the list"""
    # squares = []
    # for I in item_list:
    #     squares.append(I**2)
    # return squares

# Calling the defined fucntion 
# my_list = [17,15,10]
# my_result = square(my_list)
# print("Squares of the list are:", my_result)

################## Function Arguments #####################
# The following are the types of arguments that we can use to call a function:

# Default arguments
# Keyword arguments
# Required arguments
# Variable-length arguments

# Default arguments

# Python code to demonstrate the use of default arguments    
# defining a function    
# def function( n1, n2 = 20 ):    
#     print("number 1 is: ", n1)    
#     print("number 2 is: ", n2)


# # Calling the function and passing only one argument    
# print( "Passing only one argument" )    
# function(30)    

# # Now giving two arguments to the function    
# print( "Passing two arguments" )    
# function(50,30) 

# # Keyword arguments
# # Python code to demonstrate the use of keyword arguments    
#   # Defining a function    
# def function( n1, n2 ):    
#     print("number 1 is: ", n1)    
#     print("number 2 is: ", n2)    
    
# # Calling function and passing arguments without using keyword    
# print( "Without using keyword" )    
# function( 50, 30)       
        
# # Calling function and passing arguments using keyword    
# print( "With using keyword" )    
# function( n2 = 50, n1 = 30)    


# ######## Required Arguments ###############
# # Python code to demonstrate the use of default arguments      
# # Defining a function    
# def function( n1, n2 ):    
#     print("number 1 is: ", n1)    
#     print("number 2 is: ", n2)    

# # Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30 
# print("Passing out of order arguments")
# function(30,20)

# # Calling function and passing only one argument
# print("Passing only one argument")
# try:
#     function(30)
# except:
#     print("Function needs two positional argments")

###  Variable-Length Arguments
    
def function(*args_list):
    ans = []
    for I in args_list:
        ans.append(I.upper())
    return ans
object = function('Python', 'Functions', 'tutorial')
# print(object)

def function(**kargs_list):
    ans = []
    for key, value in kargs_list.items():
        ans.append([key,value])
    return ans
# Paasing kwargs arguments    
object = function(First = "Python", Second = "Functions", Third = "Tutorial")   
#print(object)


################# The Anonymous Functions #####################
# Python code to demonstrate ananymous functions  
# Defining a function    
# lambda_ = lambda argument1, argument2: argument1 + argument2;    
    
# # Calling the function and passing values    
# print( "Value of the function is : ", lambda_( 20, 30 ) )    
# print( "Value of the function is : ", lambda_( 40, 50 ) )   


############### Scope and Lifetime of Variables ###############
# Python code to demonstrate scope and lifetime of variables  
#defining a function to print a number.    
# def number( ):    
#     num = 50    
#     print( "Value of num inside the function: ", num)    
    
# num = 10    
# number()    
#print( "Value of num outside the function:", num)    


################## Python Capability inside Another Capability #####################

# Python code to show how to access variables of a nested functions    
# defining a nested function    
# def word():    
#     string = 'Python functions tutorial'    
#     x = 5     
#     def number():    
#         print( string )   
#         print( x )  
             
#     number()    
# word()    

# Initialize dictionary 
test_dict = {'gfg' : [1, 2], 'is' : [4, 5], 'best' : [7, 8]} 
# print("The original dictionary:" +str(test_dict))

# result = [[i for i in test_dict[x]] for x in test_dict.keys()]
# # printing result 
# print(result)
#print("The list values of keys are : " + str(result)) 


### Method #3 : Using map() + lambda ###################

# result = []
# for i in test_dict.values():
#     result.append(list(map(lambda x: x, i)))

# print(result)

#Method 4: Using a for loop to iterate over the values of the dictionary and using a list comprehension to create a new list for each value.

# result = []

# for val in test_dict.values():
#     result.append(x for x in val)
# print(str(result))

# Iterate Through Dictionary Keys And Values in Python
# Below, are the possible approaches to Iterate Through Dictionary Keys And Values In Python.

# Using list comprehension
# Using keys() and values() methods
# Using the zip() method

# defining dictionary related to GeeksforGeeks
#geeks_data = {'language': 'Python', 'framework': 'Django', 'topic': 'Data Structures'}

# keys = [key for key in geeks_data.keys()]
# values = [value for value in geeks_data.values()]

# for key in keys:
#     print(key)

# for value in values:
#     print(values)


# Iterate through keys
#print(&quot;Keys:&quot;)
# for key in geeks_data.keys():
#     print(key)

# Iterate through values
#print(&quot;\nValues:&quot;)
# for value in geeks_data.values():
#     print(value)


####### terate Through a Dictionary Using zip( ) Function

# keys, values = zip(*geeks_data.items())

# _ = [print(key) for key in keys]

# _ = [print(value) for value in values]


#### Iterate Through Specific Keys in a Dictionary in Python

d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys we want to check
keys = ["a", "b","c", "d"]

# for key in keys: 
#     value = d.get(key)
#     if value is not None:
#         print(key, value)

# Using a Simple Loop with in Keyword
        
for key in keys:
    # Check if key exists in the dictionary
    if key in d:
        print(key, d[key])

# Using Dictionary Comprehension
# Create a new dictionary with specific keys
new = {key: d[key] for key in keys if key in d}
print(new)

# Using filter() and lambda
# The filter() function is used to create an iterator of keys from the list keys that also exist in dictionary d. 
# We use a lambda function to check if each key is present in d. Then we loop through the filtered keys and print their values.

# Use filter to get keys that are in d
new_keys = filter(lambda k: k in d, keys)

# Iterate through filtered keys
for key in new_keys:
    print(key, d[key])