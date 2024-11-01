from physics.gas_laws import GasLaws
import argparse
from pprint import pprint


class FlowChangeOfAreaCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        if args['command'] == 'flow_change_of_area':
            v1 = args['v1']
            d1 = args['d1']
            ps1 = args['ps1']
            a1 = args['a1']
            a2 = args['a2']
            rsh = args['rsh']
            data = GasLaws.flow_change_of_area(a1, a2, v1, ps1, d1, rsh)
            #data = GasLaws.flow_change_of_area(v1, d1, ps1, a1, a2, rsh)

            pprint(data)

    def _add_parser_arguments(self):
        """

        """
        self._parser.add_argument('v1', type=float, help='velocity 1 meters per second')
        self._parser.add_argument('a1', type=float, help='area 1 meters squared')
        self._parser.add_argument('a2', type=float, help='area 2 meters squared')
        self._parser.add_argument('d1', type=float, help='density 1 kilograms per meter cubed')
        self._parser.add_argument('ps1', type=float, help='pressure 2 pascals')
        self._parser.add_argument('rsh', type=float, help='pressure 2 pascals')
