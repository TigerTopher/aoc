import math

with open('input') as f:
    lines = "".join(f.readlines()).split("\n\n")

grammar_rules = lines[0].split("\n")
messages = lines[1].split("\n")

grammar = {}
# Transform grammar to dictionary
for grammar_rule in grammar_rules:
    index, rule = grammar_rule.split(": ")
    if ( "\"" in rule):
        rule = rule.lstrip("\"").rstrip("\"")
    else:
        rule = rule.split("|")
        for i in range(0, len(rule)):
            rule[i] = rule[i].lstrip(" ").rstrip(" ").split(" ")
    
    grammar[int(index)] = rule

generatedMessages = []
def parseMessage(message, parseStack=[0]):
    if(len)
    print('Message: ', message, 'Stack: ', parseStack)
    if(parseStack == []):
        return generatedMessages.append(message)

    currentRules = grammar[int(parseStack.pop(0))]
    if(type(currentRules) == str):
        parseMessage(message + currentRules, parseStack)
    else:
        for rule in currentRules:
            copyParseStack = parseStack[:]
            parseMessage(message, rule + parseStack)

count = 0
parseMessage('', [0])

for message in messages:
    count += message in generatedMessages

print(count)
