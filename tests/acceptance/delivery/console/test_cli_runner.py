from doublex import Mimic, Mock, Spy, Stub
from doublex_expects import have_been_satisfied
from expects import expect

from src.common.logger import Logger
from src.delivery.console.cli_runner import CliRunner


class TestCliRunner:
    def test_cli_runner(self) -> None:
        commands = ["command1", "command2", "exit"]
        with Stub() as _input:
            _input.input().delegates(commands)
        with Mock() as _output:
            _output.print("Hello, command1!")
            _output.print("Hello, command2!")
        logger = Mimic(Spy, Logger)
        cli = CliRunner(_input.input, _output.print, logger)  # type: ignore

        cli.run()

        expect(_output).to(have_been_satisfied)
