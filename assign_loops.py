######### Calculate sum of all numbers from 1 to a given number ######################

# num=[0,1,2,3,4,5,6]
# start=0
# for i in num:
#     num=
#     print(num)
#     start+=1

# num=int(input("Enter the last value: "))
# total=0
# for i in range(1,num+1):
# #    total+=i    #or
#     total=total+i
# print(total)

##### Print multiplication table of a given number #########

# num=int(input("Enter the last value: "))
# for i in range(1,11):
# #    total+=i    #or
#     total=num*i
#     print(total)

############### Display numbers from a list using a loop  ################

# num=(1,2,3,4,5,6,7)
# for i in num:
#     print(i)

############ Count the total number of digits in a number #############

    
# num=78954
# num=abs(num)
# count=0
# for i in str(num):
#     count+=1
# print(count)


############### Print list in reverse order using a loop ##########

# num=[1,2,3,4,5,6,7]        ## only 1 time 
# for i in num:
#     num.reverse()
# print(num)

############### Display numbers from -10 to -1 using for loop ###############


# for i in range(-10,0):
#     print(i)

#      #or

# num=-10
# while num<0:
#     print(num)
#     num+=1


#################### Display a message “Done” after the successful execution of the for loop ########

# for i in range(0,7):
#     print(i)
#     print("done")

################## Print all prime numbers within a range ##########
# first=0
# last=15                  #### not working 
# num=0
# for i in range(first,last+1):
#     if last<first:
#         num % i == 0
#         print(i)
# print(num)

####################### Display Fibonacci series up to 10 terms ###########

# fi=0   
# m=1            #o/p=0,1,1,2,3,5,8,13  last+1
# l=1
# for i in range(10):
#     fi,l=l,fi+l 
#     print(fi)                    


############# Find the factorial of a given number ##########
num=5
factorial=1                         
for i in range(1,num+1):             #only 1 o/p
    factorial *=i
print("The factorial is",factorial)


#####################  Reverse a integer number #########

# num=98765432
# rev=int(str(num)[::-1])
# print(rev)

