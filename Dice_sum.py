'''
This problem was asked by Spotify

Difficulty level- Medium



Write a function, throw_dice(N, faces, total), that determines how many ways it is 
possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
'''


def throw_dice(n,faces,total):
    
    working_list=[]
    final_list=[]
    
    for a in range(1,n+1):        
        if a==1:
            working_list = list(range(1,faces+1))
        else:
            working_list = make_combinations(working_list, list(range(1,faces+1)))  
     

    for b in working_list:
        if check_sum(b, total) != False:
            final_list.append(check_sum(b, total)) 
            
        
    return final_list
    




    
    
def make_combinations(working_list,to_be_added_list):
    
    new_list=[]
    for a in to_be_added_list:
        for b in working_list:
            new_list.append(str(a) + "," + str(b))

    return new_list







def check_sum(element,total_sum):
    
    combination = list(element)
    elements_sum=0
    
    for a in combination:
        if a != ',':
            elements_sum = elements_sum + int(a)
    
    if elements_sum==total_sum:
        return element
    else:
        return False
    
    
    
    
 
df=throw_dice(3,6,7)        #Input here

print("\n")
print(df)
print("\n")
print(len(df))


