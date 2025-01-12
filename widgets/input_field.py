from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class InputField(QWidget):
    def __init__(
        self,
        title: str,
        caption: str,
        parent: QWidget | None = None,
        file_dialog=True,
        save_file_dialog=False,
        filter: str = "",
        hide=False,
        show_button=True,
    ) -> None:
        super().__init__(parent)

        self._file_dialog = file_dialog
        self._save_file_dialog = save_file_dialog
        self._caption = caption
        self._filter = filter

        if hide:
            self.hide()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        if title:
            layout.addWidget(QLabel(title))

        self.line_edit = QLineEdit()

        layout.addWidget(self.line_edit)
        # layout.addLayout(input_layout)
        if show_button:
            button = QPushButton(text="Browse")
            button.clicked.connect(self._set_input)
            layout.addWidget(button)

    def _set_input(self):
        if self._file_dialog:
            directory, _ = QFileDialog.getOpenFileName(
                caption=self._caption, filter=self._filter
            )
        elif self._save_file_dialog:
            directory, _ = QFileDialog.getSaveFileName(
                caption=self._caption, filter=self._filter
            )
        else:
            directory = QFileDialog.getExistingDirectory(caption=self._caption)
        if directory:
            self.line_edit.setText(directory)

    def getValue(self) -> str:
        return str(Path(self.line_edit.text()))
