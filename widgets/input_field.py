from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Input(QWidget):

    def __init__(self, title:str, caption:str, parent: QWidget | None = None,  file_dialog = True, filter:str = "", hide=False, show_button=True) -> None:
        super().__init__(parent)

        self._file_dialog = file_dialog
        self._caption = caption
        self._filter = filter

        if hide:
            self.hide()

        layout = QVBoxLayout()
        self.setLayout(layout)

        if title:
            layout.addWidget(QLabel(title))

        self.line_edit = QLineEdit()

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.line_edit)
        layout.addLayout(input_layout)
        if show_button:
            button = QPushButton(text="Browse")
            button.clicked.connect(self._set_input)
            input_layout.addWidget(button)

    def _set_input(self):
        if self._file_dialog:
            directory, _ = QFileDialog.getOpenFileName(caption=self._caption, filter=self._filter)
        else:
            directory = QFileDialog.getExistingDirectory(caption=self._caption)
        if directory:
            self.line_edit.setText(directory)
    
    def getValue(self)-> str:
        return self.line_edit.text()