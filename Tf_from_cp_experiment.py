from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout

from water_heat_capacity import calculate_tf_from_experiment


class TfFromCpExperimentApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout()

        label_temperature_1 = QLabel("Temperature 1 / °C:", self)
        self.input_temperature_1 = QLineEdit(self)
        label_temperature_2 = QLabel("Temperature 2 / °C:", self)
        self.input_temperature_2 = QLineEdit(self)

        label_mass_1 = QLabel("Mass 1 / g:", self)
        self.input_mass_1 = QLineEdit(self)
        label_mass_2 = QLabel("Mass 2 / g:", self)
        self.input_mass_2 = QLineEdit(self)

        grid_layout.addWidget(label_temperature_1, 0, 0)
        grid_layout.addWidget(self.input_temperature_1, 0, 1)
        grid_layout.addWidget(label_temperature_2, 1, 0)
        grid_layout.addWidget(self.input_temperature_2, 1, 1)

        grid_layout.addWidget(label_mass_1, 0, 2)
        grid_layout.addWidget(self.input_mass_1, 0, 3)
        grid_layout.addWidget(label_mass_2, 1, 2)
        grid_layout.addWidget(self.input_mass_2, 1, 3)

        self.addButton = QPushButton("Calculate", self)
        self.addButton.clicked.connect(self.add_numbers)

        self.result_label = QLabel("", self)

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(self.addButton)
        bottom_layout.addWidget(self.result_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(grid_layout)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        self.setWindowTitle("Calorimetry")
        self.show()

    def add_numbers(self):
        try:
            mass_1 = float(self.input_mass_1.text())
            temperature_1 = float(self.input_temperature_1.text())
            mass_2 = float(self.input_mass_2.text())
            temperature_2 = float(self.input_temperature_2.text())
            result = round(calculate_tf_from_experiment(mass_1, mass_2, temperature_1, temperature_2), 1)
            self.result_label.setText(f"Equilibrium temperature: {result} °C")
        except ValueError:
            self.result_label.setText("Please enter valid numbers.")
        except ZeroDivisionError:
            self.result_label.setText("Division by zero is not possible.")
