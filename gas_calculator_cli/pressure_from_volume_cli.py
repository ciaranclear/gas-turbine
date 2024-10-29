from physics.gas_laws import GasLaws
import argparse


class PressureFromVolumeCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        print(args)

        p1 = args['p1']
        v1 = args['v1']
        v2 = args['v2']
        rsh = args['rsh']

        p2 = GasLaws.presure_from_volume(p1, v1, v2, rsh)

        print(f'P1 {p1} P2 {p2} V1 {v1} V2 {v2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        p1, v1, v2, rsh
        """
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('v2', type=float, help='volume 2 meters cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


