def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': float(number)}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readAster(line, index): #read "*"
    token = {'type': 'ASTER'}
    return token, index + 1

def readSlash(line, index): #read "/"
    token = {'type': 'SLASH'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '*':
            (token, index) = readAster(line, index)
        elif line[index] == '/':
            (token, index) = readSlash(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def evaluateas(tokens): #aster&slash
    temp = 0
    float(temp)
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'ASTER':
                temp = (tokens[index-2]['number'] * tokens[index]['number'])
                tokens[index]['number'] = temp
                tokens[index - 2]['number']= 0
                tokens[index - 1]['type'] = 'PLUS'
            elif tokens[index - 1]['type'] == 'SLASH':
                temp = (tokens[index - 2]['number'] / tokens[index]['number'])
                tokens[index]['number'] = temp
                tokens[index - 2]['number']= 0
                tokens[index - 1]['type'] = 'PLUS'
            elif tokens[index - 1]['type'] != 'PLUS' and tokens[index - 1]['type'] != 'MINUS':
                print 'Invalid syntax'
        index += 1
    return tokens

def evaluatepm(tokens): #plus&minus
    answer = 0
    #tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokensas = evaluateas(tokens)
    answer = evaluatepm(tokensas)
    print "answer = %f\n" % answer
