from PySide6.QtWidgets import *
from PySide6.QtGui import *


COL_SIZE = 6


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Theme Icons')
        layout = QGridLayout(self)
        
        count = 0
        
        for attr in dir(QIcon.ThemeIcon):
            if '_' not in attr:
                ico = QIcon.fromTheme(getattr(QIcon.ThemeIcon, attr))
                
                if ico.isNull():
                    print(f'{attr} is NULL')
                    continue
                
                btn = QPushButton(icon=ico, text=attr)
                layout.addWidget(btn, count // COL_SIZE, count % COL_SIZE)
                
                count += 1


if __name__ == '__main__':
    app = QApplication()
    w = Widget()
    w.show()
    app.exec()
