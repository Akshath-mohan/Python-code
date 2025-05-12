def rev(n):
        rev=0
        while n > 0:
         r=n%10
         rev=rev*10+r
         n=n//10
        return rev
print(rev(10023))

# def stri(a):
#     # return a[::-1]
    
# print(stri("a k s h a t h a"))