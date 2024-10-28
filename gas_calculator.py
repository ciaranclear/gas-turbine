"""
01. temperature_from_presure(t1, p1, p2, rsh)

02. temperature_from_volume(t1, v1, v2, rsh)

03. temperature_from_density(t1, d1, d2, rsh)

04. volume_from_pressure(v1, p1, p2, rsh)

05. volume_from_temperature(v1, t1, t2, rsh)

06. volume_from_density(v1, d1, d2)

07. pressure_from_temperature(p1, t1, t2, rsh)

08. pressure_from_volume(p1, v1, v2, rsh)

09. pressure_from_density(p1, d1, d2, rsh)

10. density_from_temperature(d1, t1, t2, rsh)

11. density_from_pressure(d1, p1, p2, rsh)

12. density_from_volume(d1, v1, v2, rsh)

13. total_conditions_from_dynamic_conditions(rsh, v, ps, ds, ts=None, vs=None)

14. dynamic_conditions_from_total_conditions(rsh, tt, pt, vt, dt, v)

15. flow_change_of_area(a1, a2, v1, ps1, ts1, ds1, rsh)

16. speed_of_sound()

17. work_done_by_change_of_volume(p1, p2, v1, v2, rsh)

18. rotor_output_parameters()

19. stator_output_parameters()
"""

import argparse
from argparse import RawTextHelpFormatter
from physics.gas_laws import GasLaws
from gas_calculator_cli.temperature_from_pressure_cli import TemperatureFromPressureCli
from gas_calculator_cli.temperature_from_volume_cli import TemperatureFromVolumeCli
from gas_calculator_cli.temperature_from_density_cli import TemperatureFromDensityCli
from gas_calculator_cli.volume_from_pressure_cli import VolumeFromPressureCli
from gas_calculator_cli.volume_from_temperature_cli import VolumeFromTemperatureCli
from gas_calculator_cli.volume_from_density_cli import VolumeFromDensityCli
from gas_calculator_cli.pressure_from_temperature_cli import PressureFromTemperatureCli
from gas_calculator_cli.pressure_from_volume_cli import PressureFromVolumeCli
from gas_calculator_cli.pressure_from_density_cli import PressureFromDensityCli
from gas_calculator_cli.density_from_temperature_cli import DensityFromTemperatureCli
from gas_calculator_cli.density_from_pressure_cli import DensityFromPressureCli
from gas_calculator_cli.density_from_volume_cli import DensityFromVolumeCli
from gas_calculator_cli.total_conditions_from_dynamic_conditions_cli import TotalConditionsFromDynamicConditionsCli
from gas_calculator_cli.dynamic_conditions_from_total_conditions_cli import DynamicConditionsFromTotalConditionsCli
from gas_calculator_cli.flow_change_of_area_cli import FlowChangeOfAreaCli
from gas_calculator_cli.speed_of_sound_cli import SpeedOfSoundCli
from gas_calculator_cli.work_done_by_change_of_volume_cli import WorkDoneByChangeOfVolumeCli
from gas_calculator_cli.rotor_output_cli import RotorOutputCli
from gas_calculator_cli.stator_output_cli import StatorOutputCli


def gas_calculator(argv=None):

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    temperature_from_pressure = subparsers.add_parser(
        'temperature_from_pressure',
        help='get temperature from pressure')
    temperature_from_pressure_cli = TemperatureFromPressureCli(temperature_from_pressure)

    temperature_from_volume = subparsers.add_parser(
        'temperature_from_volume',
        help='get temperature from volume')
    temperature_from_volume_cli = TemperatureFromVolumeCli(temperature_from_volume)

    temperature_from_density = subparsers.add_parser(
        'temperature_from_density',
        help='get temperature from density')
    temperature_from_density_cli = TemperatureFromDensityCli(temperature_from_density)

    volume_from_pressure = subparsers.add_parser(
        'volume_from_pressure',
        help='get volume from pressure')
    volume_from_pressure_cli = VolumeFromPressureCli(volume_from_pressure)

    volume_from_temperature = subparsers.add_parser(
        'volume_from_temperature',
        help='get volume from temperature')
    volume_from_temperature_cli = VolumeFromTemperatureCli(volume_from_temperature)

    volume_from_density = subparsers.add_parser(
        'volume_from_density',
        help='get volume from density')
    volume_from_density_cli = VolumeFromDensityCli(volume_from_density)

    pressure_from_temperature = subparsers.add_parser(
        'pressure_from_temperature',
        help='get pressure from temperature')
    pressure_from_temperature_cli = PressureFromTemperatureCli(pressure_from_temperature)

    pressure_from_volume = subparsers.add_parser(
        'pressure_from_volume',
        help='get pressure from volume')
    pressure_from_volume_cli = PressureFromVolumeCli(pressure_from_volume)

    pressure_from_density = subparsers.add_parser(
        'pressure_from_density',
        help='get pressure from density')
    pressure_from_density_cli = PressureFromDensityCli(pressure_from_density)

    density_from_temperature = subparsers.add_parser(
        'density_from_temperature',
        help='get density from temperature')
    density_from_temperature_cli = DensityFromTemperatureCli(density_from_temperature)

    density_from_pressure = subparsers.add_parser(
        'density_from_pressure',
        help='get density from pressure')
    density_from_pressure_cli = DensityFromPressureCli(density_from_pressure)

    density_from_volume = subparsers.add_parser(
        'density_from_volume',
        help='get density from volume')
    density_from_volume_cli = DensityFromVolumeCli(density_from_volume)

    total_conditions_from_dynamic_conditions = subparsers.add_parser(
        'total_conditions_from_dynamic_conditions',
        help='get total conditions from dynamic conditions')
    total_conditions_from_dynamic_conditions_cli = TotalConditionsFromDynamicConditionsCli(total_conditions_from_dynamic_conditions)

    dynamic_conditions_from_total_conditions = subparsers.add_parser(
        'dynamic_conditions_from_total_conditions',
        help='get dynamic conditions from total conditions')
    dynamic_conditions_from_total_conditions_cli = DynamicConditionsFromTotalConditionsCli(dynamic_conditions_from_total_conditions)

    flow_change_of_area = subparsers.add_parser(
        'flow_change_of_area',
        help='get parameters for a change in flow area')
    flow_change_of_area_cli = FlowChangeOfAreaCli(flow_change_of_area)

    speed_of_sound = subparsers.add_parser(
        'speed_of_sound',
        help='get speed of sound')
    speed_of_sound_cli = SpeedOfSoundCli(speed_of_sound)

    work_done_by_change_of_volume = subparsers.add_parser(
        'work_done_by_change_of_volume',
        help='get work done by change of volume')
    work_done_by_change_of_volume_cli = WorkDoneByChangeOfVolumeCli(work_done_by_change_of_volume)

    rotor_output = subparsers.add_parser(
        'rotor_output',
        help='get rotor output parameters')
    rotor_output_cli = RotorOutputCli(rotor_output)

    stator_output = subparsers.add_parser(
        'stator_output',
        help='get stator output parameters')
    stator_output_cli = StatorOutputCli(stator_output)

    args = parser.parse_args(argv)
    args = vars(args)

    print(args)

    if args['command'] == 'temperature_from_pressure':
        temperature_from_pressure_cli.process_args(args)

    elif args['command'] == 'temperature_from_volume':
        temperature_from_volume_cli.process_args(args)

    elif args['command'] == 'temperature_from_density':
        temperature_from_density_cli.process_args(args)

    elif args['command'] == 'volume_from_pressure':
        volume_from_pressure_cli.process_args(args)

    elif args['command'] == 'volume_from_temperature':
        volume_from_temperature_cli.process_args(args)

    elif args['command'] == 'volume_from_density':
        volume_from_density_cli.process_args(args)

    elif args['command'] == 'presure_from_temperature':
        pressure_from_temperature_cli.process_args(args)

    elif args['command'] == 'pressure_from_volume':
        presure_from_volume_cli.process_args(args)

    elif args['command'] == 'pressure_from_density':
        pressure_from_density_cli.process_args(args)

    elif args['command'] == 'density_from_temperature':
        density_from_temperature_cli.process_args(args)

    elif args['command'] == 'density_from_pressure':
        density_from_pressure_cli.process_args(args)

    elif args['command'] == 'density_from_volume':
        density_from_volume_cli.process_args(args)

    elif args['command'] == 'total_conditions_from_dynamic_conditions':
        total_conditions_from_dynamic_conditions_cli.process_args(args)

    elif args['command'] == 'dynamic_conditions_from_total_conditions':
        dynamic_conditions_from_total_conditions_cli.process_args(args)

    elif args['command'] == 'flow_change_of_area':
        flow_change_of_area_cli.process_args(args)

    elif args['command'] == 'speed_of_sound':
        speed_of_sound_cli.process_args(args)

    elif args['command'] == 'work_done_by_change_of_volume':
        work_done_by_change_of_volume_cli.process_args(args)

    elif args['command'] == 'rotor_output':
        rotor_output_cli.process_args(args)

    elif args['command'] == 'stator_output':
        stator_output_cli.process_args(args)

    return 0


if __name__ == "__main__":
    gas_calculator()
