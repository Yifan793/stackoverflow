from PySide2.QtWidgets import QApplication
from wizardUI.wizard import tutorWizard
import sys

import resource_rc

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = tutorWizard()
    window.show()
    sys.exit(app.exec_())
