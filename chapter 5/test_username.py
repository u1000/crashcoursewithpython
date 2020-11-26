import json
print("enter your username")
print("enter 'list´of usernames' to see list of usernames")
username = input()
def write_json(data, filename="usernames.json"):
	with open (filename, "w" ) as f:
		json.dump(data, f, indent=4)
with open("usernames.json") as json_file:
	data = json.load(json_file)
	temp = data["usernames"]
	temp2 = data["usernames_lower"]
if username is str("a"):
	print(data["usernames"])
elif username not in data["usernames"] and username.lower() not in data["usernames_lower"]:
	temp.append(username)
	temp2.append(username.lower())
	write_json(data)
	print("Account has been created")
else:
	print("This username is already taken")
