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
        def _total_conditions_from_dynamic_conditions(rsh, v, ps, x, ds, ts, vs):
            """

            """
            pt = x

            vs = vs or 1

            mf = v * ds

            ek = 0.5 * mf * (v**2)

            vx = GasLaws.volume_from_pressure(v, ps, pt, rsh)
            print(f"ps {ps} pt {pt} vx {vx} rsh {rsh}")
            w = abs(GasLaws.work_done_by_change_of_volume(ps, pt, v, vx, rsh))
            print(f"ek {ek} w {w}")
            y = ek - w

            data = {
                "rsh":rsh,
                "v":v,
                "ps":ps,
                "pt":pt,
                "ds":ds,
                "dt":None,
                "y":y
            }

            if ts:
                tt = GasLaws.temperature_from_pressure(ts, ps, pt, rsh)

                data["ts"] = ts
                data["tt"] = tt

            if vs:
                vt = GasLaws.volume_from_pressure(vs, ps, pt, rsh)

                data["vs"] = vs
                data["vt"] = vt
                data["dt"] = ds * vs / vt

            return data

        if v != 0:

            data = {
                "rsh":rsh,
                "v":v,
                "ps":ps,
                "ds":ds,
                "ts":ts,
                "vs":vs
            }

            #equation_solver(fn, max_error, max_tries, kwargs, start_x=1, start_inc=1, y=0, max_lower_bound=None, max_upper_bound=None)
            data = equation_solver(_total_conditions_from_dynamic_conditions, 0.000001, 1000, data, data["ps"], data["ps"]/10, 0, data["ps"])

            return data

        elif v == 0:

            data = {
                "rsh":rsh,
                "v":v,
                "ps":ps,
                "pt":ps,
                "ds":ds,
                "dt":ds,
                "ts":ts,
                "tt":ts,
                "vs":vs,
                "vt":vs
            }

            return data

    def dynamic_conditions_from_total_conditions(rsh, tt, pt, vt, dt, v):
        """

        """
        def _flow_from_static_conditions(tt, pt, dt, rsh, v, x):
            """

            """
            print(f'tt {tt} pt {pt} dt {dt} rsh {rsh} v {v} x {x}')
            mf1 = dt

            vf1 = 1

            ek = 0.5 * mf1 * (v**2)

            vf2 = ((pt/x) * (vf1**rsh))**(1/rsh)

            w = ((pt * vf1) - (x * vf2)) / (1 - rsh)

            y = ek + w

            ps = x

            ts = tt * ((ps/pt)**((rsh-1)/rsh))

            ds = dt * (ps/pt)**(1/rsh)

            data = {
                "tt":tt,
                "pt":pt,
                "dt":dt,
                "rsh":rsh,
                "v":v,
                "x":x,
                "y":y,
                "ps":ps,
                "ts":ts,
                "ds":ds
            }

            return data

        data = {
            "tt":tt,
            "pt":pt,
            "dt":dt,
            "rsh":rsh,
            "v":v
        }

        data = equation_solver(_flow_from_static_conditions, 0.000001, 1000, data, pt, pt / 100, max_lower_bound=0, max_upper_bound=None)

        return data


    def flow_change_of_area(a1, a2, v1, ps1, d1, rsh, ts1):
        """

        """
        def _flow_change_of_area(a1, a2, v1, x, ps1, d1, rsh, ts1):
            """

            """
            print(f'################################ a1 {a1} a2 {a2} v1 {v1} ts1 {ts1}')

            mf1 = v1 * d1 * a1

            vf1 = v1 * a1

            ek1 = 0.5 * mf1 * (v1**2)

            vf2 = x * a2

            d2 = mf1 / vf2

            mf2 = x * d2 * a2

            ps2 = ps1 * (vf1/vf2)**rsh

            ts2 = None

            if ts1:
                # temperature_from_pressure(t1, p1, p2, rsh)
                ts2 = GasLaws.temperature_from_pressure(ts1, ps1, ps2, rsh)

            w = ((ps2 * vf2) - (ps1 * vf1)) / (1-rsh)

            if a1 > a2:
                ek2 = ek1 + abs(w)
            elif a2 < a2:
                ek2 = ek1 - abs(w)
            else:
                ek2 = ek1 - abs(w)

            v2 = ((2 * (ek1 + w))/ mf2)**0.5

            pt1 = GasLaws.total_pressure(ps1, vf1, ek1, rsh)

            pt2 = GasLaws.total_pressure(ps2, vf2, ek2, rsh)

            # total_conditions_from_dynamic_conditions(rsh, v, ps, ds, ts=None, vs=None)
            inlet_total_data = GasLaws.total_conditions_from_dynamic_conditions(rsh, v1, ps1, d1, ts1, 1)
            print("INLET TOTAL DATA")
            print(inlet_total_data)
            dt1 = inlet_total_data['dt']
            tt1 = inlet_total_data['tt']

            outlet_total_data = GasLaws.total_conditions_from_dynamic_conditions(rsh, v2, ps2, d2, ts2, 1)
            print("OUTLET TOTAL DATA")
            print(outlet_total_data)
            dt2 = outlet_total_data['dt']
            tt2 = outlet_total_data['tt']

            y = ek1 - (ek2 - w)

            data = {
                "v1":v1,
                "v2":v2,
                "x":x,
                "y":y,
                "ts1":ts1,
                "tt1":tt1,
                "ts2":ts2,
                "tt2":tt2,
                "ds1":d1,
                "ds2":d2,
                "dt1":dt1,
                "dt2":dt2,
                "mf1":mf1,
                "mf2":mf2,
                "vf1":vf1,
                "vf2":vf2,
                "w":w,
                "a1":a1,
                "a2":a2,
                "rsh":rsh,
                "ek1":ek1,
                "ek2":ek2,
                "ps1":ps1,
                "ps2":ps2,
                "pt1":pt1["p2"],
                "pt2":pt2["p2"]
            }

            return data

        input_data = {
            "v1":v1,
            "a1":a1,
            "a2":a2,
            "ps1":ps1,
            "d1":d1,
            "rsh":rsh,
            "ts1":ts1
        }

        inc = v1 / 10

        #if a1 > a2:
        #    output_data = equation_solver(_flow_change_of_area, 0.000001, 1000, input_data, v1/4, inc, 0, v1, None)
        #elif a1 < a2:
        #    output_data = equation_solver(_flow_change_of_area, 0.000001, 1000, input_data, v1/4, inc, 0, None, v1)
        #else:
        output_data = equation_solver(_flow_change_of_area, 0.000001, 1000, input_data, v1, inc, 0)

        return output_data

    def speed_of_sound():
        """

        """
        pass

    def work_done_by_change_of_volume(p1, p2, v1, v2, rsh):
        """

        """
        w = ((p2 * v2) - (p1 * v1)) / (1 - rsh)

        return w

    def total_pressure(p1, v1, w, rsh):
        """

        """
        def _total_pressure(p1, v1, w, rsh, x):
            """

            """
            v2 = ((p1/x)*(v1**rsh))**(1/rsh)

            _w = ((p1*v1) - (x*v2)) / (1 - rsh)

            y = w - _w

            data = {
                "p1":p1,
                "p2":x,
                "v1":v1,
                "v2":v2,
                "w":w,
                "rsh":rsh,
                "x":x,
                "y":y
            }

            return data

        data = {
            "p1":p1,
            "v1":v1,
            "w":w,
            "rsh":rsh
        }

        data = equation_solver(_total_pressure, 0.000001, 1000, data, data["p1"], data["p1"]/10)

        return data
