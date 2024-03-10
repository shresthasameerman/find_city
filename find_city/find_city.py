'''6. Write a function to accept a 2 parameters, 
one is the list of cities and another is the city that the user wants to search.
The function should search the city in the list of cities and return the index of the list where the city is available. 
If the city is not available, the program should return a proper message.'''

def find_city(cities,city):
    if city in cities:
        return cities.index(city)
    else:
        return f"{city} is not in the list of cities"
print(find_city(["new york","Los angeles","Chicago"],"Chicago"))
print(find_city(["london","Kathmandu","paris","TOkyo"], "Berlin"))
print(find_city([],"Sydney"))


      
    
