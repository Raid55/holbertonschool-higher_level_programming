#!/usr/bin/python3
"""
    Indenting text since the Le Monde newspapper
"""
def text_indentation(text):
    """
        Indents text at . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tmpStr = list(text)
    for x in range(0, len(tmpStr)):
        try:
            if tmpStr[x] == '.' or tmpStr[x] == '?' or tmpStr[x] == ':':
                tmpStr.insert(x + 1, '\n')
        except:
            continue

    tmpStr = "".join(tmpStr).split('\n')
    for x in tmpStr:
        print(x.strip())
        print()
