from abc import ABC, abstractmethod
from . import constants
import math

def single_country_filter(params):
    return [FilterBetween(attr_name, value) for attr_name, value in params.items()]

def both_country_filter(params):
    return [FilterBetween(f"a_{attr_name}", value) for attr_name, value in params["country_alpha"].items()] + \
        [FilterBetween(f"b_{attr_name}", value) for attr_name, value in params["country_beta"].items()]

def is_ignore_char(val):
    if (isinstance(val, str)):
        return val in constants.IGNORE_CHARS
    else:
        return math.isnan(val)

class Filter(ABC):

    parameters: set[str]

    @abstractmethod
    def strict_filter_row(self, row) -> bool:
        pass

    @abstractmethod
    def filter_row(self, row) -> bool:
        pass

    def row_contains_attrs(self, row):
        return self.parameters.issubset(row.keys())

    def filter(self, idict):
        return [row for row in idict if self.filter_row(row)]

class FilterBetween(Filter):

    def __init__(self, attr_name, value) -> None:
        self.attr_name = attr_name
        self.value = value
        self.min_name = FilterBetween.get_attr_min(self.attr_name)
        self.max_name = FilterBetween.get_attr_max(self.attr_name)
        self.parameters = set([self.min_name, self.max_name])

    def strict_filter_row(self, row) -> bool:
        return not self.row_contains_attrs(row) or \
            self.within(row)

    def filter_row(self, row) -> bool:
        if not self.row_contains_attrs(row):
            return True

        if is_ignore_char(self.min_name):
            return self.value <= row[self.max_name]

        elif is_ignore_char(self.max_name):
            return row[self.min_name] <= self.value

        else:
            return self.within(row)

    def within(self, row):
        return row[self.min_name] <= self.value <= row[self.max_name]
        
    @staticmethod
    def get_attr_min(attr):
        return f"{attr}_min"

    @staticmethod
    def get_attr_max(attr):
        return f"{attr}_max"

class ExactMatchFilter(Filter):
    def __init__(self, attr_name, value):
        self.attr_name = attr_name
        self.value = value
        self.parameters = set([attr_name])

    def strict_filter_row(self, row):
        return not self.row_contains_attr(row) or \
            self.value == row[self.attr_name]

    def filter_row(self, row):
        return self.strict_filter_row(row) or is_ignore_char(row[self.attr_name])
