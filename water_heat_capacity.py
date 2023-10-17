from constants import CAL_JOULE, CC_MC, C_K, CW, MM_WATER, WATER_HEAT_CAPACITY_POLYNOMIAL


def calculate_tf(mass_1: float, mass_2: float, temperature_1: float, temperature_2: float) -> float:
    numerator = CC_MC * temperature_1 + CW * (mass_1 * temperature_1 + mass_2 * temperature_2)
    denominator = CC_MC + (mass_1 + mass_2) * CW
    return numerator / denominator


def water_heat_capacity_J_mol_K(T: float) -> float:
    polynomial = WATER_HEAT_CAPACITY_POLYNOMIAL
    return polynomial[0] + polynomial[1] * T + polynomial[2] * T**2 + polynomial[3] * T**3


def water_heat_capacity_cal_g_C(T_C: float) -> float:
    T = T_C + C_K
    return water_heat_capacity_J_mol_K(T) / CAL_JOULE / MM_WATER

