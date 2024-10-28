from physics.gas_laws import GasLaws
import argparse


class TemperatureFromVolumeCli:

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
        t1, v1, v2, rsh
        """
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('v2', type=float, help='volume 2 meters cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


