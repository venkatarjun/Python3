from l_00_inventory import inventory
import json

# CONVERT INVENTORY TO JSON AND WRITE TO FILE
with open("l_00_inventory.json", "w") as json_out:
    json_out.write(json.dumps(inventory, indent=4))
    #dumps aswe r converting form py to json
#taking that invetory data stru and dumping it to json and writing i.e saving as new file as inventory.json

# READ JSON INVENTORY FROM FILE
with open("l_00_inventory.json", "r") as json_in:
    json_inventory = json_in.read()

# PRINT JSON INVENTORY STRING
print("l_00_inventory.json file:", json_inventory)

# CONVERT JSON INVENTORY TO PYTHON, THEN CONVERT BACK TO STRING FOR PRINTING
print("\njson pretty version:")
print(json.dumps(json.loads(json_inventory), indent=4))

# COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
saved_inventory = json.loads(json_inventory)
if saved_inventory == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")
#in normal python we call 
    #dict = object
    #list = array
#just for prononucation and max all are same like we 
#we have nested loops in python as well as this json
#we can coinvert  python data to json data and vice versas
#load() is from json to python file
#dump is from python file to json file