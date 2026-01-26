prev_num = 0
for i in range(1,11):
    #print(i)
    sum = prev_num+i
    #print("current number is " + str(i) + "prev_number is " +str (prev_num ) + "sum is " +str(sum))
    prev_num = i
########syntax### Print the even index, range (start index, stop index and step)
#word =input("enter a word")
#size = len(word)
#print("the length of word is " + str(size))
#for i in range(0,size-1, 2):
    #print(word[i])
###print even index using slicing
""" word1 =input("enter a word")
x = list(word1)
for i in x[0::2]:
    print (i) """

###########remove first n characters from a string
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
######################Check if the first and last numbers of a list are the same
print("##############################Next problem#########################################################################")
def first_last_num_same(numberList):
    print("Given List" + str(numberList))
    firstNum = numberList[0]
    lastNum = numberList[0]
    if(firstNum ==numberList):
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print("the first list is: " + str(first_last_num_same(numbers_x)))
#print("the first list is: " + first_last_num_same(numbers_y))
print("##############################Next problem#########################################################################")
def divisibleByFive(numberList):
    for i in numberList:
        if i%5 == 0:
            print(i)
num_list = [10, 20, 33, 46, 55]
print("the numbers divisible for 5 are" +str(divisibleByFive(num_list)) )
print("##############################Next problem#########################################################################")
#Find the number of occurrences of a substring in a string
def findTheWord(word):
    count= 0
    for i in range(len(word)-1):
        count += word[i: i+4] == 'Emma'
    return count
count =   findTheWord("Emma is good developer. Emma is a writer")    
print("emma appeared" + str(count) )
#################Print the following pattern#######################
for num in range(10):
    for i in range(num):
        print (num, end=" ") # print number
    # new line after each row to display pattern correctly
    print("\n")
######################    Check Palindrome Number#########################
def is_palindrome(number):
    if number < 0:
        return False

    original_string = str(number)
    print(original_string)
    reversed_string = original_string[::-1]##### This is used to get the reverse of string using negative step
    if original_string == reversed_string:
        return True
    else:
        return False

# Example usage:
print(is_palindrome(121))   # Output: True
print(is_palindrome(123))   # Output: False
#################### Merge two lists using the following condition
def firstOddSecondEven(list1,list2):
    list3 = []
    for num in list1:
        if num %2!= 0:
            print(num)
            list3.append(num)
    for num1 in list2:
       if num1 % 2== 0:
            print(num)
            list3.append(num1)
    return list3
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("the result ofr list3 is  " + str(firstOddSecondEven(list1,list2)))

    
