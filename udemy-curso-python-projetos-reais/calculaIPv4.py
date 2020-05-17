import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ipv4pyqt5.ipv4lib import *
from ipv4pyqt5.ipv4gui import *


class CalculaIPv4(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnLimpar.clicked.connect(self.limpa_campos)
        self.btnCalcular.clicked.connect(self.calcula_ipv4)

    def calcula_ipv4(self):
        ip = self.txtIP.text()
        prefixo = self.txtPrefixo.text()
        mascara = self.txtMascara.text()

        calc_ipv4_1 = None

        if prefixo:
            calc_ipv4_1 = CalcIPv4(ip=ip, prefixo=prefixo)
        elif mascara:
            calc_ipv4_1 = CalcIPv4(ip=ip, mascara=mascara)

        self.lblIP.setText(calc_ipv4_1.ip)
        self.lblMascara.setText(calc_ipv4_1.mascara)
        self.lblRede.setText(calc_ipv4_1.rede)
        self.lblBroadcast.setText(calc_ipv4_1.broadcast)
        self.lblPrefixo.setText(str(calc_ipv4_1.prefixo))
        self.lblNumeroIPs.setText(str(calc_ipv4_1.numero_ips))

    def limpa_campos(self):
        self.lblBroadcast.setText('')
        self.lblIP.setText('')
        self.lblMascara.setText('')
        self.lblNumeroIPs.setText('')
        self.lblPrefixo.setText('')
        self.lblRede.setText('')
        self.txtIP.setText('')
        self.txtMascara.setText('')
        self.txtPrefixo.setText('')


if __name__ == '__main__':
    # main()
    qt = QApplication(sys.argv)
    calcula_ipv4 = CalculaIPv4()
    calcula_ipv4.show()
    qt.exec_()
