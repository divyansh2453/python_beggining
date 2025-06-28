# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class programmer:
    company="Microsoft"
    
    def __init__(self, name, dep, lang):
        self.name=name
        self.dep=dep
        self.lang=lang
        print("the __init__ function ran")
        pass
    def printt(self):
        print(self.name,self.dep,self.lang)

divyansh= programmer("divyansh","IT","Python")
divyansh.printt()