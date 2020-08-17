"""
Open brace {
Close brace }
Open parenthesis \(
Close parenthesis \)
Semicolon ;
Int keyword int
Return keyword return
Identifier [a-zA-Z]\w*
Integer literal [0-9]+
"""

# accepts a file and returns a list of tokens
import sys, os, re, json

def lex(source_file):
    tokens = r'{}\(\);'
    s = "afaf{ } {;()()() int  2 return main sfafasf"
    keywords = [r'int', r'return', r'main']
    identifier = r'[a-zA-Z]\w*'
    intlit = r'[0-9]+'

    data = {
        "keywords": [],
        "operator": [],
        "identifier": [],
        "symbols": [],
        "intlit": []
    }
    #search for tokens
    for w in s:
        if w in tokens:
            data['symbols'].append(w)


    ax = s.split()
    for a in ax:
        isAKeyword = False
        for k in keywords:
            m = re.match(k, a)
            if m != None:
                data['keywords'].append(a)
                isAKeyword = True

        if isAKeyword == False:
            m = re.match(identifier, a)
            if m != None:
                data["identifier"].append(a)
            else:
                m = re.match(intlit, a)
                if m != None:
                    data["intlit"].append(a)
    
    return data

def main():
    try:
        source_file = open(sys.argv[1], 'r')
        tokens = lex(source_file)
        print(tokens)
    except IOError:
        print("cant open file")

if __name__=="__main__":
    main()    
