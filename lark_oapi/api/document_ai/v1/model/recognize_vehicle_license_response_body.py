# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .vehicle_license import VehicleLicense


class RecognizeVehicleLicenseResponseBody(object):
    _types = {
        "vehicle_license": VehicleLicense,
    }

    def __init__(self, d=None):
        self.vehicle_license: Optional[VehicleLicense] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecognizeVehicleLicenseResponseBodyBuilder":
        return RecognizeVehicleLicenseResponseBodyBuilder()


class RecognizeVehicleLicenseResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._recognize_vehicle_license_response_body = RecognizeVehicleLicenseResponseBody()

    def vehicle_license(self, vehicle_license: VehicleLicense) -> "RecognizeVehicleLicenseResponseBodyBuilder":
        self._recognize_vehicle_license_response_body.vehicle_license = vehicle_license
        return self

    def build(self) -> "RecognizeVehicleLicenseResponseBody":
        return self._recognize_vehicle_license_response_body