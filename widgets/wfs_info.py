from PySide6.QtWidgets import QVBoxLayout, QWidget

from . import wfs_args
from .input_type import InputType


class WFSInfo(QWidget):
    name = "wfs-info"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = InputType()
        self.otp = wfs_args.otp()
        self.seeprom = wfs_args.seeprom()

        layout.addWidget(self.input)
        layout.addWidget(self.otp)
        layout.addWidget(self.seeprom)
        layout.setStretchFactor(layout, 1)
        layout.addStretch()

    @property
    def args(self):
        # return f"--input {self.input_type.getInput()} --type {self.input_type.getInputType()} --otp {self.otp.getValue()} --seeprom {self.seeprom.getValue()}"
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
