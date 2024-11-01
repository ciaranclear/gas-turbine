from physics.gas_laws import GasLaws
from pprint import pprint
import argparse


class DynamicConditionsFromTotalConditionsCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        if args['command'] == 'dynamic_conditions_from_total_conditions':
            print(args)

            rsh = args['rsh']
            tt = args['tt']
            pt = args['pt']
            vt = args['vt']
            dt = args['dt']
            v = args['v']

            data = GasLaws.dynamic_conditions_from_total_conditions(rsh, tt, pt, vt, dt, v)

            pprint(data)

    def _add_parser_arguments(self):
        """

        """
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')
        self._parser.add_argument('tt', type=float, help='total temperature degrees kelvin')
        self._parser.add_argument('pt', type=float, help='total pressure pascals')
        self._parser.add_argument('vt', type=float, help='total volume meters cubed')
        self._parser.add_argument('dt', type=float, help='total density kilograms per meter cubed')
        self._parser.add_argument('v', type=float, help='velocity meters per second')
