from physics.gas_laws import GasLaws
import argparse


class TemperatureFromPressureCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        if args['command'] == 'temperature_from_pressure':
            t1 = args['t1']
            p1 = args['p1']
            p2 = args['p2']
            rsh = args['rsh']

            t2 = GasLaws.temperature_from_pressure(t1, p1, p2, rsh)

            print(f'T1 = {t1} T2 = {t2} P1 = {p1} P2 = {p2} RSH = {rsh}')

    def _add_parser_arguments(self):
        """
        t1, p1, p2, rsh
        """
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('p2', type=float, help='pressure 2 pascals')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


