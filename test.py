from physics.unit_converter_interface import unit_converter_interface
from physics.rotor_stage import RotorStage
from physics.convert_units import ConvertUnits
from pprint import pprint


if __name__ == "__main__":
    #unit_converter_interface()
    #ain, velocity, rotor_rpm, arin, arout, number_of_blades, rin_radius, rout_radius, rin_width, rout_width, ps, ds, ts, rsh

    # imperial units
    ain = 45			# degrees
    rin_inner_radius = 1.5	# feet
    rout_inner_radius = 1.5	# feet
    rin_sector_width = 0.4	# feet
    rout_sector_width = 0.4	# feet
    arin = 45			# degrees
    arout = 30			# degrees
    number_of_blades = 100	# integer
    rotor_rpm = 7000		# rotations per second
    velocity = 650		# feet per second
    ps = 14.7			# static pressure psi
    ds = 0.0765			# static density pounds per cubic feet
    ts = 273			# static temperature kelvin
    rsh = 1.4			# ratio

    # metric units
    rin_inner_radius = ConvertUnits.feet_to_meters(rin_inner_radius)
    rout_inner_radius = ConvertUnits.feet_to_meters(rout_inner_radius)
    rin_sector_width = ConvertUnits.feet_to_meters(rin_sector_width)
    rout_sector_width = ConvertUnits.feet_to_meters(rout_sector_width)
    velocity = ConvertUnits.feet_to_meters(velocity)
    ps = ConvertUnits.psi_to_pascals(ps)
    ds = ConvertUnits.pounds_to_kilograms(ds) / ConvertUnits.feet_cubed_to_meters_cubed(1)

    rs = RotorStage(ain, velocity, rotor_rpm, arin, arout, number_of_blades, rin_inner_radius, rout_inner_radius, rin_sector_width, rout_sector_width, ps, ds, ts, rsh)

    rs.solve_rotor()

    attrs = vars(rs)

    pprint(attrs)
