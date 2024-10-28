from physics.gas_laws import GasLaws
import argparse


class VolumeFromTemperatureCli:

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

        """
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('t2', type=float, help='temperature 2 degrees kelvin')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


