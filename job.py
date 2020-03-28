class Job():
    def __init__(self,
                 jobname: str,
                 hp: int,
                 mp: int,
                 defense: int,
                 attack: int,
                 can_attach_weapon: dict,
                 skill: dict,
                 buff: dict
                 ):
        self.jobname = jobname
        self.jobhp = hp
        self.jobmp = mp
        self.jobdefense = defense
        self.jobattack = attack
        self.can_attach_weapon = can_attach_weapon
        self.skill = skill
        self.buff = buff

class Knight(Job):
    def __init__(self):
        super().__init__("騎士", 50, 10, 30, 30, {"wood_sword": True}, {}, {})

class Wizard(Job):
    def __init__(self):
        super().__init__("魔法使い", 50, 60, 10, 20, {"dagger": True, "wood_cane": True}, {}, {})