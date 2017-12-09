# coding: utf-8

import sys # 동기화 임포트
from PyQt4.QtGui import * # PyQt4 라이브러리 GUI설정 임포트
from PyQt4.QtCore import * # PyQt4 라이브러리 핵심 설정 임포트

class MyWindow(QMainWindow): # 메인 윈도우 선언

    def __init__(self):
        QMainWindow.__init__(self)
        
        #윈도우 특성 설정
        self.setWindowTitle('DaishinAutoLearning') # 윈도우 타이틀 지정 선언문
        self.setGeometry(600, 600, 200, 200) # 윈도우 위치/크기 설정 문법
        #self.statusBar().showMessage('ready')
        
        idtext = QLabel(self)
        idtext.text()
        #idtext.resize(15,15)
        idtext.setText("ID")
        idtext.move(35,20)
        
        pwtext = QLabel(self)
        pwtext.text()
        #idtext.resize(15,10)
        pwtext.setText("PW")
        pwtext.move(35,50)
                
        #ID Textbox 추가
        self.idbox = QLineEdit(self)
        self.idbox.resize(120,25)
        self.idbox.move(60, 20)
        
        #PW Textbox 추가
        self.pwbox = QLineEdit(self)
        self.pwbox.resize(120,25)
        self.pwbox.move(60, 50)
                
        # 버튼1 추가
        btn1 = QPushButton('START', self)
        #btn1.resize(btn1.sizeHint())
        btn1.move(50, 90)
        btn1.clicked.connect(self.btnClicked)
        
        # 종료 버튼 추가
        btnQuit = QPushButton('END', self)
        btnQuit.move(50, 130) # 종료창 위치/크기 설정
        btnQuit.clicked.connect(QCoreApplication.instance().quit)
        
        #윈도우 화면 출력
        self.show()

    def btnClicked(self):
        inputid = self.idbox.text()
        inputpw = self.idbox.text()
        #QMessageBox.information(self, "button", "Button Click!")

    
def main():
    app = QApplication(sys.argv)
    dx = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()