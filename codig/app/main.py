import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QLabel
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class GlassFrame(QFrame):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        color = QColor(255, 255, 255, 30)
        painter.setBrush(color)

        painter.drawRoundedRect(self.rect(), 10, 10)

class HoverLabel(QLabel):
    def __init__(self, normal, hover, parent=None):
        super().__init__(parent)

        self.normal = QPixmap(normal).scaled(QSize(100, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.hover = QPixmap(hover).scaled(QSize(100, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.setPixmap(self.normal)

    def enterEvent(self, event):
        self.setPixmap(self.hover)

    def leaveEvent(self, event):
        self.setPixmap(self.normal)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")
        self.setGeometry(100, 100, 500, 500)

        glassFrame = GlassFrame(self)
        glassFrame.setGeometry(50, 50, 400, 400)

        image_label = HoverLabel('windows_bw.png', 'windows.png', glassFrame)
        image_label.setGeometry(150, 100, 100, 100)

        button = QPushButton("Descargar herramientas", glassFrame)
        button.setGeometry(50, 250, 300, 100)
        button.clicked.connect(self.descargar_archivo)

        self.manager = QNetworkAccessManager()

    def descargar_archivo(self):
        url = "http://ejemplo.com/archivo.zip"
        file_name = "archivo.zip"
        request = QNetworkRequest(url)
        reply = self.manager.get(request)
        reply.finished.connect(lambda: self.descarga_terminada(reply, file_name))

    def descarga_terminada(self, reply, file_name):
        data = reply.readAll()
        with open(file_name, "wb") as f:
            f.write(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    