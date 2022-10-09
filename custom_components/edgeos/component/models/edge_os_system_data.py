from __future__ import annotations

from ..helpers.const import *


class EdgeOSSystemData:
    hostname: str | None
    timezone: str | None
    ntp_servers: list | None
    hardware_offload: bool | None
    ipsec_offload: bool | None
    deep_packet_inspection: bool | None
    traffic_analysis_export: bool | None
    leased_devices: int
    fw_version: str | None
    sw_version: str | None
    upgrade_available: bool
    upgrade_url: str | None
    upgrade_version: str | None
    product: str | None

    uptime: float | None
    cpu: int | None
    mem: int | None

    def __init__(self):
        self.hostname = None
        self.timezone = None
        self.ntp_servers = None
        self.hardware_offload = None
        self.ipsec_offload = None
        self.deep_packet_inspection = None
        self.traffic_analysis_export = None
        self.leased_devices = 0
        self.fw_version = None
        self.sw_version = None
        self.product = None
        self.uptime = None
        self.cpu = None
        self.mem = None
        self.upgrade_available = False
        self.upgrade_url = None
        self.upgrade_version = None

    @staticmethod
    def is_enabled(data: dict, key: str) -> bool:
        value = data.get(key, SYSTEM_DATA_DISABLED)
        is_enabled = value == SYSTEM_DATA_ENABLED

        return is_enabled

    def update_stats(self, system_stats_data: dict, discovery_data: dict):
        self.fw_version = discovery_data.get(DISCOVER_DATA_FW_VERSION)
        self.product = discovery_data.get(DISCOVER_DATA_PRODUCT)

        self.uptime = float(system_stats_data.get(SYSTEM_STATS_DATA_UPTIME, 0))
        self.cpu = int(system_stats_data.get(SYSTEM_STATS_DATA_CPU, 0))
        self.mem = int(system_stats_data.get(SYSTEM_STATS_DATA_MEM, 0))

    def to_dict(self):
        obj = {
            SYSTEM_DATA_HOSTNAME: self.hostname,
            SYSTEM_DATA_TIME_ZONE: self.timezone,
            SYSTEM_DATA_NTP: self.ntp_servers,
            SYSTEM_DATA_OFFLOAD_HW_NAT: self.hardware_offload,
            SYSTEM_DATA_TRAFFIC_ANALYSIS_DPI: self.deep_packet_inspection,
            SYSTEM_DATA_TRAFFIC_ANALYSIS_EXPORT: self.traffic_analysis_export,
            DHCP_SERVER_LEASES: self.leased_devices
        }

        return obj

    def __repr__(self):
        to_string = f"{self.to_dict()}"

        return to_string