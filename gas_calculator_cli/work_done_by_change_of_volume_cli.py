from physics.gas_laws import GasLaws
import argparse


class WorkDoneByChangeOfVolumeCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        if args['command'] == 'work_done_by_change_of_volume':
            p1 = args['p1']
            p2 = args['p2']
            v1 = args['v1']
            v2 = args['v2']
            rsh = args['rsh']

            w = GasLaws.work_done_by_change_of_volume(p1, p2, v1, v2, rsh)

            print(f'P1 {p1} P2 {p2} V1 {v1} V2 {v2} RSH {rsh} W {w}')

    def _add_parser_arguments(self):
        """

        """
        self._parser.add_argument('p1', type=float, help='pressure 1 pascals')
        self._parser.add_argument('p2', type=float, help='pressure 2 pascals')
        self._parser.add_argument('v1', type=float, help='volume 1 meters cubed')
        self._parser.add_argument('v2', type=float, help='volume 2 meters cubed')
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')


