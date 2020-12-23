import sys, random
from PyQt5 import QtCore,uic
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication, QComboBox,QPushButton, QLineEdit, QLabel, QMessageBox

def a(str_n, b, ha):
    str_list = list(str_n)
    d = list(b)
    changes_list = list(ha)
    n = 0
    for i in range(len(str_list)):
        for j in range(len(d)):
            if n > (len(d) - 1) or i > (len(str_list)-1) or j > (len(d)-1) : continue
            elif (str_list[i] == d[j]):
                str_list[i] = changes_list[n]
                del (d[j])
                del (changes_list[n])
                n += 1
    str_n = "".join(str_list)
    b = "".join(d)
    ha = "".join(changes_list)
    return str_n, b, ha
def compare_changes(str_n, b):
    str_list = list(str_n)
    d = list(b)
    n = 0
    for i in range(len(str_list)):
        for j in range(len(d)):
            if n > (len(d) - 1) or i > (len(str_list)-1) or j > (len(d)-1) : continue
            elif (str_list[i] == d[j]):
                del (d[j])
                del (str_list[i])
    str_n = "".join(str_list)
    b = "".join(d)
    return str_n, b
def on_cross_pushbutton_clicked():
    if len(father_line_edit.text()) != 10 or len(father_line_edit.text()) != 10:
        QMessageBox.warning(QMessageBox(), "AVISO", "Entrada deve conter 10 caracteres")
        return
    if method_combo_box.currentText() == "Corte Simples":
        band = simple_cut_crossover(1)
        filhao1_label_3.setText("")
        filhao2_label_3.setText("")
    elif method_combo_box.currentText() == "Corte Duplo":
        band = simple_cut_crossover(2)
    elif method_combo_box.currentText() == "PMX":
        if len(father_line_edit.text()) != len(set(father_line_edit.text())) \
                or len(mother_line_edit.text()) != len(set(mother_line_edit.text())):
            QMessageBox.warning(QMessageBox(), "AVISO", "Entrada deve conter valores unicos")
            return
        band = pmx_crossover()
def on_method_combobox_current_text_changed():
    if method_combo_box.currentText() == "PMX":
        father_line_edit.setInputMask("AAAAAAAAAA")
        mother_line_edit.setInputMask("AAAAAAAAAA")
        father_line_edit.setText("ABCDEFGHIJ")
        mother_line_edit.setText("KLMNOPQRST")
    else:
        father_line_edit.setInputMask("BBBBBBBBBB")
        mother_line_edit.setInputMask("BBBBBBBBBB")
        father_line_edit.setText("0000000000")
        mother_line_edit.setText("1111111111")
def pmx_crossover():
    cuts = 2
    trades = 1
    papa = father_line_edit.text()
    mama = mother_line_edit.text()
    parts = random.sample(range(1, len(papa)), cuts)
    parts.sort()
    choose = random.sample(range(0, len(parts)+1), trades)
    filhao_1 = []
    for i in range (len(parts)+1):
        filhao_1.append(0)
        if i == 0:
            filhao_1[i] = papa[:parts[0]]
        elif i == len(parts):
            filhao_1[i] = papa[parts[i-1]:]
        else:
            filhao_1[i] = papa[parts[i-1]:parts[i]]
    filhao_2 = []
    for i in range(len(parts) + 1):
        filhao_2.append(0)
        if i == 0:
            filhao_2[i] = mama[:parts[0]]
        elif i == len(parts):
            filhao_2[i] = mama[parts[i - 1]:]
        else:
            filhao_2[i] = mama[parts[i - 1]:parts[i]]
    filhao_x = filhao_1.copy()
    son_1_changes_1 = ""
    son_1_changes_2 = ""
    for i in range(len(choose)):
        filhao_1[choose[i]] = filhao_2[choose[i]]
        son_1_changes_2 += filhao_2[choose[i]]
        filhao_2[choose[i]] = filhao_x[choose[i]]
        son_1_changes_1 += filhao_x[choose[i]]
    boys = compare_changes(son_1_changes_1, son_1_changes_2)
    son_1_changes_1 = boys[0]
    son_1_changes_2 = boys[1]
    son_2_changes_1 = son_1_changes_2
    son_2_changes_2 = son_1_changes_1
    for i in range(len(filhao_1)):
        if i == choose[0]:
            continue
        boys = a(filhao_1[i], son_1_changes_2, son_1_changes_1)
        filhao_1[i] = boys[0]
        son_1_changes_2 = boys[1]
        son_1_changes_1 = boys[2]
    for i in range(len(filhao_2)):
        if i == choose[0]:
            continue
        boys = a(filhao_2[i], son_2_changes_2, son_2_changes_1)
        filhao_2[i] = boys[0]
        son_2_changes_2 = boys[1]
        son_2_changes_1 = boys[2]
    filhao1_label_1.setText(filhao_1[0])
    filhao1_label_2.setText(filhao_1[1])
    filhao1_label_3.setText(filhao_1[2])
    filhao2_label_1.setText(filhao_2[0])
    filhao2_label_2.setText(filhao_2[1])
    filhao2_label_3.setText(filhao_2[2])
def simple_cut_crossover(cuts):
    trades = 1
    papa = father_line_edit.text()
    mama = mother_line_edit.text()
    parts = random.sample(range(1, len(papa)), cuts)
    parts.sort()
    choose = random.sample(range(0, len(parts)+1), trades)
    filhao_1 = []
    for i in range (len(parts)+1):
        filhao_1.append(0)
        if i == 0:
            filhao_1[i] = papa[:parts[0]]
        elif i == len(parts):
            filhao_1[i] = papa[parts[i-1]:]
        else:
            filhao_1[i] = papa[parts[i-1]:parts[i]]
    filhao_2 = []
    for i in range(len(parts) + 1):
        filhao_2.append(0)
        if i == 0:
            filhao_2[i] = mama[:parts[0]]
        elif i == len(parts):
            filhao_2[i] = mama[parts[i - 1]:]
        else:
            filhao_2[i] = mama[parts[i - 1]:parts[i]]
    filhao_x = filhao_1.copy()
    for i in range(len(choose)):
        filhao_1[choose[i]] = filhao_2[choose[i]]
        filhao_2[choose[i]] = filhao_x[choose[i]]
    filhao1_label_1.setText(filhao_1[0])
    filhao1_label_2.setText(filhao_1[1])
    filhao2_label_1.setText(filhao_2[0])
    filhao2_label_2.setText(filhao_2[1])
    if cuts == 2:
        filhao1_label_3.setText(filhao_1[2])
        filhao2_label_3.setText(filhao_2[2])
if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = uic.loadUi(f"7_crossover_operation\crossover_operation.ui")
    window.show()
    father_line_edit = window.findChild(QLineEdit, 'fatherLineEdit')
    mother_line_edit = window.findChild(QLineEdit, 'motherLineEdit')
    filhao1_label_1 = window.findChild(QLabel, 'filhao1Label1')
    filhao1_label_2 = window.findChild(QLabel, 'filhao1Label2')
    filhao1_label_3 = window.findChild(QLabel, 'filhao1Label3')
    filhao2_label_1 = window.findChild(QLabel, 'filhao2Label1')
    filhao2_label_2 = window.findChild(QLabel, 'filhao2Label2')
    filhao2_label_3 = window.findChild(QLabel, 'filhao2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_method_combobox_current_text_changed)
    sys.exit(app.exec_())