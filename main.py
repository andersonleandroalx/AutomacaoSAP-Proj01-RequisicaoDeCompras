from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from ui_main import Ui_MainWindow
import sys
import win32com.client
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Requisiçao de compra")

        ######################## Buttons
        self.bt_open.clicked.connect(self.open_file)
        self.bt_go.clicked.connect(self.registrar_compras)


    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Selecione a planilha com os dados")
        self.li_filepath.setText(str(self.file[0]))

    def connect_sap(self):
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.Children(0)
        self.session = connection.Children(0)

    def registrar_compras(self):
        self.connect_sap()
        self.file = self.li_filepath.text()

        data = pd.read_excel(self.file)
        data = data.values.tolist()

        #self.ession.findById("wnd[0]").resizeWorkingPane(84, 18, False)
        try:
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "me51n"
            self.session.findById("wnd[0]").sendVKey(0)
            self.session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:3327/cmbMEREQ_TOPLINE-BSART").key = "DIT1"


            path_fields1 = self.session.findById(
                "wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell")

            id = 0
            for i, j in enumerate(data):
                if id == 0:
                    path_fields1.modifyCell(i, "MATNR", j[0])
                    path_fields1.modifyCell(i, "MENGE", j[1])
                    path_fields1.modifyCell(i, "NAME1", j[2])
                    #path_fields1.currentCellColumn = j[3]
                    path_fields1.pressEnter()
                else:
                    path_fields2 = self.session.findById(
                        "wnd[0]/usr/subSUB0:SAPLMEGUI:0015/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell")
                    path_fields2.modifyCell(i, "MATNR", j[0])
                    path_fields2.modifyCell(i, "MENGE", j[1])
                    path_fields2.modifyCell(i, "NAME1", j[2])
                    #path_fields2.currentCellColumn = j[3]
                    path_fields2.pressEnter()
                    # path_fields1 = session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell")
                id += 1
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Registros Efetuados com sucesso")
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Módulo já iniciado, feche e tente novamente")
            msg.exec_()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()