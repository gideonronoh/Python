utensils = {"Fork", "Spoon", "Knife"}
dishes = {"Plate", "Cups", "Bowl"}

# Update utensils with the elements of dishes
utensils.update(dishes)

# Create the dinner_table set by taking the union of utensils and dishes
dinner_table = utensils.union(dishes)

# Print the difference between utensils and dishes for each element in dinner_table
for x in dinner_table:
    print(f"Difference for {x}: {utensils.difference(dishes)}")
print(utensils.intersection(dishes))
