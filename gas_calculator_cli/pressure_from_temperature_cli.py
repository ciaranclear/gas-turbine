from physics.gas_laws import GasLaws
import argparse


class PressureFromTemperatureCli:

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
        p1, t1, t2, rsh
        """
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('t2', type=float, help='temperature 2 degrees kelvin')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


