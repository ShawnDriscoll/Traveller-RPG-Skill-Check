# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog.ui'
#
# Created: Tue Mar 30 10:32:47 2021
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(480, 357)
        aboutDialog.setMinimumSize(QtCore.QSize(480, 357))
        aboutDialog.setMaximumSize(QtCore.QSize(480, 357))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sc_icon_16x16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        self.aboutOKButton = QtGui.QPushButton(aboutDialog)
        self.aboutOKButton.setGeometry(QtCore.QRect(380, 320, 75, 23))
        self.aboutOKButton.setObjectName(_fromUtf8("aboutOKButton"))
        self.bgArtLabel = QtGui.QLabel(aboutDialog)
        self.bgArtLabel.setGeometry(QtCore.QRect(0, 0, 481, 301))
        self.bgArtLabel.setText(_fromUtf8(""))
        self.bgArtLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/sc_dialog.png")))
        self.bgArtLabel.setObjectName(_fromUtf8("bgArtLabel"))
        self.textLabel = QtGui.QLabel(aboutDialog)
        self.textLabel.setGeometry(QtCore.QRect(140, 20, 321, 261))
        self.textLabel.setTextFormat(QtCore.Qt.RichText)
        self.textLabel.setScaledContents(False)
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setOpenExternalLinks(True)
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.line = QtGui.QFrame(aboutDialog)
        self.line.setGeometry(QtCore.QRect(137, 210, 321, 20))
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QtGui.QApplication.translate("aboutDialog", "About Skill Check", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutOKButton.setText(QtGui.QApplication.translate("aboutDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel.setText(QtGui.QApplication.translate("aboutDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Skill Check for Windows 32-bit</span></p><p>Version: Mongoose Traveller Edition</p><p>Build: 0.7.6 (Beta)</p><p>Produced by Shonner Corp. Copyright (C) 2014. Visit us on the web at <a href=\"http://www.shonner.com\"><span style=\" text-decoration: underline; color:#0000ff;\">www.shonner.com</span></a></p><p>Software design by Shawn Driscoll. Contact him at <a href=\"mailto:shawndriscoll@hotmail.com?subject=Skill Check for Mongoose Traveller\"><span style=\" text-decoration: underline; color:#0000ff;\">shawndriscoll@hotmail.com</span></a></p><p>Qt GUI Toolkit is copyright (C) 2012 Nokia Corporation</p><p><br/></p><p>The Traveller game in all forms is owned by Far Future Enterprises. Copyright 1977 - 2021 Far Future Enterprises. Traveller is a registered trademark of Far Future Enterprises.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import skillcheck_rc
