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
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} file.md")
        sys.exit(1)

    app = QApplication(sys.argv)

    viewer = MarkdownViewer(sys.argv[1])
    viewer.show()

    sys.exit(app.exec())
