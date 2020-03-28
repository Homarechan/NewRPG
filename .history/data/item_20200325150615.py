from RpgError import LostError, UnknownTypeError


class Item():
    def __init__(name: str,  # アイテム名
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
        self.prose = prise if canBuy else None
        self.sold = sold
        self.description = description
        self.rename = rename if rename != None else name
