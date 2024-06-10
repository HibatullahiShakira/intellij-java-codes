import unittest
from Airconditioner import *


class TestAirConditionerFunction(unittest.TestCase):
    def test_that_ac_is_off_by_default(self):
        self.assertFalse(AirConditioner().ac_is_off_by_default(), "The air conditioner should be off by default")

    def test_that_ac_can_on(self):
        self.assertTrue(AirConditioner().turn_ac_on(), "The air conditioner is now on")

    def test_that_ac_can_off(self):
        self.assertFalse(AirConditioner().turn_off_ac(), "The air conditioner is off")

    def test_that_function_can_get_temperature(self):
        expected_temperature = 25
        actual_temperature = AirConditioner().get_ac_temperature()
        self.assertEqual(actual_temperature, expected_temperature)

    def test_that_ac_can_increase_temperature(self):
        expected_temperature_increase = 26
        actual_temperature_increase = AirConditioner().increase_ac_temperature()
        self.assertEqual(expected_temperature_increase, actual_temperature_increase)

    def test_that_ac_is_on_before_increase_temperature(self):
        self.assertTrue(AirConditioner().increase_ac_temperature, "The ac is on before increasing temperature")

    def test_that_ac_can_decrease_temperature(self):
        expected_temperature_decrease = 24
        actual_temperature_decrease = AirConditioner().decrease_ac_temperature()
        self.assertEqual(expected_temperature_decrease, actual_temperature_decrease)

    def test_that_ac_is_on_before_decrease_temperature(self):
        self.assertTrue(AirConditioner().decrease_ac_temperature, "The ac is on before increasing temperature")

    def test_to_check_if_the_ac_temperature_below_thirty_degree_can_increase(self):
        expected_below_thirty_degree_increase = 26
        actual_below_thirty_degree_increase = AirConditioner().below_thirty_degree_increase()
        self.assertEqual(expected_below_thirty_degree_increase, actual_below_thirty_degree_increase)

    def test_to_check_if_the_ac_temperature_above_sixteen_degree_can_decrease(self):
        expected_above_sixteen_degree_decrease = 24
        actual_above_sixteen_degree_decrease = AirConditioner().above_sixteen_degree_decrease()
        self.assertEqual(expected_above_sixteen_degree_decrease, actual_above_sixteen_degree_decrease)






