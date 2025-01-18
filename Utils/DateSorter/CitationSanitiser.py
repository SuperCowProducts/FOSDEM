


"""

#m

# #f

- ~~why does it seem to generate non-existant numbers?~~
 - this is because you're adding today's date to the list


# Resoconto

- https://stackoverflow.com/questions/14472795/how-do-i-sort-a-list-of-datetime-or-date-objects

- https://stackoverflow.com/questions/2803852/python-date-string-to-date-object

- https://stackoverflow.com/questions/24160831/how-to-create-an-list-of-a-specific-type-but-empty

- https://www.w3schools.com/python/gloss_python_error_handling.asp

"""
from datetime import datetime,date,timedelta



# 0. setup environment

import re

with open("code.txt", "r", encoding="utf-8") as f:
    code = f.read()

with open("input.txt", "r", encoding="utf-8") as f:
    output = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    print(output, file=f)





# 1. fetch input
#regexes = [[r'### Traduzione[\s\S]*?^### ', r'\g<0>', False], [r'^[#]{1,} ([^\n]*)', r'\1', False]]
exec(code)

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
        output = re.sub(regex, subst, output, 0, re.MULTILINE)
    else:
        output = re.findall(regex, output, re.MULTILINE)



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
        if i[2] == True:
            print(output, file=f)
            print(output)
        else: #ch make sure findall gives you match, not just empty strings > debug in regex101 
            for i in output:
                if i[0] == "":
                    print(i[1], file=f)
                else:
                    print(i[0], file=f)
                
#'''

dateList = [date.today()]
with open("output.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        print("\n=S=")
        print(line)
        print("=E=\n")
        #if str(line) != "\n": #u/i this stops it from taking empty lines in file
        if str(line) != "":
            try:
                dateList.append(datetime.strptime(line, "%d-%m-%y").date())
            finally:
                print("finally done")
        '''
        except:
            print("exception encountered, therfore skipped")
        #datetime.datetime.strptime(l, "%d%m%y").date()
        '''

with open("output.txt", "w", encoding="utf-8") as f:
    dateList.sort()
    print(dateList)
    for i in dateList:
        print(i.strftime('%d-%m-%y'),file=f)





    