from PySide6.QtWidgets import (
    QButtonGroup,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from .input_field import Input


class USBInput(QLabel):
    pass

class InputType(QWidget):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        radio_layout = QHBoxLayout()
        layout.addLayout(radio_layout)
        self.mlc = Input( "", "Select MLC Image", filter="image (*.img);;All (*)", hide=True)
        self.plain = Input("", "Select Mount Path", file_dialog=False, hide=True) 
        self.input_types = {"USB": USBInput(text="USB Input"), "MLC":self.mlc, "Plain":self.plain}


        radio_layout.addWidget(QLabel("Input Type:"))
        self.input_radio = QButtonGroup()
        self.input_radio.buttonToggled.connect(self.radio_changed)
        for t in self.input_types:
            button = QRadioButton(t)
            if t == "USB":
                button.setChecked(True)
            self.input_radio.addButton(button)
            radio_layout.addWidget(button)
        
        for t in self.input_types.values():
            layout.addWidget(t)
        

        
        # layout.setContentsMargins(0,0,0,0)
        radio_layout.addStretch()

    def radio_changed(self, button:QRadioButton):
        print(button.text(), button.isChecked())
        input_widget = self.input_types[button.text()]
        if button.isChecked():
            input_widget.show()
        else:
            input_widget.hide()