import nltk

### Input
#grammar = "NP: {<DT>?<JJ>*<NN>}"; "VP: {<RB>*<VBZ>}"; # TODO think up better example
###  Shallow Parsing
###  https://www.commonlounge.com/chunking-shallow-parsing-understanding-text-syntax-and-structures-part-2-97d603f60c044bcd8fc98991e515e29d/

grammar = '''
    NP: {<DT>? <ADJ>* <NN>*}
    P: {<PREP>}
    V: {<VBZ*>}
    PP: {<PREP> <NN>}
    VP: {<VBZ> <NN|PREP>*} '''

# input_data = "The operator launch the application gracefully."
input_data = "The concept also aims to reduce the need for human labor, save inputs and increase production efficiency."


### Processing

chunking = nltk.RegexpParser(grammar)
tokens = nltk.word_tokenize(input_data)
tags = nltk.pos_tag(tokens)
tree = chunking.parse(tags)

### Reporting
print(tree)
tree.pretty_print()
