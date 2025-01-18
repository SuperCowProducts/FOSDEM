### USER MODIFIABLE VARS ###


############################
"""

- https://www.w3schools.com/python/python_classes.asp

- [1aa5a72e-ecd3-4d02-b5a7-24d1a2328ea6] [Test e metodo di studio 1.pdf]

- https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given-but-i-only-pa [^1]

- https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a [^2]

- [^4] [Test e metodo di studio 1.pdf] [169854fd-0ea0-4efe-8f54-f8f5f8cb0dd1]



# #l 

- https://stackoverflow.com/questions/1538342/how-can-i-get-the-name-of-an-object [^3]

"""
class Subject:
    defaultQuestionCount = 20
    defaultTimeLimit = 50
    
    # £< when you do division it's like you're trying to find an equivalent fraction which has 1 as its denominator
    name = ""
    
    totalQuestionCount = -1.0
    defaultTimePerQuestion = -1.0
    maxTimePerQuestion = -1.0 #[^4]
    totalTimeCount = -1.0
    # [^1]
    def __init__(self, TQC, N):
        #self.name = self.__name__ #[^3]
        self.name = N
        self.totalQuestionCount = TQC
        self.defaultTimePerQuestion = self.defaultTimeLimit / self.defaultQuestionCount
        self.totalTimeCount = self.defaultTimePerQuestion*self.totalQuestionCount
        
        self.maxTimePerQuestion = self.defaultTimePerQuestion*1.2
        
        #############


        print(f"\nA new Subject called '{self.name}' was created:\n")
        print("### Time Utils (in minutes)")
        
        
        print(f"- total time available: {self.totalTimeCount}")
        print(f"- time per question (when divided equally): {self.defaultTimePerQuestion}")
        print(f"- maximum time per question (not mandatory but recommended): {self.maxTimePerQuestion}")
        
        '''
        print(f"It has the following totalQuestionCount value: {self.totalQuestionCount}")
        print(f"And the following defaultTimePerQuestion value: {self.defaultTimePerQuestion}\n")
        '''


'''
'''
with open ("input.txt", "r", encoding="utf-8") as f:
    n = f.read()
    maths = Subject(int(n), "maths")
# [^2]



"""
from pprint import pprint
pprint(vars(maths))
"""


