from PyQt5.QtWidgets import QWidget, QPushButton, QRadioButton, QMessageBox
from PyQt5 import uic
from sistemaExpertoMecanica import SistemaExpertoMecanica


class Diagnostico2(QWidget):
    def __init__(self, stacked, label,  parent = None):
        super(Diagnostico2, self).__init__(parent)
        self.iniciarGui()
        self.sistemaExperto = SistemaExpertoMecanica()
        self.stacked = stacked
        self.label = label
        self.show()
    
    def iniciarGui(self):
        uic.loadUi(r'diagnostico2UI.ui', self)

        self.inyector_sucio = self.findChild(QRadioButton, 'radioButton')
        self.inyector_desc = self.findChild(QRadioButton, 'radioButton_2')
        self.electrico = self.findChild(QRadioButton, 'radioButton_3')
        self.sis_arranque = self.findChild(QRadioButton, 'radioButton_4')
        self.sis_refr = self.findChild(QRadioButton, 'radioButton_5')
        self.radiador = self.findChild(QRadioButton, 'radioButton_6')
        self.bomba_aceite = self.findChild(QRadioButton, 'radioButton_7')
        self.correa = self.findChild(QRadioButton, 'radioButton_8')
        self.pistones = self.findChild(QRadioButton, 'radioButton_9')
        self.anillos = self.findChild(QRadioButton, 'radioButton_10')
        self.bomba_agua = self.findChild(QRadioButton, 'radioButton_11')
        self.bujias = self.findChild(QRadioButton, 'radioButton_12')
        self.sensores = self.findChild(QRadioButton, 'radioButton_13')
        
        self.consulta = self.findChild(QPushButton, 'pushButton')
        self.cambio = self.findChild(QPushButton, 'pushButton_2')

        self.consulta.clicked.connect(lambda: self.consultaSintomas())
        self.cambio.clicked.connect(lambda: self.change())

    def consultaSintomas(self):
        if (self.obtenerProblema() != ""):
            msg = QMessageBox()
            res = 'Los posibles sintomas son : \n'
            i = 1
            for problema in self.sistemaExperto.diagnostico2("posiblesSintomas(" + self.obtenerProblema() + ", Y)"):
                res += str(i) + ". " + problema["Y"] + "\n"
                i += 1
            msg.setText(res)
            msg.setWindowTitle("Sintomas")
            msg.exec_()

    def obtenerProblema(self):
        problema = ""
        if (self.inyector_sucio.isChecked()):
            problema += "inyectores_sucios"
        
        if (self.inyector_desc.isChecked()):
            problema += "inyectores_descalibrados"
        
        if (self.electrico.isChecked()):
            problema += "problema_electrico"
        
        if (self.sis_arranque.isChecked()):
            problema += "problema_sistema_arranque"
        
        if (self.sis_refr.isChecked()):
            problema += "problema_sistema_de_refrigeracion"
        
        if (self.radiador.isChecked()):
            problema += "problema_radiador"
        
        if (self.bomba_aceite.isChecked()):
            problema += "problema_bomba_de_aceite"
        
        if (self.pistones.isChecked()):
            problema += "problema_pistones"
        
        if (self.correa.isChecked()):
            problema += "problema_correa_de_distribucion"
        
        if (self.anillos.isChecked()):
            problema += "problema_anillos"
        
        if (self.bomba_agua.isChecked()):
            problema += "problema_bomba_de_agua"
        
        if (self.bujias.isChecked()):
            problema += "problema_bujias"
        
        if (self.sensores.isChecked()):
            problema += "problema_sensores"
        
        return problema


    def change(self):
        self.label.setText("  Seleccione los Sintomas :")
        self.stacked.setCurrentIndex(0)