from .RpgError import LostError


class Armor():
    def __init__(self,
                 jp_name: str,
                 description: str,
                 defense: int,
                 strength: int,
                 effect: dict,
                 rename: str=None,
                 ):
        # 名前
        self.jp_name = jp_name
        # ユーザー独自の名前
        self.rename = rename if rename is not None else jp_name
        # 攻撃力
        self.defense = defense
        # 説明
        self.description = description
        # 耐久力 0になると使用不可になる
        self.strength = strength
        # エフェクト
        if effect.get("increase_defense", False) and effect.get("anti_attack", False):
            self.effect = effect
        else:
            self.effect = {
                "increase_defense": 0,
                "anti_attack": 0
            }

    def get_defense(self):
        """防具による防御力計算"""
        if self.strength > 0:
            return self.defense / 100 * self.effect["increase_defense"]
        e

    def enchant(self, defense: int, anti: int):
        """エンチャントして防具を強く"""
        effect = {
            "increase_defense": self.effect.get("increase_defense", 0) + defense,
            "anti_attack": self.effect.get("anti_attack", 0) + anti
        }
        self.effect = effect

    def increase_strength(self, val: int):
        """耐久力を増やす"""
        self.strength += val

    def decrease_strength(self, val: int):
        """使用などで耐久力を減らす"""
        if (self.strength - val) > 0:
            self.strength = (self.strength - val)
        else:
            raise LostError("耐久力が足りません")

    def change_name(self, name: str):
        """ユーザー独自の名前を変更する"""
        self.rename = name

    def status(self):
        """武器の情報"""
        txt = f"""    ╭════ [ Status ] ══════
    ╠ name : {self.jp_name}
    ╠ rename : {self.rename}
    ╠ about : {self.description}
    ╠ defense : {self.defense}
    ╠ strength : {self.strength}
    ╠ increase defense : {self.effect['increase_defense']}
    ╠ anti attack : {self.effect['anti_attack']}
    ╰════ [ status ] ══════"""
        return txt


#部位ごとにいろいろつけます

class Body_armor(Armor):
    pass


class Leggings_armor(Armor):
    pass


class Boots_armor(Armor):
    pass

class Head_armor(Armor):
    pass



#初期衣装


class Poor_Head(Head_armor):
    def __init__(self, jp_name="帽子", description="粗末な帽子", defense=2, strength=10, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)


class Poor_Body(Body_armor):
    def __init__(self, jp_name="服", description="粗末な服", defense=2, strength=10, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)


class Poor_Leggings(Leggings_armor):
    def __init__(self, jp_name="ズボン", description="粗末なズボン", defense=2, strength=10, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)


class Poor_Boots(Boots_armor):
    def __init__(self, jp_name="ブーツ", description="粗末なブーツ", defense=2, strength=10, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)



#革の鎧


class Leather_Head(Head_armor):
    def __init__(self, jp_name="革の甲", description="革でできた甲", defense=10, strength=20, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)


class Leather_Body(Body_armor):
    def __init__(self, jp_name="革の鎧", description="革でできた鎧", defense=30, strength=50, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)


class Leather_Leggings(Leggings_armor):
    def __init__(self, jp_name="革の足鎧", description="革でできた足の鎧", defense=20, strength=30, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)


class Leather_Boots(Boots_armor):
    def __init__(self, jp_name="革のブーツ", description="革でできたブーツ", defense=15, strength=20, effect={}, rename=None):
        super().__init__(jp_name, description, defense, strength, effect, rename)


