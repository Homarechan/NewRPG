from RpgError import LostError


class Armor():
    def __init__(self,
                 jp_name: str,
                 description: str,
                 defense: int,
                 strength: int,
                 effect: dict,
                 rename=None,
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

    def getDefense(self):
        """防具による防御力計算"""
        if self.strength > 0:
            return self.defense / 100 * self.effect["increase_defense"]

    def enchant(self, defense: int, anti: int):
        """エンチャントして防具を強く"""
        effect = {
            "increase_defense": self.effect.get("increase_defense", 0) + defense,
            "anti_attack": self.effect.get("anti_attack", 0) + anti
        }
        self.effect = effect

    def increaseStrength(self, val: int):
        """耐久力を増やす"""
        self.strength += val

    def decreaseStrength(self, val: int):
        """使用などで耐久力を減らす"""
        if (self.strength - val) > 0:
            self.strength = (self.strength - val)
        else:
            raise LostError("耐久力が足りません")

    def changeName(self, name: str):
        """ユーザー独自の名前を変更する"""
        self.rename = name

    def status(self)-> str:
        """武器の情報"""
        txt = f"""    ╭════ [ Status ] ══════
    ╠ name : {self.jp_name}
    ╠ rename : {self.rename}
    ╠ about : {self.description}
    ╠ defense : {self.defense}
    ╠ strength : {self.strength}
    ╠ increase defense : {self.effect['increase_defense']}
    ╠ anto attack : {self.effect['anti_attack']}
    ╰════ [ status ] ══════"""
        return txt
