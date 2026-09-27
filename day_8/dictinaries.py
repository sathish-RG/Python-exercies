#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.


empty_dict={}

person={"name":"sathish","age":28,"gender":"male","skils":["python","javascript","react"],"address":{"street":"1/18 North Street","pincode":600001}}
print(len(person))
print(person["name"])
print(person["skils"][1])
print(person["address"]["pincode"])
print(person.get("ages")) # This will return None because the key "ages" does not exist in the dictionary


person["Job"]="Software Engineer"
print(person)

person["skils"].append("Node.js")
print(person.items())

print(person.values())