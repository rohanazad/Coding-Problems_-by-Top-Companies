'''
This problem was asked by Apple

Difficulty level- Easy



A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

'''



# Printing the Collatz sequence for a given number

num=1100
list=[]

list.append(num)        

while (num!=1):
    if num%2==0:
        list.append(int(num/2))
        num=num/2
    else:
        list.append(int(3*num+1))
        num=3*num+1


print(list)
print('Length of sequence is- ' + str(len(list)))







