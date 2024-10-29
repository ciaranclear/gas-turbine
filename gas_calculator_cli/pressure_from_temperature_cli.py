from physics.gas_laws import GasLaws
import argparse


class PressureFromTemperatureCli:

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
        t1 = args['t1']
        t2 = args['t2']

        p2 = GasLaws.pressure_from_temperature(p1, t1, t2, rsh)

        print(f'P1 {p1} P2 {p2} T1 {t1} T2 {t2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        p1, t1, t2, rsh
        """
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('t2', type=float, help='temperature 2 degrees kelvin')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


