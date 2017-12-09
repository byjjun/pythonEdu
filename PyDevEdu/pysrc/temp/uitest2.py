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
        self.statusBar().showMessage('ready')
        
        #
        
        # 버튼1 추가
        btn1 = QPushButton('message Button', self)
        btn1.setToolTip('If u Press this button <b>the message box</b>will be spring out')
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)
        btn1.clicked.connect(self.btnClicked)
        
        # 종료 버튼 추가
        btnQuit = QPushButton('Shut Down', self)
        btnQuit.move(50, 100) # 종료창 위치/크기 설정
        btnQuit.clicked.connect(QCoreApplication.instance().quit)

        
        #윈도우 화면 출력
        self.show()

    def btnClicked(self):
        QMessageBox.information(self, "button", "Button Click!")

    
def main():
    app = QApplication(sys.argv)
    dx = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()