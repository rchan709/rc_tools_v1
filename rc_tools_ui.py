# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rc_tools.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QButtonGroup, QCheckBox,
    QColumnView, QDoubleSpinBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1108, 669)
        MainWindow.setMinimumSize(QSize(400, 600))
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setToolTipDuration(-1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.columnView_3 = QColumnView(self.groupBox)
        self.columnView_3.setObjectName(u"columnView_3")

        self.verticalLayout_6.addWidget(self.columnView_3)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.treeWidget = QTreeWidget(self.groupBox_2)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.treeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setMinimumSectionSize(40)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setProperty("showSortIndicator", False)

        self.verticalLayout_5.addWidget(self.treeWidget)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.columnView_2 = QColumnView(self.groupBox_4)
        self.columnView_2.setObjectName(u"columnView_2")

        self.verticalLayout_8.addWidget(self.columnView_2)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_7.addWidget(self.pushButton_3)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_7 = QPushButton(self.tab)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_38 = QPushButton(self.tab)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMaximumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_38)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.pushButton_8 = QPushButton(self.tab)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.tab)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.tab)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.groupBox_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 536, 438))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_17 = QPushButton(self.groupBox_5)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_9.addWidget(self.pushButton_17)

        self.pushButton_16 = QPushButton(self.groupBox_5)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_9.addWidget(self.pushButton_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_36 = QPushButton(self.groupBox_5)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.horizontalLayout_12.addWidget(self.pushButton_36)

        self.pushButton_11 = QPushButton(self.groupBox_5)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_12.addWidget(self.pushButton_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.pushButton_37 = QPushButton(self.groupBox_5)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.verticalLayout_3.addWidget(self.pushButton_37)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_3 = QRadioButton(self.groupBox_8)
        self.BG_shape_mirror_space = QButtonGroup(MainWindow)
        self.BG_shape_mirror_space.setObjectName(u"BG_shape_mirror_space")
        self.BG_shape_mirror_space.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(True)

        self.horizontalLayout_7.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_8)
        self.BG_shape_mirror_space.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_7.addWidget(self.radioButton_4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_14 = QPushButton(self.groupBox_8)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_6.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.groupBox_8)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_6.addWidget(self.pushButton_15)


        self.verticalLayout_15.addLayout(self.horizontalLayout_6)

        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setEnabled(False)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_3 = QCheckBox(self.groupBox_9)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setTristate(False)

        self.horizontalLayout_8.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.groupBox_9)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_8.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.groupBox_9)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_8.addWidget(self.checkBox)


        self.verticalLayout_15.addWidget(self.groupBox_9)


        self.horizontalLayout.addWidget(self.groupBox_8)

        self.groupBox_12 = QGroupBox(self.groupBox_6)
        self.groupBox_12.setObjectName(u"groupBox_12")

        self.horizontalLayout.addWidget(self.groupBox_12)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.radioButton_2 = QRadioButton(self.groupBox_7)
        self.BG_shape_translate_space = QButtonGroup(MainWindow)
        self.BG_shape_translate_space.setObjectName(u"BG_shape_translate_space")
        self.BG_shape_translate_space.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.verticalLayout_13.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox_7)
        self.BG_shape_translate_space.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_13.addWidget(self.radioButton)


        self.horizontalLayout_5.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_12 = QPushButton(self.groupBox_7)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_14.addWidget(self.pushButton_12)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setSingleStep(0.100000000000000)
        self.doubleSpinBox.setValue(0.100000000000000)

        self.verticalLayout_14.addWidget(self.doubleSpinBox)

        self.pushButton_13 = QPushButton(self.groupBox_7)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_14.addWidget(self.pushButton_13)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_18 = QPushButton(self.groupBox_7)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_19.addWidget(self.pushButton_18)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setSingleStep(0.100000000000000)
        self.doubleSpinBox_3.setValue(0.100000000000000)

        self.verticalLayout_19.addWidget(self.doubleSpinBox_3)

        self.pushButton_19 = QPushButton(self.groupBox_7)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_19.addWidget(self.pushButton_19)


        self.horizontalLayout_5.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pushButton_20 = QPushButton(self.groupBox_7)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout_20.addWidget(self.pushButton_20)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_7)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setSingleStep(0.100000000000000)
        self.doubleSpinBox_4.setValue(0.100000000000000)

        self.verticalLayout_20.addWidget(self.doubleSpinBox_4)

        self.pushButton_21 = QPushButton(self.groupBox_7)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.verticalLayout_20.addWidget(self.pushButton_21)


        self.horizontalLayout_5.addLayout(self.verticalLayout_20)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_11.addWidget(self.groupBox_7)

        self.groupBox_10 = QGroupBox(self.groupBox_6)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.radioButton_7 = QRadioButton(self.groupBox_10)
        self.BG_shape_rotate_space = QButtonGroup(MainWindow)
        self.BG_shape_rotate_space.setObjectName(u"BG_shape_rotate_space")
        self.BG_shape_rotate_space.addButton(self.radioButton_7)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setChecked(True)

        self.verticalLayout_18.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.groupBox_10)
        self.BG_shape_rotate_space.addButton(self.radioButton_8)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.verticalLayout_18.addWidget(self.radioButton_8)


        self.horizontalLayout_10.addLayout(self.verticalLayout_18)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.pushButton_22 = QPushButton(self.groupBox_10)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.verticalLayout_21.addWidget(self.pushButton_22)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setDecimals(0)
        self.doubleSpinBox_5.setMaximum(360.000000000000000)
        self.doubleSpinBox_5.setSingleStep(5.000000000000000)
        self.doubleSpinBox_5.setValue(15.000000000000000)

        self.verticalLayout_21.addWidget(self.doubleSpinBox_5)

        self.pushButton_23 = QPushButton(self.groupBox_10)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.verticalLayout_21.addWidget(self.pushButton_23)


        self.horizontalLayout_10.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.pushButton_24 = QPushButton(self.groupBox_10)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_22.addWidget(self.pushButton_24)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setDecimals(0)
        self.doubleSpinBox_6.setMaximum(360.000000000000000)
        self.doubleSpinBox_6.setSingleStep(5.000000000000000)
        self.doubleSpinBox_6.setValue(15.000000000000000)

        self.verticalLayout_22.addWidget(self.doubleSpinBox_6)

        self.pushButton_25 = QPushButton(self.groupBox_10)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.verticalLayout_22.addWidget(self.pushButton_25)


        self.horizontalLayout_10.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_26 = QPushButton(self.groupBox_10)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.verticalLayout_23.addWidget(self.pushButton_26)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setDecimals(0)
        self.doubleSpinBox_7.setMaximum(360.000000000000000)
        self.doubleSpinBox_7.setSingleStep(5.000000000000000)
        self.doubleSpinBox_7.setValue(15.000000000000000)

        self.verticalLayout_23.addWidget(self.doubleSpinBox_7)

        self.pushButton_27 = QPushButton(self.groupBox_10)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_23.addWidget(self.pushButton_27)


        self.horizontalLayout_10.addLayout(self.verticalLayout_23)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.groupBox_6)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.radioButton_9 = QRadioButton(self.groupBox_11)
        self.BG_shape_scale_space = QButtonGroup(MainWindow)
        self.BG_shape_scale_space.setObjectName(u"BG_shape_scale_space")
        self.BG_shape_scale_space.addButton(self.radioButton_9)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setChecked(True)

        self.verticalLayout_24.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.groupBox_11)
        self.BG_shape_scale_space.addButton(self.radioButton_10)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.verticalLayout_24.addWidget(self.radioButton_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_28 = QPushButton(self.groupBox_11)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.verticalLayout_25.addWidget(self.pushButton_28)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setMaximum(100.000000000000000)
        self.doubleSpinBox_8.setSingleStep(0.100000000000000)
        self.doubleSpinBox_8.setValue(0.100000000000000)

        self.verticalLayout_25.addWidget(self.doubleSpinBox_8)

        self.pushButton_29 = QPushButton(self.groupBox_11)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.verticalLayout_25.addWidget(self.pushButton_29)


        self.horizontalLayout_11.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pushButton_30 = QPushButton(self.groupBox_11)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.verticalLayout_26.addWidget(self.pushButton_30)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setMaximum(100.000000000000000)
        self.doubleSpinBox_9.setSingleStep(0.100000000000000)
        self.doubleSpinBox_9.setValue(0.100000000000000)

        self.verticalLayout_26.addWidget(self.doubleSpinBox_9)

        self.pushButton_31 = QPushButton(self.groupBox_11)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.verticalLayout_26.addWidget(self.pushButton_31)


        self.horizontalLayout_11.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pushButton_32 = QPushButton(self.groupBox_11)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.verticalLayout_27.addWidget(self.pushButton_32)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setMaximum(100.000000000000000)
        self.doubleSpinBox_10.setSingleStep(0.100000000000000)
        self.doubleSpinBox_10.setValue(0.100000000000000)

        self.verticalLayout_27.addWidget(self.doubleSpinBox_10)

        self.pushButton_33 = QPushButton(self.groupBox_11)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.verticalLayout_27.addWidget(self.pushButton_33)


        self.horizontalLayout_11.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_34 = QPushButton(self.groupBox_11)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.verticalLayout_28.addWidget(self.pushButton_34)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setMaximum(100.000000000000000)
        self.doubleSpinBox_11.setSingleStep(0.100000000000000)
        self.doubleSpinBox_11.setValue(0.100000000000000)

        self.verticalLayout_28.addWidget(self.doubleSpinBox_11)

        self.pushButton_35 = QPushButton(self.groupBox_11)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.verticalLayout_28.addWidget(self.pushButton_35)


        self.horizontalLayout_11.addLayout(self.verticalLayout_28)


        self.verticalLayout_11.addWidget(self.groupBox_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_11.addWidget(self.pushButton_4)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_6 = QPushButton(self.tab_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.label_2 = QLabel(self.tab_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 140, 241, 101))
        self.label_2.setWordWrap(True)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label = QLabel(self.tab_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 100, 331, 191))
        self.label.setWordWrap(True)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit = QLineEdit(self.tab_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton_5 = QPushButton(self.tab_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1108, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionImport)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
#if QT_CONFIG(tooltip)
        self.actionImport.setToolTip(QCoreApplication.translate("MainWindow", u"This will open a maya file. Please save your work!", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Rig Assets", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Rig Tree", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Version", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Attribute Editor", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Selected joint", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Update Rig", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Show Locators", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Show mesh", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"ShowControls", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"ShopLRA", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Rigging", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Shapes", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Save As New Shape", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Add selected shape to control", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Replace control with selected shape", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"New control on selected object with selected shape", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Edit Shape", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Mirror", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Left -> Right", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Right -> Left", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"+X", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"-X", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"+Y", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"-Y", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"+Z", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"-Z", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"+X", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"-X", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"+Y", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"-Y", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"+Z", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"-Z", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"+X", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"-X", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"+Y", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"-Y", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"+Z", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"-Z", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"+XYZ", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"-XYZ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Control Shape Editor", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Skin Weight Helper", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"this is where i would have cloth/hair sim, rope sim, jiggle sim be", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Physics", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Was thinking about a game/animation exporter, but the game rig and maybe mesh can be exported with the other exporter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Page", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Save as file name then reopen as filename_working (the file exported is not being worked on, but is replaced when exported.)", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Exporter", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

