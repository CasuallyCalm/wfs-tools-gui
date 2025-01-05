from PySide6.QtWidgets import QLabel, QSpacerItem, QVBoxLayout, QWidget

from . import wfs_args
from .input_type import InputType


class WFSReencryptor(QWidget):
    name = "wfs-reencryptor"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = InputType()
        self.otp = wfs_args.otp()
        self.seeprom = wfs_args.seeprom()

        self.output = InputType(has_none=True)
        self.output_otp = wfs_args.otp()
        self.output_seeprom = wfs_args.seeprom()

        layout.addWidget(QLabel("Input"))
        layout.addWidget(self.input)
        layout.addWidget(self.otp)
        layout.addWidget(self.seeprom)
        layout.addSpacerItem(QSpacerItem(0, 10))
        layout.addWidget(QLabel("Output"))
        layout.addWidget(self.output)
        layout.addWidget(self.output_otp)
        layout.addWidget(self.output_seeprom)

        layout.setStretchFactor(layout, 1)
        layout.addStretch()

    @property
    def args(self):
        _args = [
            "--input",
            self.input.getInput(),
            "--input-type",
            self.input.getInputType(),
            "--input-otp",
            self.otp.getValue(),
            "--input-seeprom",
            self.seeprom.getValue(),
            "--output-otp",
            self.output_otp.getValue(),
            "--output-seeprom",
            self.output_seeprom.getValue(),
        ]
        if self.output.getInput() is None:
            _args.extend(
                [
                    "--output",
                    self.input.getInput(),
                    "--output-type",
                    self.input.getInputType(),
                ]
            )
        else:
            _args.extend(
                [
                    "--output",
                    self.output.getInput(),
                    "--output-type",
                    self.output.getInputType(),
                ]
            )
        return _args
