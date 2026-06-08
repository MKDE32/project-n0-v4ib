#!/usr/bin/env python3

import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QTextBrowser
from markdown import markdown


class MarkdownViewer(QTextBrowser):
    def __init__(self, filename):
        super().__init__()

        self.setWindowTitle(Path(filename).name)
        self.resize(900, 700)

        with open(filename, "r", encoding="utf-8") as f:
            md_text = f.read()

        self.setHtml(markdown(md_text, extensions=["fenced_code", "tables"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        from PyQt6.QtWidgets import QFileDialog

        filename, _ = QFileDialog.getOpenFileName(
            None,
            "Open Markdown File",
            "",
            "Markdown Files (*.md);;All Files (*)"
        )

        if not filename:
            sys.exit(0)

    viewer = MarkdownViewer(filename)
    viewer.show()

    sys.exit(app.exec())
