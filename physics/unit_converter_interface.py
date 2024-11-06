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
                f"14. milimeters to inches.\n"
                f"15. meters square to inches square.\n"
                f"16. meters square to inches square.\n"
                f"17. meters square to centimeters square.\n"
                f"18. meters square to milimeters square.\n"
                f"19. feet square to meters square.\n"
                f"20. feet square to inches square.\n"
                f"21. feet square to centimeters square.\n"
                f"22. feet square to milimeters square.\n"
                f"23. inches square to meters square.\n"
                f"24. inches square to feet square.\n"
                f"25. inches square to milimeters square.\n"
                f"26. milimeters square to meters square.\n"
                f"27. milimeters square to feet square.\n"
                f"28. milimeters square to inches square.\n"
                f"29. kilograms to pounds.\n"
                f"30. kilograms to ounces.\n"
                f"31. kilograms to grams.\n"
                f"32. pounds to kilograms.\n"
                f"33. pounds to ounces.\n"
                f"34. pounds to grams.\n"
                f"35. ounces to kilograms.\n"
                f"36. ounces to pounds.\n"
                f"37. ounces to grams.\n"
                f"38. grams to kilograms.\n"
                f"39. grams to pounds.\n"
                f"40. grams to ounces.\n"
                f"41. meters cubed to feet cubed.\n"
                f"42. meters cubed to inches cubed.\n"
                f"43. meters cubed to centimeters cubed.\n"
                f"44. meters cubed to milimeters cubed.\n"
                f"45. feet cubed to meters cubed.\n"
                f"46. feet cubed to inches cubed.\n"
                f"47. feet cubed to centimeters cubed.\n"
                f"48. feet cubed to milimeters cubed.\n"
                f"49. inches cubed to meters cubed.\n"
                f"50. inches cubed to feet cubed.\n"
                f"51. inches cubed to centimeters cubed.\n"
                f"52. inches cubed to milimeters cubed.\n"
                f"53. centimeters cubed to meters cubed.\n"
                f"54. centimeters cubed to feet cubed.\n"
                f"55. centimeters cubed to inches cubed.\n"
                f"56. centimeters cubed to milimeters cubed.\n"
                f"57. milimeters cubed to meters cubed.\n"
                f"58. milimeters cubed to feet cubed.\n"
                f"59. milimeters cubed to inches cubed.\n"
                f"60. milimeters cubed to centimeters cubed.\n"
                f"61. kelvin to celcius.\n"
                f"62. kelvin to rankine.\n"
                f"63. kelvin to farenheit.\n"
                f"64. celcius to kelvin.\n"
                f"65. celcius to rankine.\n"
                f"66. celcius to farenheit.\n"
                f"67. rankine to kelvin.\n"
                f"68. rankine to celcius.\n"
                f"69. rankine to farenheit.\n"
                f"70. farenheit to kelvin.\n"
                f"71. farenheit to celcius.\n"
                f"72. farenheit to rankine.\n"
                f"73. pascals to psi.\n"
                f"74. pascals to bar.\n"
                f"75. psi to pascals.\n"
                f"76. psi to bar.\n"
                f"77. bar to pascals.\n"
                f"78. bar to psi.\n"
                f"79. degrees to radians.\n"
                f"80. radians to degrees.\n"
                f"81. degrees per second to rpm.\n"
                f"82. degrees per second to rps.\n"
                f"83. rpm to degrees per second.\n"
                f"84. rps to degrees per second.\n"
                f"85. rpm to degrees per minute.\n"
                f"86. rps to degrees per minute.\n"
                f"87. rpm to radians per minute.\n"
                f"88. rpm to radians per second.\n"
                f"89. rps to radians per minute.\n"
                f"90. rps to radians per second.\n"
                f"91. circumference to diameter.\n"
                f"92. circumference to radius.\n"
                f"93. circumference to area.\n"
                f"94. diameter to circumference.\n"
                f"95. diameter to radius.\n"
                f"96. radius to circumference.\n"
                f"97. radius to diameter.\n"
                f"98. radius to area.\n"
                f"99. area to circumference.\n"
                f"100. area to diameter.\n"
                f"101. area to radius.\n"
                f"102. sector area.\n")

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
            else:
                print("Invalid input!. Try again.")
