# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\electrodearraydetectorwidget.ui'
#
# Created: Thu Dec  6 10:30:38 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ElectrodeArrayDetectorWidget(object):
    def setupUi(self, shared_open_gl_widget, ElectrodeArrayDetectorWidget):
        ElectrodeArrayDetectorWidget.setObjectName("ElectrodeArrayDetectorWidget")
        ElectrodeArrayDetectorWidget.resize(870, 576)
        self.horizontalLayout = QtGui.QHBoxLayout(ElectrodeArrayDetectorWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.controlPanel_groupBox = QtGui.QGroupBox(ElectrodeArrayDetectorWidget)
        self.controlPanel_groupBox.setObjectName("controlPanel_groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.controlPanel_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.time_groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.time_groupBox.setObjectName("time_groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.time_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.timePlayStop_pushButton = QtGui.QPushButton(self.time_groupBox)
        self.timePlayStop_pushButton.setObjectName("timePlayStop_pushButton")
        self.gridLayout_4.addWidget(self.timePlayStop_pushButton, 1, 1, 1, 1)
        self.timeValue_label = QtGui.QLabel(self.time_groupBox)
        self.timeValue_label.setObjectName("timeValue_label")
        self.gridLayout_4.addWidget(self.timeValue_label, 0, 0, 1, 1)
        self.timeValue_doubleSpinBox = QtGui.QDoubleSpinBox(self.time_groupBox)
        self.timeValue_doubleSpinBox.setMaximum(12000.0)
        self.timeValue_doubleSpinBox.setObjectName("timeValue_doubleSpinBox")
        self.gridLayout_4.addWidget(self.timeValue_doubleSpinBox, 0, 1, 1, 1)
        self.timeLoop_checkBox = QtGui.QCheckBox(self.time_groupBox)
        self.timeLoop_checkBox.setObjectName("timeLoop_checkBox")
        self.gridLayout_4.addWidget(self.timeLoop_checkBox, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.time_groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.detectElectrodes_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.detectElectrodes_pushButton.setObjectName("detectElectrodes_pushButton")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.detectElectrodes_pushButton)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.trackElectrodePoints_pushButton = QtGui.QPushButton(self.groupBox_3)
        self.trackElectrodePoints_pushButton.setObjectName("trackElectrodePoints_pushButton")
        self.horizontalLayout_4.addWidget(self.trackElectrodePoints_pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox_3)
        self.reset_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.reset_pushButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.frame_2 = QtGui.QFrame(self.controlPanel_groupBox)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cheat_pushButton = QtGui.QPushButton(self.frame_2)
        self.cheat_pushButton.setFlat(True)
        self.cheat_pushButton.setObjectName("cheat_pushButton")
        self.horizontalLayout_5.addWidget(self.cheat_pushButton)
        spacerItem3 = QtGui.QSpacerItem(104, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_2)
        self.groupBox = QtGui.QGroupBox(self.controlPanel_groupBox)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statusText_label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusText_label.sizePolicy().hasHeightForWidth())
        self.statusText_label.setSizePolicy(sizePolicy)
        self.statusText_label.setObjectName("statusText_label")
        self.horizontalLayout_3.addWidget(self.statusText_label)
        self.verticalLayout.addWidget(self.groupBox)
        self.frame = QtGui.QFrame(self.controlPanel_groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.done_pushButton = QtGui.QPushButton(self.frame)
        self.done_pushButton.setObjectName("done_pushButton")
        self.horizontalLayout_2.addWidget(self.done_pushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.controlPanel_groupBox)
        self.sceneviewer_widget = BaseSceneviewerWidget(ElectrodeArrayDetectorWidget, shared_open_gl_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)
        self.sceneviewer_widget.setObjectName("sceneviewer_widget")
        self.horizontalLayout.addWidget(self.sceneviewer_widget)

        self.retranslateUi(ElectrodeArrayDetectorWidget)
        QtCore.QMetaObject.connectSlotsByName(ElectrodeArrayDetectorWidget)

    def retranslateUi(self, ElectrodeArrayDetectorWidget):
        ElectrodeArrayDetectorWidget.setWindowTitle(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Electrode Array Detector", None, QtGui.QApplication.UnicodeUTF8))
        self.controlPanel_groupBox.setTitle(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Control Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.time_groupBox.setTitle(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.timePlayStop_pushButton.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.timeValue_label.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Time value:", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLoop_checkBox.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Loop", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Activity:", None, QtGui.QApplication.UnicodeUTF8))
        self.detectElectrodes_pushButton.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Detect electrodes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Track electrode points", None, QtGui.QApplication.UnicodeUTF8))
        self.trackElectrodePoints_pushButton.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Track", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_pushButton.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.cheat_pushButton.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "         ", None, QtGui.QApplication.UnicodeUTF8))
        self.statusText_label.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.done_pushButton.setText(QtGui.QApplication.translate("ElectrodeArrayDetectorWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.basesceneviewerwidget import BaseSceneviewerWidget
