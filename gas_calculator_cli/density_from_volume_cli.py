from physics.gas_laws import GasLaws
import argparse


class DensityFromVolumeCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        d1 = args['d1']
        v1 = args['v1']
        v2 = args['v2']
        rsh = args['rsh']

        d2 = GasLaws.density_from_volume(d1, v1, v2, rsh)

        print(f'D1 {d1} D2 {d2} V1 {v1} V2 {v2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        d1, v1, v2, rsh
        """
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meter cubed')
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('v2', type=float, help='volume 2 meters cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


