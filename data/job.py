class Job():
    def __init__(self,
                 jobname: str,
                 hp: int,
                 mp: int,
                 defense: int,
                 attack: int,
                 can_attach_weapon=[],
                 skill=[],
                 buff={}
                 ):
        self.jobName = jobname
        self.jobHp = hp
        self.jobMp = mp
        self.jobDefense = defense
        self.jobAttack = attack
        self.jobWeapon = can_attach_weapon
        self.skill = skill
        self.buff = buff


class Knight(Job):
    def __init__(self, jobname, hp, mp, defense, attack, can_attach_weapon, skill, buff):
        super().__init__()
