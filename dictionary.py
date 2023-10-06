cars={'Japan':'Godzilla',
         'British':'Porsche',
         'German':'Volkswagon',
         'USA':'Ford'}
cars.update({'German':'Audi'})
#print(cars['Japan'])
#print(cars.keys())
#print(cars.values())
#print(cars.items())
for keys,values in cars.items():
    print(keys,values)
    #cars.pop will remove an item from the dictionary
    #cars.clear will clear everything on the dictionary.
