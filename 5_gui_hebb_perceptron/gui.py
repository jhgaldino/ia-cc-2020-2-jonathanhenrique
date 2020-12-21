import sys
from PyQt5 import QtCore
from PyQt5.QtUiTools import QUiLoader
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QRadioButton, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import QFile
from hebb import Hebb
from perceptron import Perceptron
from neuron import Neuron
n = Neuron()

def hebb_split(txt):
    split_1 = txt.split("\n")
    split_2 = []
    for i in range(len(split_1)):
        floats = [float(x) for x in split_1[i].split()]
        target = floats[-1]
        floats.pop()
        tupleAux = (floats, target)
        split_2.append(tupleAux)
    return split_2
def perceptron_split(txt):
    split_1 = txt.split("\n")
    split_2 = []
    a_t = []
    for i in range(len(split_1)):
        floats = [float(x) for x in split_1[i].split()]
        if(i < len(split_1) - 2):
            target = floats[-1]
            floats.pop()
            tupleAux = (floats, target)
            split_2.append(tupleAux)
        else:
            a_t.append(floats[0])
    return [split_2, a_t[0], a_t[1]]
def hebb_setWeight():
    values = Hebb(hebb_split(tranning_plainText.toPlainText()))
    list_weight = values.step_n()
    n.values = hebb_split(tranning_plainText.toPlainText())
    n.list_weight = list_weight
    p1_label.setText("{: .2f}".format(list_weight[0]))
    p2_label.setText("{: .2f}".format(list_weight[1]))
    pB_label.setText("{: .2f}".format(list_weight[2]))
    return
def perceptron_setweights():
    values = perceptron_split(tranning_plainText.toPlainText())
    neuron_perceptron = Perceptron(values[0], values[1], values[2])
    list_weight = neuron_perceptron.step_n()
    n.values = values
    n.list_weight = list_weight
    p1_label.setText("{: .2f}".format(list_weight[0]))
    p2_label.setText("{: .2f}".format(list_weight[1]))
    pB_label.setText("{: .2f}".format(list_weight[2]))
def on_treinar_pushbutton_clicked():
    if tranning_plainText.toPlainText() == "":
        QMessageBox.warning(QMessageBox(), "ERRO", "Entre com uma entrada")
        return
    if hebb_radio.isChecked():
        hebb_setWeight()
    elif perceptron_radio.isChecked():
        perceptron_setweights()
    else:
        QMessageBox.warning(QMessageBox(), "ERRO", "Entre Metodo")
        return
    test_lineEdit.setFocus()
    return 1
def on_testar_pushbutton_clicked():
    if p1_label.text() == "":
        QMessageBox.warning(QMessageBox(), "ERRO", "Faca treinamento")
        test_lineEdit.clear()
        tranning_plainText.setFocus()
        return
    if test_lineEdit.text() == "":
        QMessageBox.warning(QMessageBox(), "ERRO", "falta de entradas")
        test_lineEdit.setFocus()
        return
    if hebb_radio.isChecked():
        resposta_label.setText(str(n.h_saida([float(x) for x in test_lineEdit.text().split()])))
        return
    elif perceptron_radio.isChecked():
        resposta_label.setText(str(n.p_saida([float(x) for x in test_lineEdit.text().split()], n.entradas[2])))
        return
    return
if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    ui_file = QFile("hebb_perceptron.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    hebb_radio = window.findChild(QRadioButton, 'hebbRadioButton')
    perceptron_radio = window.findChild(QRadioButton, 'perceptronRadioButton')
    tranning_label = window.findChild(QLabel, 'trainLabel')
    test_label = window.findChild(QLabel, 'testLabel')
    pesos_label = window.findChild(QLabel, 'testLabel_2')
    saida_label = window.findChild(QLabel, 'saidaLabel')
    peso1_label = window.findChild(QLabel, 'weight1Label')
    peso2_label = window.findChild(QLabel, 'weight2Label')
    pesoB_label = window.findChild(QLabel, 'weightBLabel')
    p1_label = window.findChild(QLabel, 'p1Label')
    p2_label = window.findChild(QLabel, 'p2Label')
    pB_label = window.findChild(QLabel, 'pBLabel')
    resposta_label = window.findChild(QLabel, 'resLabel')
    tranning_plainText = window.findChild(QPlainTextEdit, 'trainPlainTextEdit')
    test_lineEdit = window.findChild(QLineEdit, 'testLineEdit')
    treinar_btn = window.findChild(QPushButton, 'trainPushButton')
    treinar_btn.clicked.connect(on_treinar_pushbutton_clicked)
    testar_btn = window.findChild(QPushButton, 'testPushButton')
    testar_btn.clicked.connect(on_testar_pushbutton_clicked)
    window.show()
    sys.exit(app.exec_())