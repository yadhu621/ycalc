class Calculator(object):
    """
    A class to calculate simple and compound interest

    Methods
    -------
    calc_si(principle, rate, years):
    calc_ci(principle, rate, years):
    """
    def calc_si(self, principle, rate, years):
        """
        Returns the simple interest
            Parameters:
                    principle (int): A decimal integer
                    rate (int): Another decimal integer
                    years (int): Another decimal integer

            Returns:
                    simple_interest (int): Another decimal integer
        """
        simple_interest = principle * rate * years
        return simple_interest

    def calc_ci(self, principle, rate, years):
        """
        Returns the compound interest
            Parameters:
                    principle (int): A decimal integer
                    rate (int): Another decimal integer
                    years (int): Another decimal integer

            Returns:
                    compound_interest (int): Another decimal integer
        """
        compound_interest = principle*(1 + rate)**years - principle
        return compound_interest
