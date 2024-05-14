'''
types of data in python
1. number - int, float, complex - immutable, non-iterable
2. str - immutable, iterable
3. list - mutable , iterable
4. tuple - immutable, iterable
5. dictionary
6. set
7. boolean
'''

# Swap two numbers
# approach1
# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)

# approach2
# x = 1
# y = 2
# z = x
# x = y
# y = z
# print(x)
# print(y)

# check if number is prime or not
# num = 13
# count = 0
#
# if num > 1:
#     for i in range(1,num+1):
#         if num%i==0:
#             count += 1
#     if count==2:
#         print("Number is prime")
#     else:
#         print("Number is not prime")

# Find factorial of a number
# factorial = 1
# number = 10
#
# if number<1:
#     print("Factorial does not exist for -ve number")
# elif number==0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1,number+1):
#         factorial = factorial*i
#     print("Factorial of",number,"is",factorial)


# Fibonacci series
# n1 = 0
# n2 = 1
#
# print(n1)
# print(n2)

# for i in range(2,10):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum


# sum of list, max and min
# list = [1,3,5,7,9]
# # print(sum(list,10))
#
# #max element in list
# print(max(list))
#
# #min element in list
# print(min(list))
#
# list2=['a', 'b', 'c']
# print(max(list2))
# print(min(list2))

# approach2
# list = [10,3,5,7]
# max = list[0]
#
# # for i in range(len(list)):
# #     if list[i]>max:
# #         max=list[i]
# # print(max)
#
# min = list[0]
#
# for i in range(len(list)):
#     if list[i]<min:
#         min=list[i]
# print(min)

# how to swap first and last element of list
# approach1
# list = [1,3,5,7,9]
#
# size = len(list)
# x = list[0]
#
# list[0] = list[size-1]
# list[size-1] = x
#
# print(list)

# approach2
# list = [1,3,5,7,9]
#
# list[0], list[-1], list[2], list[3] = list[-1], list[0], list[3], list[2]
#
# print(list)


# remove nth occurrence of given word ##doubt
# list = ['a', 'b', 'c', 'a','d','a']
# element = 'a'
# n = 2
# count = 0
#
# for i in range(len(list)):
#     if list[i]==element:
#         count += 1
#         if count==n:
#             del list[i]
# print("updated list:",list)


# find element in the list
# list = [2,5,6,8,0]
# ele = 8
# flag = 0
# #using loop
# # for i in list:
# #     if ele==i:
# #         print("Element found in list")
# #         flag = 1
# #         break
# # if flag==0:
# #     print("Element not found in the list")
#
# #approach2
# if ele in list:
#     print("element found")
# else:
#     print("element not found")

# how to clear a list
# list = [2,5,6,8,0]
# list.clear()
# print(list)

# how to reverse a list
# list = [2,5,6,8,0]
# # print("List before reverse:",list)
# # list.reverse()
# # print("List after Reverse",list)
#
# #approach2
# list = list[-1::-1]
# print(list)

# approach3

# how to clone or copy a list
# list = [2,5,6,8,0]
# list_copy = list[:]
# print(list_copy)

# how to count occurrence of an element in a list?
# list = [2,3,4,5,6,7,8,9,8,6,5,5,5]
# x = 5
# count = 0
#
# for i in list:
#     if i==x:
#         count += 1
# print("Occurrence of 5 in list is",count)
#
# #sum of the elements in list
# list = [2,3,4,5,6,7,8,9,8,6,5,5,5]
# print(sum(list))

# #how to multiply all numbers in the list
# list = [2,3,4,5,6,7,8,9,8,6,5,5,5]
# multiply = 1
#
# for i in list:
#     multiply = multiply*i
# print(multiply)

# approach2 numpy
# import numpy
# list = [1,2,3]
# result = numpy.prod(list)
# print(result)


# min, max, 2nd largest
# list = [1,3,5,6,7,9]
# # min = list[0]
# #
# # for i in range(len(list)):
# #     if list[i]>min:
# #         min=list[i]
# # print(min)
#
# # print(min(list))
# # print(max(list))
#


# list.sort()
# print(list)
# print(list[0]) #min
# print(list[len(list)-1]) #max
# #(or)
# print(list[-1])
# print(list[-2])#2nd largest


# Palidrome string - spells same from both sides eg madam
# s = str(input())
# reverse = s[::-1]
#
# if s==reverse:
#     print("string is palidrome")
# else:
#     print("String is not palidrome")


# reverse wrods in a sentence
# string = "This is for an interview"
# word = string.split(" ")
# print(word)
# #now word is a list and we have to reverse it
# # word.reverse()
# # print(word)
# #(or)
# word = word[-1::-1]
# print(word)
# output = " ".join(word)
# print(output)


# find a substr in a string
string = "This is for an interview"
sub_str = "for"
print(string.find(sub_str))

# find length of string
string = "Welcome"
print(len(string))
counter = 0
for i in string:
    counter += 1
print(counter)

'''
# how to check if the string contains any special character? check this
import re

input1 = "vijay!@#$%^&khalate*&"
regex = re.compile("[@_!#$%^&()<>/\|}{~:]")

if (regex.search(input1) == None):
    print("No special character found")
else:
    print(True)
'''

