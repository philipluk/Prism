# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrismSettings.ui'
#
# Created: Wed Jan  8 01:12:27 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlg_PrismSettings(object):
    def setupUi(self, dlg_PrismSettings):
        dlg_PrismSettings.setObjectName("dlg_PrismSettings")
        dlg_PrismSettings.resize(843, 685)
        self.verticalLayout = QtGui.QVBoxLayout(dlg_PrismSettings)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(dlg_PrismSettings)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 841, 683))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tw_settings = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.tw_settings.setObjectName("tw_settings")
        self.tabWidgetPage4 = QtGui.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabWidgetPage4)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.tabWidgetPage4)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.l_about = QtGui.QLabel(self.groupBox)
        self.l_about.setText("")
        self.l_about.setOpenExternalLinks(True)
        self.l_about.setObjectName("l_about")
        self.horizontalLayout_11.addWidget(self.l_about)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.tabWidgetPage4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_updateInfo = QtGui.QLabel(self.groupBox_3)
        self.l_updateInfo.setText("")
        self.l_updateInfo.setObjectName("l_updateInfo")
        self.verticalLayout_4.addWidget(self.l_updateInfo)
        self.w_checkForUpdates_2 = QtGui.QWidget(self.groupBox_3)
        self.w_checkForUpdates_2.setObjectName("w_checkForUpdates_2")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.w_checkForUpdates_2)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.b_checkForUpdates = QtGui.QPushButton(self.w_checkForUpdates_2)
        self.b_checkForUpdates.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_checkForUpdates.setObjectName("b_checkForUpdates")
        self.horizontalLayout_12.addWidget(self.b_checkForUpdates)
        self.b_changelog = QtGui.QPushButton(self.w_checkForUpdates_2)
        self.b_changelog.setObjectName("b_changelog")
        self.horizontalLayout_12.addWidget(self.b_changelog)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.w_checkForUpdates_2)
        self.w_checkForUpdates = QtGui.QWidget(self.groupBox_3)
        self.w_checkForUpdates.setObjectName("w_checkForUpdates")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.w_checkForUpdates)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.l_checkForUpdates = QtGui.QLabel(self.w_checkForUpdates)
        self.l_checkForUpdates.setObjectName("l_checkForUpdates")
        self.horizontalLayout_10.addWidget(self.l_checkForUpdates)
        self.cb_checkForUpdates = QtGui.QComboBox(self.w_checkForUpdates)
        self.cb_checkForUpdates.setObjectName("cb_checkForUpdates")
        self.horizontalLayout_10.addWidget(self.cb_checkForUpdates)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.w_checkForUpdates)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.tw_settings.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtGui.QWidget(self.tabWidgetPage1)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.e_lname = QtGui.QLineEdit(self.widget)
        self.e_lname.setObjectName("e_lname")
        self.gridLayout_2.addWidget(self.e_lname, 1, 2, 1, 1)
        self.l_fname = QtGui.QLabel(self.widget)
        self.l_fname.setObjectName("l_fname")
        self.gridLayout_2.addWidget(self.l_fname, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.l_lname = QtGui.QLabel(self.widget)
        self.l_lname.setObjectName("l_lname")
        self.gridLayout_2.addWidget(self.l_lname, 1, 0, 1, 1)
        self.e_fname = QtGui.QLineEdit(self.widget)
        self.e_fname.setObjectName("e_fname")
        self.gridLayout_2.addWidget(self.e_fname, 0, 2, 1, 1)
        self.e_abbreviation = QtGui.QLineEdit(self.widget)
        self.e_abbreviation.setObjectName("e_abbreviation")
        self.gridLayout_2.addWidget(self.e_abbreviation, 2, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.widget)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.tw_settings.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.w_curPrj = QtGui.QGroupBox(self.tabWidgetPage2)
        self.w_curPrj.setObjectName("w_curPrj")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.w_curPrj)
        self.verticalLayout_6.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.l_projectName = QtGui.QLabel(self.w_curPrj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_projectName.sizePolicy().hasHeightForWidth())
        self.l_projectName.setSizePolicy(sizePolicy)
        self.l_projectName.setText("")
        self.l_projectName.setObjectName("l_projectName")
        self.verticalLayout_6.addWidget(self.l_projectName)
        self.l_projectPath = QtGui.QLabel(self.w_curPrj)
        self.l_projectPath.setText("")
        self.l_projectPath.setObjectName("l_projectPath")
        self.verticalLayout_6.addWidget(self.l_projectPath)
        spacerItem4 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem4)
        self.l_localPath = QtGui.QLabel(self.w_curPrj)
        self.l_localPath.setObjectName("l_localPath")
        self.verticalLayout_6.addWidget(self.l_localPath)
        self.widget_3 = QtGui.QWidget(self.w_curPrj)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.e_localPath = QtGui.QLineEdit(self.widget_3)
        self.e_localPath.setObjectName("e_localPath")
        self.horizontalLayout.addWidget(self.e_localPath)
        self.b_browseLocal = QtGui.QPushButton(self.widget_3)
        self.b_browseLocal.setMinimumSize(QtCore.QSize(50, 0))
        self.b_browseLocal.setMaximumSize(QtCore.QSize(50, 16777215))
        self.b_browseLocal.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseLocal.setObjectName("b_browseLocal")
        self.horizontalLayout.addWidget(self.b_browseLocal)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.w_resetPrjScripts = QtGui.QWidget(self.w_curPrj)
        self.w_resetPrjScripts.setObjectName("w_resetPrjScripts")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.w_resetPrjScripts)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6.addWidget(self.w_resetPrjScripts)
        self.verticalLayout_8.addWidget(self.w_curPrj)
        spacerItem5 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem5)
        self.widget_2 = QtGui.QWidget(self.tabWidgetPage2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8.addWidget(self.widget_2)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem6)
        self.widget_9 = QtGui.QWidget(self.tabWidgetPage2)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8.addWidget(self.widget_9)
        self.w_projects = QtGui.QWidget(self.tabWidgetPage2)
        self.w_projects.setObjectName("w_projects")
        self.lo_projects = QtGui.QVBoxLayout(self.w_projects)
        self.lo_projects.setContentsMargins(0, 0, 0, 0)
        self.lo_projects.setObjectName("lo_projects")
        self.verticalLayout_8.addWidget(self.w_projects)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.tw_settings.addTab(self.tabWidgetPage2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.w_prjSettings = QtGui.QWidget(self.tab)
        self.w_prjSettings.setEnabled(True)
        self.w_prjSettings.setObjectName("w_prjSettings")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.w_prjSettings)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem8 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem8)
        self.widget_5 = QtGui.QWidget(self.w_prjSettings)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtGui.QGridLayout(self.widget_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.e_curPname = QtGui.QLineEdit(self.widget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e_curPname.sizePolicy().hasHeightForWidth())
        self.e_curPname.setSizePolicy(sizePolicy)
        self.e_curPname.setObjectName("e_curPname")
        self.gridLayout.addWidget(self.e_curPname, 0, 2, 1, 1)
        self.l_curPname = QtGui.QLabel(self.widget_5)
        self.l_curPname.setObjectName("l_curPname")
        self.gridLayout.addWidget(self.l_curPname, 0, 0, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_5)
        self.widget_10 = QtGui.QWidget(self.w_prjSettings)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtGui.QLabel(self.widget_10)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.chb_curPuseLocal = QtGui.QCheckBox(self.widget_10)
        self.chb_curPuseLocal.setText("")
        self.chb_curPuseLocal.setChecked(True)
        self.chb_curPuseLocal.setObjectName("chb_curPuseLocal")
        self.horizontalLayout_5.addWidget(self.chb_curPuseLocal)
        self.verticalLayout_9.addWidget(self.widget_10)
        self.w_curPfps = QtGui.QWidget(self.w_prjSettings)
        self.w_curPfps.setObjectName("w_curPfps")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.w_curPfps)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtGui.QLabel(self.w_curPfps)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.chb_curPuseFps = QtGui.QCheckBox(self.w_curPfps)
        self.chb_curPuseFps.setText("")
        self.chb_curPuseFps.setChecked(False)
        self.chb_curPuseFps.setObjectName("chb_curPuseFps")
        self.horizontalLayout_6.addWidget(self.chb_curPuseFps)
        self.sp_curPfps = QtGui.QDoubleSpinBox(self.w_curPfps)
        self.sp_curPfps.setMinimumSize(QtCore.QSize(60, 0))
        self.sp_curPfps.setMinimum(1.0)
        self.sp_curPfps.setMaximum(9999.99)
        self.sp_curPfps.setProperty("value", 24.0)
        self.sp_curPfps.setObjectName("sp_curPfps")
        self.horizontalLayout_6.addWidget(self.sp_curPfps)
        self.verticalLayout_9.addWidget(self.w_curPfps)
        self.gb_curPversions = QtGui.QGroupBox(self.w_prjSettings)
        self.gb_curPversions.setCheckable(True)
        self.gb_curPversions.setChecked(False)
        self.gb_curPversions.setObjectName("gb_curPversions")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.gb_curPversions)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.w_versions = QtGui.QWidget(self.gb_curPversions)
        self.w_versions.setObjectName("w_versions")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.w_versions)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_11.addWidget(self.w_versions)
        self.verticalLayout_9.addWidget(self.gb_curPversions)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem12)
        self.verticalLayout_13.addWidget(self.w_prjSettings)
        self.tw_settings.addTab(self.tab, "")
        self.tab_dccApps = QtGui.QWidget()
        self.tab_dccApps.setObjectName("tab_dccApps")
        self.verticalLayout_24 = QtGui.QVBoxLayout(self.tab_dccApps)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.widget_23 = QtGui.QWidget(self.tab_dccApps)
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_26 = QtGui.QVBoxLayout(self.widget_23)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_24.addWidget(self.widget_23)
        self.tw_settings.addTab(self.tab_dccApps, "")
        self.tab_Plugins = QtGui.QWidget()
        self.tab_Plugins.setObjectName("tab_Plugins")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_Plugins)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtGui.QLabel(self.tab_Plugins)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tw_plugins = QtGui.QTableWidget(self.tab_Plugins)
        self.tw_plugins.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tw_plugins.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tw_plugins.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tw_plugins.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tw_plugins.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tw_plugins.setObjectName("tw_plugins")
        self.tw_plugins.setColumnCount(0)
        self.tw_plugins.setRowCount(0)
        self.tw_plugins.horizontalHeader().setHighlightSections(False)
        self.tw_plugins.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tw_plugins)
        self.widget_4 = QtGui.QWidget(self.tab_Plugins)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.b_reloadPlugins = QtGui.QPushButton(self.widget_4)
        self.b_reloadPlugins.setObjectName("b_reloadPlugins")
        self.horizontalLayout_8.addWidget(self.b_reloadPlugins)
        self.b_createPlugin = QtGui.QPushButton(self.widget_4)
        self.b_createPlugin.setObjectName("b_createPlugin")
        self.horizontalLayout_8.addWidget(self.b_createPlugin)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.tw_settings.addTab(self.tab_Plugins, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.chb_autosave = QtGui.QCheckBox(self.groupBox_4)
        self.chb_autosave.setChecked(True)
        self.chb_autosave.setObjectName("chb_autosave")
        self.verticalLayout_12.addWidget(self.chb_autosave)
        self.chb_browserStartup = QtGui.QCheckBox(self.groupBox_4)
        self.chb_browserStartup.setChecked(True)
        self.chb_browserStartup.setObjectName("chb_browserStartup")
        self.verticalLayout_12.addWidget(self.chb_browserStartup)
        self.chb_trayStartup = QtGui.QCheckBox(self.groupBox_4)
        self.chb_trayStartup.setChecked(True)
        self.chb_trayStartup.setObjectName("chb_trayStartup")
        self.verticalLayout_12.addWidget(self.chb_trayStartup)
        self.w_startTray = QtGui.QWidget(self.groupBox_4)
        self.w_startTray.setObjectName("w_startTray")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.w_startTray)
        self.horizontalLayout_7.setContentsMargins(17, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.b_startTray = QtGui.QPushButton(self.w_startTray)
        self.b_startTray.setMinimumSize(QtCore.QSize(150, 0))
        self.b_startTray.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.b_startTray.setObjectName("b_startTray")
        self.horizontalLayout_7.addWidget(self.b_startTray)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_12.addWidget(self.w_startTray)
        self.chb_highDPI = QtGui.QCheckBox(self.groupBox_4)
        self.chb_highDPI.setObjectName("chb_highDPI")
        self.verticalLayout_12.addWidget(self.chb_highDPI)
        self.verticalLayout_14.addWidget(self.groupBox_4)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_15.addWidget(self.label_10)
        self.widget_7 = QtGui.QWidget(self.groupBox_2)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.e_rvPath = QtGui.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.e_rvPath.setFont(font)
        self.e_rvPath.setObjectName("e_rvPath")
        self.horizontalLayout_3.addWidget(self.e_rvPath)
        self.b_browseRV = QtGui.QPushButton(self.widget_7)
        self.b_browseRV.setMinimumSize(QtCore.QSize(50, 0))
        self.b_browseRV.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.b_browseRV.setFont(font)
        self.b_browseRV.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseRV.setObjectName("b_browseRV")
        self.horizontalLayout_3.addWidget(self.b_browseRV)
        self.verticalLayout_15.addWidget(self.widget_7)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_15.addWidget(self.label_11)
        self.widget_19 = QtGui.QWidget(self.groupBox_2)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.widget_19)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.e_djvPath = QtGui.QLineEdit(self.widget_19)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.e_djvPath.setFont(font)
        self.e_djvPath.setObjectName("e_djvPath")
        self.horizontalLayout_9.addWidget(self.e_djvPath)
        self.b_browseDJV = QtGui.QPushButton(self.widget_19)
        self.b_browseDJV.setMinimumSize(QtCore.QSize(50, 0))
        self.b_browseDJV.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.b_browseDJV.setFont(font)
        self.b_browseDJV.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browseDJV.setObjectName("b_browseDJV")
        self.horizontalLayout_9.addWidget(self.b_browseDJV)
        self.verticalLayout_15.addWidget(self.widget_19)
        self.chb_preferDJV = QtGui.QCheckBox(self.groupBox_2)
        self.chb_preferDJV.setObjectName("chb_preferDJV")
        self.verticalLayout_15.addWidget(self.chb_preferDJV)
        self.verticalLayout_14.addWidget(self.groupBox_2)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem14)
        self.tw_settings.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tw_settings)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem15)
        self.buttonBox = QtGui.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(dlg_PrismSettings)
        self.tw_settings.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlg_PrismSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlg_PrismSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_PrismSettings)
        dlg_PrismSettings.setTabOrder(self.scrollArea, self.tw_settings)
        dlg_PrismSettings.setTabOrder(self.tw_settings, self.e_fname)
        dlg_PrismSettings.setTabOrder(self.e_fname, self.e_lname)
        dlg_PrismSettings.setTabOrder(self.e_lname, self.e_localPath)
        dlg_PrismSettings.setTabOrder(self.e_localPath, self.b_browseLocal)
        dlg_PrismSettings.setTabOrder(self.b_browseLocal, self.e_curPname)
        dlg_PrismSettings.setTabOrder(self.e_curPname, self.chb_curPuseLocal)
        dlg_PrismSettings.setTabOrder(self.chb_curPuseLocal, self.chb_curPuseFps)
        dlg_PrismSettings.setTabOrder(self.chb_curPuseFps, self.sp_curPfps)
        dlg_PrismSettings.setTabOrder(self.sp_curPfps, self.gb_curPversions)
        dlg_PrismSettings.setTabOrder(self.gb_curPversions, self.buttonBox)

    def retranslateUi(self, dlg_PrismSettings):
        dlg_PrismSettings.setWindowTitle(QtGui.QApplication.translate("dlg_PrismSettings", "Prism Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("dlg_PrismSettings", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("dlg_PrismSettings", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.b_checkForUpdates.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Check now", None, QtGui.QApplication.UnicodeUTF8))
        self.b_changelog.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Changelog", None, QtGui.QApplication.UnicodeUTF8))
        self.l_checkForUpdates.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Check for updates:", None, QtGui.QApplication.UnicodeUTF8))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tabWidgetPage4), QtGui.QApplication.translate("dlg_PrismSettings", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.l_fname.setText(QtGui.QApplication.translate("dlg_PrismSettings", "First Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Abbreviation:    ", None, QtGui.QApplication.UnicodeUTF8))
        self.l_lname.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Last Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tabWidgetPage1), QtGui.QApplication.translate("dlg_PrismSettings", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.w_curPrj.setTitle(QtGui.QApplication.translate("dlg_PrismSettings", "Current Project", None, QtGui.QApplication.UnicodeUTF8))
        self.l_projectName.setToolTip(QtGui.QApplication.translate("dlg_PrismSettings", "current project", None, QtGui.QApplication.UnicodeUTF8))
        self.l_projectPath.setToolTip(QtGui.QApplication.translate("dlg_PrismSettings", "current project path", None, QtGui.QApplication.UnicodeUTF8))
        self.l_localPath.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Local path:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_browseLocal.setText(QtGui.QApplication.translate("dlg_PrismSettings", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tabWidgetPage2), QtGui.QApplication.translate("dlg_PrismSettings", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.l_curPname.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Use additional local project folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Force FPS in scenefiles:", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_curPversions.setTitle(QtGui.QApplication.translate("dlg_PrismSettings", "Force program versions", None, QtGui.QApplication.UnicodeUTF8))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab), QtGui.QApplication.translate("dlg_PrismSettings", "Project Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_dccApps), QtGui.QApplication.translate("dlg_PrismSettings", "DCC apps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Loaded Plugins:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_reloadPlugins.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Reload all plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.b_createPlugin.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Create new plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_Plugins), QtGui.QApplication.translate("dlg_PrismSettings", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("dlg_PrismSettings", "Miscellaneous", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_autosave.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Autosave popup", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_browserStartup.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Open Project Browser on application startup", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_trayStartup.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Show Prism tray icon on system startup", None, QtGui.QApplication.UnicodeUTF8))
        self.b_startTray.setText(QtGui.QApplication.translate("dlg_PrismSettings", "Start Prism tray now", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_highDPI.setText(QtGui.QApplication.translate("dlg_PrismSettings", "HighDPI support (requires complete application restart) (experimental)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("dlg_PrismSettings", "Image player", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("dlg_PrismSettings", "RV path:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_browseRV.setText(QtGui.QApplication.translate("dlg_PrismSettings", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("dlg_PrismSettings", "DJV path:", None, QtGui.QApplication.UnicodeUTF8))
        self.b_browseDJV.setText(QtGui.QApplication.translate("dlg_PrismSettings", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.chb_preferDJV.setText(QtGui.QApplication.translate("dlg_PrismSettings", "prefer DJV", None, QtGui.QApplication.UnicodeUTF8))
        self.tw_settings.setTabText(self.tw_settings.indexOf(self.tab_2), QtGui.QApplication.translate("dlg_PrismSettings", "Miscellaneous", None, QtGui.QApplication.UnicodeUTF8))

