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