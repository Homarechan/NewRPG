class Item():
    def __init__(self, name: str, prise: int, sold: int, description: str, canBuy: bool, rename=None):
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
