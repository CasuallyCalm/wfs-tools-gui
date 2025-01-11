from PySide6.QtWidgets import (
    QButtonGroup,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from platforms import PLATFORM

from .input_field import InputField


class USBInput(QWidget):
    drives: dict[str, str] = {}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        refresh = QPushButton(text="Refresh Drives")
        refresh.clicked.connect(self.refresh_drives)

        self.combo_box = QComboBox()

        layout.addWidget(refresh)
        layout.addWidget(self.combo_box, stretch=1)

        self.refresh_drives()

    def refresh_drives(self):
        self.combo_box.clear()
        self.drives.clear()
        self.drives = PLATFORM.get_drives()
        self.combo_box.addItems(self.drives.keys())

    def getValue(self):
        return self.drives[self.combo_box.currentText()]


class SameAsInput(QWidget):
    def getValue(self):
        return


class InputType(QWidget):
    __input_type: str

    def __init__(
        self,
        parent: QWidget | None = None,
        has_none: bool = False,
        output: bool = False,
    ) -> None:
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        radio_layout = QHBoxLayout()
        layout.addLayout(radio_layout)
        self.mlc = InputField(
            "",
            "Select MLC Image",
            filter="mlc (mlc.*);;.bin (*.bin);;.img (*.img);;All (*)",
            hide=True,
            file_dialog=not output,
            save_file_dialog=output,
        )
        self.plain = InputField(
            "",
            "Select Plain Image",
            filter=".bin (*.bin);;.img (*.img);;All (*)",
            hide=True,
            file_dialog=not output,
            save_file_dialog=output,
        )
        self.input_types = {
            "USB": USBInput(),
            "MLC": self.mlc,
            "Plain": self.plain,
        }
        if has_none:
            self.input_types["Same as Input"] = SameAsInput()

        radio_layout.addWidget(QLabel("WFS File Type:"))
        self.radio = QButtonGroup()
        self.radio.buttonToggled.connect(self.radio_changed)
        for t in self.input_types:
            button = QRadioButton(t)
            if t in ["USB", "Same as Input"]:
                button.setChecked(True)
                self.__input_type = t
            self.radio.addButton(button)
            radio_layout.addWidget(button)

        for t in self.input_types.values():
            layout.addWidget(t)

        radio_layout.addStretch()

    def radio_changed(self, button: QRadioButton):
        input_widget = self.input_types[button.text()]
        if button.isChecked():
            input_widget.show()
            self.__input_type = button.text()
        else:
            input_widget.hide()

    def getInputType(self):
        return self.__input_type.lower()

    def getInput(self):
        return self.input_types[self.__input_type].getValue()
