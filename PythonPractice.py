#String Methods
#isalpha()
#isdigit()
#isalnum()
#isspace()
#isupper()
#islower()
#isidentifier()

#endswith()
#startswith()
#count()
#find()
#rfind()
#split() - it takes two optional argument delimiter and max splits. It is used to split strings. path("C:\Users\faiza\Documents\Credence_Notes\Notes\#MyNotes\AutomationsNotes\PythonSplit.png")
#join() - it works opposite of split. It joins an iterable path("C:\Users\faiza\Documents\Credence_Notes\Notes\#MyNotes\AutomationsNotes\PythonJoin.png")

#upper()
#lower()
#title()
#capitalize()
#swapcase()
#replace()

#************************************

#listmethods
#append()
#extend()
#remove()
#pop()
#reverse()
#sort()
#index()
#insert() takes two argument first index second obj
#count()

#************************************

#dictionarymethods
#popitem()
#pop(key)
#clear()
#keys()
#values()
#get(key)




# Swap two numbers
# a = 10
# b = 100
# a,b = b,a
# print(a,b)

#approach 2
# a = 10
# b = 100
# c = a
# a = b
# b = c
# print(a,b)

# **************************************************

# check if number is prime or not
# num = int(input("write a number:"))
#
# count=0
#
# for i in range(2,num+1):
#     if num%i==0:
#         count+=1
# if count==1:
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")

#***************************************************

# Find factorial of a number
# num = int(input("write a number:"))
# fac = 1
# for i in range(1,num+1):
#     fac = fac*i
# print(fac)

#approach2
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (n * factorial(n-1))
#
# print(factorial(5))

#***************************************************

# Fibonacci series
# n = int(input("Enter the number:"))
# num1 = 0
# num2 = 1
# print(num1)
# print(num2)
#
# for i in range(1,n+1):
#     sum = num1+num2
#     print(sum)
#     num1 = num2
#     num2 = sum

#approach2
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
#
#
# for i in range(10):
#     print(fibonacci(i))

#***************************************************

# sum of list, max and min
# list = [1,23,4,5,6,7,88]
#sum
# print(sum(list))
# #2
# sum = 0
# for i in list:
#     sum = sum + i
# print(sum)

#max

# def max(lst):
#     max = lst[0]
#     for i in range(1,len(lst)):
#         if lst[i]>max:
#             max=lst[i]
#     return max
#
# str = '12345'
# list = [1,2,3,4,5,6,7]
# print(len(str))
# max_lst = max(str)
# print(max_lst)

#min
# min = list[0]
#
# for i in range(len(list)):
#     if list[i]<min:
#         min=list[i]
# print()

#***************************************************

# how to swap first and last element of list
# list = [1,2,3,4,5,6,7,8]

#approach1
# list[0],list[-1] = list[-1],list[0]
# print(list)

#approach2 using another variable
# a = list[0]
# list[0] = list[-1]
# list[-1] = a
# print(list)

#***************************************************

# remove nth occurrence of given word for list ##doubt
# list = ["M","A","D","A","M","A"]
# print(len(list))
# ele = "A"
# count = 0
#
# for i in range(len(list)-1):
#     if list[i]==ele:
#         count+=1
#         if count==3:
#             del list[i]
# print(list)

#***************************************************

# remove nth occurrence of given word for string ##doubt
#in this case remove 2nd A
# text = "AFZAL"
# list = []
#
# for i in text:
#     list.append(i)
#
# count = 0
# new_list = []
#
# for w in list:
#     if w=="A":
#         count+=1
#         if count==2:
#             continue
#     new_list.append(w)
# print(new_list)
# new_text = "".join(new_list)
# print(new_text)

#for a sentence
# text = "Test : Remove sencond occurrence of word Test"
# list = text.split()
# word = "Test"
# count = 0
# new_list = []
#
# for w in list:
#     if w==word:
#         count+=1
#         if count==2:
#             continue
#     new_list.append(w)
# new_word = " ".join(new_list)
# print(new_word)

#function for same
# def remove_nth_occurrenceOfWord(text,word,n):
#     words = text.split()
#     new_words = []
#     count = 0
#
#     for w in words:
#         if w==word:
#             count+=1
#             if count==n:
#                 continue
#         new_words.append(w)
#     result = " ".join(new_words)
#     return result
#
# text = "This is a test to remove word  test"
# word = "test"
# n = 2
# object = remove_nth_occurrenceOfWord(text,word,n)
# print(object)

#***************************************************

# find if element is present in the list
# list = ['apple', 'banana', 'tomato']
# ele = 'apple'
#
# for i in list:                    #we don't even have to run a loop
#     if ele in list:
#         print("Element is present in the list")
#         break
#     else:
#         print("Element is not present in the list")

#create method for same
# def findElement(list,element):
#     if element in list:
#         print("element present in list")
#     else:
#         print("element is not present in list")
#
# list = ['apple', 'banana', 'tomato']
# ele = 'apple'
#
# findElement(list,ele)

#***************************************************

# how to clear a list
# list = [1,2,3,4,5]
# list.clear()
# print(list)

#***************************************************

# how to reverse a list
# list = [1,2,3,4,5]
#approach1
# list.reverse()
# print(list)
#approach2
# new_list = list[::-1]
# print(new_list)
#approach3
# new_list = []
# for i in range(len(list)-1,-1,-1):
#     new_list.append(list[i])
# print(new_list)

#******************************************


# how to clone or copy a list
# list = [1,2,3,4,5]
# new_list = list[:]

# how to count occurrence of an element in a list?
# list = [1,2,23,4,3,23,234,23,42,4,24,2,43]
# ele = 23
# count = 0
# for i in list:
#     if i==23:
#         count+=1
# print(count)

#************************************************

#count occurrence of each element in the list
# list = [1,2,23,4,3,23,234,23,42,4,24,2,43]
# result = {}
#
# for i in list:
#     if i in result:
#         continue
#     result[i]=list.count(i)
# print(result)

#************************************************

#count occurrence of each element in the string
# a = 'c5re8de1ngc7e'
# result = {}
#
# for i in a:
#     result[i] = a.count(i)      #key:value pair
# print(result)
#
# #better code but achieves same result
# for i in a:
#     if (i in result):
#         continue
#     result[i] = a.count(i)      #key:value pair
# print(result)

#method for above question
# def countElementOccurrenceString(Str):
#     result = {}
#
#     for i in Str:
#         if (i in result):
#             continue
#         result[i] = Str.count(i)
#     print(result)
#
# text = "fjalksdjfajlghklafjglkjklsjfdlkjgakljlk"
# countElementOccurrenceString(text)

# #sum of the elements in list
# list = [1,2,23,4,3,23,234,23,42,4,24,2,43]
# print(sum(list))
# #approach2
# sum = 0
# for i in list:
#     sum = sum + i
# print(sum)

# #how to multiply all numbers in the list(numpy)
# min, max, 2nd largest
# Palindrome string - spells same from both sides eg madam

#************************************************************

# reverse words in a sentence
# def reverseWords(text):
#     words = text.split()
#     new_list = []
#
#     for i in range(len(words)-1,-1,-1):
#         new_list.append(words[i])
#
#     result = " ".join(new_list)
#     return result
#
# text = "Hello this is a test string"
# print(reverseWords(text))

#****************************************

# find the position of substr in a string
# string = "BreakBreak"
# substr = "ak"
# print(string.find(substr))
#
#
# # find length of string
# print(len(string))

# how to check if the string contains any special character? check this


# Ajit
#list comprehension:
# a=['John','Gol','Janhvi', 'Nitya'] #find names which starts with J

# def findNamesWithJ(lst):
#     new_list = []
#
#     for i in lst:
#         if i.startswith("J"):
#             new_list.append(i)
#     return new_list
# print(findNamesWithJ(lst=['John','Gol','Janhvi', 'Nitya']))

#from list comprehension
# lst = ['John','Gol','Janhvi', 'Nitya']
# list = [x for x in lst if x.startswith("J")]
# print(list)

#Lambda Function:
#Tuple UNPACK concept:
#String never changes?
#Join function:
#split and strip
# # x = "this/is/also/string"
# # y = "this is also string"
# # a = '//////>>>>>for strip function88888//'


# Int Q
#************************************************************************
##How to count each letter from a string and write it in front of it.
# def charCount(str):
#     lst = []
#     result = {}
#
#     for i in str:
#         lst.append(i)
#
#     for x in lst:
#         if x in result:
#             continue
#         result[x] = str.count(x)
#
#     return result
#
# print(charCount(str="fkjdalksjflkdjasklfjlkjljdlsjflkadsjlghlvnncvcnx,mzvn,mcnv,mcz"))

#***************************************************************************************

##Counting unique characters from string?
#same answer as above

#***************************************************************************************

##How to find the unique characters and their count in a string??
#same answer as above

#***************************************************************************************

##How to find the duplicate characters and their count in a string??
# def charCountForDuplicates(str):
#     lst = []
#     result = {}
#
#     for x in str:
#         lst.append(x)
#
#     for i in str:
#         if i in result:
#             continue
#         if str.count(i)>1:
#             result[i] = str.count(i)
#     return result
#
# print(charCountForDuplicates(str="fkjdaljglhdsaljfoiutqeoiutoireqvc,mn,znx,n,mz"))

#***************************************************************************************

# # l1 = [2,3,4,5,6]
# # l2 = [2,2,4,1,4]
# # l3=[]
# #
# # counter1=0
# # counter2=0
# #
# # i=0
# #
# # while i < len(l1):
# #     l3.append(l1[counter1] * l2[counter2])
# #     counter1 +=1
# #     counter2 +=1
# #     i+=1
# # print(l3)

#***************************************************************************************

##10. How to remove duplicates from list?
# def removeDuplicates(lst):
#     new_list = []
#
#     for i in lst:
#         if lst.count(i)>1:
#             continue
#         else:
#             new_list.append(i)
#     return new_list
# print(removeDuplicates(lst=[1,2,3,4,5,1,3,10,20]))

##How to remove nth occurence of given word from list ?

##11. How to search an element in the list?
##18. How to find the smallest and largest numbers on the list?
##19. How to find the second largest number in a list?
##24. How to check if the string contains any special character?
## How to reverse a string.map
##20. How to check string is palindrome or not?

#***************************************************************

# Check if the string starts with "The" and ends with "Spain":
# def checkString(str):
#     if str.startswith('The') and str.endswith('Spain'):
#         print("True")
#     else:
#         print("False")
#
# checkString(str="The fjdksl Spai")

#***************************************************************

 # Split the string at every white-space character:
##Git branching?
# ##Git branchg conflict?
# ##How do you push code on Git?
# ##What kind of automations you do in your project?
# ##Mock and Patch in python?
# ##Monkey patching in python?

#***************************************************************

 # Convert list into string with spaces.
# list = ["apple","banana","potato"]
# str = ""
# for x in list:
#     str = str + " " + x
# print(str)

#**********************************************************************

#create list2 using lambda function which will have squares of all elements of list1:
#listcomprehension
# list = [1,2,3,4,5,6,7,8,9,10]
# list2 = [x*x for x in list]
# print(list2)



## reverse the string with upper case letters:
#Create and update values in ditionary if value is of type int   {'k1' : 'mango', 'k2' : 'apple', 'k3' : 5, 'k4' : 2}
## create class,object and instance variables.
##Filter even numbers from list [1,2,3,6,2,7,1,3] using list comprehension:

# Q.1 Remove duplicates from list and print updated list:

# ##Q.2 What is multithreading and multiprocessing in python?
# ##Ans: Written in notes.
#
# ##Q.3 What is Overloading and Overriding in Python?
#
#
# ##Q.4 What is session handling in python?
#
# ##Q.5 What is Hash map in python?
 #Given the integer number find the sum of digits of that number until sum becomes single digit.
#Reverse the given number
##How to find duplicate 'words' from a string?
##Finding Unique substring from given string:
#Q1. Derive this o/p:
# #Q.2: difference between append() and extend():
#
# #Q.3: synchronization in selenium?
#
# #Q.4: set up and tear down in fixtures.
#
# #Q.5: Authorization token in Postman API
# ##
# #Q.6: 401 status code?
# ## Unauthorized Access
#
# #Q.7: Python generators?
#
# #Q.8: Map and filters?
#
# #Q.9: Mutable and Immutable data types?
#
# #Q.10: Different Markers?
#
# #Q.11: alternative to click in selenium webdriver
# #Ans:
# # 1. By Ascii Value : driver.findElement(By.cssSelector(".dbl")).sendKey("ASCII VALUE FOR Left Click");
# # 2. .sendKeys(Keys.ENTER)
# # 3. driver.execute_script("arguments[0].click();", yourelement)
# # 4. actions.moveToElement(signOnImage).click().perform();
# # 5. driver.findElement(By.linkText("Selenium")).sendKeys(Keys.ENTER);
# ##Input: Selenium3 Output: se, le, ni, um, 3_
#Q.1 Find the largest number from list without using largest number
#Q.2 Get the following o/p:
#Q.3 Mutable and Immutable types?
#
# #Q.4 I f we fetch test case names from database and do not want change their names and execution so what should i use?
# #Ans: Tuples. As they are immutable.
##Q.6 customized XPATH for web table elements?
# Q.Convert every alternate character to Capital in string:
# Q. Replace every special character with space:
# Q.How to identify and switch to the frame in selenium webdriver when frame does not have id?
#Q1. Remove duplicate elements from dictionary.
#Q2. Difference between remove and delete method? (remove() vs del() vs pop() )
# #Q.3 Try except finally
# #Q.4 How to achieve 100% abstraction in python?
# #Q.5 Generators?
# #Q.6 How to define abstract class?
# #Q.7 How to do you raise pull request in GitHub?
# #Q.8 List and dictionary comprehension using two for loops?
# #Q.9 How to handle Windows in Selenium?
# #Q.10 Explain OOPS concepts in the context of Framework implementation?

# #Q.11 What is type casting in python?
# #Q.12 Can we achieve method overloading and overriding in python
# # Typescript?
# # Pandas?
# # Dataframes?
# # How to compare 2 excel sheets?
# # Hackerrank/Litcode/Hackerearth for coding practice?
# # Jenkins local master slave structure? how it works?










