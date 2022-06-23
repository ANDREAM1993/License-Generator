from models import Model
from views import View
from controllers import Controller
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    controller = Controller(model)
    view = View(model,controller)
    controller.start()
    sys.exit(app.exec_())