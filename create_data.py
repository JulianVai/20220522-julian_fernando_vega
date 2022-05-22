from ast import Try
import random
import json
import sys

def create_test_data(n_ex) -> list:
    """"""
    d_list = []
    for i in range(n_ex):
        d_point = {}
        d_point["HeightCm"] = random.randint(140, 210)
        d_point["WeightKg"] = random.randint(50,150)

        if random.randint(0,1) == 0:
            d_point["Gender"] = "Male"
        else:
            d_point["Gender"] = "Female"
        
        d_list.append(d_point)
    return d_list

if __name__ == "__main__":
    try: 
        sys.argv[1]
        n = int(sys.argv[1])

        if n < 0:
            print("The number of examples should be a positive number")
            sys.exit()
    except:
        ## Number of examples created by default.
        n = 4
    data = create_test_data(n)

    ## Write data to data.json
    with open('data.json', 'w') as data_o:
        json.dump(data, data_o)
