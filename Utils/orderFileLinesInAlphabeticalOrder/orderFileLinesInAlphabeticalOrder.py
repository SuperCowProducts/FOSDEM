'''

- https://stackoverflow.com/questions/11266068/python-avoid-new-line-with-print-command

# Caveats 
(> #w)

- doesn't work with accented letters
- requires last line to be blank  


'''

shopping = open('input.txt')
lines = shopping.readlines()
lines.sort()

with open('output.txt','w',encoding='utf-8') as f:
    j=0
    for i in lines:
        print(i, file=f, end=""),
        j+=1