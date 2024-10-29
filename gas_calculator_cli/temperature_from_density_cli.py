from physics.gas_laws import GasLaws
import argparse


class TemperatureFromDensityCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        t1 = args['t1']
        d1 = args['d1']
        d2 = args['d2']
        rsh = args['rsh']

        t2 = GasLaws.temperature_from_density(t1, d1, d2, rsh)

        print(f'T1 {t1} T2 {t2} D1 {d1} D2 {d2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        t1, d1, d2, rsh
        """
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meter cubed')
        self._parser.add_argument('d2', type=float, help='density 2 kilograms per meter cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


