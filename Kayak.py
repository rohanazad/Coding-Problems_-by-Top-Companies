'''
This problem was asked by Google

Difficulty level- Hard



Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string 'kaayaak', you should return the following- 
["kaayaak", "k,aayaa,k", "k,aa,y,aa,k", "k,a,aya,a,k", 
 "k,a,a,y,aa,k", "k,aa,y,a,a,k", "k,a,a,y,a,a,k"]

'''





def split_into_two(string):
    list1=[]
    for a in range(0,len(string)-1):
          list1.append( string[:a+1] + "," + string[a+1:] )
    return list1
    



def clean_list(list1):
    
    cleansed_list = []
    
    for a in list1:
        splitted_list_by_comma = a.split(",")
        merged = ""
    
        for b in splitted_list_by_comma:
            if b != "":
                if merged != "" :
                    merged=merged+","+b   
                else:
                    merged = b
                    
        cleansed_list.append(merged)
    
    cleansed_list=list(set(cleansed_list))
    cleansed_list.sort(key=len)
    return cleansed_list
    
    


def check_palindrome(string_to_be_checked):
    if string_to_be_checked == string_to_be_checked [::-1]:
        return True
    else:
        return False
 
   
    
   
    
   
    

                
    
input_string='kaayaak'
list2=[]
list2.append(input_string)


for a in list2:
    
    if len(a.split(",")) != len(input_string): #all len is not 1
        
        element = a.split(",")
        element_index = -1
        
        for b in element:   #What part is to be splitted
            
            element_index = element_index + 1
            element_new = element
            
            
            if len(b)>1:
                
                to_be_merged_list = split_into_two (b)
                
                
                for c in to_be_merged_list:
                    d_index = -1
                    merged = ""
                    
                    for d in element:    
                        d_index = d_index + 1
                        if d_index == element_index:
                            merged=merged + "," + c
                        else:
                            merged=merged + "," + d
                    
                    list2.append(merged[1:])
                        
    
                        

cleansed_list=clean_list(list2)
       



#Check if palindrome    

palindrome_list=[]

for i in cleansed_list:
    
    i_list = i.split(",")
    
    for j in i_list:
        if check_palindrome(j)==False:
            break
    
    if check_palindrome(j)==True:
        palindrome_list.append(i)
        

print("\n")
print(palindrome_list)

    
    
    
            
    
            
            
            
            
            
            
            
            
            





