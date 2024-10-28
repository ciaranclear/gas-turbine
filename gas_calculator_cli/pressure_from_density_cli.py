from physics.gas_laws import GasLaws
import argparse


class PressureFromDensityCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        print(args)

    def _add_parser_arguments(self):
        """
        p1, d1, d2, rsh
        """
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meter cubed')
        self._parser.add_argument('d2', type=float, help='density 2 kilograms per meter cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


