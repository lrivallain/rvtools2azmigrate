# rvtools2azmigrate

Convert an [RVTools](https://www.robware.net/rvtools/) export to an [Azure Migrate CSV inventory file](https://learn.microsoft.com/en-us/azure/migrate/tutorial-discover-import).

* Free software: MIT license

# Features

* Convert an RVTools export to an Azure Migrate CSV inventory file
* Anonymize the VM data by replacing the hostname with UUIDs
* Filter powered-off VMs

# Installation

## Using `PIP`

```bash
pip install rvtools2azmigrate
```

## From sources

The sources for `rvtools2azmigrate` can be downloaded from the [`Github repo`](https://github.com/lrivallain/rvtools2azmigrate).

You can either clone the public repository:

```bash
git clone git://github.com/lrivallain/rvtools2azmigrate
```

Or download the [`tarball`](https://github.com/lrivallain/rvtools2azmigrate/tarball/master):

```bash
curl -OJL https://github.com/lrivallain/rvtools2azmigrate/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
python setup.py install
```

or

```bash
pip install .
```

# Usage

```bash
rvtools2azmigrate --help
# Output
Usage: rvtools2azmigrate [OPTIONS] COMMAND[ARGS]...

Options:
  --debug
  --help   Show this message and exit.

Commands:
  convert  Convert RVTools file to Azure Migrate format
```

## Convert RVTools file to Azure Migrate format

```bash
rvtools2azmigrate convert --help
# Output
Usage: rvtools2azmigrate convert [OPTIONS]

Convert RVTools file to Azure Migrate format

Options:
  -i, --rvtools PATH  RVTools input file  [required]
  -o, --output PATH   Ouptut file  [required]
  --anonymized        Anonymize the output file by replacing VM names with UUIDs
  --filter-off-vms    Filter the powered-off VMs
  --help              Show this message and exit.
```

### Examples

#### Anonymized

```bash
rvtools2azmigrate convert -i rvtools.xlsx -o azuremigrate.csv --anonymized
```

This will provide a CSV file to be imported in Azure Migrate manual discovery section. VMs names will be replaced by their UUID to anonymize the content of the exported file.

#### Filter off VMs

```bash
rvtools2azmigrate convert -i rvtools.xlsx -o azuremigrate.csv --filter-off-vms
```

This will provide a CSV file to be imported in Azure Migrate manual discovery section. Powered-Off VMs will not be exported to the CSV file.
