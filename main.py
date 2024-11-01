import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Записная книжка</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>471</width>
      <height>201</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Имя</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="contactNumber"/>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Телефон</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="contactName"/>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="addContactBtn">
    <property name="geometry">
     <rect>
      <x>490</x>
      <y>60</y>
      <width>221</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QListWidget" name="contactList">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>201</y>
      <width>801</width>
      <height>351</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.addContactBtn.clicked.connect(self.action)

    def action(self):
        self.contactList.addItem(self.contactName.text() + ' ' + self.contactNumber.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
