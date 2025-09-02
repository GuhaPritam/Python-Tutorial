import os

name = input("What is your name? ")
age = input("Your age? ")

file_name = "user_data.txt"
with open(file_name, "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")

print("File is created", file_name)

next_year_age = int(age) + 1
print(f"Next year your age will be: {next_year_age}")

new_file_name = f"{name}_info.txt"
os.rename(file_name, new_file_name)

print("File name is changing", new_file_name)
print("Automation successful")
