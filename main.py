from src.common.logger import logger
from src.delivery.console.cli_runner import CliRunner

cli = CliRunner(input, print, logger)
cli.run()
