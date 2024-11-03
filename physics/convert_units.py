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
        feet_to_meters = 1 / cls.meters_to_feet(1)

        meters = feet * feet_to_meters

        return cls.meters_to_inches(meters)

    @classmethod
    def feet_to_centimeters(cls, feet):
        """

        """
        feet_to_meters = 1 / cls.meters_to_feet(1)

        meters = feet * feet_to_meters

        return cls.meters_to_centimeters(meters)

    @classmethod
    def feet_to_milimeters(cls, feet):
        """

        """
        feet_to_meters = 1 / cls.meters_to_feet(1)

        meters = feet * feet_to_meters

        return cls.meters_to_milimeters(meters)

    @classmethod
    def inches_to_meters(cls, inches):
        """

        """
        inches_to_meters = 1 / cls.meters_to_inches(1)

        meters = inches * inches_to_meters

        return cls.meters_to_inches(meters)

    @classmethod
    def inches_to_feet(cls, inches):
        """

        """
        inches_to_meters = 1 / cls.meters_to_inches(1)

        meters = inches * inches_to_meters

        return cls.meters_to_feet(meters)

    @classmethod
    def inches_to_milimeters(cls, inches):
        """

        """
        inches_to_meters = 1 / cls.meters_to_inches(1)

        meters = inches * inches_to_meters

        return cls.meters_to_milimeters(meters)

    @classmethod
    def milimeters_to_meters(cls, milimeters):
        """

        """
        milimeters_to_meters = 1 / cls.meters_to_milimeters(1)

        return milimeters * milimeters_to_meters

    @classmethod
    def milimeters_to_feet(cls, milimeters):
        """

        """
        milimeters_to_meters = 1 / cls.meters_to_milimeters(1)

        meters = milimeters * milimeters_to_meters

        return cls.meters_to_feet(meters)

    @classmethod
    def milimeters_to_inches(cls, milimeters):
        """

        """
        milimeters_to_meters = 1 / cls.meters_to_milimeters(1)

        meters = milimeters * milimeters_to_meters

        return cls.meters_to_inches(meter)

    @classmethod
    def meters_square_to_feet_square(cls, meters_square):
        """

        """
        return meters_square * cls.METERS_SQUARE_TO_FEET_SQUARE

    @classmethod
    def meters_square_to_inches_square(cls, meters_square):
        """

        """
        return meters_square * cls.METERS_SQUARE_TO_INCHES_SQUARE

    @classmethod
    def meters_square_to_centimeters_square(cls, meters_square):
        """

        """
        return meters_square * cls.METERS_SQUARE_TO_CENTIMETERS_SQUARE

    @classmethod
    def meters_square_to_milimeters_square(cls, meters_square):
        """

        """
        return meters_square * cls.METERS_SQUARE_TO_MILIMETERS_SQUARE

    @classmethod
    def feet_square_to_meters_square(cls, feet_square):
        """

        """
        feet_square_to_meters_square = 1 / cls.meters_square_to_feet_square(1)

        return feet_square * feet_square_to_meters_square

    @classmethod
    def feet_square_to_inches_square(cls, feet_square):
        """

        """
        feet_square_to_meters_square = 1 / cls.meters_square_to_feet_square(1)

        meters_square = feet_square * feet_square_to_meters_square

        return cls.meters_square_to_inches_square(meters_square)

    @classmethod
    def feet_square_to_centimeters_square(cls, feet_square):
        """

        """
        feet_square_to_meters_square = 1 / cls.meters_square_to_feet_square(1)

        meters_square = feet_square * feet_square_to_meters_square

        return cls.meters_square_to_centimeters_square(meters_square)

    @classmethod
    def feet_square_to_milimeters_square(cls, feet_square):
        """

        """
        feet_square_to_meters_square = 1 / cls.meters_square_to_feet_square(1)

        meters_square = feet_square * feet_square_to_meters_square

        return cls.meters_square_to_milimeters_square(meters_square)

    @classmethod
    def inches_square_to_meters_square(cls, inches_square):
        """

        """
        inches_square_to_meters_square = 1 / cls.meters_square_to_inches_square(1)

        return inches_square * inches_square_to_meters_square

    @classmethod
    def inches_square_to_feet_square(cls, inches_square):
        """

        """
        inches_square_to_meters_square = 1 / cls.meters_square_to_inches_square(1)

        meters_square = inches_square * inches_square_to_meters_square

        return cls.meters_square_to_feet_square(meters_Square)

    @classmethod
    def inches_square_to_milimeters_square(cls, inches_square):
        """

        """
        inches_square_to_meters_square = 1 / cls.meters_square_to_inches_square(1)

        meters_square = inches_square * inches_square_to_meters_square

        return cls.meters_square_to_milimters_square(meters_Square)

    @classmethod
    def milimeters_square_to_meters_square(cls, milimeters_square):
        """

        """
        milimeters_square_to_meters_square = 1 / cls.meters_square_to_milimeters_square(1)

        return milimeters_square * milimeters_square_to_meters_square

    @classmethod
    def milimeters_square_to_feet_square(cls, milimeters_square):
        """

        """
        milimeters_square_to_meters_square = 1 / cls.meters_square_to_milimeters_square(1)

        meters_square = milimeters_square * milimeters_square_to_meters_square

        return cls.meters_square_to_feet_square(meters_square)

    @classmethod
    def milimeters_square_to_inches_square(cls, milimeters_square):
        """

        """
        milimeters_square_to_meters_square = 1 / cls.meters_square_to_milimeters_square(1)

        meters_square = milimeters_square * milimeters_square_to_meters_square

        return cls.meters_square_to_inches_square(meters_square)

    @classmethod
    def kilograms_to_pounds(cls, kilograms):
        """

        """
        return kilograms * cls.KILOGRAMS_TO_POUNDS

    @classmethod
    def kilograms_to_ounces(cls, kilograms):
        """

        """
        return kilograms * cls.KILOGRAMS_TO_OUNCES

    @classmethod
    def kilograms_to_grams(cls, kilograms):
        """

        """
        return kilograms * cls.KILOGRAMS_TO_GRAMS

    @classmethod
    def pounds_to_kilograms(cls, pounds):
        """

        """
        pounds_to_kilograms = 1 / cls.kilograms_to_pounds(1)

        return pounds * pounds_to_kilograms

    @classmethod
    def pounds_to_ounces(cls, pounds):
        """

        """
        pounds_to_kilograms = 1 / cls.kilograms_to_pounds(1)

        kilograms = pounds * pounds_to_kilograms

        return cls.kilograms_to_ounces(kilograms)

    @classmethod
    def pounds_to_grams(cls, pounds):
        """

        """
        pounds_to_kilograms = 1 / cls.kilograms_to_pounds(1)

        kilograms = pounds * pounds_to_kilograms

        return cls.kilograms_to_grams(kilograms)

    @classmethod
    def ounces_to_kilograms(cls, ounces):
        """

        """
        ounces_to_kilograms = 1 / cls.kilograms_to_ounces(1)

        return ounces * ounces_to_kilograms

    @classmethod
    def ounces_to_pounds(cls, ounces):
        """

        """
        ounces_to_kilograms = 1 / cls.kilograms_to_ounces(1)

        kilograms = ounces * ounces_to_kilograms

        return cls.kilograms_to_pounds(kilograms)

    @classmethod
    def ounces_to_grams(cls, ounces):
        """

        """
        ounces_to_kilograms = 1 / cls.kilograms_to_ounces(1)

        kilograms = ounces * ounces_to_kilograms

        return cls.kilograms_to_grams(kilograms)

    @classmethod
    def grams_to_kilograms(cls, grams):
        """

        """
        grams_to_kilograms = 1 / cls.kilograms_to_grams(1)

        return grams * grams_to_kilograms

    @classmethod
    def grams_to_pounds(cls, grams):
        """

        """
        grams_to_kilograms = 1 / cls.kilograms_to_grams(1)

        kilograms = grams * grams_to_kilograms

        return cls.kilograms_to_pounds(kilograms)

    @classmethod
    def grams_to_ounces(cls, grams):
        """

        """
        grams_to_kilograms = 1 / cls.kilograms_to_grams(1)

        kilograms = grams * grams_to_kilograms

        return cls.kilograms_to_ounces(kilograms)

    ################

    @classmethod
    def meters_cubed_to_feet_cubed(cls, meters_cubed):
        """

        """
        return meters_cubed * cls.METERS_CUBED_TO_FEET_CUBED

    @classmethod
    def meters_cubed_to_inches_cubed(cls, meters_cubed):
        """

        """
        return meters_cubed * cls.METERS_CUBED_TO_INCHES_CUBED

    @classmethod
    def meters_cubed_to_centimeters_cubed(cls, meters_cubed):
        """

        """
        return meters_cubed * cls.METERS_CUBED_TO_CENTIMETERS_CUBED

    @classmethod
    def meters_cubed_to_milimeters_cubed(cls, meters_cubed):
        """

        """
        return meters_cubed * cls.METERS_CUBED_TO_MILIMETERS_CUBED

    @classmethod
    def feet_cubed_to_meters_cubed(cls, feet_cubed):
        """

        """
        feet_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_feet_cubed(1)

        return feet_cubed * feet_cubed_to_meters_cubed

    @classmethod
    def feet_cubed_to_inches_cubed(cls, feet_cubed):
        """

        """
        feet_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_feet_cubed(1)

        meters_cubed = feet_cubed * feet_cubed_to_meters_cubed

        return cls.meters_cubed_to_inches_cubed(meters_cubed)

    @classmethod
    def feet_cubed_to_centimeters_cubed(cls, feet_cubed):
        """

        """
        feet_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_feet_cubed(1)

        meters_cubed = feet_cubed * feet_cubed_to_meters_cubed

        return cls.meters_cubed_to_centimeters_cubed(meters_cubed)

    @classmethod
    def feet_cubed_to_milimeters_cubed(cls, feet_cubed):
        """

        """
        feet_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_feet_cubed(1)

        meters_cubed = feet_cubed * feet_cubed_to_meters_cubed

        return cls.meters_cubed_to_milimeters_cubed(meters_cubed)

    @classmethod
    def inches_cubed_to_meters_cubed(cls, inches_cubed):
        """

        """
        inches_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_inches_cubed(1)

        return inches_cubed * inches_cubed_to_meters_cubed

    @classmethod
    def inches_cubed_to_feet_cubed(cls, inches_cubed):
        """

        """
        inches_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_inches_cubed(1)

        meters_cubed = inches_cubed * inches_cubed_to_meters_cubed

        return cls.meters_cubed_to_feet_cubed(meters_cubed)

    @classmethod
    def inches_cubed_to_centimeters_cubed(cls, inches_cubed):
        """

        """
        inches_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_inches_cubed(1)

        meters_cubed = inches_cubed * inches_cubed_to_meters_cubed

        return cls.meters_cubed_to_centimeters_cubed(meters_cubed)

    @classmethod
    def inches_cubed_to_milimeters_cubed(cls, inches_cubed):
        """

        """
        inches_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_inches_cubed(1)

        meters_cubed = inches_cubed * inches_cubed_to_meters_cubed

        return cls.meters_cubed_to_milimeters_cubed(meters_cubed)

    @classmethod
    def centimeters_cubed_to_meters_cubed(cls, centimeters_cubed):
        """

        """
        centimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_centimeters_cubed(1)

        return centimeters_cubed * centimeters_cubed_to_meters_cubed

    @classmethod
    def centimeters_cubed_to_feet_cubed(cls, centimeters_cubed):
        """

        """
        centimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_centimeters_cubed(1)

        meters_cubed = centimeters_cubed * centimeters_cubed_to_meters_cubed

        return cls.meters_cubed_to_feet_cubed(meters_cubed)

    @classmethod
    def centimeters_cubed_to_inches_cubed(cls, centimeters_cubed):
        """

        """
        centimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_centimeters_cubed(1)

        meters_cubed = centimeters_cubed * centimeters_cubed_to_meters_cubed

        return cls.meters_cubed_to_inches_cubed(meters_cubed)

    @classmethod
    def centimeters_cubed_to_milimeters_cubed(cls, centimeters_cubed):
        """

        """
        centimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_centimeters_cubed(1)

        meters_cubed = centimeters_cubed * centimeters_cubed_to_milimeters_cubed

        return cls.meters_cubed_to_milimeters_cubed(meters_cubed)

    @classmethod
    def milimeters_cubed_to_meters_cubed(cls, milimeters_cubed):
        """

        """
        milimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_milimeters_cubed(1)

        return milimeters_cubed * milimeters_cubed_to_meters_cubed

    @classmethod
    def milimeters_cubed_to_feet_cubed(cls, milimeters_cubed):
        """

        """
        milimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_milimeters_cubed(1)

        meters_cubed = milimeters_cubed * milimeters_cubed_to_meters_cubed

        return cls.meters_cubed_to_feet_cubed(meters_cubed)

    @classmethod
    def milimeters_cubed_to_inches_cubed(cls, milimeters_cubed):
        """

        """
        milimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_milimeters_cubed(1)

        meters_cubed = milimeters_cubed * milimeters_cubed_to_meters_cubed

        return cls.meters_cubed_to_inches_cubed(meters_cubed)

    @classmethod
    def milimeters_cubed_to_centimeters_cubed(cls, milimeters_cubed):
        """

        """
        milimeters_cubed_to_meters_cubed = 1 / cls.meters_cubed_to_milimeters_cubed(1)

        meters_cubed = milimeters_cubed * milimeters_cubed_to_meters_cubed

        return cls.meters_cubed_to_milimeters_cubed(meters_cubed)

    ################

    @classmethod
    def kelvin_to_celcius(cls, kelvin):
        """

        """
        return kelvin - 273.15

    @classmethod
    def kelvin_to_rankine(cls, kelvin):
        """

        """
        return kelvin * (9/5)

    @classmethod
    def kelvin_to_farenheit(cls, kelvin):
        """

        """
        return 1.8 * (kelvin - 273.15) + 32

    @classmethod
    def celcius_to_kelvin(cls, celcius):
        """

        """
        return celcius + 273.15

    @classmethod
    def celcius_to_rankine(cls, celcius):
        """

        """
        return celcius * (9/5) + 491.67

    @classmethod
    def celcius_to_farenheit(cls, celcius):
        """

        """
        return (celcius * (9/5)) + 32

    @classmethod
    def rankine_to_kelvin(cls, rankine):
        """

        """
        return ((rankine - 491.67) / 1.8) + 273.15

    @classmethod
    def rankine_to_celcius(cls, rankine):
        """

        """
        return (rankine - 491.67) / 1.8

    @classmethod
    def rankine_to_farenheit(cls, rankine):
        """

        """
        return rankine - 491.67

    @classmethod
    def farenheit_to_kelvin(cls, farenheit):
        """

        """
        return ((farenheit - 32) / 1.8) + 273.15

    @classmethod
    def farenheit_to_celcius(cls, farenheit):
        """

        """
        return (farenheit - 32) * 5/9

    @classmethod
    def farenheit_to_rankine(cls, farenheit):
        """

        """
        return farenheit + 491.67

    ################

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

    ################

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
