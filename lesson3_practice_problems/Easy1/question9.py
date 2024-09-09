advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
target = 'house'
end_index = advice.find(target)
print(advice[:end_index])

#more precise way:
print(advice.split("house")[0])