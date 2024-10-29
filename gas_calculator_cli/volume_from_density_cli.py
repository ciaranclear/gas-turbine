from physics.gas_laws import GasLaws
import argparse


class VolumeFromDensityCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        if args['command'] == 'volume_from_density':
            v1 = args['v1']
            d1 = args['d1']
            d2 = args['d2']
            rsh = args['rsh']

            v2 = GasLaws.volume_from_density(v1, d1, d2, rsh)

            print(f'V1 {v1} V2 {v2} D1 {d1} D2 {d2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        v1, d1, d2, rsh
        """
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meter cubed')
        self._parser.add_argument('d2', type=float, help='density 2 kilograms per meter cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


