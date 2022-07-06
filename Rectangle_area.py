'''
This problem was asked by Google

Difficulty level- Easy



Given two rectangles on a 2D graph, return the area of their intersection. 

If the rectangles don't intersect, return 0.



For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}


and


{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}


return 6

'''


#Inputs here

rectangle1_topleft='1,4'
rectangle1_dimension='3,3' #W,H

rectangle2_topleft='0,5'
rectangle2_dimension='4,3' #W,H

 


 

#Find coordinates

rectangle1_height_min = int(rectangle1_topleft.split(',')[1]) - int(rectangle1_dimension.split(',')[1] )
rectangle1_height_max = int(rectangle1_topleft.split(',')[1])

rectangle1_width_min = int(rectangle1_topleft.split(',')[0])
rectangle1_width_max = int(rectangle1_topleft.split(',')[0] ) + int(rectangle1_dimension.split(',')[0])

 
rectangle2_height_min = int(rectangle2_topleft.split(',')[1]) - int(rectangle2_dimension.split(',')[1] )
rectangle2_height_max = int(rectangle2_topleft.split(',')[1])

rectangle2_width_min = int(rectangle2_topleft.split(',')[0])
rectangle2_width_max = int(rectangle2_topleft.split(',')[0] ) + int(rectangle2_dimension.split(',')[0])

 

#Find x,y range to compare and find the overalp length 

rectange1_xrange = list(range (rectangle1_width_min, rectangle1_width_max + 1))
rectange1_yrange = list(range (rectangle1_height_min, rectangle1_height_max + 1))

rectange2_xrange = list(range (rectangle2_width_min, rectangle2_width_max + 1))
rectange2_yrange = list(range (rectangle2_height_min, rectangle2_height_max + 1))

 

 


#Find overlap of x and y length

x_overlap=[]

for a in rectange1_xrange:
    if a in rectange2_xrange:
        x_overlap.append(a)

    

y_overlap=[]

for a in rectange1_yrange:
    if a in rectange2_yrange:
        y_overlap.append(a)

       




#Multiply x length and y length

if len(x_overlap) in [0,1] or len(y_overlap) in [0,1]:
    overlap_area=0
else:
    overlap_area = (max(x_overlap)-min(x_overlap)) * (max(y_overlap)-min(y_overlap))

 
print("\n")
print(overlap_area)   




