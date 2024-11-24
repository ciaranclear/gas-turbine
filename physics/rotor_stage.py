"""

CALCULATIONS

dpr = 360 / number of rotor blades

Ainnormal = ((dpr/360) * Pi * (rotor inlet radius + rotor inlet sector width) ** 2) - ((dpr/360) * Pi * (rotor inlet inner radius) ** 2)

Ain = cos(arin) * Ainnormal

AoA = (90 - arin) - a2

EAin = cos(arin + AoA) * Ainnormal -> where AoA > 0

EAin = Ainnormal / cos(arin + AoA) -> where AoA < 0

W = F * S

T = F * S

1 joule = 0.0013404825737265

PROCESS STEPS

1. rin sector velocity.
2. rout sector velocity.
3. rin blade spacing.
4. rout blade spacing.
5. rin area normal to the axial direction.
6. rout area normal to the axial direction.
7. calculate a2.
8. calculate a3.
9. calculate v3.
10. angle of attack.
11. effective rin area.
12. v4 total conditions.
13. calculate a6.
14. v6 total conditions.
15. vinaxial.
16. voutaxial.
17. work done.
18. torque.
"""

from physics.gas_laws import GasLaws
import math
from pprint import pprint


class RotorStage:

    def __init__(self, ain, velocity, rotor_rpm, arin, arout, number_of_blades, rin_radius, rout_radius, rin_width, rout_width, ps, ds, ts, rsh):
        """
        ain: angle in range +90 to -90 degrees.
        v1 velocity: meters per second.
        rpm: revolutions per minute.
        arin: rotor in angle in range 0 to 90 degrees.
        arout: rotor out angle in range 0 to 90 degrees.
        number of blades: number of rotor blades in stage.
        rin inner radius: inner radius of rotor inlet in meters.
        rout inner radius: inner radius of rotor outlet in meters.
        rin sector width: sector width of rotor inlet in meters.
        rout sector width: sector width of rotor outlet in meters.
        v1 ps: static pressure of rotor inlet stream in pascals.
        v1 ds: static density of rotor inlet stream in kilograms per meter cubed.
        v1 ts: static temperature of rotor inlet stream in kelvin.
        rsh: ratio of specific heats (no units).
        """
        self.ain = ain
        self.a1 = None
        self.a2 = None
        self.a3 = None
        self.a4 = None
        self.a5 = None
        self.a6 = None
        self.v1_velocity = velocity
        self.v2_velocity = None
        self.v3_velocity = None
        self.v4_velocity = None
        self.v5_velocity = None
        self.v6_velocity = None
        self.vinaxial = None
        self.voutaxial = None
        self.v1_ps = ps
        self.v3_ps = None
        self.v4_ps = None
        self.v6_ps = None
        self.v1_pt = None
        self.v3_pt = None
        self.v4_pt = None
        self.v6_pt = None
        self.v1_ts = ts
        self.v3_ts = None
        self.v4_ts = None
        self.v6_ts = None
        self.v1_tt = None
        self.v3_tt = None
        self.v4_tt = None
        self.v6_tt = None
        self.v1_ds = ds
        self.v3_ds = None
        self.v4_ds = None
        self.v6_ds = None
        self.v1_dt = None
        self.v3_dt = None
        self.v4_dt = None
        self.v6_dt = None
        self.ainnormal = None
        self.ain_actual = None
        self.ain_effective = None
        self.aoutnormal = None
        self.aout_actual = None
        self.arin = arin
        self.arout = arout
        self.rpm = rotor_rpm
        self.rin_inner_radius = rin_radius
        self.rin_sector_width = rin_width
        self.rout_inner_radius = rout_radius
        self.rout_sector_width = rout_width
        self.number_of_blades = number_of_blades
        self.rotor_blade_spacing = None
        self.angle_of_attack = None
        self.rsh = rsh

    def solve_rotor(self):
        """

        """
        self._vinaxial()
        self._rotor_blade_spacing()
        self._v2_velocity()
        self._calculate_a3()
        self._calculate_a1()
        self._v3_velocity()
        self._angle_of_attack()
        self._normal_rin_area()
        self._actual_rin_area()
        self._effective_rin_area()
        self._v1_total_conditions()
        self._v3_total_conditions()
        self._v5_velocity()
        self._normal_rout_area()
        self._actual_rout_area()
        return
        self._v4_total_conditions()
        self._calculate_a6()
        """
        self._voutaxial()
        self._calculate_a4()
        self._v6_velocity()
        self._v6_total_conditions()
        self._work_done()
        """

    def rotor_data(self):
        """

        """
        pass

    def __str__(self):
        """

        """
        return (
            f"ain {self.ain}\n"
            f"a1 {self.a1}\n"
            f"a2 {self.a2}\n"
            f"a3 {self.a3}\n"
            f"a4 {self.a4}\n"
            f"a5 {self.a5}\n"
            f"a6 {self.a6}\n"
            f"v1 velocity {self.v1_velocity}\n"
            f"v2 velocity {self.v2_velocity}\n"
            f"v3 velocity {self.v3_velocity}\n"
            f"v4 velocity {self.v4_velocity}\n"
            f"v5 velocity {self.v5_velocity}\n"
            f"v6 velocity {self.v6_velocity}\n"
            f"vinaxial {self.vinaxial}\n"
            f"voutaxial {self.voutaxial}\n"
            f"v1 ps {self.v1_ps}\n"
            f"v3 ps {self.v3_ps}\n"
            f"v4 ps {self.v4_ps}\n"
            f"v6 ps {self.v6_ps}\n"
            f"v1 pt {self.v1_pt}\n"
            f"v3 pt {self.v3_pt}\n"
            f"v4 pt {self.v4_pt}\n"
            f"v6 pt {self.v6_pt}\n"
            f"v1 ts {self.v1_ts}\n"
            f"v3 ts {self.v3_ts}\n"
            f"v4 ts {self.v4_ts}\n"
            f"v6 ts {self.v6_ts}\n"
            f"v1 tt {self.v1_tt}\n"
            f"v3 tt {self.v3_tt}\n"
            f"v4 tt {self.v4_tt}\n"
            f"v6 tt {self.v6_tt}\n"
            f"v1 ds {self.v1_ds}\n"
            f"v3 ds {self.v3_ds}\n"
            f"v4 ds {self.v4_ds}\n"
            f"v6 ds {self.v6_ds}\n"
            f"v1 dt {self.v1_dt}\n"
            f"v3 dt {self.v3_dt}\n"
            f"v4 dt {self.v4_dt}\n"
            f"v6 dt {self.v6_dt}\n"
            f"ainnormal {self.ainnormal}\n"
            f"ain actual {self.ain_actual}\n"
            f"ain effective {self.ain_effective}\n"
            f"aout normal {self.aoutnormal}\n"
            f"aout actual {self.aout_actual}\n"
            f"arin {self.arin}\n"
            f"arout {self.arout}\n"
            f"rpm {self.rpm}\n"
            f"rin inner radius {self.rin_inner_radius}\n"
            f"rin sector width {self.rin_sector_width}\n"
            f"rout inner radius {self.rout_inner_radius}\n"
            f"rout sector width {self.rout_sector_width}\n"
            f"number of blades {self.number_of_blades}\n"
            f"rotor blade spacing {self.rotor_blade_spacing}\n"
            f"angle of attack {self.angle_of_attack}\n"
            f"rsh {self.rsh}\n")

    def _v1_total_conditions(self):
        """

        """
        # total_conditions_from_dynamic_conditions(rsh, v, ps, ds, ts=None, vs=None)
        data = GasLaws.total_conditions_from_dynamic_conditions(self.rsh, self.v1_velocity, self.v1_ps, self.v1_ds, self.v1_ts)
        print("V1 DATA")
        pprint(data)

    def _v3_total_conditions(self):
        """

        """
        pass

    def _v4_total_conditions(self):
        """

        """
        # flow_change_of_area(a1, a2, v1, ps1, d1, rsh)
        data = GasLaws.flow_change_of_area(self.ain_effective, self.aout_actual, self.v3_velocity, self.v3_ps, self.v3_ds, self.rsh)
        pprint(data)

    def _v6_total_conditions(self):
        """

        """
        pass

    def _rotor_blade_spacing(self):
        """

        """
        self.rotor_blade_spacing = 360 / self.number_of_blades

    def _normal_rin_area(self):
        """

        """
        self.ainnormal = ((self.rotor_blade_spacing / 360) * math.pi * (self.rin_inner_radius + self.rin_sector_width)**2) - ((self.rotor_blade_spacing / 360) * math.pi * (self.rin_inner_radius)**2)

    def _actual_rin_area(self):
        """

        """
        self.ain_actual = math.cos(math.radians(self.arin)) * self.ainnormal

    def _normal_rout_area(self):
        """

        """
        self.aoutnormal = ((self.rotor_blade_spacing / 360) * math.pi * (self.rout_inner_radius + self.rout_sector_width)**2) - ((self.rotor_blade_spacing / 360) * math.pi * (self.rout_inner_radius)**2)

    def _actual_rout_area(self):
        """

        """
        self.aout_actual = math.cos(math.radians(self.arout)) * self.aoutnormal

    def _effective_rin_area(self):
        """

        """
        if self.angle_of_attack >= 0:
            self.ain_effective = math.cos(math.radians(self.arin + self.angle_of_attack)) * self.ainnormal
        elif self.angle_of_attack < 0:
            self.ain_effective = self.ainnormal / math.cos(math.radians(self.arin + self.angle_of_attack))

    def _v2_velocity(self):
        """

        """
        c = 2 * math.pi * (self.rin_inner_radius + (self.rin_sector_width/2))

        self.v2_velocity = (c * self.rpm) / 60

    def _v3_velocity(self):
        """
        use rinaxial velocity,
        """
        self.v3_velocity = ((self.v1_velocity**2) + (self.v2_velocity**2) - (2 * self.v1_velocity * self.v2_velocity * math.cos(math.radians(self.a3))))**0.5

    def _v5_velocity(self):
        """

        """
        c = 2 * math.pi * (self.rout_inner_radius + (self.rout_sector_width/2))

        self.v5_velocity = (c * self.rpm) / 60

    def _v6_velocity(self):
        """

        """
        pass

    def _calculate_a1(self):
        """
        use ain to get a3
        """
        if self.ain >= 0:
            # use rinaxial and v1 velocity to calculate third side
            third_side = (self.v1_velocity**2 - self.vinaxial**2)**0.5
            # use third side and v2 velocity to calculate a1
            self.a1 = math.degrees(math.atan(self.vinaxial / (self.v2_velocity - third_side)))
        elif self.ain < 0:
            third_side = (self.v1_velocity**2 - self.vinaxial**2)**0.5
            self.a1 = math.degrees(math.atan(self.vinaxial / (self.v2_velocity + third_side)))

    def _calculate_a2(self):
        """
        use ain, a3, v2, rinaxial to solve for a2
        """
        self.a2 = 180 - self.a1 - self.a3

    def _calculate_a3(self):
        """
        use ain to solve for a3
        """
        if self.ain >= 0:
            self.a3 = 90 - self.ain
        elif self.ain < 0:
            self.a3 = 90 + self.ain

    def _calculate_a4(self):
        """
        use arout, routaxial, v5 velocity to solve for a4
        """
        pass

    def _calculate_a5(self):
        """
        use a4, arout to solve for a5
        """
        pass

    def _calculate_a6(self):
        """
        use arout to solve for a6
        """
        pass

    def _angle_of_attack(self):
        """

        """
        self.angle_of_attack = (90 - self.arin) - self.a1

    def _vinaxial(self):
        """

        """
        self.vinaxial = self.v1_velocity * math.cos(math.radians(self.ain))

    def _voutaxial(self):
        """

        """
        self.voutaxial = self.v4_velocity * math.cos(math.radians(self.arout))

    def _work_done(self):
        """

        """
        pass

