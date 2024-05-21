"""Console script for rvtools2azmigrate."""
import sys
import click
import logging
from rich.logging import RichHandler

from rvtools2azmigrate.convert import convert_rvtools_to_azmigrate


LOG_FORMAT = "%(message)s"
log = logging.getLogger(__name__)


@click.group()
@click.option("--debug", default=False, is_flag=True)
def cli(debug):
    # Configure logging level and formating
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format=LOG_FORMAT,
        datefmt="[%X]",
        handlers=[RichHandler()],
    )
    click.echo("RVTools to Azure Migrate converter")
    log.debug(f"Debug mode is {'on' if debug else 'off'}")
    return 0


@cli.command()
@click.option(
    "-i",
    "--rvtools",
    help="RVTools input file",
    required=True,
    type=click.Path(exists=True),
)
@click.option("-o", "--output", help="Output file", required=True, type=click.Path(exists=False))
@click.option(
    "--anonymized",
    default=False,
    is_flag=True,
    help="Anonymize the output file by replacing VM names with UUIDs",
)
@click.option(
    "--filter-off-vms",
    default=False,
    is_flag=True,
    help="Filter the powered-off VMs",
)
@click.option(
    "--filter-out",
    default=[],
    multiple=True,
    help="Filter out VMs based on the provided patterns (contains + case-insensitive)",
)
def convert(rvtools: str, output: str, anonymized: bool, filter_off_vms: bool, filter_out: list[str]):
    """Convert RVTools file to Azure Migrate format"""
    log.info("Starting RVTools file conversion to Azure Migrate format...")
    log.debug(f"Input file: {click.format_filename(rvtools)}")
    log.debug(f"Output file: {click.format_filename(output)}")
    log.debug(f"Anonymized: {anonymized}")
    log.debug(f"Filter powered-off VMs: {filter_off_vms}")
    if filter_out:
        log.debug(f"Filter VMs with following patterns: {", ".join(filter_out)}")
    convert_rvtools_to_azmigrate(rvtools=rvtools, output=output, anonymized=anonymized, filter_off_vms=filter_off_vms, filter_out=filter_out)
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
