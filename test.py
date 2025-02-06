import re

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    data = file.read()

raw_data = re.split(r'([,.:;?_!"()\']|--|\s)', data) 
data = []
for i in raw_data:
    if i.strip():
        data.append(i.strip())

sorted_data = sorted(set(data))

vocabulary = {}
for index, token in enumerate(sorted_data):
    vocabulary[token] = index

#print(vocabulary)

class Tokenizer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_id = {index:token for token, index in vocabulary.items()}

    def encode(self, raw_data):
        raw_data = re.split(r'([,.:;?_!"()\']|--|\s)', raw_data) 
        data = []
        for i in raw_data:
            if i.strip():
                data.append(i.strip())
        tokens_ids = []
        for index in data:
            tokens_ids.append(vocabulary[index])
        return tokens_ids

    def decode(self, tokens_ids):
        text = " ".join([self.token_id[i] for i in tokens_ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
test = Tokenizer(vocabulary)

text = '''"It's the last he painted, you know,"'''

res = test.encode(text)

print(res)

res2 = test.decode(res)

print(res2)


