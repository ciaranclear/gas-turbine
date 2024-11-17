from physics.convert_units import ConvertUnits


def get_input_value(inpt_str):
    while True:
        inpt = float(input(f"Enter a value to convert {inpt_str}\n"))
        return inpt


def unit_converter_interface():
    """

    """
    menu_str = (f"Select an option from menu\n"
                f"01. meters to feet.\n"
                f"02. meters to inches.\n"
                f"03. meters to centimeters.\n"
                f"04. meters to milimeters.\n"
                f"05. feet to meters.\n"
                f"06. feet to inches.\n"
                f"07. feet to centimeters.\n"
                f"08. feet to milimeters.\n"
                f"09. inches to meters.\n"
                f"10. inches to feet.\n"
                f"11. inches to milimeters.\n"
                f"12. milimeters to meters.\n"
                f"13. milimeters to feet.\n"
                f"14. milimeters to centimeters.\n"
                f"15. milimeters to inches.\n"
                f"16. meters square to feet square.\n"
                f"17. meters square to inches square.\n"
                f"18. meters square to centimeters square.\n"
                f"19. meters square to milimeters square.\n"
                f"20. feet square to meters square.\n"
                f"21. feet square to inches square.\n"
                f"22. feet square to centimeters square.\n"
                f"23. feet square to milimeters square.\n"
                f"24. inches square to meters square.\n"
                f"25. inches square to feet square.\n"
                f"26. inches square to centimeters square.\n"
                f"27. inches square to milimeters square.\n"
                f"28. centimeters square to meters square.\n"
                f"29. centimeters square to feet square.\n"
                f"30. centimeters square to inches square.\n"
                f"31. centimeters square to milimeters square.\n"
                f"32. milimeters square to meters square.\n"
                f"33. milimeters square to feet square.\n"
                f"34. milimeters square to inches square.\n"
                f"35. milimeters square to centimeters square.\n"
                f"36. kilograms to pounds.\n"
                f"37. kilograms to ounces.\n"
                f"38. kilograms to grams.\n"
                f"39. pounds to kilograms.\n"
                f"40. pounds to ounces.\n"
                f"41. pounds to grams.\n"
                f"42. ounces to kilograms.\n"
                f"43. ounces to pounds.\n"
                f"44. ounces to grams.\n"
                f"45. grams to kilograms.\n"
                f"46. grams to pounds.\n"
                f"47. grams to ounces.\n"
                f"48. meters cubed to feet cubed.\n"
                f"49. meters cubed to inches cubed.\n"
                f"50. meters cubed to centimeters cubed.\n"
                f"51. meters cubed to milimeters cubed.\n"
                f"52. feet cubed to meters cubed.\n"
                f"53. feet cubed to inches cubed.\n"
                f"54. feet cubed to centimeters cubed.\n"
                f"55. feet cubed to milimeters cubed.\n"
                f"56. inches cubed to meters cubed.\n"
                f"57. inches cubed to feet cubed.\n"
                f"58. inches cubed to centimeters cubed.\n"
                f"59. inches cubed to milimeters cubed.\n"
                f"60. centimeters cubed to meters cubed.\n"
                f"61. centimeters cubed to feet cubed.\n"
                f"62. centimeters cubed to inches cubed.\n"
                f"63. centimeters cubed to milimeters cubed.\n"
                f"64. milimeters cubed to meters cubed.\n"
                f"65. milimeters cubed to feet cubed.\n"
                f"66. milimeters cubed to inches cubed.\n"
                f"67. milimeters cubed to centimeters cubed.\n"
                f"68. kelvin to celcius.\n"
                f"69. kelvin to rankine.\n"
                f"70. kelvin to farenheit.\n"
                f"71. celcius to kelvin.\n"
                f"72. celcius to rankine.\n"
                f"73. celcius to farenheit.\n"
                f"74. rankine to kelvin.\n"
                f"75. rankine to celcius.\n"
                f"76. rankine to farenheit.\n"
                f"77. farenheit to kelvin.\n"
                f"78. farenheit to celcius.\n"
                f"79. farenheit to rankine.\n"
                f"80. pascals to psi.\n"
                f"81. pascals to bar.\n"
                f"82. psi to pascals.\n"
                f"83. psi to bar.\n"
                f"84. bar to pascals.\n"
                f"85. bar to psi.\n"
                f"86. degrees to radians.\n"
                f"87. radians to degrees.\n"
                f"88. degrees per second to rpm.\n"
                f"89. degrees per second to rps.\n"
                f"90. rpm to degrees per second.\n"
                f"91. rps to degrees per second.\n"
                f"92. rpm to degrees per minute.\n"
                f"93. rps to degrees per minute.\n"
                f"94. rpm to radians per minute.\n"
                f"95. rpm to radians per second.\n"
                f"96. rps to radians per minute.\n"
                f"97. rps to radians per second.\n"
                f"98. circumference to diameter.\n"
                f"99. circumference to radius.\n"
                f"100. circumference to area.\n"
                f"101. diameter to circumference.\n"
                f"102. diameter to radius.\n"
                f"103. radius to circumference.\n"
                f"104. radius to diameter.\n"
                f"105. radius to area.\n"
                f"106. area to circumference.\n"
                f"107. area to diameter.\n"
                f"108. area to radius.\n"
                f"109. sector area.\n")

    while True:

        try:
            inpt = int(input(menu_str))
        except Exception:
            print("Invalid input!. Try again.")
            continue
        else:
            if inpt == 1:
                fn_inpt = get_input_value("meters to feet")
                output = ConvertUnits.meters_to_feet(fn_inpt)
                print(output)
                break
            elif inpt == 2:
                fn_inpt = get_input_value("meters to inches")
                output = ConvertUnits.meters_to_inches(fn_inpt)
                print(output)
                break
            elif inpt == 3:
                fn_inpt = get_input_value("meters to centimeters")
                output = ConvertUnits.meters_to_centimeters(fn_inpt)
                print(output)
                break
            elif inpt == 4:
                fn_inpt = get_input_value("meters to milimeters")
                output = ConvertUnits.meters_to_milimeters(fn_inpt)
                print(output)
                break
            elif inpt == 5:
                fn_inpt = get_input_value("feet to meters")
                output = ConvertUnits.feet_to_meters(fn_inpt)
                print(output)
                break
            elif inpt == 6:
                fn_inpt = get_input_value("feet to inches")
                output = ConvertUnits.feet_to_inches(fn_inpt)
                print(output)
                break
            elif inpt == 7:
                fn_inpt = get_input_value("feet_to_centimeters")
                output = ConvertUnits.feet_to_centimeters(fn_inpt)
                print(output)
                break
            elif inpt == 8:
                fn_inpt = get_input_value("feet to milimeters")
                output = ConvertUnits.feet_to_milimeters(fn_inpt)
                print(output)
                break
            elif inpt == 9:
                fn_inpt = get_input_value("inches to meters")
                output = ConvertUnits.inches_to_meters(fn_inpt)
                print(output)
                break
            elif inpt == 10:
                fn_inpt = get_input_value("inches to feet")
                output = ConvertUnits.inches_to_feet(fn_inpt)
                print(output)
                break
            elif inpt == 11:
                fn_inpt = get_input_value("inches to milimeters")
                output = ConvertUnits.inches_to_milimeters(fn_inpt)
                print(output)
                break
            elif inpt == 12:
                fn_inpt = get_input_value("milimeters to meters")
                output = ConvertUnits.milimeters_to_meters(fn_inpt)
                print(output)
                break
            elif inpt == 13:
                fn_inpt = get_input_value("milimeters to feet")
                output = ConvertUnits.milimeters_to_feet(fn_inpt)
                print(output)
                break
            elif inpt == 14:
                fn_inpt = get_input_value("milimeters to inches")
                output = ConvertUnits.milimeters_to_inches(fn_inpt)
                print(output)
                break
            elif inpt == 15:
                fn_inpt = get_input_value("meters square to feet square")
                output = ConvertUnits.meters_square_to_feet_square(fn_inpt)
                print(output)
                break
            elif inpt == 16:
                fn_inpt = get_input_value("meters square to inches square")
                output = ConvertUnits.meters_square_to_inches_square(fn_inpt)
                print(output)
                break
            elif inpt == 17:
                fn_inpt = get_input_value("meters square to centimeters square")
                output = ConvertUnits.meters_square_to_centimeters_square(fn_inpt)
                print(output)
                break
            elif inpt == 18:
                fn_inpt = get_input_value("meters square to milimeters square")
                output = ConvertUnits.meters_square_to_milimeters_square(fn_inpt)
                print(output)
                break
            elif inpt == 19:
                fn_inpt = get_input_value("feet square to meters square")
                output = ConvertUnits.feet_square_to_meters_square(fn_inpt)
                print(output)
                break
            elif inpt == 20:
                fn_inpt = get_input_value("feet square to inches square")
                output = ConvertUnits.feet_square_to_inches_square(fn_inpt)
                print(output)
                break
            elif inpt == 21:
                fn_inpt = get_input_value("feet square to centimeters square")
                output = ConvertUnits.feet_square_to_centimeters_square(fn_inpt)
                print(output)
                break
            elif inpt == 22:
                fn_inpt = get_input_value("feet square to milimeters square")
                output = ConvertUnits.feet_square_to_milimeters_square(fn_inpt)
                print(output)
                break
            elif inpt == 23:
                fn_inpt = get_input_value("inches square to meters square")
                output = ConvertUnits.inches_square_to_meters_square(fn_inpt)
                print(output)
                break
            elif inpt == 24:
                fn_inpt = get_input_value("inches square to feet square")
                output = ConvertUnits.inches_square_to_feet_square(fn_inpt)
                print(output)
                break
            elif inpt == 25:
                fn_inpt = get_input_value("inches square to centimeters square")
                output = ConvertUnits.inches_square_to_centimeters_square(fn_inpt)
                print(output)
                break
            elif inpt == 26:
                fn_inpt = get_input_value("inches square to milimeters square")
                output = ConvertUnits.inches_square_to_milimeters_square(fn_inpt)
                print(output)
                break
            elif inpt == 27:
                fn_inpt = get_input_value("centimeters square to meters square")
                output = ConvertUnits.centimeters_square_to_meters_square(fn_inpt)
                print(output)
                break
            elif inpt == 28:
                fn_inpt = get_input_value("centimeters square to feet square")
                output = ConvertUnits.centimeters_square_to_feet_square(fn_inpt)
                print(output)
                break
            elif inpt == 29:
                fn_inpt = get_input_value("centimeters square to inches square")
                output = ConvertUnits.centimeters_square_to_inches_square(fn_inpt)
                print(output)
                break
            elif inpt == 30:
                fn_inpt = get_input_value("centimeters square to milimeters square")
                output = ConvertUnits.centimeters_square_to_milimeters_square(fn_inpt)
                print(output)
                break
            elif inpt == 31:
                fn_inpt = get_input_value("milimeters square to meters square")
                output = ConvertUnits.milimeters_square_to_meters_square(fn_inpt)
                print(output)
                break
            elif inpt == 32:
                fn_inpt = get_input_value("milimeters square to feet square")
                output = ConvertUnits.milimeters_square_to_feet_square(fn_inpt)
                print(output)
                break
            elif inpt == 33:
                fn_inpt = get_input_value("milimeters square to inches square")
                output = ConvertUnits.milimeters_square_to_inches_square(fn_inpt)
                print(output)
                break
            elif inpt == 34:
                fn_inpt = get_input_value("milimeters square to centimeters square")
                output = ConvertUnits.milimeters_square_to_centimeters_square(fn_inpt)
                print(output)
                break

            else:
                print("Invalid input!. Try again.")
