"""
TAKES ARGUMENTS

1. Function.
2. Max Error.
3. Max Tries.
4. Start Value (optional. defaults to 1).
5. Start Increment (optional. defaults to 1).
6. Arguments Dictionary.

FUNCTION SIGNATURE fn(**args, x)

FUNCTION RETURN VALUE is a dictionary with an entry for value y.
"""

class EquationSolverException(Exception):

    def __init__(self, err_msg):
        super().__init__(err_msg)


class EquationSolver:

    def __init__(self, fn, kwargs, max_error, max_tries=1000, start_x=1, start_inc=1, y=0, max_lower_bound=None, max_upper_bound=None):
        """

        """
        #max_lower_bound = 0
        print(f'y {y} max_lower_bound {max_lower_bound} max_upper_bound {max_upper_bound}')
        self.fn = fn
        self.max_error = max_error
        self.max_tries = max_tries
        self.kwargs = kwargs
        self.start_x = start_x
        self.start_inc = start_inc
        self.y = y
        self.max_lower_bound = max_lower_bound
        self.max_upper_bound = max_upper_bound
        self.lower_bound = max_lower_bound
        self.upper_bound = max_upper_bound
        self.prev_x = None
        self.curr_x = None
        self.prev_y = None
        self.curr_y = None
        self.inc = None
        self.mode = None
        self.tries = 0
        self.results = None

    def __str__(self):
        """

        """
        lower = self.lower_bound
        upper = self.upper_bound

        if self.lower_bound == None:
            lower = 'None'
        if self.upper_bound == None:
            upper = 'None'

        if self.lower_bound or self.upper_bound:
            return f"TRIES {self.tries} MODE {self.mode} INC {self.inc:.9f} PREV_X {self.prev_x:.4f} CURR_X {self.curr_x:.4f} PREV_Y {self.prev_y:.4f} CURR_Y {self.curr_y:.4f} Y {self.y:.4f} ERROR {abs(self.y - self.curr_y):.9f} LOWER_BOUND {lower} UPPER_BOUND {upper}"
        else:
            return f"TRIES {self.tries} MODE {self.mode} INC {self.inc:.9f} PREV_X {self.prev_x:.4f} CURR_X {self.curr_x:.4f} PREV_Y {self.prev_y:.4f} CURR_Y {self.curr_y:.4f} Y {self.y:.4f} ERROR {abs(self.y - self.curr_y):.9f} LOWER_BOUND {lower} UPPER_BOUND {upper}"

    def solve(self):
        """

        """
        # check increment is valid
        # get first two x values and first two y values
        # enter while loop
        # check mode
        # check in tolerance (break out of while loop if in tolerance)
        # set bounds
        # get next y value

        self._check_increment()

        self.results = self.fn(x=self.start_x, **self.kwargs)

        self.prev_x = self.start_x

        self.prev_y = self.results["y"]

        x2 = self.start_x + self.start_inc

        self.curr_x = x2

        self.results = self.fn(x=x2, **self.kwargs)

        self.curr_y = self.results["y"]

        while self.tries < self.max_tries:
            print(self)

            self._set_mode()

            if self._in_tolerance():
                break

            self._set_bounds()

            self._increment()

            self._next_y_value()

            self.tries += 1

        if self.tries != self.max_tries:
            self.results["x"] = self.curr_x

            return self.results
        else:
            err_msg = f""
            raise EquationSolverException(err_msg)

    def _check_increment(self):
        """
        Check if the increment is within bounds.
        """
        self.inc = self.start_inc

    def _crossover(self):
        """
        Checks if the desired y value is between the previous and current y values.
        Returns True is crossing over else returns False.
        """
        if self.prev_y <= self.y <= self.curr_y or self.curr_y <= self.y <= self.prev_y:
            self.mode = "CROSSOVER"

    def _converging(self):
        """
        Uses the previous and current y value to check if the y values are converging.
        """
        if self.prev_y < self.curr_y < self.y or self.prev_y > self.curr_y > self.y:
            self.mode = "CONVERGING"

    def _diverging(self):
        """
        Uses the previous and current y value to check if the y values are diverging.
        """
        if self.curr_y < self.prev_y < self.y or self.y < self.prev_y < self.curr_y:
            self.mode = "DIVERGING"

    def _set_mode(self):
        """
        Checks if the current mode is CROSSOVER, CONVERGING or DIVERGING.
        """
        self._crossover()
        self._converging()
        self._diverging()

    def _in_tolerance(self):
        """
        Check if the current y value is within the tolerance of the desired y value.
        Returns True if in tolerance else returns False.
        """
        if abs(self.y - self.curr_y) < self.max_error:
            return True
        else:
            return False

    def _increment(self):
        """
        Creates the next increment based on if the previous and current y values arre converging.
        If crossover increment * -2/3.
        If converging increment * 2.
        If diverging increment * -1.
        Check if new increment will make x go out of bounds.
        If out of bounds set increment to half the distance to the bound.
        """
        if self.mode == "CROSSOVER":
            self.inc = self.inc * -2/3
        elif self.mode == "CONVERGING":
            self.inc = self.inc * 1.4
        elif self.mode == "DIVERGING":
            self.inc = self.inc * -3/2

        if self.lower_bound != None and self.upper_bound != None:
            if self.inc > 0 and (self.curr_x + self.inc) > self.upper_bound:
                self.inc = self.upper_bound - self.curr_x
            elif self.inc < 0 and (self.curr_x + self.inc) < self.lower_bound:
                self.inc = self.curr_x - self.lower_bound

    def _set_bounds(self):
        """
        converging and x increasing  lower bound = current x
        converging and x decreasing  upper bound = current x
        diverging  and x increasing  upper bound = previous x
        diverging  and x decreasing  lower bound = previous x
        crossover  and x increasing  lower bound = previous x | upper bound = current x
        crossover  and x decreasing  lower bound = current x | upper bound = previous x
        """
        if self.mode == "CONVERGING" and self.curr_x > self.prev_x:
            self.lower_bound = self.curr_x
        elif self.mode == "CONVERGING" and self.curr_x < self.prev_x:
            self.upper_bound = self.curr_x
        elif self.mode == "DIVERGING" and self.curr_x > self.prev_x:
            self.upper_bound = self.prev_x
        elif self.mode == "DIVERGING" and self.curr_x < self.prev_x:
            self.lower_bound = self.prev_x
        elif self.mode == "CROSSOVER" and self.curr_x > self.prev_x:
            self.lower_bound = self.prev_x
            self.upper_bound = self.curr_x
        elif self.mode == "CROSSOVER" and self.curr_x < self.prev_x:
            self.lower_bound = self.curr_x
            self.upper_bound = self.prev_x

    def _next_y_value(self):
        """
        Calculates the next y value and updates prev and curr x and y values.
        """
        x = self.curr_x + self.inc

        self.results = self.fn(x=x, **self.kwargs)

        y = self.results["y"]

        self.prev_x = self.curr_x
        self.curr_x = x

        self.prev_y = self.curr_y
        self.curr_y = y


def equation_solver(fn, max_error, max_tries, kwargs, start_x=1, start_inc=1, y=0, max_lower_bound=None, max_upper_bound=None):
    """

    """
    solver = EquationSolver(fn, kwargs, max_error, max_tries, start_x, start_inc, y, max_lower_bound, max_upper_bound)

    try:
        results = solver.solve()
    except Exception as e:
        raise e
    else:
        return results

def test_function(m, c, x):
    """

    """
    y = (m*x) + c

    results = {
        "m":m,
        "c":c,
        "y":y
    }

    return results


if __name__ == "__main__":
    results = equation_solver(test_function, 0.0000001, 1000, {"m":1,"c":2}, 2, 2, -134)

    print(results)

