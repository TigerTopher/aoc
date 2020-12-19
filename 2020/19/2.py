import math

with open('input2') as f:
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

validMessages = set()
def parseMessage(message, parseStack, actualMessage):
    if(parseStack == [] or len(message) == 0):
        if(len(message) == 0 and parseStack == []):
            validMessages.add(actualMessage)
        return
        
    currentRules = grammar[int(parseStack.pop(0))]
    if(type(currentRules) == str):
        if(currentRules == message[0]):
            parseMessage(message[1:], parseStack, actualMessage)
        else:
            return  # Invalid
    else:
        for rule in currentRules:
            copyParseStack = parseStack[:]
            parseMessage(message, rule + parseStack, actualMessage)

for message in messages:
    parseMessage(message, [0], message)

print(len(validMessages))
