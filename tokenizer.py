import re

with open('the-verdict.txt', 'r', encoding='utf-8') as file:
    raw_data = file.read()

#creating tokens
split_data = re.split(r'([,.:;?_!"()\']|--|\s)', raw_data)
data = [item.strip() for item in split_data if item.strip()]
sorted_data = sorted(set(data))
#print(data[:200])

#assigning tokens ids
vocabulary = {}
for index,token in enumerate(sorted_data):
    vocabulary[token]=index

# print(vocabulary)

class simple_tokenizer_v1:
    def __init__(self, tokens):
        self.tokens = tokens

    def tokens_ids(self, raw_data):
        split_data = re.split(r'([,.:;?_!"()\']|--|\s)', raw_data)
        data = [] #[item.strip() for item in split_data if item.strip()]
        for item in split_data:
            if item.strip():
                data.append(item.strip())
        tokens_ids = [self.tokens[token_id] for token_id in data]
        return tokens_ids

tokenizer = simple_tokenizer_v1(vocabulary)
txt1 = '''"It's the last he painted, you know,"'''
token_id = tokenizer.tokens_ids(txt1)
print(token_id)
        