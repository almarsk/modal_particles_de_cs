"""



input: textfile containing all matches with -grep 
output: textfile containing only matches of searched token

"""

import codecs

tok = "wohl"

with open(f"{tok}.txt", mode="r", encoding="UTF-8") as infile:
    all_tok = infile.read().split("--\n")

outfile = codecs.open(f"{tok}_match.txt", mode="wb", encoding="UTF-8")

word_list = [f"{tok}", f"{tok}.", f"{tok},", f"{tok}:", f"{tok}?", f"{tok}!",]
tok_out = []

c_tok = 0
for match in all_tok:
    tokens = match.split()
    for token in tokens:
        if token in word_list:
            c_tok += 1
            #tok_out.append(match + "--\n")
            outfile.write(match + "--\n")
print(c_tok)
outfile.close()
            



######################################

#from somajo import SoMaJo
#import re

#tokenizer = SoMaJo("de_CMC", split_camel_case=True)

#tokenlist = []
#sentences = tokenizer.tokenize_text(all_wohl)
#for sent in sentences:
#    for token in sent:
#        #print(token.text)
#        tokenlist.append(token.text)