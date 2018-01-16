class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0


    def describe_restaurant(self):
        print('Welcome to {} Restaurant'.format(self.restaurant_name))
        print('What would you like to try from our {} cuisine?'.format(self.cuisine_type))


    def open_restaurant(self):
        print('{} Restaurant is now open'.format(self.restaurant_name))


Cafe_Mondegar=Restaurant('Cafe Mondegar','Indian American')