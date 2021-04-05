# from resistor import Resistor, ParallelResistance, SeriesResistance
#
#
# def test_resistor():
#     resistance = 5
#     resistor = Resistor(resistance)
#     assert isinstance(resistor, Resistor)
#     assert resistor.resistance == resistance
#
# def test_series_resistance_positive():
#     r1 = 5
#     r2 = 5
#     resistor1 = Resistor(r1)
#     resistor2 = Resistor(r2)
#     series_resistance_result = r1 + r2
#     series_resistance = SeriesResistance(resistor1, resistor2)
#
#     assert not isinstance(series_resistance, Resistor)
#     assert not isinstance(series_resistance, ParallelResistance)
#     assert isinstance(series_resistance, SeriesResistance)
#     assert series_resistance.resistance == series_resistance_result
