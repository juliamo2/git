class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        print("start")
        yield self.__skills[0]
        print("next")
        yield self.__skills[1]


manager = SkillManager()
manager.add_skill("12")
manager.add_skill("36")
for item in manager:
    print(item)
