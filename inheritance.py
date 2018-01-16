from Restaurantclass import Restaurant

abhi=Restaurant('resty-name','kerala')


""" Create Child Class """
class RestaurantClass_detailed(Restaurant):

    def __init__(self,restaurant_name,cuisine_type,hours,*members):
        super().__init__(restaurant_name,cuisine_type)
        self.hours=hours
        self.members=members

    def describe_restaurant(self):
        print('This is {}  Restaurant and the food is awesome!!!! We are open {}'.format(self.restaurant_name,self.hours))

    def print_members(self):
        print('Members at {} :'.format(self.restaurant_name))
        for member in self.members:
            print(member.title())

    def add_members(self,*new_mems):
        # self.new_mems=new_mems
        self.members=self.members + new_mems


josie_rest=RestaurantClass_detailed('Josie Pizza','Italian','6pm onwards','Abhijit','Radhika','Shri','Ani')
josie_rest.describe_restaurant()
josie_rest.print_members()
josie_rest.add_members('Aniket','Anishka','nisha')
josie_rest.print_members()