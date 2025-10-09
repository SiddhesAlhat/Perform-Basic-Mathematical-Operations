

file_name = "sidd.txt"

user_input = input("Enter some text to write to the file: ")
with open(file_name, "w") as file:
    file.write(user_input + "\n")
print("  Data written to file.")

additional_data = input("Enter additional text to append to the file: ")
with open(file_name, "a") as file:
    file.write(additional_data + "\n")
print(" Additional data appended to file.")


print("\n Final content of 'output.txt':")
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())
