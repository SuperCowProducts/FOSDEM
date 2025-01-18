"""

- https://docs.python.org/3.10/library/uuid.html
 - https://docs.python.org/3.10/library/uuid.html#uuid.uuid5

- https://stackoverflow.com/questions/20342058/which-uuid-version-to-use

- https://pypi.org/project/pyperclip/


- https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python

- https://stackoverflow.com/questions/20364396/how-to-delete-the-first-line-of-a-text-file

"""


import uuid


link = uuid.uuid4()

with open("history.txt", "a", encoding="utf-8") as f:
    print(link,file=f,end="")
    
with open("output.txt", "w", encoding="utf-8") as f:
    print(f"[{link}]",file=f,end="")

#""" delete first line #w this works

with open('history.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('history.txt', 'w') as fout:
    fout.writelines(data[1:])

#"""
