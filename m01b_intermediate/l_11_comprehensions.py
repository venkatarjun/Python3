device_str = "  r3-L-n7, cisco, catalyst 2960, ios , extra stupid stuff "   #string

# NON LIST COMPREHENSION WAY
device = list()  #we are crating a empty list [0,1,2,3,4]
for item in device_str.split(","): #item 0, ittem 1, item 2 etc...
    device.append(item.strip()) #remove begining and ending spaces for every item in list
print("\ndevice using for loop:\n\t\t", device)

# LIST COMPREHENSION
device = [item.strip() for item in device_str.split(",")]  #by seeing [] list
print("\ndevice using list comprehension:\n\t\t", device)

# SIMPLER LIST COMPREHENSION
device_info_list = device_str.split(",")
device = [item.strip() for item in device_info_list]
print("\ndevice using simpler list comprehension:\n\t\t", device)

# LIST COMPREHENSION WITH CONDITIONAL
device = [item.strip() for item in device_str.split(",") if "stupid" not in item]
# Logical operator in Python that will return True if the expression is False
print("\ndevice using list comprehension with conditional:\n\t\t", device)

device_info = [                     #list[] inside 
    ("name", "r3-L-n7"),          #tuple and inside are key values : 
    ("vendor", "cisco"),
    ("model", "catalyst 2960"),
    ("os", "ios"),
]

# DICT COMPREHENSION FROM LIST OF TUPLES
device = {item[0]: item[1] for item in device_info}   #{} rep dic
print("\ndevice using dict comprehension:\n\t\t", device)
print("device nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

device_info_str = "name:r3-L-n7, vendor:cisco, model:catalyst 2960, os:ios, version:12.1(T)"

# LIST THEN DICT COMPREHENSION FROM STRING
device_info_pairs = [kv_pair.split(":") for kv_pair in device_info_str.split(",")] #list
#maybe like split(",") will split each item into pair like "name:r3-L-n7","vendor:cisco"etc
#now again split that particular pair with : as 'name':'r3-L-n7' etc 
device = {item[0].strip(): item[1].strip() for item in device_info_pairs}
#this removes the spaces for each of the item
print("\ndevice using list and dict comprehension:\n\t\t", device)
print("device nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

# DICT COMPREHENSION FROM STRING
device = {item.split(":")[0].strip(): item.split(":")[1].strip() for item in device_info_str.split(",")}
#{} dict   this is some more advanced 
print("\ndevice using dict comprehension:\n\t\t", device)
print("device nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {value}")
