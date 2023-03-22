import nltk

### Input
grammar = "NP: {<DT>?<JJ>*<NN>}" # TODO think up better example
input_data = "The operator launch the application gracefully."

### Processing

chunking = nltk.RegexpParser(grammar)
tokens = nltk.word_tokenize(input_data)
tags = nltk.pos_tag(tokens)
tree = chunking.parse(tags)

### Reporting
print(tree)
tree.pretty_print()
