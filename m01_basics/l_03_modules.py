from tabulate import tabulate#from file import function or sometimes actual data
# from l_03_create_devices import create_devices
from util.create_utils import create_devices

# --- Main program --------------------------------------------
if __name__ == '__main__':

    devices = create_devices(num_subnets=3, num_devices=3, random_ip=True)
    #we are just calling that function(create_devices) and passing
    #and passing parameters
    print("\n", tabulate(devices, headers="keys"))
