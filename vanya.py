import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import json
import re

import design, table, saveForm, deleteForm, allTable

# Класс главного окна
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    # Присваиваем переменные и обработчики
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.setupUi(self)
        # обработчики по клику, в аргементе метод класса без функция(ангументов)
        self.updateTable.clicked.connect(self.open_table_window)
        self.pushButton.clicked.connect(self.open_all_table_window)

    # обработчик открытия окна с таблицей и её изменений. Кнопка - изменить таблицу
    def open_table_window(self):
        # делаю переменную глобальной для автоматического закрытия окна в другом классе, при триггере друого обработчика
        global window_table
        # создаю экземпляр класса окна с таблицей для изменений, в аргумент передаю инфу выбранную из comboBox
        self.window_table = TableWindow(self.comboBox.currentText()) 
        # открываю окно
        self.window_table.show()
        # присваиваю глобал к локал переменной
        window_table = self.window_table

    # Обработчик открытия окна со всеми таблицами. Это окно нужно для заполнения таблицы с операндом
    def open_all_table_window(self):
        self.window_all_table = AllTableWindow() 
        self.window_all_table.show()

# открываю файл json, r = read, декодируем в utf-8
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Класс окна всех таблиц
class AllTableWindow(QtWidgets.QDialog, allTable.Ui_Dialog):
    def __init__(self):
        super(AllTableWindow, self).__init__()
        self.setupUi(self)

        # заплдняем каждую таблицу отдельно из json
        self.ageTable.setColumnCount(1)
        self.ageTable.setRowCount(len(data['data']['age']))
        # Функция для загрузки данных в таблицу
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

        self.operandTable.setColumnCount(3)
        self.operandTable.setRowCount(len(data['operand']))
        set_item(data["operand"], table_widget=self.operandTable, col_cur=True)


# Класс окна таблицы для её изменения
class TableWindow(QtWidgets.QDialog, table.Ui_Dialog):
    # передали комбоБокс именно в этот класс, здесь переменная и сидит
    def __init__(self, combo_box):
        # нужно пересвоить переменную с селфом
        self.combo_box = combo_box
        super(TableWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_save_window)
        self.pushButton_2.clicked.connect(self.open_delete_window)

        # В зависемости от комбоБокса создаются разные таблицы
        if self.combo_box == "operand":
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setRowCount(len(self.combo_box[0]))
            set_item(data["operand"], table_widget=self.tableWidget, col_cur=True)
            # Новая переменная, которая нужна для того, чтобы другой комбоБокс появлялся в SaveFormWindow только у операнда
            self.operand = True
        else:
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setRowCount(len(data['data'][self.combo_box]))
            set_item(data['data'][self.combo_box], table_widget=self.tableWidget)
            self.operand = False
    
    # обработчик открытия добавления данных в таблицу
    def open_save_window(self):
        global window_save
        # передаём аргумент операнда
        self.window_save = SaveFormWindow(self.operand, self.combo_box) 
        self.window_save.show()
        window_save = self.window_save

    # обработчик для удаления данных из таблицы по id
    def open_delete_window(self):
        global window_delete
        self.window_delete = DeleteFormWindow(self.operand, self.combo_box) 
        self.window_delete.show()
        window_delete = self.window_delete

# Функция для добавления данных в таблицу
# data_items - данные, которые нужно обработать
# table_widget - передаём экземпляр таблицы, которую нужно изменить
# col_cur - если таблица имеет более 1 колнки, то ставим True
def set_item(data_items, table_widget, col_cur=False):
    if col_cur:
        # счётчик строк
        row = 0
        for list_row in data_items:
            # счётчик колонок
            col = 0
            for item in list_row:
                # экземпляр элемента, который нужно добавить в таблицу
                cellinfo = QTableWidgetItem(str(item))
                # добавляем по чёткому месту номер колонки, номер строки и сами данные
                table_widget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        # Прерываем прогу
        return 0
    # цикл добавления для таблицы с 1 колонной
    col = 0
    for item in data_items:
        cellinfo = QTableWidgetItem(str(item))
        table_widget.setItem(0, col, cellinfo)
        col += 1  

# Класс окна для записи данных
class SaveFormWindow(QtWidgets.QDialog, saveForm.Ui_Dialog):
    def __init__(self, operand, combo_data):
        super(SaveFormWindow, self).__init__()
        self.setupUi(self)
        self.combo_data = combo_data

        self.pushButton.clicked.connect(self.print_line)

        self.operand = operand
        # Если это таблица операнд, то добавляем комбобокс
        if self.operand:
            self.comboBox = QtWidgets.QComboBox(self)
            for key in data['data'].keys():
                self.comboBox.addItem(key)
            self.verticalLayout.addWidget(self.comboBox)
        else:
            self.lineEdit_2.setEnabled(False)

    # обработчик для записи данных
    def print_line(self):
        global window_table
        list_save = []

        if self.operand:
            list_save.append(self.lineEdit_2.text())
            list_save.append(self.lineEdit.text())
            list_save.append(self.comboBox.currentText())
            data['operand'].append(list_save)
        else:
            data['data'][self.combo_data].append(self.lineEdit.text())
        # вот для чего присваивали окна к глобал переменным, чтобыф те закрыть
        window_table.close()
        window_save.close()
        # и открыть заново, но с новой информацией
        self.window_table = TableWindow(self.combo_data)
        self.window_table.show()
        window_table = self.window_table
        dump_json()

# Класс окна удаления из таблицы
class DeleteFormWindow(QtWidgets.QDialog, deleteForm.Ui_Dialog):
    def __init__(self, operand, combo_data):
        super(DeleteFormWindow, self).__init__()
        self.setupUi(self)
        self.combo_data = combo_data
        self.operand = operand

        self.pushButton.clicked.connect(self.delete_line)

    # обработчик удаления данных
    def delete_line(self):
        global window_table
        # регулярное выражение ищет все цифирки
        matches = re.findall("\\d+", self.lineEdit.text())
        # цифиркы были str станут int
        for id, el in enumerate(matches):
            matches[id] = int(el)
        # сортируем по убыванию чтобы удаление 
        matches = sorted(matches, reverse=True)

        for el in matches:
            try:
                if self.operand:
                    data['operand'].pop(int(el) - 1)
                else:
                    data['data'][self.combo_data].pop(int(el) - 1)
            except IndexError:
                pass

        window_table.close()
        window_delete.close()
        self.window_table = TableWindow(self.combo_data)
        self.window_table.show()
        window_table = self.window_table
        dump_json()
        
# Загружаем данные 
def dump_json():
    with open('data.json', 'w') as fp:
        json.dump(data, fp)

# Функция для открытия главного окна
def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp() 
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()