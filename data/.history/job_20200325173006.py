from RpgError import LostError, UnknownTypeError


class Job():
    def __init__(self,
                jobname: str,
                hp: int,
                mp: int,
                defense: int,
                attack: int,
                types="",
                can_attach_weapon=[],
                skill=[],
                buff={}
                ):
        jobTypeList = ["physical", "masic"]
        if types in jobTypeList:
            self.jobType = types
        else:
            raise UnknownTypeError("JobTypes does't match any jobTypes")
        self.jobName = jobname
        self.jobHp = hp
        self.jobMp = mp
        self.jobDefense = defense
        self.jobAttack = attack
        self.jobWeapon = can_attach_weapon
        self.skill = skill
        self.buff = buff


class Knight(Job):
    def __init__(self):
        super().__init__("騎士", 60, 10, 30, 30, "physical",
                        ["wood_sword"], {}, {})


class Wizard(Job):
    def __init__(self):
        super().__init__("魔法使い", 50, 60, 10, 20, "masic",
                        ["dagger", "wood_cane"], {}, {})


class Apprentice(Job):
    def __init__(self):
        super().__init__("見習い", 50, 0, 0, 15, "physical",
                        ["wood_rod"], {}, {})
