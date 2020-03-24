from RpgError import LostError

class Weapon():
	def __init__(self,
				 jp_name: str,
				 description: str,
				 damage: int,
				 strength: int,
				 ranges: (float, float),
				 effect: dict,
				 rename=None,
				):
		#名前
		self.jp_name = jp_name
		#ユーザー独自の名前
		self.rename = rename if rename != None else jp_name
		#攻撃力
		self.damage = damage
		#攻撃範囲
		self.ranges = ranges
		#説明
		self.description = description
		#耐久力 0になると使用不可になる
		self.strength = strength
		#エフェクト
		if (effect.get("increase_damage")) and (effect.get("anti_defense")):
			self.effect = effect
		else:
			self.effect = {
				"increase_damage": 0,
				"anti_defense": 0
			}

	def getDamage(self):
		"""武器が与えるダメージを計算
		なお、 anti_defenseは反映されない"""
		return self.damage / 100 * self.effect["increase_damage"]

	def enchant(self, damage: int, anti: int):
		"""エンチャントして武器を強く"""
		effect = {
			"increase_damage": self.effect.get("increase_damage", 0) + damage,
			"anti_defense": self.effect.get("anti_defense", 0) + anti
		}
		self.effect = effect

	def increaseStrength(self, val: int):
		"""耐久力を増やす"""
		self.strength += val

	def decreaseStrength(self, val: int):
		"""使用などで耐久力を減らす"""
		if (num := self.strength - val) > 0:
			self.strength = num
		else:
			raise LostError("耐久力が足りません")

	def changeName(self, name: str):
		"""ユーザー独自の名前を変更する"""
		self.rename = name

	def status(self):
		"""武器の情報"""
		txt = f"""    ╭════ [ Status ] ══════
	╠ name : {self.jp_name}
	╠ rename : {self.rename}
	╠ about : {self.description}
	╠ damage : {self.damage}
	╠ range : {self.ranges}
	╠ strength : {self.strength}
	╠ anti defense : {self.effect['anti_defense']}
	╠ increase damage : {self.effect['increase_damage']}
	╰════ [ status ] ══════"""
		return txt



class Dagger(Weapon):
	def __init__(self):
		super().__init__("短剣", "短い剣だよ", 30, 50, (1.0, 1.0), {})


class WooddenSword(Weapon):
	def __init__(self):
		super().__init__("木の剣", "木でできた剣だよ", 15, 30, (1.5, 1.5), {})


class WooddenRod(Weapon):
	def __init__(self):
		super().__init__("木の棒", "木でできた棒だよ", 10, 30, (1.5, 1.5), {})

