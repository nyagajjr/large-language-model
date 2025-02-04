import re

with open('the-verdict.txt', 'r', encoding='utf-8') as file:
    raw_data = file.read()

#creating tokens
split_data = re.split(r'([,.:;?!]|--|\s)', raw_data)
data = [item for item in split_data if item.strip()]
#print(data[:200])

#assigning tokens ids
sorted_data = sorted(set(data))
vocabulary = {}
for index,token in enumerate(sorted_data):
    vocabulary[index]=token

print(vocabulary)