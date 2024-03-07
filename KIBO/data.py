# Program: Working with Data
# Author: You (with some help from Kibo)
# This program helps you make some sense out of a bunch of data.
# Follow the steps in the instructions to find the insights!

# This line stores the name of the file that contains our data
csv_file_path = 'students_study_habits.csv'

### Part 1
### Read the data
print("--- Part 1 ---")

# TODO: Copy and paste the code to read the data here
file = open(csv_file_path, mode='r')
raw_data = file.read()
lines = raw_data.splitlines()
file.close();
print(raw_data)

### Part 2
### Aggregate the Data
print("\n--- Part 2 ---")

# TODO: Copy and paste the code to aggregate the data here
study_habits_effectiveness = {}
for line in lines[1:]:
  row = line.split(",")
  habit = row[1]
  effectiveness = int(row[2])
  if habit not in study_habits_effectiveness:
    study_habits_effectiveness[habit] = {'total': 0, 'count': 0}
  study_habits_effectiveness[habit]['total'] += effectiveness
  study_habits_effectiveness[habit]['count'] += 1
print(study_habits_effectiveness)


### Part 3
### Process the Data
print("\n--- Part 3 ---")

# TODO: Copy and paste the code to process the data here
average_effectiveness = {}
for habit, data in study_habits_effectiveness.items():
  average_effectiveness[habit] = data['total'] / data['count']
sorted_habits = sorted(average_effectiveness.items(), key=lambda x: x[1], reverse=True)
print(sorted_habits)

### Part 4
### Output the Results
print("\n--- Part 4 ---")

# TODO: Copy and paste the code to output the results here
for habit, effectiveness in sorted_habits[0:3]:
  print("Study Habit: {}, Average Effectiveness: {:.2f}".format(habit, effectiveness))
