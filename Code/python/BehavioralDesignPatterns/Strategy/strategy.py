# *********************************************************************
# Strategy interface
from abc import ABC, abstractmethod
from typing import List


class SortingStrategy(ABC):
    @classmethod
    @abstractmethod
    def sort(self, data: List[int]) -> None:
        pass


# *********************************************************************
# Concrete Strategy
class BubbleSortStrategy(SortingStrategy):
    @classmethod
    def sort(self, data: List[int]):
        # TODO
        print("sort BubbleSortStrategy")
        pass


class QuickSortStrategy(SortingStrategy):
    @classmethod
    def sort(self, data):
        # TODO
        print("sort QuickSortStrategy")
        pass


class MergeSortStrategy(SortingStrategy):
    @classmethod
    def sort(self, data):
        # TODO
        print("sort MergeSortStrategy")
        pass


# *********************************************************************
# Context
class SortingContext:
    def __init__(self, sorting_strategy: SortingStrategy | None = None):
        self.sorting_strategy = sorting_strategy

    def set_sorting_strategy(self, sorting_strategy: SortingStrategy):
        self.sorting_strategy = sorting_strategy

    def perform_sort(self, data: List[int]):
        self.sorting_strategy.sort(data)


# *********************************************************************
# Client

data: List[int] = [2, 3, 5, 33, 2333, 12, 8]

sorting_context = SortingContext(BubbleSortStrategy())
sorting_context.perform_sort(data)


sorting_context = SortingContext()
sorting_context.set_sorting_strategy(QuickSortStrategy())
sorting_context.perform_sort(data)

sorting_context = SortingContext()
sorting_context.set_sorting_strategy(MergeSortStrategy())
sorting_context.perform_sort(data)
