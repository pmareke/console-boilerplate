from logging import Logger
from typing import Callable


class Cli:
    def __init__(self, _in: Callable, _out: Callable, logger: Logger) -> None:
        self._in = _in
        self._out = _out
        self.logger = logger

    def run(self) -> None:
        self.logger.info("Starting CLI")
        while True:
            try:
                result = self._in()
                self._out(result)
                if result == "exit":
                    self.logger.info("Exiting CLI")
                    break
            except KeyboardInterrupt:
                self.logger.info("Exiting CLI")
                break
