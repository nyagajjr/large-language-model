import re

with open('the-verdict.txt', 'r', encoding='utf-8') as file:
    raw_data = file.read()

split_data = re.split(r'([,.:;?!]|--|\s)', raw_data)
data = [item for item in split_data if item.strip()]
print(data[:200])