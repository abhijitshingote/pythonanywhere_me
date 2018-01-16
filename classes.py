class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    self.self_variable='self variable'
    global_adiable='global adiable'

    def describe_restaurant(self):
        print('Welcome to {} Restaurant'.format(self.restaurant_name))
        print('What would you like to try from our {} cuisine?'.format(self.cuisine_type))


    def open_restaurant(self):
        print('{} Restaurant is now open'.format(self.restaurant_name))


Cafe_Mondegar=Restaurant('Cafe Mondegar','Indian American')
print('Name is {} and serves Cuisne Type - {}'.format(Cafe_Mondegar.restaurant_name,Cafe_Mondegar.cuisine_type))

Cafe_Mondegar.describe_restaurant()
Cafe_Mondegar.open_restaurant()