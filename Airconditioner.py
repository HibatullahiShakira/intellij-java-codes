class AirConditioner:
    def __init__(self, ):
        self.temperature = 25
        self.is_ac_on = False

    def ac_is_off_by_default(self):
        return self.is_ac_on

    def turn_ac_on(self):
        self.is_ac_on = True
        return self.is_ac_on

    def turn_off_ac(self):
        self.is_ac_on = False
        return self.is_ac_on

    def get_ac_temperature(self):
        return self.temperature

    def increase_ac_temperature(self):
        self.is_ac_on = True
        self.temperature += 1
        return self.temperature

    def decrease_ac_temperature(self):
        self.is_ac_on = True
        self.temperature -= 1
        return self.temperature

    def below_thirty_degree_increase(self):
        self.is_ac_on = True
        if self.temperature < 30:
            self.temperature += 1
            return self.temperature

    def above_sixteen_degree_decrease(self):
        self.is_ac_on = True
        if self.temperature > 16:
            self.temperature -= 1
            return self.temperature






