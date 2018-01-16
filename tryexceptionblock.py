try:
    num1=int(input('Enter 1st number'))
    num2=int(input('Enter 2nd number'))
except ValueError:
    print('Enter numbers only!')
    num1=int(input('Enter 1st number'))
    num2=int(input('Enter 2nd number'))
else:
    pass
sum=num1+num2
print('The sum is ' + str(sum))