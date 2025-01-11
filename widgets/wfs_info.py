from PySide6.QtWidgets import QRadioButton, QVBoxLayout, QWidget

from . import wfs_args
from .input_type import InputType


class WFSInfo(QWidget):
    name = "wfs-info"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = InputType()
        self.input.radio.buttonToggled.connect(self.input_type_check)

        self.otp = wfs_args.otp()
        self.seeprom = wfs_args.seeprom()

        layout.addWidget(self.input)
        layout.addWidget(self.otp)
        layout.addWidget(self.seeprom)
        layout.setStretchFactor(layout, 1)
        layout.addStretch()

    def input_type_check(self, button: QRadioButton):
        if button.text() == "Plain":
            self.otp.hide()
            self.seeprom.hide()
        elif button.text() == "MLC":
            self.otp.show()
            self.seeprom.hide()
        elif button.text() == "USB":
            self.otp.show()
            self.seeprom.show()

    @property
    def args(self):
        return [
            "--input",
            self.input.getInput(),
            "--type",
            self.input.getInputType(),
            "--otp",
            self.otp.getValue(),
            "--seeprom",
            self.seeprom.getValue(),
        ]
