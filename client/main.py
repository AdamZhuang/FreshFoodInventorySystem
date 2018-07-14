from client.ui.signin import SignIn
import sys
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    signin = SignIn()
    signin.show()

    sys.exit(app.exec_())