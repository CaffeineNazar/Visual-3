from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button 1")
        
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()