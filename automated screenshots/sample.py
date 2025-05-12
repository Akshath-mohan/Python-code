from pydoc import text

from pyparsing import line


a="The company has multiple subsidiaries, including Amazon Web Services, providing cloud computing; Zoox, a self-driving car division; Kuiper Systems, a satellite Internet provider; and Amazon Lab126, a computer hardware R&D provider"
#split the string , make to list of words 
# iterate through the words 
# o/p = c=company,cloud
split_text=a.split()
#print(split_text)
dict={}

for word  in split_text:
    fl=word[0].lower()
    # if word.lower().startswith('c'):
    #     print(word)
    if fl not in dict:
        dict[fl]=[]
    dict[fl].append(word)

for let,word_list in dict.items():
    print(f"{let},{word_list}")
    # print(split_text)


