"""
length
	feet
	meters
	inch
	centimeter
	milimeter

area
	feet
	meters
	inch
	centimeter
	milimeter

mass
	kilogram
	pound
	gram
	ounce

volume
	feet
	meters
	inch
	centimeter
	milimeter

temperature
	kelvin
	celcius
	rankine
	farenheit

pressure
	pascals
	psi

angle
	degrees
	radians
        rpm
	rps

circle
        circumferance
	diameter
	radius
	area
        sector area
"""


class ConvertUnits:

    METERS_TO_FEET = 3.2808399
    METERS_TO_INCHES = 39.3700787
    METERS_TO_CENTIMETERS = 100.0
    METERS_TO_MILIMETERS = 1000.0
    KILOGRAMS_TO_POUNDS = 2.20462262
    KILOGRAMS_TO_GRAMS = 1000.0
    KILOGRAMS_TO_OUNCE = 35.2739619
    METERS_SQUARE_TO_FEET_SQUARE = 10.7639104
    METERS_SQUARE_TO_INCHES_SQUARE = 1550.0031000062
    METERS_SQUARE_TO_CENTIMETERS_SQUARE = 10000.0
    METERS_SQUARE_TO_MILIMETERS_SQUARE = 1000000.0
    METERS_CUBED_TO_FEET_CUBED = 35.3146667
    METERS_CUBED_TO_INCHES_CUBED = 61023.7441
    METERS_CUBED_TO_CENTIMETERS_CUBED = 1000000.0
    METERS_CUBED_TO_MILIMETERS_CUBED = 1000000000.0
    PASCALS_TO_PSI = 0.00014504
    PASCALS_TO_BAR = 0.00001

    @classmethod
    def meters_to_feet(cls, meters):
        """

        """
        return meters * cls.METERS_TO_FEET

    @classmethod
    def meters_to_inches(cls, meters):
        """

        """
        return meters * cls.METERS_TO_INCHES

    @classmethod
    def meters_to_centimeters(cls, meters):
        """

        """
        return meters * cls.METERS_TO_CENTIMETERS

    @classmethod
    def meters_to_milimeters(cls, meters):
        """

        """
        return meters * cls.METERS_TO_MILIMETERS

    @classmethod
    def feet_to_meters(cls, feet):
        """

        """
        c = 1 / cls.meters_to_feet(1)

        return feet * c

    @classmethod
    def feet_to_inches(cls, feet):
        """

        """
        pass

    @classmethod
    def feet_to_centimeters(cls, feet):
        """

        """
        pass

    @classmethod
    def feet_to_milimeters(cls, feet):
        """

        """
        pass

    @classmethod
    def inches_to_meters(cls, inches):
        """

        """
        pass

    @classmethod
    def inches_to_feet(cls, inches):
        """

        """
        pass

    @classmethod
    def inches_to_milimeters(cls, inches):
        """

        """
        pass

    @classmethod
    def milimeters_to_meters(cls, milimeters):
        """

        """
        pass

    @classmethod
    def milimeters_to_feet(cls, milimeters):
        """

        """
        pass

    @classmethod
    def milimeters_to_inches(cls, milimeters):
        """

        """
        pass

    @classmethod
    def meters_square_to_feet_square(cls, meters_square):
        """

        """
        pass

    @classmethod
    def meters_square_to_inches_square(cls, meters_square):
        """

        """
        pass

    @classmethod
    def meters_square_to_centimeters_square(cls, meters_square):
        """

        """
        pass

    @classmethod
    def meters_square_to_milimeters_square(cls, meters_square):
        """

        """
        pass

    @classmethod
    def feet_square_to_meters_square(cls, feet_square):
        """

        """
        pass

    @classmethod
    def feet_square_to_inches_square(cls, feet_square):
        """

        """
        pass

    @classmethod
    def feet_square_to_centimeters_square(cls, feet_square):
        """

        """
        pass

    @classmethod
    def feet_square_to_milimeters_square(cls, feet_square):
        """

        """
        pass

    @classmethod
    def inches_square_to_meters_square(cls, inches_square):
        """

        """
        pass

    @classmethod
    def inches_square_to_feet_square(cls, inches_square):
        """

        """
        pass

    @classmethod
    def inches_square_to_milimeters_square(cls, inches_square):
        """

        """
        pass

    @classmethod
    def milimeters_square_to_meters_square(cls, milimeters_square):
        """

        """
        pass

    @classmethod
    def milimeters_square_to_feet_square(cls, milimeters_square):
        """

        """
        pass

    @classmethod
    def milimeters_square_to_inches_square(cls, milimeters_square):
        """

        """
        pass

    @classmethod
    def kilograms_to_pounds(cls, kilograms):
        """

        """
        pass

    @classmethod
    def kilograms_to_ounces(cls, kilograms):
        """

        """
        pass

    @classmethod
    def kilograms_to_grams(cls, kilograms):
        """

        """
        pass

    @classmethod
    def pounds_to_kilograms(cls, pounds):
        """

        """
        pass

    @classmethod
    def pounds_to_ounces(cls, pounds):
        """

        """
        pass

    @classmethod
    def pounds_to_grams(cls, pounds):
        """

        """
        pass

    @classmethod
    def ounces_to_kilograms(cls, ounces):
        """

        """
        pass

    @classmethod
    def ounces_to_pounds(cls, ounces):
        """

        """
        pass

    @classmethod
    def ounces_to_grams(cls, ounces):
        """

        """
        pass

    @classmethod
    def grams_to_kilograms(cls, grams):
        """

        """
        pass

    @classmethod
    def grams_to_pounds(cls, grams):
        """

        """
        pass

    @classmethod
    def grams_to_ounces(cls, grams):
        """

        """
        pass

    @classmethod
    def meters_cubed_to_feet_cubed(cls, meters_cubed):
        """

        """
        pass

    @classmethod
    def meters_cubed_to_inches_cubed(cls, meters_cubed):
        """

        """
        pass

    @classmethod
    def meters_cubed_to_centimeters_cubed(cls, meters_cubed):
        """

        """
        pass

    @classmethod
    def meters_cubed_to_milimeters_cubed(cls, meters_cubed):
        """

        """
        pass

    @classmethod
    def feet_cubed_to_meters_cubed(cls, feet_cubed):
        """

        """
        pass

    @classmethod
    def feet_cubed_to_inches_cubed(cls, feet_cubed):
        """

        """
        pass

    @classmethod
    def feet_cubed_to_centimeters_cubed(cls, feet_cubed):
        """

        """
        pass

    @classmethod
    def feet_cubed_to_milimeters_cubed(cls, feet_cubed):
        """

        """
        pass

    @classmethod
    def inches_cubed_to_meters_cubed(cls, inches_cubed):
        """

        """
        pass

    @classmethod
    def inches_cubed_to_feet_cubed(cls, inches_cubed):
        """

        """
        pass

    @classmethod
    def inches_cubed_to_centimeters_cubed(cls, inches_cubed):
        """

        """
        pass

    @classmethod
    def inches_cubed_to_milimeters_cubed(cls, inches_cubed):
        """

        """
        pass

    @classmethod
    def centimeters_cubed_to_meters_cubed(cls, centimeters_cubed):
        """

        """
        pass

    @classmethod
    def centimeters_cubed_to_feet_cubed(cls, centimeters_cubed):
        """

        """
        pass

    @classmethod
    def centimeters_cubed_to_inches_cubed(cls, centimeters_cubed):
        """

        """
        pass

    @classmethod
    def centimeters_cubed_to_milimeters_cubed(cls, centimeters_cubed):
        """

        """
        pass

    @classmethod
    def milimeters_cubed_to_meters_cubed(cls, milimeters_cubed):
        """

        """
        pass

    @classmethod
    def milimeters_cubed_to_feet_cubed(cls, milimeters_cubed):
        """

        """
        pass

    @classmethod
    def milimeters_cubed_to_inches_cubed(cls, milimeters_cubed):
        """

        """
        pass

    @classmethod
    def milimeters_cubed_to_centimeters_cubed(cls, milimeters_cubed):
        """

        """
        pass

    @classmethod
    def kelvin_to_celcius(cls, kelvin):
        """

        """
        pass

    @classmethod
    def kelvin_to_rankine(cls, kelvin):
        """

        """
        pass

    @classmethod
    def kelvin_to_farenheit(cls, kelvin):
        """

        """
        pass

    @classmethod
    def celcius_to_kelvin(cls, celcius):
        """

        """
        pass

    @classmethod
    def celcius_to_rankine(cls, celcius):
        """

        """
        pass

    @classmethod
    def celcius_to_farenheit(cls, celcius):
        """

        """
        pass

    @classmethod
    def rankine_to_kelvin(cls, rankine):
        """

        """
        pass

    @classmethod
    def rankine_to_celcius(cls, rankine):
        """

        """
        pass

    @classmethod
    def rankine_to_farenheit(cls, rankine):
        """

        """
        pass

    @classmethod
    def farenheit_to_kelvin(cls, farenheit):
        """

        """
        pass

    @classmethod
    def farenheit_to_celcius(cls, farenheit):
        """

        """
        pass

    @classmethod
    def farenheit_to_rankine(cls, farenheit):
        """

        """
        pass
    @classmethod
    def pascals_to_psi(cls, pascals):
        """

        """
        pass

    @classmethod
    def pascals_to_bar(cls, pascals):
        """

        """
        pass

    @classmethod
    def psi_to_pascals(cls, psi):
        """

        """
        pass

    @classmethod
    def psi_to_bar(cls, psi):
        """

        """
        pass

    @classmethod
    def bar_to_pascals(cls, bar):
        """

        """
        pass

    @classmethod
    def bar_to_psi(cls, bar):
        """

        """
        pass

    @classmethod
    def degrees_to_radians(cls, degrees):
        """

        """
        pass

    @classmethod
    def radians_to_degrees(cls, radians):
        """

        """
        pass

    @classmethod
    def degrees_per_second_to_rpm(cls, degrees_per_second):
        """

        """
        pass

    @classmethod
    def degrees_per_second_to_rps(cls, degrees_per_second):
        """

        """
        pass

    @classmethod
    def rpm_to_degrees_per_second(cls, rpm):
        """

        """
        pass

    @classmethod
    def rps_to_degrees_per_second(cls, rps):
        """

        """
        pass

    @classmethod
    def rpm_to_degrees_per_minute(cls, rpm):
        """

        """
        pass

    @classmethod
    def rps_to_degrees_per_minute(cls, rps):
        """

        """
        pass

    @classmethod
    def rpm_to_radians_per_minute(cls, rpm):
        """

        """
        pass

    @classmethod
    def rpm_to_radians_per_second(cls, rpm):
        """

        """
        pass

    @classmethod
    def rps_to_radians_per_minute(cls, rps):
        """

        """
        pass

    @classmethod
    def rps_to_radians_per_second(cls, rps):
        """

        """
        pass

    @classmethod
    def circumferance_to_diameter(cls, circumferance):
        """

        """
        pass

    @classmethod
    def circumferance_to_radius(cls, circumferance):
        """

        """
        pass

    @classmethod
    def circumferance_to_area(cls, circumferance):
        """

        """
        pass

    @classmethod
    def diameter_to_circumferance(cls, diameter):
        """

        """
        pass

    @classmethod
    def diameter_to_radius(cls, diameter):
        """

        """
        pass

    @classmethod
    def diameter_to_area(cls, diameter):
        """

        """
        pass

    @classmethod
    def radius_to_circumferance(cls, radius):
        """

        """
        pass

    @classmethod
    def radius_to_diameter(cls, radius):
        """

        """
        pass

    @classmethod
    def radius_to_area(cls, radius):
        """

        """
        pass

    @classmethod
    def area_to_circumferance(cls, area):
        """

        """
        pass

    @classmethod
    def area_to_diameter(cls, area):
        """

        """
        pass

    @classmethod
    def area_to_radius(cls, area):
        """

        """
        pass

    @classmethod
    def sector_area(cls, radius, radians):
        """

        """
        pass
