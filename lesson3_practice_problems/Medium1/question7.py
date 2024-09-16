import copy
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}
"""
def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"
    print(demo_dict)

mess_with_demographics(munsters)
"""
#Yes, the above dictionary is in shambles because the list is mutable.
#to avoid this, make a copy or in this case a deep copy to keep the original.

def mess_with_dict_copy(demo_dict):
    demo_dict_copy = copy.deepcopy(demo_dict)

    for key, value in demo_dict_copy.items():
        value["age"] += 42
        value["gender"] = "other"
    print(demo_dict_copy)

#prints the copied/changed dict
mess_with_dict_copy(munsters)
#prints original
print(munsters)
