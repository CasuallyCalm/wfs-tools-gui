from PySide6.QtWidgets import (
    # QFileDialog,
    # QComboBox,
    # QLineEdit,
    QButtonGroup,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QWidget,
)


class USBInput(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("USB Input"))

class MLCInput(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.hide()
        
        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("MLC Input"))

class PlainInput(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.hide()

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Plain Input"))


class InputType(QWidget):
    # input_types = ("USB", "MLC", "Plain")

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.input_types = {"USB": USBInput(), "MLC":MLCInput(), "Plain":PlainInput()}


        layout.addWidget(QLabel("Input Type:"))
        self.input_radio = QButtonGroup()
        self.input_radio.buttonToggled.connect(self.radio_changed)
        for t in self.input_types:
            button = QRadioButton(t)
            if t == "USB":
                button.setChecked(True)
            self.input_radio.addButton(button)
            layout.addWidget(button)
        
        for t in self.input_types.values():
            layout.addWidget(t)
        

        
        layout.setContentsMargins(0,0,0,0)
        layout.addStretch()

    def radio_changed(self, button:QRadioButton):
        print(button.text(), button.isChecked())
        input_widget = self.input_types[button.text()]
        if button.isChecked():
            input_widget.show()
        else:
            input_widget.hide()