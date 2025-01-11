from PySide6.QtWidgets import QRadioButton, QVBoxLayout, QWidget

from . import wfs_args
from .input_field import InputField
from .input_type import InputType


class WFSFileInjector(QWidget):
    name = "wfs-file-injector"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = InputType()
        self.input.radio.buttonToggled.connect(self.input_type_check)

        self.otp = wfs_args.otp()
        self.seeprom = wfs_args.seeprom()
        self.inject_file = InputField("Inject File", "File to Inject")
        self.inject_path = InputField(
            "Inject Path", "WFS Inject Path", show_button=False
        )

        layout.addWidget(self.input)
        layout.addWidget(self.otp)
        layout.addWidget(self.seeprom)
        layout.addWidget(self.inject_file)
        layout.addWidget(self.inject_path)
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
            "--image",
            self.input.getInput(),
            "--type",
            self.input.getInputType(),
            "--otp",
            self.otp.getValue(),
            "--seeprom",
            self.seeprom.getValue(),
            "--inject-file",
            self.inject_file.getValue(),
            "--inject-path",
            self.inject_path.getValue(),
        ]
