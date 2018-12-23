# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 09:46:33 2018

@author: Jerimiah
"""
## exercise 4 
cars = 100
space_in_a_car = 4
drivers = 30 
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("there will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have",passengers, "to carpool today.")
print ("We need to put about",average_passenger_per_car, "in each car.")

##exercise 5
