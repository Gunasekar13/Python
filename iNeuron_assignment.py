1. Given a list of numbers, write a python program to find the sum of allthe element
in the list?
input arr = [2,4,5,10], i=1, j=3
Output : 19
input arr = [4,10,5,3,3], i=3,j=3
Output : 3
--------------
code:
-------------
arr=list(map(int,input('Enter array element: ').strip().split()))
i=int(input('Enter starting index: '))
j=int(input('Enter ending index: '))
sum=0
for idx in range(i,j+1):
	sum+=arr[idx]
print('Output :',sum)

_____________________________________________________________________________________________
2.Given an array of integers arr[] of size N and an integer, the task is to rotate the array 
element to the left by d positions.?
Input arr[] ={1,2,3,4,5,6,7}, d=2
Output: 3 4 5 6 7 1 2
INput arr[]={3,4,5,6,7,1,2}, d=2
Output : 5 6 7 1 2 3 4
---------------------------------
Code:
---------------------------------
arr=list(map(int,input('Enter array element: ').strip().split()))
d=int(input('Enter the number rotation : '))

list1=[]
list2=[]
for i in range(0,len(arr)):
	if i<d:
		list1.append(arr[i])
	else:
		list2.append(arr[i])

#merge the two list
print(list2+list1)
_____________________________________________________________________________
3.Given a sequence of strings, The task is to find out the second most repeated
(of frequent) string in given sequence.
input : ["aaa","bbb","ccc","bbb","aaa","aaa"]
Output : bbb
---------------------
Code:
-------------------
arr=list(map(str,input('Enter array element: ').strip().split()))
d={}
#count the each element in arr
for i in arr:
	if i in d:
		d[i]+=1 
	else:
		d[i]=1 
print('Count of each element in arr: ',d)
# sort the dict desc sort by values
sort_dict_desc=sorted(d.items(), key=lambda x:x[1], reverse=True)
#covert to dict
d=dict(sort_dict_desc)
#find max value in dict
Max_val=max(d.values())
# find second element
for key,value in d.items():
	if value<Max_val:
		print('The second most occured element :' ,key,value)
		break
_________________________________________________________________________
4.Difference between two lists?
input list1 = [10,15,20,25,30,35,40]
list2=[25,40,35]
 Output : [10,20,30,15]
 -------------------
 Code :
 ------------------
arr1=list(map(int,input('Enter array1 element: ').strip().split()))
arr2=list(map(int,input('Enter array2 element: ').strip().split()))

result=[]

for i in arr1:
	if i not in arr2: # frist element array not in second element
		result.append(i)
print('difference between two list : ',result)
_____________________________________________________________________________________________
5. Print all positive numbers from given list using for loop iterate each element in the list
using for loop and check if number is greater than or equal to 0. If condition satisfies, then 
only print the number?
input list1=[12,-7,5,64,-14]
Output : 12 5 64
input list1=[12,14,-95,3]
Output : 12 14 3
-----------------------
Code :
----------------------
arr1=list(map(int,input('Enter array1 element: ').strip().split()))
for i in arr1:
	if i>0:
		print(i,end=' ')
_________________________________________________________________________
6. Write a Python program to Flatten a given nested list Structure ?
Original list : [0,10,[10,20],40,50,[60,70,80],[90,100,110,120]]
Flatten list : [0,10,20,30,40,50,60,70,80,90,100,110,120]
----------------
Code :
----------------
arr1=[0,10,[10,20],40,50,[60,70,80],[90,100,110,120]]

print('Original List: ',arr1)

Flatten_array=[]

for ele in arr1:
	if type(ele) is int : #check the element is list
		Flatten_array.append(ele)
	else:
		for num in ele: #element is list then flat
			Flatten_array.append(num)

print('The Flatten array: ',Flatten_array)
_________________________________________________________________________
7. Given an array and a value , find if there is a triplet in array whose sum is equal
to the given value. If there is such a triplet present in array, then print the
triplet and return true. Else return False.?
* input array =[12,3,4,1,6,9]
sum=24
Output : 12 3 9
Explanation: There is a triplet(12,3 and 9) present
in the array whose sum is 24

* input array =[1,2,3,4,5]
sum=9
Output : 5 3 1
Explanation: There is a triplet(5,3 and 1) present
in the array whose sum is 9
-------------------------
Code :
------------------------
arr1=list(map(int,input('Enter the arr element: ').strip().split()))
sum=int(input('Enter the sum input: '))
add=0
n=len(arr1)
for i in range(0,n): #frist ele
	for j in range(i+1,n): #second ele
		for k in range(j+1,n): #Third element
			add=arr1[i]+arr1[j]+arr1[k]  #add
			if add==sum:
				print('Output : 'arr1[i],arr1[j],arr1[k])
_________________________________________________________________________
                       STRINGS
1. Pangram is a sentence containing every letter in the English alphabet.
Given a string,find all characters that are missing from the string ,
The characters that can make the string a Pangram. 
We need to print Output in alphabetic order.

input : Welcome to geeksforgeeks 
Output : abdhijnpquvxyz

input : The quick brown fox jumps 
Output : adglvyz 
-----------------
Code :
-----------------
str1=str(input('Enter the sum input: '))
str1=str1.lower()
s="abcdefghijklmnopqrstuvwxyz"
result=''
for char in s:
	if char not in str1:
		result=result+char
		
print('Output: ',result)
_________________________________________________________________________
2. Find total number of non-empty substring of a string with N characters?
input str='abc'
Output : 6
Every substring of given string : 'a','b','c','ab','bc','abc'

input str='abcd'
Output : 10
Every substring of given string : 'a','b','c','d','ab','bc','cd','abc','bcd' and 'abcd'
----------------
Code :
---------------
str1=str(input('Enter the sum input: '))
n=len(str1)
result=n*(n+1)//2
print('Output : ',result)
_________________________________________________________________________
3. Given a string containing lowercase and uppercase letters. Sort it in such a manner
that the uppercase and lowercase letters come in an alternate manner but in a sorted way?
input : bAwutndekWEdkd
Output : AbEdWddekkntuw

Here we can see that letter 'A','E','W' are sorted as well as letters 
"b,d,d,e,k,k,n,t,u,w" are sorted but both appers alternately in the string as far as 
possible.
---------------
Code :
--------------
str1=str(input('Enter the string input: '))
#str1=str1.upper()
n=len(str1)
#sort the str
order_str=''.join(sorted(str1))
print(order_str)
#seperate upper and lowercase
u_str=''
l_str=''
for char in order_str:
	if char.islower() :
		l_str=l_str+char 
	else:
		u_str=u_str+char

print('Upper_str: ',u_str)
u=len(u_str)
print('Upper_str length :',u)
print('Lower_str: ',l_str)
l=len(l_str)
print('Lower_str length :',l)
#make alternate
result=""
for i in range(0,u):
	result=result+u_str[i]
	for j in range(i,l):
		if i==j:
			result=result+l_str[j]
c=l-u
print(c,l)
result=result+l_str[u:]

print('Output : ',result)
_________________________________________________________________________

4. Write a Python program that accepts a comma seperated sequence of words as 
input and prints the unique words in sorted from (alphanumerically)?
Sample words : red,white,black,red,green,black 
Excepted Result  : black,green,red,white,red 
-----------
Code :
-----------
str1=str(input('Enter the sum input: '))
list1=list(str1.split(' ')) #string to list
d={}  #count word 

for i in list1:
	if i in d:
		d[i]+=1
	else:
		d[i]=1 


print(d)
to_li=list(d) #convert dict to list
print('Unique strings',to_li)
#reverse list
rev_li=to_li[::-1]
#list to string
print('Output: ',' '.join(rev_li))
_________________________________________________________________________
5. Write a python program to count the number of characters(character frequency)
in a string?
Sample string : google.com'
Excepted Result : {'g':2,'o':3,'l':1,'e':1,'.':1,'c':1,'m':1}
-----------------
Code :
----------------
str1=str(input('Enter the sum input: '))
d={}
for i in str1:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
print('Output : ',d)
_________________________________________________________________________
6. Find the frequency of minimum occuring character in a python string?
The Original string is : iNeuronNet.com 
The minimum of all characters in GeeksforGeeks is : i 
--------------
Code :
--------------
 str1=str(input('Enter the string input: '))
d={}
for i in str1:
	if i in d:
		d[i]+=1
	else:
		d[i]=1

res=min(d)
print('min',res)
print('Output : ',d)
_________________________________________________________________________
7. Write a program extract all the string characters which have odd number of
occurrences.
The Original string is : geeksforgeeks is best for geeks 
The Odd frequency characters are : ['k','i','t','g','e','b']
-------------
Code :
-------------
str1=str(input('Enter the string input: '))
d={}
for i in str1:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
print('Odd frequency Characters are : ')
for key,value in d.items():
	if (value%2!=0):
		print('{}'.format(key),end=' ')
_________________________________________________________________________
                          DICTIONARY
                          ----------
1. Given an input string and a pattern, check if characters in the input string
follows the same order as determined by characters present in the pattern. Assume 
there won't be any duplicate characters in the pattern?
input : string='engineers rock'
pattern = 'er'
Output : true 
Explanation : all 'e' in the input string are before all 'r'
------------
Code :
-----------
str1=str(input('Enter the string input: '))
p=str(input('Enter the pattern in: '))
n=len(str1)
m=len(p)
#common char
s=''
for i in str1:
	for j in p:
		if i==j:
			s=s+i

print('Commen char Output : ',s)
# check sub
for k in range(0,len(s)):
	r=s[k:k+m]
	print(r,end=' ')
	if r==p:
		count=1
		break
	else:
		count=0
		continue

if count!=0:
	print('\nOutput :',True)
else:
	print('\nOutput :',False)
_________________________________________________________________________
2. Given a list and dictonary, map each element of list with each item of dictonary 
forming nested dictonary as value?
input : test_dict ={'Gfg':4,'best':9},   test_list=[8,2]
Output : {8:{'Gfg':4},2:{'best':9}}
Explanation : Index-wise key value pairing from list[8] to dict {'Gfg':4} and so on.
--------------
Code :
--------------
test_dict ={'Gfg':4,'best':9}
test_list=[8,2]
d={}
for key,value in zip(test_list,test_dict.items()):
	d[key]=dict([value])

print("Output :",d)
_________________________________________________________________________
3. Sort dictonary key and value List ?
input : test_dict={'c':[3],'b':[12,10],'a':[19,4]}
Output : {'a':[4,19],'b':[10,12],'c':[3]}
input : test_dict = {'c':[10,34,3]}
Output : {'c':[3,10,34]}
-----------------------
Code :
----------------------
test_dict ={'c':[3],'b':[12,10],'a':[19,4]}
result={}

for key in sorted(test_dict): # sorted key
	result[key]=sorted(test_dict[key]) #sort the value and store dict

print('Output :',result)
_________________________________________________________________________
4. Remove all Duplicates words from a given sentence?
input : python is great and java is also great 
Output : is also java python and great
------------
Code :
-------------
str1=str(input('Enter the string element: '))
#str to list
list1=list(str1.split(' '))
#count the word
duplicate={}
for i in list1:
	if i in duplicate:
		duplicate[i]+=1 
	else:
		duplicate[i]=1
#dict to list
result=list(duplicate)
print('remove duplicate:',result)
#list to str
print('Output : ',' '.join(result))
_________________________________________________________________________
5. Inversion in nested dictonary?
input : test_dict={'a':{'b':{}},'d':{'e'{}},'f':{'g',{}}}
Output : {'b',{'a':{}},'e':{'d':{}},'g':{'f':{}}}
Explanation : nested dictonaries inverted as outer dictonary keys and viz-a-vis
----------------
Code :
----------------
_________________________________________________________________________
6. Given an array of n string containing lowercase letters. Find the size of
largest subset of string which are anagram of each others. An anagram of
a string is another string that contains same characters, only the order of
characters can be different. For example, “abcd” and “dabc” are anagram
of each other.?
input:ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3
input: cars bikes arcs steer
Output: 2
----------------
Code :
----------------
str1=str(input('Enter the string value: '))
#str to list
li=list(str1.split(' '))
#sort each word and store list
mylist=[]
for i in li:
	res=''.join(sorted(i))
	mylist.append(res)

print(mylist)
#count word
d={}
for j in mylist:
	if j in d:
		d[j]+=1
	else:
		d[j]=1
# find max value in dict
max_val=max(d.values())
print('Output: ',max_val)
_________________________________________________________________________
                                Sets
                                ----
1. Given two lists a, b. Check if two lists have at least one element common in
them.
input : a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
Output : True
input : a=[1, 2, 3, 4, 5]
b=[6, 7, 8, 9]
Output : False
-------------------
Code :
-------------------
set1=list(map(int,input('Enter the set1 element: ').strip().split()))
set2=list(map(int,input('Enter the set2 element: ').strip().split()))
for i in set1:
	if i in set2:
		count=1 
	else:
		count=0

if count!=0:
	print('True')
else:
	print('False')
_________________________________________________________________________
2. Return a new set of identical items from two sets.
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
Excepted Output : {40,50,30}
----------------
Code :
----------------
list1=list(map(int,input('Enter the set1 element: ').strip().split()))
list2=list(map(int,input('Enter the set2 element: ').strip().split()))
set1=set(list1)
set2=set(list2)
for i in set1:
	if i in set2:
		print(i,end=' ')
_________________________________________________________________________
3. Maximum and minimum in a Set without use of inbuild max/min functions?
input : set = ([8,16,24,1,25,3,10,65,55])
Output : max is 65
input : set=([4,12,10,9,4,13])
Output : min is 4
------------------
Code :
-----------------
list1=list(map(int,input('Enter the set1 element: ').strip().split()))
set1=set(list1)
print('Maximum of set is :',max(set1))
print('Minimum of set is :',min(set1))
_________________________________________________________________________
4. Write a Python program to check if a set is a subset of another set 
input : x: {'mango','apple'}
y : {'mango','orange'}
z : {'mango'}
Output : If x is subset of y 
False 
False
If y is subset of x 
False
False
If z is subset of y 
----------------------
Code :
--------------------
x = {'mango','apple'}
y = {'mango','orange'}
z = {'mango'}
for i in x:
	if i in y:
		print('True')
	else:
		print('False')

for i in y:
	if i in x:
		print('True')
	else:
		print('False')

for i in z:
	if i in y:
		print('True')
	else:
		print('False')
_________________________________________________________________________
5. Write a Python program to remove the intersection of a 2nd from the 1st set 
input:-
Original sets:
{1, 2, 3, 4, 5}
{4, 5, 6, 7, 8}
Output:-
sn1: {1, 2, 3}
sn2: {4, 5, 6, 7, 8}
------------------
Code :
------------------
list1=list(map(int,input('Enter the set1 element: ').strip().split()))
list2=list(map(int,input('Enter the set2 element: ').strip().split()))
set1=set(list1)
set2=set(list2)
print('sn1 :',set1-set2)
_________________________________________________________________________
6. What is the result of passing a dictionary to a set constructor?
    Result of passing a dictionary to a set constructor only the key is passed.
d={'a':1,'b':2,'c':3}
print(set(d))
_________________________________________________________________________
Tuple
1. Remove Tuples of Length K ?
input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
Explanation : (4, 5) of len = 2 is removed.
------------
Code :
------------

