numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))         
print(squared)



#wap to print even num and odd num from given list of numbers

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))       #filter cmd
print("these are the even number:",even_numbers)
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("these are the odd number:",odd_numbers)
