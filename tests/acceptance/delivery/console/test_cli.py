from doublex import Mimic, Mock, Spy, Stub
from doublex_expects import have_been_satisfied
from expects import expect

from src.common.logger import Logger
from src.delivery.console.cli import Cli


class TestCli:
    def test_cli(self) -> None:
        commands = ["command1", "command2", "exit"]
        with Stub() as _in:
            _in.input().delegates(commands)
        with Mock() as _out:
            _out.print("Hello, command1!")
            _out.print("Hello, command2!")
        logger = Mimic(Spy, Logger)
        cli = Cli(_in.input, _out.print, logger)  # type: ignore

        cli.run()

        expect(_out).to(have_been_satisfied)
