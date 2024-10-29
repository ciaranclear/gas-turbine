from physics.gas_laws import GasLaws
import argparse


class TemperatureFromVolumeCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        if args['command'] == 'temperature_from_volume':
            t1 = args['t1']
            v1 = args['v1']
            v2 = args['v2']
            rsh = args['rsh']

            t2 = GasLaws.temperature_from_volume(t1, v1, v2, rsh)

            print(f'T1 {t1} T2 {t2} V1 {v1} V2 {v2} RSH {rsh}')

    def _add_parser_arguments(self):
        """
        t1, v1, v2, rsh
        """
        self._parser.add_argument('t1', type=float, help='temperature 1 degrees kelvin')
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('v2', type=float, help='volume 2 meters cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


