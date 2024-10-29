from physics.gas_laws import GasLaws
import argparse


class VolumeFromPressureCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        if args['command'] == 'volume_from_pressure':
            v1 = args['v1']
            p1 = args['p1']
            p2 = args['p2']
            rsh = args['rsh']

            v2 = GasLaws.volume_from_pressure(v1, p1, p2, rsh)

            print(f'V1 {v1} V2 {v2} P1 {p1} P2 {p2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        v1, p1, p2, rsh
        """
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('p2', type=float, help='pressure 2 pascals')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


