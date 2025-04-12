from logging import Logger
from typing import Callable

from src.domain.command import Command, CommandHandler
from src.infrastructure.hello.hello_client import DummyHelloClient
from src.use_cases.say_hello_command import SayHelloCommand, SayHelloCommandHandler


class Cli:
    def __init__(self, _in: Callable, _out: Callable, logger: Logger) -> None:
        self._in = _in
        self._out = _out
        self.logger = logger

    def run(self) -> None:
        self.logger.info("Starting CLI")
        while True:
            try:
                _input = self._in()
                if _input == "exit":
                    self.logger.info("Exiting CLI")
                    break
                command = self._parse_command(_input)
                command_handler = self._parse_handler(_input)
                response = command_handler.execute(command)
                result = response.message()
                self._out(result)
            except KeyboardInterrupt:
                self.logger.info("Exiting CLI")
                break

    def _parse_command(self, _input: str) -> Command:
        return SayHelloCommand(_input)

    def _parse_handler(self, _input: str) -> CommandHandler:
        hello_client = DummyHelloClient()
        return SayHelloCommandHandler(hello_client)
