from .RpgError import UnknownTypeError


class Job:
    def __init__(self,
                 jobname: str,
                 hp: int,
                 mp: int,
                 defense: int,
                 attack: int,
                 types: str,
                 can_attach_weapon: list,
                 skill: dict,
                 buff: dict
                 ):
        jobTypeList = ["physical", "masic"]
        if types in jobTypeList:
            self.jobType = types
        else:
            raise UnknownTypeError("JobTypes does't match any jobTypes")
        self.job_ame = jobname
        self.job_hp = hp
        self.job_mp = mp
        self.job_defense = defense
        self.job_attack = attack
        self.job_weapon = can_attach_weapon
        self.skill = skill
        self.buff = buff

#TODO こっちもjob.pyのように職業覗く性ごとに分ける


class Knight(Job):
    def __init__(self, jobname="騎士", hp=60, mp=10, defense=30, attack=30,
                 types="physical", can_attach_weapon=["wood_sword"],
                 skill={}, buff={}):
        super().__init__(jobname, hp, mp, defense, attack,
                         types, can_attach_weapon, skill, buff)


class Wizard(Job):
    def __init__(self, jobname="魔法使い", hp=50, mp=60, defense=10, attack=20,
                 types="masic", can_attach_weapon=["dagger", "wood_cane"],
                 skill={}, buff={}):
        super().__init__(jobname, hp, mp, defense, attack,
                         types, can_attach_weapon, skill, buff)


class Apprentice(Job):
    def __init__(self, jobname="見習い", hp=50, mp=0, defense=0, attack=16,
                 types="physical", can_attach_weapon=["wood_rod"],
                 skill={}, buff={}):
        super().__init__(jobname, hp, mp, defense, attack,
                         types, can_attach_weapon, skill, buff)
