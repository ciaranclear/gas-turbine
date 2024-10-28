from physics.equation_solver import equation_solver


class GasLaws:

    def temperature_from_pressure(t1, p1, p2, rsh):
        """

        """
        t2 = t1 * (p2/p1)**((rsh - 1)/rsh)

        return t2

    def temperature_from_volume(t1, v1, v2, rsh):
        """

        """
        t2 = t1 * (v1/v2)**(rsh - 1)

        return t2

    def temperature_from_density(t1, d1, d2, rsh):
        """

        """
        t2 = t1 * (d2/d1)**(rsh - 1)

        return t2

    def volume_from_pressure(v1, p1, p2, rsh):
        """

        """
        v2 = v1 * (p1/p2)**(1/rsh)

        return v2

    def volume_from_temperature(v1, t1, t2, rsh):
        """

        """
        v2 = v1 * (t1/t2)**(1/(rsh - 1))

        return v2

    def volume_from_density(v1, d1, d2):
        """

        """
        v2 = v1 * (d1/d2)

        return v2

    def pressure_from_temperature(p1, t1, t2, rsh):
        """

        """
        p2 = p1 * (t2/t1)**(rsh/(rsh - 1))

        return p2

    def pressure_from_volume(p1, v1, v2, rsh):
        """

        """
        p2 = p1 * (v1/v2)**rsh

        return p2

    def pressure_from_density(p1, d1, d2, rsh):
        """

        """
        p2 = p1 * (d2/d1)**rsh

        return p2

    def density_from_temperature(d1, t1, t2, rsh):
        """

        """
        d2 = d1 * (t2/t1)**(1/(rsh - 1))

        return d2

    def density_from_pressure(d1, p1, p2, rsh):
        """

        """
        d2 = d1 * (p2/p1)**(1/rsh)

        return d2

    def density_from_volume(d1, v1, v2, rsh):
        """

        """
        d2 = d1 * (v1/v2)

        return d2

    def total_conditions_from_dynamic_conditions(rsh, v, ps, ds, ts=None, vs=None):
        """

        """
        def _total_conditions_from_dynamic_conditions(rsh, v, ps, x, ds, ts):
            """

            """
            pt = x

            mf = v * ds

            ek = 0.5 * mf * (v**2)

            vx = GasLaws.volume_from_pressure(1, ps, px, rsh)

            w = GasLaws.work_done_by_change_of_volume(ps, px, 1, vx, rsh)

            y = ek - w

            data = {
                "rsh":rsh,
                "v":v,
                "ps":ps,
                "pt":pt,
                "ds":ds,
                "dt":dt,
                "y":y
            }

            if ts:
                tt = GasLaws.temperature_from_pressure(ts, ps, pt, rsh)

                data["ts"] = ts
                data["tt"] = tt

            if vs:
                vt = GasLaws.volume_from_pressure(vs, ps, pt, rsh)

                data["ps"] = ps
                data["pt"] = pt

            return data

        data = {
            "rsh":rsh,
            "v":v,
            "ps":ps,
            "ds":ds,
            "ts":ts,
            "vs":vs
        }

        #equation_solver(fn, max_error, max_tries, kwargs, start_x=1, start_inc=1, y=0, max_lower_bound=None, max_upper_bound=None)
        data = equation_solver(_total_conditions_from_dynamic_conditions, 0.000001, 1000, data, data["p1"], data["p1"]/10)

        return data

    def dynamic_conditions_from_total_conditions(rsh, tt, pt, vt, dt, v):
        """

        """
        pass

    def flow_change_of_area(a1, a2, v1, ps1, ts1, ds1, rsh):
        """

        """
        pass

    def speed_of_sound():
        """

        """
        pass

    def work_done_by_change_of_volume(p1, p2, v1, v2, rsh):
        """

        """
        w = ((p2 * v2) - (p1 * v1)) / (1 - rsh)

