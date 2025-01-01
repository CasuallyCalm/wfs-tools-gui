import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from widgets.input_field import Input
from widgets.input_type import InputType


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        main_widget = QWidget(self)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.tools_dir = Input(
            "WFS Tools Dir:", "WFS Tools Directory", file_dialog=False
        )
        self.otp = Input(
            "OTP:", "Slect OTP File", filter="otp (otp.bin);;bin (*.bin);;All (*)"
        )
        self.seeprom = Input(
            "Seeprom:",
            "Slect Seeprom File",
            filter="seeprom (seeprom.bin);;bin (*.bin);;All (*)",
        )
        self.inject_file = Input(
            "Inject File", "Slect File to Inject", filter="zip (*.zip);;All (*)"
        )
        # self.mlc = Input("", "Select MLC Image", filter="image (*.img);;All (*)", hide=True)
        # self.plain = Input("", "Select Mount Path", file_dialog=False, hide=True)

        layout.addWidget(self.tools_dir)
        layout.addWidget(InputType())
        # layout.addWidget(self.mlc)
        # layout.addWidget(self.plain)
        layout.addWidget(self.otp)
        layout.addWidget(self.seeprom)
        layout.addWidget(self.inject_file)

        layout.addStretch()


def run():
    # sys.argv += ["-platform", "windows:darkmode=2"]
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")

    window = MainWindow()
    window.setWindowTitle("WFS Tools GUI")
    window.setFixedSize(800, 600)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run()
