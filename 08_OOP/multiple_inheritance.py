class Teacher:
    def teaching(self):
        print("I am a Teacher")

class Researcher:
    def research(self):
        print("I am a Researcher")

class Professor(Teacher, Researcher):
    def profession(self):
        print("I am a Professor")

obj = Professor()

obj.teaching()
obj.research()
obj.profession()
