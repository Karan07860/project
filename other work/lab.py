#full_name = "James Bond"
full_name = input("Enter your full name (first last):")
 # get the first letter of the first name
first_letter = full_name[0]

#find the last name
space_index = full_name.find(" ")

last_name = full_name[space_index+1:]
initialled_name = first_letter + "." + last_name
print(initialled_name)