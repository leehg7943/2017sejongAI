from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
input_text = " Today, we are launching a campaign called HeForShe. I am reaching out to you before we need your help. We want to end gender inequality and to do this, we need everyone involved. This is the first campaign of its kind at the UN. We want to try to galvanise as many men and boys as possible to be advocates for change and we don’t just want to talk about it. We want to try and make sure that it’s tangible. "

print("\nSentence Tokenizer:") 
print(sent_tokenize(input_text))


print("\nWord tokenizer : ") 
print(word_tokenize(input_text))


print("\nWord Punct Tokenizer : ") 
print(WordPunctTokenizer().tokenize(input_text))
