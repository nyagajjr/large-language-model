import re

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    data = file.read()

raw_data = re.split(r'([,.:;?_!"()\']|--|\s)', data) 
data = []
for i in raw_data:
    if i.strip():
        data.append(i.strip())

sorted_data = sorted(set(data))
sorted_data.extend(["<|endoftext|>", "<|unk|>"]) # for the unknown words and combining more documents

vocabulary = {}
for index, token in enumerate(sorted_data):
    vocabulary[token] = index

#print(len(vocabulary))

class Simple_tokenizer_v2:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_id = {index:token for token, index in vocabulary.items()}

    def encode(self, raw_data):
        raw_data = re.split(r'([,.:;?_!"()\']|--|\s)', raw_data) 

        data = []
        for i in raw_data:
            if i.strip():
                data.append(i.strip())

        fin_data = []
        for item in data:
            if item in vocabulary:
                fin_data.append(item)
            else:
                fin_data.append("<|unk|>")

        tokens_ids = [] #[self.tokens[token_id] for token_id in fin_data]
        for token_id in fin_data:
            tokens_ids.append(self.tokens[token_id])
        return tokens_ids
    

    def decode(self, tokens_ids):
        text = " ".join([self.token_id[i] for i in tokens_ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
test = Simple_tokenizer_v2(vocabulary)

#text = '''"It's the last he painted, you know,"'''

t1 = "Hello, do you like tea?"
t2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((t1,t2))
res = test.encode(text)

print(text)
print(res)

#res2 = test.decode(res)

# print(res2)


