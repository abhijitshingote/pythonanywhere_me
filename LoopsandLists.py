# '''rad_toys=['elephant','giraffe','napkins','headphones','remotes','phones']
# for i in rad_toys:
#     print (i)

# abc=range(10)
# print(abc[10])
# '''
# pizzas=['peproni','onion','sausage'
# ,'bad pizza']
# for i in pizzas:
#     print ('i like '+ i)
# print("That's all the pizzas")

Age=int(input('What is your age?'))
while Age!='quit':
    if Age<3:
        print('Ticket is free')
        # Age=int(input('What is your age?'))
    elif 3 <= Age <= 12:
        print('Ticket is $12')
        # Age=int(input('What is your age?'))
    else:
        print('Ticket is $15')
        # Age=int(input('What is your age?'))
    Age=int(input('What is your age?'))
print('/nThank you')