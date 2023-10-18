import sys

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
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
        self.combo_box = QComboBox()
        self.combo_box.addItem("Calculate Cp")
        self.combo_box.addItem("Calculate Tf")
        self.combo_box.activated.connect(self.show_widget_calculator)

        self.combo_box_layout = QHBoxLayout()
        self.combo_box_layout.addWidget(self.combo_box)

        self.cp_from_experiment_app = CpFromExperimentApp()
        self.tf_from_experiment_app = TfFromCpExperimentApp()

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.cp_from_experiment_app)
        self.stacked_widget.addWidget(self.tf_from_experiment_app)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.combo_box_layout)
        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)

    def show_widget_calculator(self):
        self.stacked_widget.setCurrentIndex(self.combo_box.currentIndex())


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
