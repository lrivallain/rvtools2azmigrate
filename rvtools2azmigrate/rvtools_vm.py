import logging

from rvtools2azmigrate.config import DEFAULT_OS_NAME, MIB_TO_MB_CONVERSION_FACTOR
from rvtools2azmigrate.azmigrate_vm import AzMigrateVM

log = logging.getLogger(__name__)


class RvToolsVM:
    """Class to represent a VM from the RVTools file"""

    def __init__(
        self,
        is_anonymized: bool,
        name: str,
        power_state: str,
        cores: int,
        memory: int,
        os_config: str,
        os_vmtools: str,
        storage_capacity: int,
        is_mib: bool,
        dns_name: str,
        uuid: str,
        firmware: str,
    ):
        """Init the RvToolsVM class

        Args:
            is_anonymized (bool): Does the VM needs needs to be anonymized?
            name (str): Name of the VM in RVTools report
            power_state (str): Power status of VM
            cores (int): Number of vCPU for the VM
            memory (int): Memory allocated to the VM
            os_config (str): OS name from the configuration
            os_vmtools (str): OS name from the VMware Tools
            storage_capacity (int): Storage capacity of the VM
            is_mib (bool): Is the storage in MiB ?
            dns_name (str): DNS name of the VM
            uuid (str): UUID of the VM
            firmware (str): Boot firmware of the VM
        """
        if is_anonymized:
            self.name = uuid
        else:
            self.name = name
        self.power_state = power_state
        self.cores = cores
        self.memory = memory
        if os_vmtools:
            self.os = os_vmtools
        elif os_config:
            self.os = os_config
        else:
            log.warning(f"OS not found for VM {self.name}")
            self.os = DEFAULT_OS_NAME
        if "64-bit" in self.os:
            self.architecture = "x64"
        elif "32-bit" in self.os:
            self.architecture = "x86"
        else:
            log.warning(f"Architecture not found for VM {self.name}")
            self.architecture = ""
        if is_mib:
            self.storage_capacity = int(storage_capacity / MIB_TO_MB_CONVERSION_FACTOR)
        self.storage_capacity_gb = int(storage_capacity / 1024)
        self.dns_name = dns_name
        self.uuid = uuid
        self.firmware = firmware

    def __repr__(self):
        return f"RvToolsVM({self.name}"

    def convert_to_az_migrate(self):
        """Convert the data to AzMigrateVM object"""
        return AzMigrateVM(
            server_name=self.name,
            cores=self.cores,
            memory=self.memory,
            os=self.os,
            architecture=self.architecture,
            boot_type="UEFI" if self.firmware == "efi" else "BIOS",
            disk1_size=self.storage_capacity_gb,
        )
