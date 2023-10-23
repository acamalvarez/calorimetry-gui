from constants import CAL_JOULE, CALORIMETER_CONSTANT, C_K, C_WATER, MM_WATER, WATER_HEAT_CAPACITY_POLYNOMIAL


def calculate_tf_from_experiment(mass_1: float, mass_2: float, T_1: float, T_2: float) -> float:
    numerator = CALORIMETER_CONSTANT * T_1 + C_WATER * (mass_1 * T_1 + mass_2 * T_2)
    denominator = CALORIMETER_CONSTANT + (mass_1 + mass_2) * C_WATER
    return numerator / denominator


def water_heat_capacity_J_mol_K(T: float) -> float:
    polynomial = WATER_HEAT_CAPACITY_POLYNOMIAL
    return polynomial[0] + polynomial[1] * T + polynomial[2] * T**2 + polynomial[3] * T**3


def water_heat_capacity_cal_g_C(T_C: float) -> float:
    T = T_C + C_K
    return water_heat_capacity_J_mol_K(T) / CAL_JOULE / MM_WATER
