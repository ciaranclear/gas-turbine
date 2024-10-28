from physics.gas_laws import GasLaws
import argparse


class DensityFromPressureCli:

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
        d1, p1, p2, rsh
        """
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meters cubed')
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('p2', type=float, help='pressure 2 pascals')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')
