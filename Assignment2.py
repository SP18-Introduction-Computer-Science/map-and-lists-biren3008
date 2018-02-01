# List and Map Biren 3008

# Create a List

number = []
number.append([1,2,3,'List','Map'])

n = number[0]
print("List : ")
print(n)

print("List Elements are")
for listElem in n :
    print(listElem)

# Create a Map

myMap = {0 : "List", 1 : "Map", 2 : "Biren_3008"}
print("Map Dictionary with Value : ")
print(myMap)

print("Keys in the Map : ")
for dictVar in myMap :
    print(dictVar)

print("Values in Map : ")
for dictVar in myMap :
    print(myMap[dictVar])

print("key" + str(dictVar)+ "value"+ str(myMap))
