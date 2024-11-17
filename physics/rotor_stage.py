


class RotorStage:

    self.a1 = None
    self.a2 = None
    self.a4 = None
    self.a6 = None
    self.arin = None
    self.arout = None
    self.v1_velocity = None
    self.v1_ps = None
    self.v1_ts = None
    self.v1_ds = None
    self.v1_pt = None
    self.v1_tt = None
    self.v1_dt = None
    self.v2_velocity = None
    self.v3_velocity = None
    self.v3_ps = None
    self.v3_ts = None
    self.v3_ds = None
    self.v3_pt = None
    self.v3_tt = None
    self.v3_dt = None
    self.v4_velocity = None
    self.v4_ps = None
    self.v4_ts = None
    self.v4_ds = None
    self.v4_pt = None
    self.v4_tt = None
    self.v4_dt = None
    self.v6_velocity = None
    self.v6_ps = None
    self.v6_ts = None
    self.v6_ds = None
    self.v6_pt = None
    self.v6_tt = None
    self.v6_dt = None
    self.rin_inner_radius = None
    self.rout_inner_radius = None
    self.rin_sector_width = None
    self.rout_sector_width = None
    self.vinaxial = None
    self.voutaxial = None
    self.rotor_rpm = None
    self.number_of_rotor_blades = None
    self.rin_area = None
    self.rout_area = None
    self.rin_effective_area = None
    self.rout_effective_area = None
    self.angle_of_attack = None
    self.rsh = None

    def __init__(self, a1, rotor_rpm, arin, arout, number_of_blades, rin_radius, rout_radius, rin_width, rout_width, ps, ds, ts, rsh):
        self.a1 = a1
        self.rotor_rpm = rotor_rpm
        self.arin = arin
        self.arout = arout
        self.number_of_rotor_blades = number_of_blades
        self.rin_inner_radius = rin_radius
        self.rout_inner_radius = rout_radius
        self.rin_sector_width = rin_width
        self.rout_sector_width = rout_width
        self.v1_ps = ps
        self.v1_ts = ts
        self.v1_ds = ds
        self.rsh = rsh

    def solve_rotor(self):
        """

        """
        self._rin_sector_velocity()
        self._rout_sector_velocity()
        self._rin_blade_spacing()
        self._rout_blade_spacing()
        self._actual_rin_area()
        self._actual_rout_area()
        self._rin_sector_velocity()
        self._calculate_a2()
        self._v1_total_conditions()
        self._v3_total_conditions()
        self._angle_of_attack()
        self._effective_rin_area()
        self._v4_total_conditions()
        self._calculate_a6()
        self._v6_total_conditions()
        self._vinaxial()
        self._voutaxial()

    def rotor_data(self):
        """

        """
        pass

    def _v1_total_conditions(self):
        """

        """
        pass

    def _v3_total_conditions(self):
        """

        """
        pass

    def _v4_total_conditions(self):
        """

        """
        pass

    def _v6_total_conditions(self):
        """

        """
        pass

    def _rin_sector_velocity(self):
        """

        """
        pass

    def _rout_sector_velocity(self):
        """

        """
        pass

    def _calculate_a2(self):
        """

        """
        pass

    def _calculate_a6(self):
        """

        """
        pass

    def _rin_blade_spacing(self):
        """

        """
        pass

    def _rout_blade_spacing(self):
        """

        """
        pass

    def _actual_rin_area(self):
        """

        """
        pass

    def _actual_rout_area(self):
        """

        """
        pass

    def _effective_rin_area(self):
        """

        """
        pass

    def _angle_of_attack(self):
        """

        """
        pass

    def _vinaxial(self):
        """

        """
        pass

    def _voutaxial(self):
        """

        """
        pass

