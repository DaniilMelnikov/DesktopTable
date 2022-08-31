import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import json
import re

import design, table, saveForm, deleteForm, allTable

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.setupUi(self)

        self.updateTable.clicked.connect(self.open_table_window)
        self.pushButton.clicked.connect(self.open_all_table_window)


    def open_table_window(self):
        global window_table
        self.window_table = TableWindow(self.comboBox.currentText()) 
        self.window_table.show()
        window_table = self.window_table

    def open_all_table_window(self):
        self.window_all_table = AllTableWindow() 
        self.window_all_table.show()

with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

class AllTableWindow(QtWidgets.QDialog, allTable.Ui_Dialog):
    def __init__(self):
        super(AllTableWindow, self).__init__()
        self.setupUi(self)

        self.ageTable.setColumnCount(1)
        self.ageTable.setRowCount(len(data['data']['age']))
        set_item(data['data']['age'], table_widget=self.ageTable)

        self.nameTable.setColumnCount(1)
        self.nameTable.setRowCount(len(data['data']['name']))
        set_item(data['data']['name'], table_widget=self.nameTable)

        self.nationTable.setColumnCount(1)
        self.nationTable.setRowCount(len(data['data']['nation']))
        set_item(data['data']['nation'], table_widget=self.nationTable)

        self.univerTable.setColumnCount(1)
        self.univerTable.setRowCount(len(data['data']['univer']))
        set_item(data['data']['univer'], table_widget=self.univerTable)

        self.schoolTable.setColumnCount(1)
        self.schoolTable.setRowCount(len(data['data']['school']))
        set_item(data['data']['school'], table_widget=self.schoolTable)

        self.operandTable.setColumnCount(2)
        self.operandTable.setRowCount(len(data['operand']))
        set_item(data["operand"], table_widget=self.operandTable, col_cur=True)


class TableWindow(QtWidgets.QDialog, table.Ui_Dialog):
    def __init__(self, combo_box):
        self.combo_box = combo_box
        super(TableWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_save_window)
        self.pushButton_2.clicked.connect(self.open_delete_window)

        if self.combo_box == "operand":
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setRowCount(len(self.combo_box[0]))
            set_item(data["operand"], table_widget=self.tableWidget, col_cur=True)
        else:
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(len(data['data'][self.combo_box]))
            set_item(data['data'][self.combo_box], table_widget=self.tableWidget)
    
    def open_save_window(self):
        global window_save
        self.window_save = SaveFormWindow() 
        self.window_save.show()
        window_save = self.window_save


    def open_delete_window(self):
        global window_delete
        self.window_delete = DeleteFormWindow() 
        self.window_delete.show()
        window_delete = self.window_delete

             
def set_item(data_items, table_widget, col_cur=False):
    if col_cur:
        row = 0
        for list_row in data_items:
            col = 0
            for item in list_row:
                cellinfo = QTableWidgetItem(str(item))
                table_widget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        return 0
    col = 0
    for item in data_items:
        cellinfo = QTableWidgetItem(str(item))
        table_widget.setItem(0, col, cellinfo)
        col += 1  

        
class SaveFormWindow(QtWidgets.QDialog, saveForm.Ui_Dialog):
    def __init__(self):
        super(SaveFormWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.print_line)


    def print_line(self):
        global window_table
        list_save = []
        list_save.append(self.lineEdit_2.text())
        list_save.append(self.lineEdit.text())
        data['data'].append(list_save)
        window_table.close()
        window_save.close()
        self.window_table = TableWindow()
        self.window_table.show()
        window_table = self.window_table
        dump_json()


class DeleteFormWindow(QtWidgets.QDialog, deleteForm.Ui_Dialog):
    def __init__(self):
        super(DeleteFormWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.delete_line)


    def delete_line(self):
        global window_table
        matches = re.findall("\\d+", self.lineEdit.text())
        for id, el in enumerate(matches):
            matches[id] = int(el)

        matches = sorted(matches, reverse=True)

        for el in matches:
            try:
                data['data'].pop(int(el) - 1)
            except IndexError:
                pass

        window_table.close()
        window_delete.close()
        self.window_table = TableWindow()
        self.window_table.show()
        window_table = self.window_table
        dump_json()
        

def dump_json():
    with open('data.json', 'w') as fp:
        json.dump(data, fp)


def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp() 
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()