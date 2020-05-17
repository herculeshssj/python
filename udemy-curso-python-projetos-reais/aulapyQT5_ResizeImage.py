"""
Para baixar o QT Design para Windows ou Mac:

https://build-system.fman.io/qt-designer-download

Para converter o arquivo design.ui para um arquivo .py, execute o comando
abaixo com o virtualenv ativado:

pyuic5 design.ui -o design.py
"""

import sys
import os
from ui.design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QImage


class RedimensionarImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        super().setupUi(self)
        self.btnAbrirArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar_imagem)
        self.btnSalvar.clicked.connect(self.salvar_imagem)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self, 'Abrir imagem', os.getenv('HOME'))
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap = self.original_img
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar_imagem(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap = self.nova_imagem
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar_imagem(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self, 'Salvar imagem', os.getenv('HOME'))
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = RedimensionarImagem()
    app.show()
    qt.exec_()
