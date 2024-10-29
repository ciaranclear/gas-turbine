from physics.gas_laws import GasLaws
import argparse


class DensityFromTemperatureCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        d1 = args['d1']
        t1 = args['t1']
        t2 = args['t2']
        rsh = args['rsh']

        d2 = GasLaws.density_from_temperature(d1, t1, t2, rsh)

        print(f'D1 {d1} D2 {d2} T1 {t1} T2 {t2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        d1, t1, t2, rsh
        """
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meter cubed')
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('t2', type=float, help='temperature 2 degrees kelvin')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


