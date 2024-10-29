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
        d1 = args['d1']
        p1 = args['p1']
        p2 = args['p2']
        rsh = args['rsh']

        d2 = GasLaws.density_from_pressure(d1, p1, p2, rsh)

        print(f'D1 {d1} D2 {d2} P1 {p1} P2 {p2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        d1, p1, p2, rsh
        """
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meters cubed')
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('p2', type=float, help='pressure 2 pascals')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')
