from src.common.logger import logger
from src.delivery.console.cli import Cli

cli = Cli(input, print, logger)
cli.run()
