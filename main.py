# poetry run python -m unittest

from abc import ABC, abstractmethod
from typing import Any, Callable, List, Dict
from dataclasses import dataclass

import unittest


@dataclass
class Item:
    name: str


class IInventory(ABC):
    @abstractmethod
    def add(self, item: Item): ...

    @abstractmethod
    def remove(self, item: Item): ...

    @abstractmethod
    def get(self, name: str) -> Item: ...

    @abstractmethod
    def amount(self, name) -> bool: ...


class Inventory(IInventory):
    def __init__(self) -> None:
        self.items: List[Item] = []

    def add(self, item: Item):
        self.items.append(item)

    def remove(self, item: Item):
        self.items.remove(item)

    def get(self, name: str) -> Item:
        try:
            return list(filter(lambda item: item.name == name, self.items))[0]
        except IndexError:
            raise Exception("Not found")

    def amount(self, name: str) -> int:
        return len(list(filter(lambda item: item.name == name, self.items)))


class Icommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...


class CraftCommand(Icommand):
    def __init__(self, inventory: IInventory, name: str):
        self.inventory = inventory
        self.name = name

    def execute(self) -> None:
        ...


class TestOTUSRefactoring(unittest.TestCase):
    # @unittest.skip
    def test_craft_basic_torpedo1(self):
        # Arrange
        inventory = Inventory()
        inventory.add(Item("Steel"))
        inventory.add(Item("Chip"))
        inventory.add(Item("Fuel"))

        # Act
        inventory.remove(Item("Steel"))
        inventory.remove(Item("Chip"))
        inventory.remove(Item("Fuel"))
        inventory.add(Item("BasicTorpedo"))
        # Assert
        self.assertEquals(inventory.amount("Steel"), 0)
        self.assertEquals(inventory.amount("Chip"), 0)
        self.assertEquals(inventory.amount("Fuel"), 0)
        self.assertEquals(inventory.amount("BasicTorpedo"), 1)

    def test_craft_basic_torpedo2(self):
        # Arrange
        inventory = Inventory()
        inventory.add(Item("Steel"))
        inventory.add(Item("Chip"))
        inventory.add(Item("Fuel"))

        # Act
        CraftCommand(inventory, 'BasicTorpedo').execute()
        # Assert
        self.assertEquals(inventory.amount("Steel"), 0)
        self.assertEquals(inventory.amount("Chip"), 0)
        self.assertEquals(inventory.amount("Fuel"), 0)
        self.assertEquals(inventory.amount("BasicTorpedo"), 1)

    def test_craft_photon_torpedo1(self):
        # Arrange
        inventory = Inventory()
        inventory.add(Item("Steel"))
        inventory.add(Item("Chip"))
        inventory.add(Item("Photon"))
        inventory.add(Item("Photon"))

        # Act
        CraftCommand(inventory, 'PhotonTorpedo').execute()
        # Assert
        self.assertEquals(inventory.amount("Steel"), 0)
        self.assertEquals(inventory.amount("Chip"), 0)
        self.assertEquals(inventory.amount("Photon"), 0)
        self.assertEquals(inventory.amount("PhotonTorpedo"), 1)