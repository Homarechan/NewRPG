class Item():
<<<<<<< HEAD
    def __init__(self,
                 name: str,  # アイテム名
                 prise: int,  # 販売される価格
                 sold: int,  # 売った時の価格
                 description: str,  # 説明
                 types: str,  # アイテム属性,
                 canBuy: bool,  # 買えるかどうか
                 rename=None  # ユーザー独自の名前
                 ):
        self.typeslist = [
            "recovery",  # 回復系アイテム
            "change",  # 変更系アイテム
            "material",  # 素材系アイテム
            "quest"  # クエスト系アイテム
        ]
        if types in self.typeslist:
            self.itemTypes = types
        else:
            raise UnknownTypeError("Doesn't match any item types")
=======
    def __init__(self, name: str, prise: int, sold: int, description: str, canBuy: bool, rename=None):
>>>>>>> 8dac46c14b71ecfad25c86ef7b7e2b37b4dadce8
        self.name = name
        self.prise = prise if canBuy else None
        self.sold = sold
        self.description = description
        self.rename = rename if rename is not None else name


class QuestItem(Item):
    def __init__(self, name: str, prise: int, sold: int, description: str, canBuy: bool, rename=None):
        super().__init__(name, prise, sold, description, canBuy, rename)


class RecoveryItem(Item):
    def __init__(self, name: str, prise: int, sold: int, description: str, canBuy: bool, rename=None):
        super().__init__(name, prise, sold, description, canBuy, rename)


class ChangeItem(Item):
    def __init__(self, name: str, prise: int, sold: int, description: str, canBuy: bool, rename=None):
        super().__init__(name, prise, sold, description, canBuy, rename)


class MaterialItem(Item):
    def __init__(self, name: str, prise: int, sold: int, description: str, canBuy: bool, rename=None):
        super().__init__(name, prise, sold, description, canBuy, rename)
