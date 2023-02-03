"""AzMigrateVM class definition
"""

import logging

log = logging.getLogger(__name__)


class AzMigrateVM:
    """Class to represent a VM in Azure Migrate import format"""

    def __init__(
        self, server_name: str, cores: int, memory: int, os: str, architecture: str, boot_type: str, disk1_size: int
    ):
        """Init the AzMigrateVM class

        Args:
            server_name (str): Name of the server
            cores (int): Number of CPU cores for the server
            memory (int): Memory allocated to the server (MB)
            os (str): OS name
            architecture (str): Architecture of the OS
            boot_type (str): Boot type of the server
            disk1_size (int): Disk size of the server (GB)
        """
        self.server_name = server_name
        self.cores = cores
        self.memory = memory
        self.os = os
        self.architecture = architecture
        self.boot_type = boot_type
        self.disk1_size = disk1_size

    def __repr__(self):
        return f"AzMigrateVM({self.server_name})"

    def as_csv_row(self, forced_name: str = None) -> dict:
        """Represent the current object as a CSV row for Azure Migrate import format

        Args:
            forced_name (str): Force a specific name in the data (default: None)

        Returns:
            dict: a dict representation of CSV data to use in Azure Migrate import file.
        """
        csv_data = {}
        if forced_name:
            csv_data["*Server Name"] = forced_name
        else:
            csv_data["*Server Name"] = self.server_name
        csv_data["IP addresses"] = ""
        csv_data["*Cores"] = self.cores
        csv_data["*Memory (In MB)"] = self.memory
        csv_data["*OS name"] = self.os
        csv_data["OS version"] = ""
        csv_data["OS architecture"] = self.architecture
        csv_data["CPU utilization percentage"] = ""
        csv_data["Memory utilization percentage"] = ""
        csv_data["Network adapters"] = ""
        csv_data["Network In throughput"] = ""
        csv_data["Network Out throughput"] = ""
        csv_data["Boot type"] = self.boot_type
        csv_data["Number of disks"] = ""
        csv_data["Disk 1 size (In GB)"] = self.disk1_size
        csv_data["Disk 1 read throughput (MB per second)"] = ""
        csv_data["Disk 1 write throughput (MB per second)"] = ""
        csv_data["Disk 1 read ops (operations per second)"] = ""
        csv_data["Disk 1 write ops (operations per second)"] = ""
        csv_data["Disk 2 size (In GB)"] = ""
        csv_data["Disk 2 read throughput (MB per second)"] = ""
        csv_data["Disk 2 write throughput (MB per second)"] = ""
        csv_data["Disk 2 read ops (operations per second)"] = ""
        csv_data["Disk 2 write ops (operations per second)"] = ""
        return csv_data
