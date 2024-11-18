from gas_laws import GasLaws


class StatorStage:

    self.a1 = None
    self.a2 = None
    self.asin = None
    self.asout = None
    self.sin_area = None
    self.sout_area = None
    self.v1_velocity = None
    self.v1_ps = None
    self.v1_ts = None
    self.v1_ds = None
    self.v1_pt = None
    self.v1_tt = None
    self.v1_dt = None
    self.v2_velocity = None
    self.v3_velocity = None
    self.v4_velocity = None
    self.v4_ps = None
    self.v4_ts = None
    self.v4_ds = None
    self.v4_pt = None
    self.v4_tt = None
    self.v4_dt = None
    self.v5_velocity = None
    self.v6_velocity = None
    self.sin_effective_area = None
    self.sin_inner_radius = None
    self.sout_inner_radius = None
    self.sin_sector_width = None
    self.sout_sector_width = None
    self.number_of_stator_blades = None
    self.angle_of_attack = None
    self.rsh = None

    def __init__(self, a1, asin, asout, number_of_stators, sin_radius, sout_radius, sin_width, sout_width, ps, ts, ds, rsh)
        """

        """
        self.a1 = a1
        self.asin = asin
        self.asout = asout
        self.number_of_stator_blades = number_of_stators
        self.sin_inner_radius = sin_radius
        self.sout_inner_radius = sout_radius
        self.sin_sector_width = sin_width
        self.sout_sector_width = sout_width
        self.v1_ps = ps
        self.v1_ts = ts
        self.v1_ds = ds
        self.rsh = rsh

    def solve_stator(self):
        """

        """
        self._v1_total_conditions()
        self._v2_velocity()
        self._v3_velocity()
        self._sin_actual_area()
        self._sout_actual_area()
        self._sin_effective_area()
        self._v4_total_conditions()
        self._v5_velocity()
        self._v6_velocity()
        self._angle_of_attack()

    def rotor_data(self):
        """

        """
        pass

    def _v1_total_conditions(self):
        """

        """
        pass

    def _v4_total_conditions(self):
        """

        """
        pass

    def _v2_velocity(self):
        """

        """
        pass

    def _v3_velocity(self):
        """

        """
        pass

    def _v5_velocity(self):
        """

        """
        pass

    def _v6_velocity(self):
        """

        """
        pass

    def _sin_effective_area(self):
        """

        """
        pass

    def _sin_actual_area(self):
        """

        """
        pass

    def _sout_actual_area(self):
        """

        """
        pass

    def _angle_of_attack(self):
        """

        """
        pass
