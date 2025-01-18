# [r"\\|^$\n|^[\s]+$", r"", True]
import numpy as np

'''

# Utils

-https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python

- https://stackoverflow.com/questions/25648628/why-do-python-findall-and-finditer-return-empty-matches-on-unanchored-sea


- https://stackoverflow.com/questions/4618298/randomly-mix-lines-of-3-million-line-file

- https://discuss.codecademy.com/t/can-a-dictionary-repeat-identical-keys-or-values/445983

- https://www.geeksforgeeks.org/how-to-escape-quotes-from-string-in-python/


'''

# -1. define functions
def main():
    global i
    if i[2] == True:
        print(output, file=f, end="") #https://stackoverflow.com/questions/11266068/python-avoid-new-line-with-print-command
        print(output)
    else: #ch make sure findall gives you match, not just empty strings > debug in regex101 

        print(f"========================================\n\nHere is the findall regex:\n\n {i}\n\n")
        #print(f"========================================\n\nHere is the *raw* output:\n\n {output}\n\n")
            #MODIFIED
        #print(f"========================================\n\nHere is the selected output:\n\n {output}\n\n")
        if len(i) > 3: #ch
            if isinstance(i[3], int) == True:
                for i in output:
                    print(i[j], file=f)
                    #u/ii
                    print("#", file=f)
            #""" https://docs.python.org/3/tutorial/errors.html  #f IndexError: tuple index out of range
            elif isinstance(i[3], list) == True: 
                print(f"\n\ni[3] = {i[3]}\n\n")
                for m in output:
                    print("", file=f) # this adds a newline
                    for k in i[3]:
                        print(f"\n\nm = {m}\n\n") 
                        print(m[k], file=f, end="")
                        print(m[k])
                
                # https://stackoverflow.com/questions/402504/how-to-determine-a-python-variables-type
             #"""
            
        else:
                #f
            matches = []
            for i in output:
                print(i, file=f)
                #u tmp
                #matches.append(float(i))
                exec(loopcode)
                #u/i
                print("#", file=f)
                #print(i[0], file=f)
                #print(i[1], file=f)
            print(matches)
            print(np.mean(matches))
            """#ORIGINAL
            for i in output:
                print(i, file=f)
                print(i)
            """


# 0. setup environment

import re

with open("regexdata.txt", "r", encoding="utf-8") as f:
    regexdata = f.read()

with open("loopcode.txt", "r", encoding="utf-8") as f:
    loopcode = f.read()

with open("initcode.txt", "r", encoding="utf-8") as f:
    initcode = f.read()


with open("input.txt", "r", encoding="utf-8") as f:
    output = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    print(output, file=f, end="")





# 1. fetch input
#regexes = [[r'### Traduzione[\s\S]*?^### ', r'\g<0>', False], [r'^[#]{1,} ([^\n]*)', r'\1', False]]
exec(f"regexes=[{regexdata}]")
j=0
for i in regexes:
    #ch 
    with open("output.txt", "r", encoding="utf-8") as f:
        output = f.read()
    
    # 2. process input
    
    regex = rf"{i[0]}"
    subst = rf"{i[1]}"
    print("")
    print("### CURRENT VALUES ###")
    print(f"regex: {regex}")
    print(f"subst: {subst}")
    print("")
    
    if i[2] == True:
        
        if len(i) > 3:
            if isinstance(i[3], int) == True:
            
                print(f"\n---(I'm going to repeat this {i[3]} times!)---\n")
                for x in range(0,i[3]):
                    output = re.sub(regex, subst, output, 0, re.MULTILINE)
        else:
            output = re.sub(regex, subst, output, 0, re.MULTILINE)
    else:

        output = re.findall(regex, output, re.MULTILINE)


        if len(i) > 3:
            if isinstance(i[3], int) == True:
                print(f"\n---(I'm only taking list index {i[3]} matches!)---\n")
                j = int(i[3])
            


    # 3. output result
    ''' ORIGINAL
    with open("output.txt", "w", encoding="utf-8") as f:
        if i[2] == True:
            print(output, file=f)
            print(output)
        else:
            for i in output:
                print(i, file=f)
    #'''
    #''' MODIFIED
    with open("output.txt", "w", encoding="utf-8") as f:
        main()
    if len(i) > 3:
        if i[3] == True:
            with open("tmp.txt", "w", encoding="utf-8") as f:
                    main()
                

#'''
