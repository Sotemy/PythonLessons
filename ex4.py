#mashin v nalichii
cars = 100

#maesta v odnoi mashine
space_in_car = 4

#voditelei online
drivers = 30

#passazhiri
passengers = 30

#kol-vo ne aktivnih mashin
cars_not_driven = cars - drivers

#kol-vo aktivnih mashin
cars_driven = drivers

#vsego mesta v nevozhdennih mashinah
car_pool_caparcity = cars_not_driven * space_in_car

#passazhirov v odnoi mashine
passengers_per_car = passengers / cars_driven

print("В наличии", cars, "автомобилей")
print("Работает :", drivers, "водителей")
print(cars_not_driven, "машин стоят")
print("можно перевезти", car_pool_caparcity, "человек")
print("Нужно отвезти", passengers, "пассажиров" )
print("В каждой машине примерно по ", passengers_per_car, "человек")