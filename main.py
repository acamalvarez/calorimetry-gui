import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QStackedWidget,
    QWidget,
)

from Cp_from_experiment import CpFromExperimentApp
from Tf_from_cp_experiment import TfFromCpExperimentApp


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.stacked_widget = QStackedWidget(self)

        self.cp_from_experiment_app = CpFromExperimentApp()
        self.tf_from_experiment_app = TfFromCpExperimentApp()

        self.stacked_widget.addWidget(self.cp_from_experiment_app)
        self.stacked_widget.addWidget(self.tf_from_experiment_app)

        self.show_calculate_cp_button = QPushButton("Calculate Cp", self)
        self.show_calculate_tf_button = QPushButton("Calculate Tf", self)

        self.show_calculate_cp_button.clicked.connect(self.show_calculate_cp_app)
        self.show_calculate_tf_button.clicked.connect(self.show_calculate_tf_app)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.show_calculate_cp_button)
        button_layout.addWidget(self.show_calculate_tf_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def show_calculate_cp_app(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_calculate_tf_app(self):
        self.stacked_widget.setCurrentIndex(1)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
