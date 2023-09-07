# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ConnectDataSource(object):
    _types = {
        "service_url": str,
        "project_name": str,
        "display_name": str,
        "description": str,
        "icon_url": str,
        "project_description": str,
        "contact_email": str,
        "tenant_name": str,
    }

    def __init__(self, d=None):
        self.service_url: Optional[str] = None
        self.project_name: Optional[str] = None
        self.display_name: Optional[str] = None
        self.description: Optional[str] = None
        self.icon_url: Optional[str] = None
        self.project_description: Optional[str] = None
        self.contact_email: Optional[str] = None
        self.tenant_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ConnectDataSourceBuilder":
        return ConnectDataSourceBuilder()


class ConnectDataSourceBuilder(object):
    def __init__(self) -> None:
        self._connect_data_source = ConnectDataSource()

    def service_url(self, service_url: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.service_url = service_url
        return self

    def project_name(self, project_name: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.project_name = project_name
        return self

    def display_name(self, display_name: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.display_name = display_name
        return self

    def description(self, description: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.description = description
        return self

    def icon_url(self, icon_url: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.icon_url = icon_url
        return self

    def project_description(self, project_description: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.project_description = project_description
        return self

    def contact_email(self, contact_email: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.contact_email = contact_email
        return self

    def tenant_name(self, tenant_name: str) -> "ConnectDataSourceBuilder":
        self._connect_data_source.tenant_name = tenant_name
        return self

    def build(self) -> "ConnectDataSource":
        return self._connect_data_source
