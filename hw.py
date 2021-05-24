class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + "is russian traditional restaurant")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opened now")

class User():
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def first_name(self):
        print(self.first)
    
    def last_name(self):
        print(self.last)

okroshka = Restaurant("Okroshka", "Russian")

print(okroshka.cuisine_type)
print(okroshka.restaurant_name)

okroshka.describe_restaurant()
okroshka.open_restaurant()