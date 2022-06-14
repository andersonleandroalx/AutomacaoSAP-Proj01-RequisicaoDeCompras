import win32com.client

# inicia sessao do sap já logado
SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

# escolhe a opçºao me51n
session.findById("wnd[0]").resizeWorkingPane(84, 18, False)
session.findById("wnd[0]/tbar[0]/okcd").text = "me51n"
session.findById("wnd[0]").sendVKey(0)


# preenche tela que abrir
lista = [
    ['prod305', '10', '3000', 'NAME1'],
    ['prod306', '10', '3000', 'NAME1'],
    ['prod307', '10', '3000', 'NAME1'],
    ['prod308', '10', '3000', 'NAME1']
         ]
path_fields1 = session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell")

session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB0:SAPLMEGUI:0030/subSUB1:SAPLMEGUI:3327/cmbMEREQ_TOPLINE-BSART").key = "DIT1"
id = 0
for i, j in enumerate(lista):
    if id == 0:
        path_fields1.modifyCell(i, "MATNR", j[0])
        path_fields1.modifyCell(i, "MENGE", j[1])
        path_fields1.modifyCell(i, "NAME1", j[2])
        path_fields1.currentCellColumn = j[3]
        path_fields1.pressEnter()
    else:
        path_fields2 = session.findById(
            "wnd[0]/usr/subSUB0:SAPLMEGUI:0015/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell")
        path_fields2.modifyCell(i, "MATNR", j[0])
        path_fields2.modifyCell(i, "MENGE", j[1])
        path_fields2.modifyCell(i, "NAME1", j[2])
        path_fields2.currentCellColumn = j[3]
        path_fields2.pressEnter()
        #path_fields1 = session.findById("wnd[0]/usr/subSUB0:SAPLMEGUI:0016/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell")
    id += 1

#path_fields2 = session.findById(
#           "wnd[0]/usr/subSUB0:SAPLMEGUI:0015/subSUB2:SAPLMEVIEWS:1100/subSUB2:SAPLMEVIEWS:1200/subSUB1:SAPLMEGUI:3212/cntlGRIDCONTROL/shellcont/shell")

prod = path_fields2.GetCellValue(0, "MATNR")
prod2 = path_fields2.GetCellValue(1, "MATNR")
desc = path_fields2.GetCellValue(0, "MENGE")

print(prod)

def balancete():
    session.findById("wnd[0]/tbar[0]/okcd").text = "j1bnfe"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/txtDOCNUM-LOW").text = "10000"
    session.findById("wnd[0]/usr/ctxtDATE-LOW").text = "14.06.2022"
    session.findById("wnd[0]/usr/txtSTCD1-LOW").text = "9999999999"
    session.findById("wnd[0]/usr/ctxtMODEL-LOW").text = "55"
    session.findById("wnd[0]/usr/txtNFNUM9-LOW").text = "1898"
    session.findById("wnd[0]/usr/txtSERIE-LOW").text = "2"
    session.findById("wnd[0]/usr/txtNFYEAR-LOW").text = "22"
    session.findById("wnd[0]/usr/txtNFMONT-LOW").text = "1"
    session.findById("wnd[0]/usr/ctxtBUKRS-LOW").text = "7000"
    session.findById("wnd[0]/usr/ctxtBUKRS-LOW").setFocus()
    session.findById("wnd[0]/usr/ctxtBUKRS-LOW").caretPosition = 4
    session.findById("wnd[0]").sendVKey(0)
