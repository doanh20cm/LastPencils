days = int(input())
food_cost_perday = int(input())
oneway_flight_cost = int(input())
onenight_hotel_cost = int(input())
print(oneway_flight_cost * 2 + days * food_cost_perday + (days - 1) * onenight_hotel_cost)