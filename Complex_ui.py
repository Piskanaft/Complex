# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Complex.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 632)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(40, 40))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LeftMenu = QWidget(self.tab)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.verticalLayout = QVBoxLayout(self.LeftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.load_file_button = QPushButton(self.LeftMenu)
        self.load_file_button.setObjectName(u"load_file_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_file_button.sizePolicy().hasHeightForWidth())
        self.load_file_button.setSizePolicy(sizePolicy)
        self.load_file_button.setMinimumSize(QSize(0, 50))
        self.load_file_button.setMaximumSize(QSize(99999, 70))

        self.verticalLayout.addWidget(self.load_file_button)

        self.chosen_catalog_label = QLabel(self.LeftMenu)
        self.chosen_catalog_label.setObjectName(u"chosen_catalog_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chosen_catalog_label.sizePolicy().hasHeightForWidth())
        self.chosen_catalog_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Bahnschrift Condensed"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.chosen_catalog_label.setFont(font)
        self.chosen_catalog_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.chosen_catalog_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.chosen_catalog_label)

        self.frame = QFrame(self.LeftMenu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.Mag_column_label = QLabel(self.frame)
        self.Mag_column_label.setObjectName(u"Mag_column_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Mag_column_label.sizePolicy().hasHeightForWidth())
        self.Mag_column_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.Mag_column_label)

        self.Mag_column_lineedit = QLineEdit(self.frame)
        self.Mag_column_lineedit.setObjectName(u"Mag_column_lineedit")
        self.Mag_column_lineedit.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Mag_column_lineedit.sizePolicy().hasHeightForWidth())
        self.Mag_column_lineedit.setSizePolicy(sizePolicy3)
        self.Mag_column_lineedit.setMaxLength(32762)
        self.Mag_column_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.Mag_column_lineedit)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.available_sheets_label = QLabel(self.LeftMenu)
        self.available_sheets_label.setObjectName(u"available_sheets_label")
        self.available_sheets_label.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.available_sheets_label.sizePolicy().hasHeightForWidth())
        self.available_sheets_label.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.available_sheets_label.setFont(font1)
        self.available_sheets_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.available_sheets_label)

        self.sheets_layout = QVBoxLayout()
        self.sheets_layout.setObjectName(u"sheets_layout")

        self.verticalLayout.addLayout(self.sheets_layout)


        self.horizontalLayout.addWidget(self.LeftMenu, 0, Qt.AlignTop)

        self.RightMenu = QWidget(self.tab)
        self.RightMenu.setObjectName(u"RightMenu")
        self.RightMenuLayout = QVBoxLayout(self.RightMenu)
        self.RightMenuLayout.setSpacing(5)
        self.RightMenuLayout.setObjectName(u"RightMenuLayout")
        self.RightMenuLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.RightMenuLayout.setContentsMargins(1, -1, 1, 1)
        self.chosen_sheet_status = QLabel(self.RightMenu)
        self.chosen_sheet_status.setObjectName(u"chosen_sheet_status")
        self.chosen_sheet_status.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.chosen_sheet_status.sizePolicy().hasHeightForWidth())
        self.chosen_sheet_status.setSizePolicy(sizePolicy5)
        self.chosen_sheet_status.setMinimumSize(QSize(0, 0))
        self.chosen_sheet_status.setMaximumSize(QSize(16777215, 23))
        font2 = QFont()
        font2.setFamilies([u"consolas"])
        font2.setPointSize(6)
        self.chosen_sheet_status.setFont(font2)
        self.chosen_sheet_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.chosen_sheet_status.setWordWrap(True)

        self.RightMenuLayout.addWidget(self.chosen_sheet_status)

        self.show_graph_button = QPushButton(self.RightMenu)
        self.show_graph_button.setObjectName(u"show_graph_button")
        self.show_graph_button.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.show_graph_button.sizePolicy().hasHeightForWidth())
        self.show_graph_button.setSizePolicy(sizePolicy6)
        self.show_graph_button.setAutoRepeatDelay(300)

        self.RightMenuLayout.addWidget(self.show_graph_button, 0, Qt.AlignTop)

        self.show_mc_on_graph_checkbox = QCheckBox(self.RightMenu)
        self.show_mc_on_graph_checkbox.setObjectName(u"show_mc_on_graph_checkbox")
        self.show_mc_on_graph_checkbox.setEnabled(False)
        self.show_mc_on_graph_checkbox.setChecked(True)

        self.RightMenuLayout.addWidget(self.show_mc_on_graph_checkbox)

        self.calculate_all_methods_button = QPushButton(self.RightMenu)
        self.calculate_all_methods_button.setObjectName(u"calculate_all_methods_button")
        self.calculate_all_methods_button.setEnabled(False)

        self.RightMenuLayout.addWidget(self.calculate_all_methods_button)

        self.methods_form = QWidget(self.RightMenu)
        self.methods_form.setObjectName(u"methods_form")
        self.methods_formLayout = QFormLayout(self.methods_form)
        self.methods_formLayout.setObjectName(u"methods_formLayout")
        self.calculate_maxc_button = QPushButton(self.methods_form)
        self.calculate_maxc_button.setObjectName(u"calculate_maxc_button")
        self.calculate_maxc_button.setEnabled(False)

        self.methods_formLayout.setWidget(0, QFormLayout.LabelRole, self.calculate_maxc_button)

        self.calculate_maxc_label = QLabel(self.methods_form)
        self.calculate_maxc_label.setObjectName(u"calculate_maxc_label")

        self.methods_formLayout.setWidget(0, QFormLayout.FieldRole, self.calculate_maxc_label)

        self.calculate_gft_button = QPushButton(self.methods_form)
        self.calculate_gft_button.setObjectName(u"calculate_gft_button")
        self.calculate_gft_button.setEnabled(False)

        self.methods_formLayout.setWidget(1, QFormLayout.LabelRole, self.calculate_gft_button)

        self.calculate_gft_label = QLabel(self.methods_form)
        self.calculate_gft_label.setObjectName(u"calculate_gft_label")

        self.methods_formLayout.setWidget(1, QFormLayout.FieldRole, self.calculate_gft_label)

        self.calculate_lls_button = QPushButton(self.methods_form)
        self.calculate_lls_button.setObjectName(u"calculate_lls_button")
        self.calculate_lls_button.setEnabled(False)

        self.methods_formLayout.setWidget(2, QFormLayout.LabelRole, self.calculate_lls_button)

        self.calculate_lls_label = QLabel(self.methods_form)
        self.calculate_lls_label.setObjectName(u"calculate_lls_label")

        self.methods_formLayout.setWidget(2, QFormLayout.FieldRole, self.calculate_lls_label)

        self.calculate_emr_button = QPushButton(self.methods_form)
        self.calculate_emr_button.setObjectName(u"calculate_emr_button")
        self.calculate_emr_button.setEnabled(False)

        self.methods_formLayout.setWidget(3, QFormLayout.LabelRole, self.calculate_emr_button)

        self.calculate_emr_label = QLabel(self.methods_form)
        self.calculate_emr_label.setObjectName(u"calculate_emr_label")

        self.methods_formLayout.setWidget(3, QFormLayout.FieldRole, self.calculate_emr_label)


        self.RightMenuLayout.addWidget(self.methods_form)


        self.horizontalLayout.addWidget(self.RightMenu, 0, Qt.AlignTop)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        icon1 = QIcon()
        icon1.addFile(u"icons/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Orth_horizontalLayout = QHBoxLayout()
        self.Orth_horizontalLayout.setObjectName(u"Orth_horizontalLayout")
        self.Orth_horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.orth_leftMenu = QWidget(self.tab_2)
        self.orth_leftMenu.setObjectName(u"orth_leftMenu")
        self.Orth_LeftMenu = QVBoxLayout(self.orth_leftMenu)
        self.Orth_LeftMenu.setObjectName(u"Orth_LeftMenu")
        self.orth_load_file_button = QPushButton(self.orth_leftMenu)
        self.orth_load_file_button.setObjectName(u"orth_load_file_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.orth_load_file_button.sizePolicy().hasHeightForWidth())
        self.orth_load_file_button.setSizePolicy(sizePolicy7)
        self.orth_load_file_button.setMinimumSize(QSize(0, 50))
        self.orth_load_file_button.setMaximumSize(QSize(99999, 70))

        self.Orth_LeftMenu.addWidget(self.orth_load_file_button)

        self.orth_chosen_catalog_label = QLabel(self.orth_leftMenu)
        self.orth_chosen_catalog_label.setObjectName(u"orth_chosen_catalog_label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.orth_chosen_catalog_label.sizePolicy().hasHeightForWidth())
        self.orth_chosen_catalog_label.setSizePolicy(sizePolicy8)
        self.orth_chosen_catalog_label.setFont(font)
        self.orth_chosen_catalog_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.orth_chosen_catalog_label.setWordWrap(True)

        self.Orth_LeftMenu.addWidget(self.orth_chosen_catalog_label)

        self.orth_catalog_size_label = QLabel(self.orth_leftMenu)
        self.orth_catalog_size_label.setObjectName(u"orth_catalog_size_label")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(20)
        self.orth_catalog_size_label.setFont(font3)
        self.orth_catalog_size_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.Orth_LeftMenu.addWidget(self.orth_catalog_size_label)

        self.frame_2 = QFrame(self.orth_leftMenu)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy7.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy7)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.t_criterion_label = QLabel(self.frame_2)
        self.t_criterion_label.setObjectName(u"t_criterion_label")
        sizePolicy7.setHeightForWidth(self.t_criterion_label.sizePolicy().hasHeightForWidth())
        self.t_criterion_label.setSizePolicy(sizePolicy7)

        self.horizontalLayout_5.addWidget(self.t_criterion_label)

        self.t_criterion_value_lineedit = QLineEdit(self.frame_2)
        self.t_criterion_value_lineedit.setObjectName(u"t_criterion_value_lineedit")
        self.t_criterion_value_lineedit.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.t_criterion_value_lineedit.sizePolicy().hasHeightForWidth())
        self.t_criterion_value_lineedit.setSizePolicy(sizePolicy9)
        self.t_criterion_value_lineedit.setMaxLength(32762)
        self.t_criterion_value_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.t_criterion_value_lineedit)


        self.Orth_LeftMenu.addWidget(self.frame_2)


        self.Orth_horizontalLayout.addWidget(self.orth_leftMenu)

        self.orth_rightMenu = QWidget(self.tab_2)
        self.orth_rightMenu.setObjectName(u"orth_rightMenu")
        self.Orth_RightMenu = QVBoxLayout(self.orth_rightMenu)
        self.Orth_RightMenu.setObjectName(u"Orth_RightMenu")
        self.orth_calculate_button = QPushButton(self.orth_rightMenu)
        self.orth_calculate_button.setObjectName(u"orth_calculate_button")
        self.orth_calculate_button.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.orth_calculate_button.sizePolicy().hasHeightForWidth())
        self.orth_calculate_button.setSizePolicy(sizePolicy7)
        self.orth_calculate_button.setMinimumSize(QSize(0, 50))
        self.orth_calculate_button.setMaximumSize(QSize(99999, 70))

        self.Orth_RightMenu.addWidget(self.orth_calculate_button)

        self.orth_result_textEdit = QTextEdit(self.orth_rightMenu)
        self.orth_result_textEdit.setObjectName(u"orth_result_textEdit")
        self.orth_result_textEdit.setEnabled(False)
        self.orth_result_textEdit.setReadOnly(True)

        self.Orth_RightMenu.addWidget(self.orth_result_textEdit)

        self.orth_plot_button = QPushButton(self.orth_rightMenu)
        self.orth_plot_button.setObjectName(u"orth_plot_button")
        self.orth_plot_button.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.orth_plot_button.sizePolicy().hasHeightForWidth())
        self.orth_plot_button.setSizePolicy(sizePolicy7)
        self.orth_plot_button.setMinimumSize(QSize(0, 50))
        self.orth_plot_button.setMaximumSize(QSize(99999, 70))

        self.Orth_RightMenu.addWidget(self.orth_plot_button)


        self.Orth_horizontalLayout.addWidget(self.orth_rightMenu)


        self.horizontalLayout_3.addLayout(self.Orth_horizontalLayout)

        icon2 = QIcon()
        icon2.addFile(u"linear-regression.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.dist_horizontalLayout = QHBoxLayout()
        self.dist_horizontalLayout.setObjectName(u"dist_horizontalLayout")
        self.dist_leftMenu = QWidget(self.tab_3)
        self.dist_leftMenu.setObjectName(u"dist_leftMenu")
        self.verticalLayout_3 = QVBoxLayout(self.dist_leftMenu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dist_load_file_button = QPushButton(self.dist_leftMenu)
        self.dist_load_file_button.setObjectName(u"dist_load_file_button")
        sizePolicy7.setHeightForWidth(self.dist_load_file_button.sizePolicy().hasHeightForWidth())
        self.dist_load_file_button.setSizePolicy(sizePolicy7)
        self.dist_load_file_button.setMinimumSize(QSize(0, 50))
        self.dist_load_file_button.setMaximumSize(QSize(99999, 70))

        self.verticalLayout_3.addWidget(self.dist_load_file_button)

        self.dist_chosen_catalog_label = QLabel(self.dist_leftMenu)
        self.dist_chosen_catalog_label.setObjectName(u"dist_chosen_catalog_label")
        sizePolicy8.setHeightForWidth(self.dist_chosen_catalog_label.sizePolicy().hasHeightForWidth())
        self.dist_chosen_catalog_label.setSizePolicy(sizePolicy8)
        self.dist_chosen_catalog_label.setFont(font)
        self.dist_chosen_catalog_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dist_chosen_catalog_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.dist_chosen_catalog_label)

        self.dist_catalog_size_label = QLabel(self.dist_leftMenu)
        self.dist_catalog_size_label.setObjectName(u"dist_catalog_size_label")
        self.dist_catalog_size_label.setFont(font3)
        self.dist_catalog_size_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.dist_catalog_size_label)


        self.dist_horizontalLayout.addWidget(self.dist_leftMenu)

        self.dist_rightMenu = QWidget(self.tab_3)
        self.dist_rightMenu.setObjectName(u"dist_rightMenu")
        self.verticalLayout_4 = QVBoxLayout(self.dist_rightMenu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dist_calculate_button = QPushButton(self.dist_rightMenu)
        self.dist_calculate_button.setObjectName(u"dist_calculate_button")
        self.dist_calculate_button.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.dist_calculate_button.sizePolicy().hasHeightForWidth())
        self.dist_calculate_button.setSizePolicy(sizePolicy7)
        self.dist_calculate_button.setMinimumSize(QSize(0, 50))
        self.dist_calculate_button.setMaximumSize(QSize(99999, 70))

        self.verticalLayout_4.addWidget(self.dist_calculate_button)


        self.dist_horizontalLayout.addWidget(self.dist_rightMenu)


        self.horizontalLayout_6.addLayout(self.dist_horizontalLayout)

        icon3 = QIcon()
        icon3.addFile(u"733042_orientation_512x512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.load_file_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.chosen_catalog_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.Mag_column_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u043c\u0430\u0433\u043d\u0438\u0442\u0443\u0434", None))
        self.Mag_column_lineedit.setText(QCoreApplication.translate("MainWindow", u"ML", None))
        self.available_sheets_label.setText("")
        self.chosen_sheet_status.setText("")
        self.show_graph_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0438\u0441\u0443\u043d\u043e\u043a", None))
        self.show_mc_on_graph_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043d\u0430 \u0440\u0438\u0441\u0443\u043d\u043a\u0435 \u043f\u043e\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u0435 Mc", None))
        self.calculate_all_methods_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u0441\u0435\u043c\u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c\u0438", None))
        self.calculate_maxc_button.setText(QCoreApplication.translate("MainWindow", u"MAXC", None))
        self.calculate_maxc_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calculate_gft_button.setText(QCoreApplication.translate("MainWindow", u"GFT", None))
        self.calculate_gft_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calculate_lls_button.setText(QCoreApplication.translate("MainWindow", u"LLS", None))
        self.calculate_lls_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calculate_emr_button.setText(QCoreApplication.translate("MainWindow", u"EMR", None))
        self.calculate_emr_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043c\u0430\u0433\u043d\u0438\u0442\u0443\u0434\u0430", None))
        self.orth_load_file_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.orth_chosen_catalog_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.orth_catalog_size_label.setText("")
        self.t_criterion_label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 t-\u043a\u0440\u0438\u0442\u0435\u0440\u0438\u044f \u0421\u0442\u044c\u044e\u0434\u0435\u043d\u0442\u0430", None))
        self.t_criterion_value_lineedit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.orth_calculate_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.orth_plot_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0438\u0441\u0443\u043d\u043e\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0442\u043e\u0440\u0435\u0433\u0440\u0435\u0441\u0441\u0438\u044f", None))
        self.dist_load_file_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0441 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f\u043c\u0438", None))
        self.dist_chosen_catalog_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.dist_catalog_size_label.setText("")
        self.dist_calculate_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \u0444\u0430\u0439\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
    # retranslateUi

