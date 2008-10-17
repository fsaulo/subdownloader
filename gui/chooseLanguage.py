
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, SIGNAL, QObject, QCoreApplication, \
                         QSettings, QVariant, QSize, QEventLoop, QString, \
                         QBuffer, QIODevice, QModelIndex,QDir
from PyQt4.QtGui import QPixmap, QErrorMessage, QLineEdit, \
                        QMessageBox, QFileDialog, QIcon, QDialog, QInputDialog,QDirModel, QItemSelectionModel, QListWidgetItem
from PyQt4.Qt import qDebug, qFatal, qWarning, qCritical

from languages import Languages, autodetect_lang
from gui.chooseLanguage_ui import Ui_ChooseLanguageDialog
import logging
log = logging.getLogger("subdownloader.gui.chooseLanguage")

class chooseLanguageDialog(QtGui.QDialog): 
    def __init__(self, parent, user_locale):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_ChooseLanguageDialog()
        self.ui.setupUi(self)
        self._main  = parent
        settings = QSettings()
        QObject.connect(self.ui.OKButton, SIGNAL("clicked(bool)"), self.onButtonClose)
        
        for lang_xx in self._main.interface_langs:
                item = QListWidgetItem(Languages.xx2name(lang_xx))
                item.setData(Qt.UserRole, QVariant(lang_xx))
                self.ui.languagesList.addItem(item)
                if lang_xx == user_locale:
                        self.ui.languagesList.setCurrentItem(item,QItemSelectionModel.ClearAndSelect)

    def onButtonClose(self):
        if not self.ui.languagesList.currentItem():
                QMessageBox.about(self,"Alert","Please select a language")
        else:
                choosen_lang = str(self.ui.languagesList.currentItem().data(Qt.UserRole).toString().toUtf8())
                self._main.choosenLanguage = choosen_lang
                self.reject()

