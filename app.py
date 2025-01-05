import sys
from pathlib import Path

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from platforms import PLATFORM
from widgets.input_field import InputField
from widgets.wfs_extract import WFSExtract
from widgets.wfs_file_injector import WFSFileInjector
from widgets.wfs_info import WFSInfo
from widgets.wfs_reencryptor import WFSReencryptor


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.process: QProcess | None = None

        main_widget = QWidget()
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.tools_dir = InputField(
            "WFS Tools Dir:", "WFS Tools Directory", file_dialog=False
        )

        self.tools_dir.line_edit.textChanged.connect(self.tools_dir_changed)

        self.tabs = QTabWidget()
        self.tabs.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        self.tabs.hide()
        tabs_widgets = {
            "WFS-Info": WFSInfo(),
            "WFS-Extract": WFSExtract(),
            "WFS-Reencryptor": WFSReencryptor(),
            "WFS-File-Injector": WFSFileInjector(),
        }
        self.tab_ids = {
            tab.lower(): self.tabs.addTab(widget, tab)
            for tab, widget in tabs_widgets.items()
        }

        self.execute_button = QPushButton(text="Execute")
        self.execute_button.hide()
        self.execute_button.clicked.connect(self.execute)

        self.cancel_button = QPushButton(text="Cancel")
        self.cancel_button.hide()
        self.cancel_button.clicked.connect(self.cancel)

        layout.addWidget(self.tools_dir)
        layout.addWidget(self.tabs, stretch=0)
        layout.addWidget(self.execute_button)
        layout.addWidget(self.cancel_button)
        layout.addSpacing(20)

        self.logger = QPlainTextEdit()
        self.logger.setReadOnly(True)
        layout.addWidget(self.logger)

    def tools_dir_changed(self, dir: str):
        has_tools = False
        tool_path = Path(dir)
        for tab_id in self.tab_ids.values():
            self.tabs.setTabVisible(tab_id, False)
        if tool_path.is_dir():
            for item in tool_path.iterdir():
                if item.is_file() and item.stem.lower() in self.tab_ids:
                    self.tabs.setTabVisible(self.tab_ids[item.stem.lower()], True)
                    has_tools = True
        if has_tools:
            self.execute_button.show()
            self.tabs.show()
        else:
            self.execute_button.hide()
            self.tabs.hide()

    def log(self, msg: str):
        self.logger.appendPlainText(msg)

    def cancel(self):
        if self.process:
            self.process.terminate()
            self.log("Cancelling Process!")

    def execute(self):
        self.execute_button.hide()
        self.cancel_button.show()

        tool = self.tabs.currentWidget()
        bin = str(Path(self.tools_dir.getValue(), tool.name + PLATFORM.extension))
        self.process = QProcess()
        self.process.readyReadStandardError.connect(self.log_err)
        self.process.readyReadStandardOutput.connect(self.log_std)
        self.process.finished.connect(self.finished)
        self.process.setProgram(bin)
        self.process.setArguments(tool.args)
        self.process.start()

    def log_std(self):
        msg = self.process.readAllStandardOutput()
        try:
            self.log(bytes(msg).decode())
        except UnicodeDecodeError:
            pass

    def log_err(self):
        msg = self.process.readAllStandardError()
        try:
            self.log(bytes(msg).decode())
        except UnicodeDecodeError:
            pass

    def finished(self):
        self.log("----------------------------------------------------------")
        self.process = None
        self.execute_button.show()
        self.cancel_button.hide()


def run():
    # sys.argv += ["-platform", "windows:darkmode=2"]
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")

    window = MainWindow()
    window.setWindowTitle("WFS Tools GUI")
    # window.setBaseSize(800, 600)
    window.resize(800, 600)
    # window.setFixedSize(800, 600)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run()
