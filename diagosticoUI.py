from PyQt5.QtWidgets import QMainWindow, QCheckBox, QPushButton, QMessageBox, QStackedWidget, QLabel
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from sistemaExpertoMecanica import SistemaExpertoMecanica
from diagnostico2UI import Diagnostico2
import sys



class Diagnostico(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciarGui()
        self.SistemaExperto = SistemaExpertoMecanica()
        self.show()
        
    def iniciarGui(self):
        uic.loadUi(r'diagnosticoUI.ui', self)

        self.stackedWidget = self.findChild(QStackedWidget, 'stackedWidget')

        self.golpeteo_motor = self.findChild(QCheckBox, 'checkBox')
        self.humo_Negro = self.findChild(QCheckBox, 'checkBox_2')
        self.tirones = self.findChild(QCheckBox, 'checkBox_3')
        self.luces = self.findChild(QCheckBox, 'checkBox_4')
        self.problemas_arranque = self.findChild(QCheckBox, 'checkBox_5')
        self.ruidos_encendido = self.findChild(QCheckBox, 'checkBox_6')
        self.perdida_refr = self.findChild(QCheckBox, 'checkBox_7')
        self.humo_blanco = self.findChild(QCheckBox, 'checkBox_8')
        self.testigo_temperatura = self.findChild(QCheckBox, 'checkBox_9')
        self.testigo_presion_aceite = self.findChild(QCheckBox, 'checkBox_10')
        self.ruidos_metalicos = self.findChild(QCheckBox, 'checkBox_11')
        self.perdida_potencia = self.findChild(QCheckBox, 'checkBox_12')
        self.humo_azul = self.findChild(QCheckBox, 'checkBox_14')
        self.vibraciones = self.findChild(QCheckBox, 'checkBox_13')
        self.consumo_Aceite = self.findChild(QCheckBox, 'checkBox_15')
        self.detiene = self.findChild(QCheckBox, 'checkBox_16')
        self.testigos_irregulares = self.findChild(QCheckBox, 'checkBox_17')
        self.aceleracion_lenta = self.findChild(QCheckBox, 'checkBox_18')
        self.consumo_combustible = self.findChild(QCheckBox, 'checkBox_19')
        self.sobrecalentamiento = self.findChild(QCheckBox, 'checkBox_20')
        self.humo_excesivo = self.findChild(QCheckBox, 'checkBox_21')


        self.diagnostico = self.findChild(QPushButton, 'pushButton')
        self.changeD = self.findChild(QPushButton, 'pushButton_2')

        self.label = self.findChild(QLabel, 'label_2')
    
        self.diagnostico2 = Diagnostico2(self.stackedWidget, self.label)
        self.stackedWidget.addWidget(self.diagnostico2)

        self.diagnostico.clicked.connect(lambda: self.RealizarDiagnostico())
        self.changeD.clicked.connect(lambda: self.change())
        
    
    def RealizarDiagnostico(self):
        if (len(self.obtenerListaSintomas()) > 0):
            msg = QMessageBox()
            res = 'El posible diagnostico es : \n'
            i = 1
            for problema in self.SistemaExperto.diagnostico(self.obtenerListaSintomas()):
                res += str(i) + ". " + problema["X"] + "\n"
                i += 1
            msg.setText(res)
            msg.setWindowTitle("Diagnosticos")
            msg.exec_()
        
    def change(self):
        self.label.setText("  Seleccione el Problema :")
        self.stackedWidget.setCurrentIndex(1)


    def obtenerListaSintomas(self):
        listSintomas = []
        if (self.golpeteo_motor.isChecked()):
            listSintomas.append("golpeteo_motor")

        if (self.humo_Negro.isChecked()):
            listSintomas.append("humo_negro_escape")

        if (self.tirones.isChecked()):
            listSintomas.append("tirones_motor")

        if (self.luces.isChecked()):
            listSintomas.append("luces_debiles")

        if (self.problemas_arranque.isChecked()):
            listSintomas.append("problemas_arranque")

        if (self.ruidos_encendido.isChecked()):
            listSintomas.append("ruidos_encendido")

        if (self.perdida_refr.isChecked()):
            listSintomas.append("perdida_de_refrigerante")

        if (self.humo_blanco.isChecked()):
            listSintomas.append("humo_blanco")

        if (self.testigo_temperatura.isChecked()):
            listSintomas.append("testigo_temperatura")

        if (self.testigo_presion_aceite.isChecked()):
            listSintomas.append("testigo_presion_aceite")

        if (self.ruidos_metalicos.isChecked()):
            listSintomas.append("ruidos")

        if (self.perdida_potencia.isChecked()):
            listSintomas.append("perdida_de_potencia")

        if (self.humo_azul.isChecked()):
            listSintomas.append("humo_azul")

        if (self.vibraciones.isChecked()):
            listSintomas.append("vibraciones")

        if (self.consumo_Aceite.isChecked()):
            listSintomas.append("consumo_de_aceite")

        if (self.detiene.isChecked()):
            listSintomas.append("parada_motor")

        if (self.testigos_irregulares.isChecked()):
            listSintomas.append("testigos_irregulares")

        if (self.aceleracion_lenta.isChecked()):
            listSintomas.append("acelaracion_lenta")

        if (self.consumo_combustible.isChecked()):
            listSintomas.append("consumo_excesivo_combustible")

        if (self.sobrecalentamiento.isChecked()):
            listSintomas.append("sobrecalentamiento")

        if (self.humo_excesivo.isChecked()):
            listSintomas.append("humo_excesivo_escape")
        return listSintomas



app = QApplication(sys.argv)
window = Diagnostico()
app.exec_()