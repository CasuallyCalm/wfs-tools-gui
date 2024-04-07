import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .arguments.input_arg import InputType


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        main_widget = QWidget(self)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        layout.addWidget(QLabel("WFS Tools Dir:"))
        tools_dir_layout = QHBoxLayout()
        self.tools_dir = QLineEdit()
        self.tools_dir.textChanged.connect(self.tools_dir_changed)
        tools_dir_layout.addWidget(self.tools_dir)
        dir_button = QPushButton(text="Browse")
        dir_button.clicked.connect(self.set_tools_dir)
        tools_dir_layout.addWidget(dir_button)
        layout.addLayout(tools_dir_layout)

        layout.addWidget(InputType())

        layout.addStretch()
    
    def set_tools_dir(self):
        tools_dir = QFileDialog.getExistingDirectory(caption="WFT Tools Directory")
        if tools_dir:
            self.tools_dir.setText(tools_dir)

    def tools_dir_changed(self, text:str):
        print(text)

def run():
    # sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.setWindowTitle("WFS Tools GUI")
    window.setFixedSize(800,600)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    run()