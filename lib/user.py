from .job import Apprentice
from .armor import (
    Poor_Head,
    Poor_Body,
    Poor_Leggings,
    Poor_Boots
)


class Adventurer():
    def __init__(self, name):
        self.userName = name
        self.item = {}
        self.job = Apprentice()
        self.armor = {
            "head": Poor_Head(),
            "body": Poor_Body(),
            "leggings": Poor_Leggings(),
            "boots": Poor_Boots()
        }
