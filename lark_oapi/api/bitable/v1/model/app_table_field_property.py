# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .app_table_field_property_option import AppTableFieldPropertyOption
from .app_field_property_auto_serial import AppFieldPropertyAutoSerial
from .app_field_property_location import AppFieldPropertyLocation
from .allowed_edit_modes import AllowedEditModes
from .rating import Rating


class AppTableFieldProperty(object):
    _types = {
        "options": List[AppTableFieldPropertyOption],
        "formatter": str,
        "date_formatter": str,
        "auto_fill": bool,
        "multiple": bool,
        "table_id": str,
        "table_name": str,
        "back_field_name": str,
        "auto_serial": AppFieldPropertyAutoSerial,
        "location": AppFieldPropertyLocation,
        "formula_expression": str,
        "allowed_edit_modes": AllowedEditModes,
        "min": float,
        "max": float,
        "range_customize": bool,
        "currency_code": str,
        "rating": Rating,
    }

    def __init__(self, d=None):
        self.options: Optional[List[AppTableFieldPropertyOption]] = None
        self.formatter: Optional[str] = None
        self.date_formatter: Optional[str] = None
        self.auto_fill: Optional[bool] = None
        self.multiple: Optional[bool] = None
        self.table_id: Optional[str] = None
        self.table_name: Optional[str] = None
        self.back_field_name: Optional[str] = None
        self.auto_serial: Optional[AppFieldPropertyAutoSerial] = None
        self.location: Optional[AppFieldPropertyLocation] = None
        self.formula_expression: Optional[str] = None
        self.allowed_edit_modes: Optional[AllowedEditModes] = None
        self.min: Optional[float] = None
        self.max: Optional[float] = None
        self.range_customize: Optional[bool] = None
        self.currency_code: Optional[str] = None
        self.rating: Optional[Rating] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppTableFieldPropertyBuilder":
        return AppTableFieldPropertyBuilder()


class AppTableFieldPropertyBuilder(object):
    def __init__(self) -> None:
        self._app_table_field_property = AppTableFieldProperty()

    def options(self, options: List[AppTableFieldPropertyOption]) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.options = options
        return self

    def formatter(self, formatter: str) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.formatter = formatter
        return self

    def date_formatter(self, date_formatter: str) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.date_formatter = date_formatter
        return self

    def auto_fill(self, auto_fill: bool) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.auto_fill = auto_fill
        return self

    def multiple(self, multiple: bool) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.multiple = multiple
        return self

    def table_id(self, table_id: str) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.table_id = table_id
        return self

    def table_name(self, table_name: str) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.table_name = table_name
        return self

    def back_field_name(self, back_field_name: str) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.back_field_name = back_field_name
        return self

    def auto_serial(self, auto_serial: AppFieldPropertyAutoSerial) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.auto_serial = auto_serial
        return self

    def location(self, location: AppFieldPropertyLocation) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.location = location
        return self

    def formula_expression(self, formula_expression: str) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.formula_expression = formula_expression
        return self

    def allowed_edit_modes(self, allowed_edit_modes: AllowedEditModes) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.allowed_edit_modes = allowed_edit_modes
        return self

    def min(self, min: float) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.min = min
        return self

    def max(self, max: float) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.max = max
        return self

    def range_customize(self, range_customize: bool) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.range_customize = range_customize
        return self

    def currency_code(self, currency_code: str) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.currency_code = currency_code
        return self

    def rating(self, rating: Rating) -> "AppTableFieldPropertyBuilder":
        self._app_table_field_property.rating = rating
        return self

    def build(self) -> "AppTableFieldProperty":
        return self._app_table_field_property
