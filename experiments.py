from constants import CALORIMETER_CONSTANT, C_WATER


class Experiment:
    def __init__(self, mass_1: float, mass_2: float, T_1: float, T_2: float, T_f: float) -> None:
        self.mass_1 = mass_1
        self.mass_2 = mass_2
        self.T_1 = T_1
        self.T_2 = T_2
        self.T_f = T_f

    def calculate_cp(self) -> float:
        return round(
            (
                CALORIMETER_CONSTANT
                * (self.T_f - self.T_1)
                / (self.mass_1 * self.T_1 + self.mass_2 * self.T_2 - (self.mass_1 + self.mass_2) * self.T_f)
            ),
            2,
        )

    def calculate_li(self) -> float:
        return round(
            (
                (C_WATER * self.mass_1 + CALORIMETER_CONSTANT) * (self.T_1 - self.T_f)
                - C_WATER * self.mass_2 * (self.T_f - self.T_2)
            )
            / self.mass_2,
            2,
        )

    def calculate_lv(self) -> float:
        return round(
            (
                (C_WATER * self.mass_1 + CALORIMETER_CONSTANT) * (self.T_f - self.T_1)
                - C_WATER * self.mass_2 * (self.T_2 - self.T_f)
            )
            / self.mass_2,
            2,
        )
