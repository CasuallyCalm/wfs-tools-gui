from PySide6.QtWidgets import (
    QButtonGroup,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from platforms import PLATFORM

from .input_field import Input


class USBInput(QWidget):
    drives: dict[str, str] = {}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.combo_box = QComboBox()
        layout.addWidget(self.combo_box)
        self.refresh_drives()

    def refresh_drives(self):
        self.combo_box.clear()
        self.drives.clear()
        self.drives = PLATFORM.get_drives()
        self.combo_box.addItems(self.drives.keys())

    def getValue(self):
        return self.drives[self.combo_box.currentText()]


class InputType(QWidget):
    __input_type: str

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        radio_layout = QHBoxLayout()
        # radio_layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(radio_layout)
        self.mlc = Input(
            "",
            "Select MLC Image",
            filter="mlc (mlc.bin);;.bin (*.bin);;All (*)",
            hide=True,
        )
        self.plain = Input("", "Select Mount Path", file_dialog=False, hide=True)
        self.input_types = {
            "USB": USBInput(),
            "MLC": self.mlc,
            "Plain": self.plain,
        }

        radio_layout.addWidget(QLabel("Input Type:"))
        self.input_radio = QButtonGroup()
        self.input_radio.buttonToggled.connect(self.radio_changed)
        for t in self.input_types:
            button = QRadioButton(t)
            if t == "USB":
                button.setChecked(True)
                self.__input_type = t
            self.input_radio.addButton(button)
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
