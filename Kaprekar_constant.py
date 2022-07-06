"""
This problem was asked by Salesforce

Difficulty level- Medium



The number 6174 is known as Kaprekar's contant, after the 
mathematician who discovered an associated property: for all four-digit numbers 
with at least two distinct digits, repeatedly applying a simple procedure 
eventually results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in 
ascending and descending order. Subtract the smaller number from the larger number.


For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174


Write a function that returns how many steps this will take for a given input N.

"""



def call_kaprekar(input_number,iteration_count):
    
    iteration_count = iteration_count + 1
    list_asc_input_number=[]
    list_desc_input_number=[] 
    larger_num=''
    smaller_num=''       
    
    b=list(str(input_number))
    

    for c in b:
        list_asc_input_number.append(int(c))
        list_desc_input_number.append(int(c))
       
    
    list_asc_input_number.sort()    
    list_desc_input_number.sort(reverse=True)    
    
    for a in list_asc_input_number:
        smaller_num = smaller_num + str(a)
    

    for b in list_desc_input_number:
        larger_num = larger_num + str(b)
    

    
    new_number = int(larger_num) - int(smaller_num)
    
    if new_number == 6174:
        print(str(larger_num) + " - " + str(smaller_num) + " = " + str(new_number))
        return iteration_count
    else:
        print(str(larger_num) + " - " + str(smaller_num) + " = " + str(new_number))
        
        if len(str(new_number)) == 4:
            iteration_count = call_kaprekar(str(new_number),iteration_count)
        else:
            new_number = ("0000"+str(new_number))[-4:]
            iteration_count = call_kaprekar(new_number,iteration_count)
        
    return iteration_count



print("\n")
input_number=2228       #Input here

if len(str(input_number))==4 and len(set(str(input_number)))!=1:
    iterations = call_kaprekar(str(input_number), 0)
else:
    iterations='Wrong input'

print("\n")
print('Steps = ' + str(iterations))







