# coding: utf-8

'''
Created on 2020. 10. 20.

@author: 073860
'''

import sys # 동기화 임포트
import ctypes
import subprocess

#from PyQt4.QtGui import * # PyQt4 라이브러리 GUI설정 임포트
#from PyQt4.QtCore import * # PyQt4 라이브러리 핵심 설정 임포트
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QCoreApplication


class MyWindow(QMainWindow): # 메인 윈도우 선언

    def __init__(self):
        
        #self.setWindowIcon(QIcon("icon.png"))
        QMainWindow.__init__(self)
        
        myappid = u'ds.daishin.cbpProject Linker.10' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        #윈도우 특성 설정
        self.setWindowTitle('CBP Project Linker') # 윈도우 타이틀 지정 선언문
        self.setWindowIcon(QIcon("cbplinkericon.png"))
        self.setGeometry(600, 600, 450, 200) # 윈도우 위치/크기 설정 문법
        #self.statusBar().showMessage('ready')
        
        idtext = QLabel(self)
        idtext.text()
        #idtext.resize(15,15)
        idtext.setText("Project Path : ")
        idtext.move(35,20)
        
        pwtext = QLabel(self)
        pwtext.text()
        #idtext.resize(15,10)
        pwtext.setText("Link Impl Path : ")
        pwtext.move(35,50)
        
        mdtext = QLabel(self)
        mdtext.text()
        mdtext.resize(300,20)
        mdtext.setText("CBP Project Linker. Made ByJJuN. v1.0")
        mdtext.move(110,180)
                
        #Project Text Box
        self.projectbox = QLineEdit(self)
        self.projectbox.setText("C:\GIT_AREA\cybos_psl")
        self.projectbox.resize(300,25)
        self.projectbox.move(135, 20)
        
        #Link Project 용 Text Box
        self.linkimplbox = QLineEdit(self)
        self.linkimplbox.setText("C:\GIT_AREA\cybos_cii\CIIImpl")
        self.linkimplbox.resize(300,25)
        self.linkimplbox.move(135, 50)
                
        # 버튼1 추가
        btn1 = QPushButton('MAKE Link', self)
        #btn1.resize(btn1.sizeHint())
        btn1.move(160, 90)
        btn1.clicked.connect(self.btnClicked)
        
        # 종료 버튼 추가
        btnQuit = QPushButton('EXIT', self)
        btnQuit.move(160, 130) # 종료창 위치/크기 설정
        btnQuit.clicked.connect(QCoreApplication.instance().quit)
        
        #윈도우 화면 출력
        self.show()

    def btnClicked(self):
        
        project_path = self.projectbox.text()
        link_impl_path = self.linkimplbox.text()
        
        print "PRJ PATH : " + project_path
        print "LINK IMPL PATH : " + link_impl_path
        
        link_impl_temp = str(link_impl_path).split('\\')
        link_impl_name = link_impl_temp[(len(link_impl_temp)-1)]
        print link_impl_name
        
        link_src = str(project_path)+'\\'+str(link_impl_name)
        link_target = link_impl_path
        
        print link_src
        print link_target
        
        link_qcommand = "mklink /d \"" + link_src + "\" \"" + link_target + "\"" 
        link_command = str(link_qcommand)
        print link_command
        
        result = -1
        
        if(str("git_area") not in str(str(link_src).lower())):
            QMessageBox.information(self, "Failed", "Link Failed!! \n\nProject Path must be in git_area !! \nSample : c:\git_area\cybos_psl     ")
        elif(str("git_area") not in str(str(link_impl_path).lower())):
            QMessageBox.information(self, "Failed", "Link Failed!! \n\nLink Impl Path must be in git_area !! \nSample : c:\git_area\cybos_cii\CIIImpl     ")
        else:
            result = subprocess.call(link_command, shell=True)
        
        if(result==0):
            QMessageBox.information(self, "Complete", "Making Link Complete!!   ")
        else:
            QMessageBox.information(self, "Failed", "Check Project Directory or Link Impl Directory !!   ")

                
    
def main():
    app = QApplication(sys.argv)
    dx = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
