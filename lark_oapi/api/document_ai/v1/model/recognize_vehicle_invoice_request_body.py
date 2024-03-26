# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class RecognizeVehicleInvoiceRequestBody(object):
    _types = {
        "file": IO[Any],
    }

    def __init__(self, d=None):
        self.file: Optional[IO[Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecognizeVehicleInvoiceRequestBodyBuilder":
        return RecognizeVehicleInvoiceRequestBodyBuilder()


class RecognizeVehicleInvoiceRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._recognize_vehicle_invoice_request_body = RecognizeVehicleInvoiceRequestBody()

    def file(self, file: IO[Any]) -> "RecognizeVehicleInvoiceRequestBodyBuilder":
        self._recognize_vehicle_invoice_request_body.file = file
        return self

    def build(self) -> "RecognizeVehicleInvoiceRequestBody":
        return self._recognize_vehicle_invoice_request_body
