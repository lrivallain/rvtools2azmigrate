"""Console script for rvtools2azmigrate."""
import sys
import click
import logging
from rich.logging import RichHandler

from rvtools2azmigrate import convert_rvtools_to_azmigrate


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


@cli.command()  # @cli, not @click!
@click.option(
    "-i",
    "--rvtools",
    help="RVTools input file",
    required=True,
    type=click.Path(exists=True),
)
@click.option(
    "-o", "--output", help="Ouptut file", required=True, type=click.Path(exists=False)
)
@click.option(
    "--anonymized",
    default=False,
    is_flag=True,
    help="Anonymize the output file by replacing VM names with UUIDs",
)
def convert(rvtools: str, output: str, anonymized: bool):
    """Convert RVTools file to Azure Migrate format"""
    log.info("Starting RVTools file conversion to Azure Migrate format...")
    log.debug(f"Input file: {click.format_filename(rvtools)}")
    log.debug(f"Output file: {click.format_filename(output)}")
    log.debug(f"Anonymized: {anonymized}")
    convert_rvtools_to_azmigrate(rvtools, output, anonymized)
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover