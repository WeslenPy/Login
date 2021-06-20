
class LoginMain(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(LoginMain,self).__init__(parent)

        self.loginWidget = QtWidgets.QWidget(self)
        self.progress = 0
        
        self.FormLogin()
        self.InitGui()
        
    def FormLogin(self):

        
        self.frameTop = QtWidgets.QFrame(self.loginWidget)
        self.frameCenter = QtWidgets.QFrame(self.loginWidget)
        self.frameDown = QtWidgets.QFrame(self.loginWidget)
        self.frameMessage = QtWidgets.QFrame(self.loginWidget)
        self.frameLogin = QtWidgets.QFrame(self.loginWidget)
        self.frameProgress = QtWidgets.QFrame(self.loginWidget)

        self.lb_Message = QtWidgets.QLabel('Usuario Ou Senha Incorreto.',self.loginWidget)
        self.btn_Message  = QtWidgets.QToolButton(self.loginWidget)
        self.btn_Message.setIcon(QtGui.QIcon('Icons/x_close.png'))
        self.btn_Message.setIconSize(QtCore.QSize(7,7))

        self.lb_Message.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_Message.setMinimumSize(16,16)
        self.lb_Message.setMaximumWidth(220)
        
        self.frameTop.setMaximumHeight(40)
        self.frameDown.setMaximumHeight(40)
        self.frameTop.setMinimumHeight(40)
        self.frameDown.setMinimumHeight(40)
        self.frameMessage.setMaximumWidth(250)
        self.frameMessage.setMinimumHeight(28)
        self.frameProgress.setMaximumSize(420,420)
        self.frameProgress.setMinimumSize(420,420)
        self.frameLogin.setMinimumSize(410,410)
        self.frameLogin.setMaximumSize(410,410)

        self.frameLogin.setStyleSheet('QFrame{background-color:#333333;border-radius:10px;}')
        self.frameMessage.setStyleSheet('QFrame{background-color:red;border-radius:5px;}')
        self.frameProgress.setStyleSheet('''
        QFrame{ border-radius:15px;background-color:qconicalgradient(cx:0.5,cy:0.5,angle:90,stop:0.749 rgba(255,0,127,0),stop:0.750 rgba(85,170,255,255));}
        ''')

        self.btn_Message.setStyleSheet('QToolButton{background-color:yellow;border-radius:5px;}')
        self.lb_Message.setStyleSheet('QLabel{color:white;}')

        self.setStyleSheet('QFrame{background-color:#1E1E1E;}')

        self.btn_Message.clicked.connect(lambda:self.Animation(rever=True))

        self.layoutVertical = QtWidgets.QVBoxLayout(self.loginWidget)
        self.layoutHLogin = QtWidgets.QHBoxLayout(self.frameCenter)
        self.layoutHTop = QtWidgets.QHBoxLayout(self.frameTop)
        self.layoutHMessage = QtWidgets.QHBoxLayout(self.frameMessage)
        self.layoutHProgress = QtWidgets.QHBoxLayout(self.frameProgress)

        
        self.layoutVertical.addWidget(self.frameTop)
        self.layoutVertical.addWidget(self.frameCenter)
        self.layoutVertical.addWidget(self.frameDown)

        self.layoutHLogin.addWidget(self.frameProgress)
        self.layoutHProgress.addWidget(self.frameLogin)
        self.layoutHTop.addWidget(self.frameMessage)
        self.layoutHMessage.addWidget(self.lb_Message)
        self.layoutHMessage.addWidget(self.btn_Message)

        self.layoutHMessage.setContentsMargins(0,0,0,0)
        self.layoutHProgress.setContentsMargins(0,0,0,0)
        self.layoutHMessage.setSpacing(0)
        self.layoutVertical.setContentsMargins(0,0,0,0)
        self.layoutVertical.setSpacing(0)
        self.frameMessage.hide()

        self.Form(self.frameLogin.size().width())

        self.timeProgress = QtCore.QTimer()
        self.timeProgress.timeout.connect(self.ProgressAnimation)
        self.timeProgress.start(40)

        self.setCentralWidget(self.loginWidget)

    def ProgressAnimation(self):
        value = self.progress

        stylesheet = "QFrame{ border-radius:15px;background-color:qconicalgradient(cx:0.5,cy:0.5,angle:90,stop:{stop_1} rgba(255,0,127,0),stop:{stop_2} rgba(85,170,255,255));}"
        pro = (100 -value) /100.0
        newStyle = stylesheet.replace('{stop_1}',str(pro-0.001)).replace('{stop_2}',str(pro))
        self.frameProgress.setStyleSheet(newStyle)

        self.progress+=1
        if self.progress >=100:
            self.progress = 0
    def Animation(self,rever=False):

        self.frameMessage.show()
        pos = int(self.size().width()/2)-125

        self.animation = QtCore.QPropertyAnimation(self.frameMessage,b'pos')
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        if not rever:self.animation.setStartValue(QtCore.QPoint(pos,-29)),self.animation.setEndValue(QtCore.QPoint(pos,10))
        else:self.animation.setStartValue(QtCore.QPoint(pos,10)),self.animation.setEndValue(QtCore.QPoint(pos,-29))
        self.animation.start()

    def Form(self,width):

        # self.Select_Users()
        self.IconTp = QtWidgets.QLabel(self.frameLogin)
        self.IconTp.setPixmap(QtGui.QPixmap('Icons/user4.png'))

        self.cb_users = QtWidgets.QComboBox(self.frameLogin)

        self.cb_users.addItems(['Name' for _ in range(4)])

        self.cb_users.setStyleSheet('''
        QComboBox{border:None;border-radius:12px;background-color:#595959;color:white;padding-left:%s px;}
        QComboBox:drop-down{border:0px solid;;border-radius:10px;image:url(Icons/drop2.png);padding-top:4px;margin-top:2px;margin-right:3px;}
        QComboBox:drop-down:hover {background:#22c1c3;border:None;}
        QComboBox QAbstractItemView{max-width:200px;min-height:15px;padding-top:5px;padding-left:%s px;padding-bottom:3px;background-color:#404040;color:white;border-radius:10px;selection-background-color:#404040;outline:0px;}
        ''' % (int(90- len(self.cb_users.currentText())), int(87- len(self.cb_users.currentText()))) )

        self.cb_users.setMaxVisibleItems(3)

        self.cb_users.resize(width,28)
        self.cb_users.setMaximumWidth(200)


        self.cb_users.move(int(width/2-200/2),165)
        self.IconTp.move(int(width/2-self.IconTp.size().width()/2),50)

        self.et_senha = QtWidgets.QLineEdit(self.frameLogin)

        self.et_senha.setStyleSheet('QLineEdit{border:None;border-radius:12px;background-color:#595959;color:white;font-size:12px;padding-left:5px;}\
                                     QLineEdit:hover{border:1.5px solid rgba(85,170,255,255);outline:0;}')

        self.et_senha.setFocus()

        self.et_senha.setPlaceholderText('Senha')

        self.et_senha.setEchoMode(QtWidgets.QLineEdit.Password)

        self.et_senha.resize(width,28)
        self.et_senha.setMaximumWidth(200)
        self.et_senha.move(int(width/2-200/2),200)

        self.btn_open= QtWidgets.QToolButton(self.frameLogin)
        self.btn_open.setText('Logar')
        
        self.btn_open.setStyleSheet('QToolButton{color:white;font-size:10pt;border:2px solid rgba(85,170,255,255);border-radius:12px;text-align:right;}\
                                     QToolButton:hover{background:rgba(85,170,255,255);border:None;outline:0;}')

        self.btn_open.pressed.connect(self.Animation)

        self.btn_open.resize(width,28)
        self.btn_open.setMaximumWidth(200)
        self.btn_open.move(int(width/2-200/2),250)


    def InitGui(self):

        self.setGeometry(200, 200, 600,450)
        self.setMinimumSize(600,600)
        self.move(centralWindow -self.rect().center() - QtCore.QPoint(0,20))
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    w, h = screen_rect.width(), screen_rect.height()
    centralWindow = app.desktop().screen().rect().center()

    window = LoginMain()
    window.show()
    sys.exit(app.exec_())
#
