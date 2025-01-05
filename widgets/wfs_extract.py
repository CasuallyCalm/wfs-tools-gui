from PySide6.QtWidgets import QCheckBox, QVBoxLayout, QWidget

from . import wfs_args
from .input_type import InputType


class WFSExtract(QWidget):
    name = "wfs-extract"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = InputType()
        self.otp = wfs_args.otp()
        self.seeprom = wfs_args.seeprom()
        self.output = wfs_args.output()
        self.dump_path = wfs_args.dump_path()
        self.dump_path.line_edit.setText("/")
        self.verbose = QCheckBox("Verbose Output")
        self.verbose.setChecked(True)

        layout.addWidget(self.input)
        layout.addWidget(self.otp)
        layout.addWidget(self.seeprom)
        layout.addWidget(self.output)
        layout.addWidget(self.dump_path)
        layout.addWidget(self.verbose)
        layout.setStretchFactor(layout, 1)

    @property
    def args(self):
        _args = [
            "--input",
            self.input.getInput(),
            "--type",
            self.input.getInputType(),
            "--otp",
            self.otp.getValue(),
            "--seeprom",
            self.seeprom.getValue(),
            "--output",
            self.output.getValue(),
            "--dump-path",
            "/" if not self.dump_path.line_edit.text() else self.dump_path.getValue(),
        ]
        if self.verbose.isChecked():
            _args.append("--verbose")
        return _args
