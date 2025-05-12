# ##Reverse the tuple###
# a=(1,2,3,4)    #tuple () braces
# b=(5,6,7,8)
# a=a[::-1]
# print(a)


# ### Access value 20 from the tuple ###
# tuple1 = ("Orange",[10, 20, 30],(5,15,25))
# print(tuple1[1][1])
# print(tuple1[2][1])
# print(tuple1[0])

####### Create a tuple with single item 50 ##########

# tuple1=(50,)
# print(tuple1)

################ Unpack the tuple into 4 variables #######
# tuple1 = (10,20,30,40)
# a=tuple1[0]
# b=tuple1[1]
# c=tuple1[2]
# d=tuple1[3]
# print(a,b,c,d)
#    #or
# a,b,c,d=tuple1
# print(a,b,c,d)

############# Swap two tuples in Python #########
# t1 = (10,20,30,40)
# t2 = (50,60,70,80)
# t1,t2=t2,t1       #swaping
# print(t1)
# print(t2)

##### Copy specific elements from one tuple to a new tuple ######
# t1 = (11,22,33,44,55,66)
# t2=(t1[3],t1[4],t1[5])
#     #or
# t2=(t1[3:6])         #from 3 to 6
# print(t2)

####  Modify the tuple ####
# t1 =(11,[22,33],44,55)
# t1[1][0]=66
# t1[1][1]=77   # only list value can be modified inside the tuple   
# print(t1)

####### Sort a tuple of tuples by 2nd item ###########
# t1=(('a',23),('b',37),('c',11),('d',29))
# t1=tuple(sorted(list(t1),key=lambda x:x[1]))   ### tuple is converted to list and then print
# print(t1)

############ Counts the number of occurrences of item 50 from a tuple ########

# my_tuple = (10, 20, 50, 40, 50, 60, 50)
# count_50 = my_tuple.count(50)
# print(f"The number 50 occurs {count_50} times in the tuple")

###### Check if all items in the tuple are the same #######
# t1=(11,11)
# a,b=t1
# if a==b:
#     print("Elements of the tuple are same ")
# else:
#     print("Elements of the tuple are not same ")


######## Reverse a list in Python ##########

# l=[1,2,3,4,5]
# l=l[::-1]
# print(l)

####### Concatenate/add two lists index-wise #######
# l1=[1,2]
# l2=[3,4]
# op=l1+l2
# print(op)

#### Turn every item of a list into its square ########

# l1=[1,2,3]
# l2=[]
# for i in l1:
#     l2.append(i*i)
# print(l2)

####### Concatenate two lists in the following order #######

# list1 = ["Hello ","take "]
# list2 = ["Dear","Sir"]
                #o/p = ["hello dear","hello sir","take dear","take sir"]
# a=list1[0]+list2[0]
# b=list1[0]+list2[1]
# c=list1[1]+list2[0]
# d=list1[1]+list2[1]
# print([a,b,c,d])

      #or
# list3=[a+b for a in list1 for b in list2]
# print(list3)

############# Iterate both lists simultaneously ############
l1= [10, 20, 30, 40]
l2= [100, 200, 300, 400]
# o/p = 10 ,400
#       20 ,300 
#       30, 200
#       40, 100
# for x,y in zip(l1,l2[::-1]):
#     print(x,y)


############# Exercise 6: Remove empty strings from the list of strings ##############
list1 = ["Mike","","Emma", "Kelly", "","Brad"]
a=list(filter("Emma", list1))
print(a)

########### Exercise 7: Add new item to list after a specified item ##############
############### Exercise 8: Extend nested list by adding the sublist ###############
################# Exercise 9: Replace list’s item with new value if found ############
################### Exercise 10: Remove all occurrences of a specific item from a list.##############