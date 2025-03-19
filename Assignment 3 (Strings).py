text = input("enter a string: ")
vowels = "aeiouAEIOU"

count = sum(1 for char in text if char in vowels)
print("number of vowels in the string:", count)
