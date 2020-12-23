import sys
from gui import Gui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    gui = Gui()
    gui.window.show()
    sys.exit(app.exec_())

    # 1 adicionar fonte
    # 2 criar neuronios
    # 3 criar rede de neuronios
    # train neural network -> executar o metodo train do perceptron para cada neuronio
    # run neural network -> exibir o numero reconhecido
    # percorrer lista de neuronios e verificar quais reconheceram a entrada

    # 0 bias 0 theta 1 alpha

    # train neural network -> Retornar uma lista com 10 neuronios
    # cada neuronio com uma lista de pesos com listas de pesos igual a quantidade de fontes