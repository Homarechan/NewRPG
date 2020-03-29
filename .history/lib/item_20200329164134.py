from .RpgError import UnknownTypeError


class Item:
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
        self.name = name
        self.prise = prise if canBuy else None
        self.sold = sold
        self.description = description
        self.rename = rename if rename is not None else name


class QuestItem(Item):
    """クエストで必要になってくるアイテム(キーアイテム"""
    pass


class RecoveryItem(Item):
    """回復系アイテム"""
    pass


class ChangeItem(Item):
    """変更系に必要なアイテム"""
    pass


class MaterialItem(Item):
    """素材系アイテム"""
    def __init__(self, name: str, prise: int, sold: int,
                 description: str, canBuy: bool, rename=None):
        super().__init__(name, prise, sold, description, canBuy, rename)
