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
		#名前
		self.jp_name = jp_name
		#ユーザー独自の名前
		self.rename = rename if rename != None else jp_name
		#攻撃力
		self.defense = defense
		#説明
		self.description = description
		#耐久力 0になると使用不可になる
		self.strength = strength
		#エフェクト
		if effect.get("increase_defense") and effect.get("anti_attack"):
			self.effect = effect
		else:
			self.effect = {
				"increase_defense": 0,
				"anti_attack": 0
			}

	def getDefense(self):
		"""防具による防御力計算"""
		return self.defense / 100 * self.effect["increase_defense"]

	def enchant(self, damage: int, anti: int)-> dict:
		"""エンチャントして防具を強く"""
		effect = {
			"increase_defense": self.effect["increase_defense"]+=damage,
			"anti_attack": self.effect["anti_attack"]+=anti
		}
		return self.effect = effect

	def increaseStrength(self, val: int)-> int:
		"""耐久力を増やす"""
		return self.strength += val

	def decreaseStrength(self, val: int)-> int:
		"""使用などで耐久力を減らす"""
		if (num := self.strength - val) > 0:
			return self.strength = num
		else:
			raise LostError("耐久力が足りません")

	def changeName(self, name: str)-> str:
		"""ユーザー独自の名前を変更する"""
		return self.rename = name

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



