from physics.gas_laws import GasLaws
import argparse


class TotalConditionsFromDynamicConditionsCli:

    def __init__(self, parser):
        """

        """
        self._parser = parser
        self._add_parser_arguments()

    def process_args(self, args):
        """

        """
        rsh = args['rsh']
        v = args['v']
        ps = args['ps']
        ds = args['ds']
        ts = args['ts']
        vs = args['vs']
        print(args)
        # total_conditions_from_dynamic_conditions(rsh, v, ps, ds, ts=None, vs=None)
        data = GasLaws.total_conditions_from_dynamic_conditions(rsh, v, ps, ds, ts, vs)

        print(data)

    def _add_parser_arguments(self):
        """

        """
        self._parser.add_argument('rsh', type=float, help='ratio of specific heats')
        self._parser.add_argument('v', type=float, help='velocity in meters per second')
        self._parser.add_argument('ps', type=float, help='static pressure in pascals')
        self._parser.add_argument('ds', type=float, help='static density in kilograms per meters cubed')
        self._parser.add_argument('ts', type=float, help='static temperature in degrees kelvin')
        self._parser.add_argument('vs', type=float, help='static volume in meters cubed')

