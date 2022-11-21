file_path = input().split("\\")
current_file = file_path[-1]
file_name, file_extension = current_file.split(".")
print(f"File name: {file_name}\nFile extension: {file_extension}")
