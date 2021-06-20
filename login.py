
class LoginMain(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(LoginMain,self).__init__(parent)

        self.loginWidget = QtWidgets.QWidget(self)
        
        self.FormLogin()
        self.InitGui()
        
    def FormLogin(self):

        
        self.frameTop = QtWidgets.QFrame(self.loginWidget)
        self.frameCenter = QtWidgets.QFrame(self.loginWidget)
        self.frameDown = QtWidgets.QFrame(self.loginWidget)
        self.frameMessage = QtWidgets.QFrame(self.loginWidget)
        self.frameLogin = QtWidgets.QFrame(self.loginWidget)

        self.lb_Message = QtWidgets.QLabel('Usuario Ou Senha Incorreto.',self.loginWidget)
        self.btn_Message  = QtWidgets.QToolButton(self.loginWidget)
        self.btn_Message.setIcon(QtGui.QIcon('Icons/ICONS_16/x_close.png'))
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
        self.frameLogin.setMinimumSize(400,430)
        self.frameLogin.setMaximumSize(400,430)

        self.frameLogin.setStyleSheet('QFrame{background-color:#333333;border-radius:10px;border-bottom:2px solid #22c1c3;}')
        self.frameMessage.setStyleSheet('QFrame{background-color:red;border-radius:5px;}')
        self.btn_Message.setStyleSheet('QToolButton{background-color:yellow;border-radius:5px;}')
        self.lb_Message.setStyleSheet('QLabel{color:white;}')
        self.setStyleSheet('QFrame{background-color:#1E1E1E;}')

        self.btn_Message.clicked.connect(lambda:self.Animation(rever=True))

        
        # self.frameIcon = QtWidgets.QFrame(self.frameLogin)
        # self.frameIcon.setStyleSheet("QFrame{background-image:url('Icons/ICONS_16/userIcon.png');background-repeat:no-repeat;background-position:center;}")

        self.layoutVertical = QtWidgets.QVBoxLayout(self.loginWidget)
        self.layoutHLogin = QtWidgets.QHBoxLayout(self.frameCenter)
        self.layoutHTop = QtWidgets.QHBoxLayout(self.frameTop)
        self.layoutHMessage = QtWidgets.QHBoxLayout(self.frameMessage)

        
        self.layoutVertical.addWidget(self.frameTop)
        self.layoutVertical.addWidget(self.frameCenter)
        self.layoutVertical.addWidget(self.frameDown)

        self.layoutHLogin.addWidget(self.frameLogin)
        self.layoutHTop.addWidget(self.frameMessage)
        self.layoutHMessage.addWidget(self.lb_Message)
        self.layoutHMessage.addWidget(self.btn_Message)

        self.layoutHMessage.setContentsMargins(0,0,0,0)
        self.layoutHMessage.setSpacing(0)
        self.layoutVertical.setContentsMargins(0,0,0,0)
        self.layoutVertical.setSpacing(0)
        self.frameMessage.hide()
        # self.Animation()
        self.Form(self.frameLogin.size().width())

        self.setCentralWidget(self.loginWidget)
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
        self.IconTp.setPixmap(QtGui.QPixmap('Icons/ICONS_16/user4.png'))

        self.cb_users = QtWidgets.QComboBox(self.frameLogin)

        self.cb_users.addItems(['Name' for _ in range(5)])


        self.cb_users.setStyleSheet('''
        QComboBox{border:None;border-radius:12px;background-color:#595959;color:white;padding-left:%s px;}
        QComboBox:drop-down{border:0px solid;border-radius:10px;image:url(Icons/ICONS_16/drop2.png);padding-top:4px;margin-top:2px;margin-right:3px;}
        QComboBox:drop-down:hover {background:#22c1c3;border:None;}
        QComboBox QAbstractItemView{max-width:200px;min-height:15px;padding-top:5px;padding-left:%s px;padding-bottom:3px;background-color:#404040;color:white;border-radius:10px;selection-background-color:#404040;outline:0px;}
        QComboBox QAbstractItemView:hover{selection-background-color:red;}
        ''' % (int(90- len(self.cb_users.currentText())), int(87- len(self.cb_users.currentText()))) )

        print(self.cb_users.currentText())

        self.cb_users.setMaxVisibleItems(3)


        self.cb_users.resize(width,28)
        self.cb_users.setMaximumWidth(200)


        self.cb_users.move(int(width/2-200/2),165)
        self.IconTp.move(int(width/2-self.IconTp.size().width()/2),50)

        self.et_senha = QtWidgets.QLineEdit(self.frameLogin)

        self.et_senha.setStyleSheet('QLineEdit{border:None;border-radius:12px;background-color:#595959;color:white;font-size:12px;padding-left:5px;}\
                                     QLineEdit:hover{border:1.5px solid #22c1c3;outline:0;}')

        self.et_senha.setFocus()

        self.et_senha.setPlaceholderText('Senha')

        # self.et_senha.returnPressed.connect(self.Verify_User_Pass)

        self.et_senha.setEchoMode(QtWidgets.QLineEdit.Password)

        self.et_senha.resize(width,28)
        self.et_senha.setMaximumWidth(200)
        self.et_senha.move(int(width/2-200/2),200)

        self.btn_open= QtWidgets.QToolButton(self.frameLogin)
        self.btn_open.setText('Logar')
        
        self.btn_open.setStyleSheet('QToolButton{color:white;font-size:10pt;border:2px solid #22c1c3;border-radius:12px;text-align:right;}\
                                     QToolButton:hover{background:#22c1c3;border:None;outline:0;}')

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
