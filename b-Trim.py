# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  b-Trim 1.0.3                                                                                                                        +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  MIT License                                                                                                                         +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  Copyright (c) 2020 Alexander Mielke (alexandermielke@t-online.de)                                                                   +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  Permission is hereby granted, free of charge, to any person obtaining a copy                                                        +++++++ #
# +++++++  of this software and associated documentation files (the "Software"), to deal                                                       +++++++ #
# +++++++  in the Software without restriction, including without limitation the rights                                                        +++++++ #
# +++++++  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                                                           +++++++ #
# +++++++  copies of the Software, and to permit persons to whom the Software is                                                               +++++++ #
# +++++++  furnished to do so, subject to the following conditions:                                                                            +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  The above copyright notice and this permission notice shall be included in all                                                      +++++++ #
# +++++++  copies or substantial portions of the Software.                                                                                     +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                                                          +++++++ #
# +++++++  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                                                            +++++++ #
# +++++++  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                                                         +++++++ #
# +++++++  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                                                              +++++++ #
# +++++++  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                                                       +++++++ #
# +++++++  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                                                       +++++++ #
# +++++++  SOFTWARE.                                                                                                                           +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  Written in Python 3.8.6 Code                                                                                                        +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++  External Moduls: PyQt5  (https://riverbankcomputing.com/software/pyqt/intro)                                                        +++++++ #
# +++++++                                                                                                                                      +++++++ #
# +++++++                                                                                                                                      +++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
import sys
import math
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Global Variables / Classes ++++++++++++++++++++++++++++++++++++++++++++ #


class Dimensions:
    startx = 10
    starty = 20
    width = 620
    height = 410


class MyDirectories(QtWidgets.QFileSystemModel):

    def headerData(self, section, orientation, role):
        if section == 0 and role == QtCore.Qt.DisplayRole:
            return "Folders"
        else:
            return super(QtWidgets.QFileSystemModel, self).headerData(section, orientation, role)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : Global Methods ++++++++++++++++++++++++++++++++++++++++++++++ #


def darkmode():
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.black)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)


def convert2beauty(number):
    num = str(int(number))
    if len(num) > 3:
        num2 = number/1024
        size = ' MB'
    else:
        num2 = number
        size = ' kB'
    z = str(num2).split('.')
    end = z[1][:2]
    front = z[0]
    front = f'{int(z[0]):,}'
    return front+'.'+end+size


def is_number(eingabe: str):
    number = 0.0
    yes = False
    if type(eingabe) is str:
        if eingabe != '':
            test1 = eingabe.strip()
            if ',' in eingabe:
                test1 = test1.replace(',', '.')
            if 'cm' in test1:
                test1 = test1.replace('cm', '')
            if '"' in test1:
                test1 = test1.replace('"', '')
            test2 = test1.replace('.', '')
            if test2.isdecimal() and test1.count('.') <= 1:
                number = float(test1)
                yes = True
    return yes, number


def is_resolution(eingabe: str):
    width, height = 0, 0
    yes = False
    if type(eingabe) is str:
        if eingabe != '':
            test1 = eingabe.strip()
            test2 = None
            if 'x' in test1:
                test2 = test1.split('x')
            if 'X' in test1:
                test2 = test1.split('X')
            if '*' in test1:
                test2 = test1.split('*')
            if '/' in test1:
                test2 = test1.split('/')
            if ':' in test1:
                test2 = test1.split(':')
            if test2 and len(test2) == 2:
                x = test2[0].strip()
                y = test2[1].strip()
                if x.isdecimal() and y.isdecimal():
                    width = int(x)
                    height = int(y)
                    yes = True
    return yes, width, height

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MainWindows +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class bTrim(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Begin / Variablen +++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.dualx, self.dualy, self. dualspan, self.dualgpx = 0, 0, 0, 0
        self.lastx, self.lasty = 0, 0
        self.startx, self.starty = 0, 0
        self.difx, self.dify = 0, 0
        self.max_width, self.max_height = 0, 0
        self.pixmap = None
        self.new_pic = None
        self.image = ''
        self.dim = Dimensions()
        self.rec = Dimensions()
        self.last_dir = ''
        self.isAdvanced = False
        self.fileIndex = -10
        self.fileList = []
        self.workedList = []


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Begin / Menu ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.setWindowTitle("b-Trim  -  ©2020 Alexander Mielke")
        self.setGeometry(100, 100, 1312, 810)
        self.setMouseTracking(True)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Groupbox: Original ++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.Box_original = QtWidgets.QGroupBox(self)
        self.Box_original.setGeometry(QtCore.QRect(10, 10, 641, 451))
        self.Box_original.setObjectName("Box_original")
        self.original = QtWidgets.QLabel(self.Box_original)
        self.original.setGeometry(QtCore.QRect(10, 30, 621, 411))
        self.original.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.original.setAlignment(QtCore.Qt.AlignCenter)
        self.original.setObjectName("original")
        self.original.setMouseTracking(True)
        self.original.setScaledContents(True)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Groupbox: Wallpaper +++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.Box_wallpaper = QtWidgets.QGroupBox(self)
        self.Box_wallpaper.setGeometry(QtCore.QRect(660, 10, 641, 451))
        self.Box_wallpaper.setObjectName("Box_wallpaper")
        self.wallpaper = QtWidgets.QLabel(self.Box_wallpaper)
        self.wallpaper.setGeometry(QtCore.QRect(10, 30, 621, 411))
        self.wallpaper.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.wallpaper.setAlignment(QtCore.Qt.AlignCenter)
        self.wallpaper.setObjectName("wallpaper")
        self.wallpaper.setScaledContents(True)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Groupbox: Information +++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.Box_info = QtWidgets.QGroupBox(self)
        self.Box_info.setGeometry(QtCore.QRect(660, 470, 641, 291))
        self.Box_info.setObjectName("Box_info")
        self.information = QtWidgets.QTableWidget(self.Box_info)
        self.information.setGeometry(QtCore.QRect(10, 30, 621, 251))
        self.information.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.information.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.information.setTabKeyNavigation(False)
        self.information.setProperty("showDropIndicator", False)
        self.information.setDragDropOverwriteMode(False)
        self.information.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.information.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.information.setGridStyle(QtCore.Qt.NoPen)
        self.information.setObjectName("information")
        self.information.setColumnCount(2)
        self.information.setRowCount(0)
        self.information.verticalHeader().setDefaultSectionSize(9)
        self.information.horizontalHeader().setDefaultSectionSize(200)
        self.information.horizontalHeader().setMinimumSectionSize(200)
        self.information.horizontalHeader().setStretchLastSection(True)
        self.information.horizontalHeader().setVisible(False)
        self.information.verticalHeader().setVisible(False)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Groupbox: Options +++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.Box_options = QtWidgets.QGroupBox(self)
        self.Box_options.setGeometry(QtCore.QRect(10, 470, 641, 291))
        self.Box_options.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Box_options.setObjectName("Box_options")

        self.output_format = QtWidgets.QButtonGroup(self)
        self.output_format.setObjectName("output_format")

        self.radio_fullHD = QtWidgets.QRadioButton(self.Box_options)
        self.radio_fullHD.setGeometry(QtCore.QRect(20, 60, 230, 26))
        self.radio_fullHD.setChecked(True)
        self.radio_fullHD.setAutoExclusive(True)
        self.radio_fullHD.setObjectName("radio_fullHD")
        self.output_format.addButton(self.radio_fullHD)

        self.radio_dual = QtWidgets.QRadioButton(self.Box_options)
        self.radio_dual.setGeometry(QtCore.QRect(20, 90, 330, 26))
        self.radio_dual.setObjectName("radio_dual")
        self.output_format.addButton(self.radio_dual)

        self.radio_custom = QtWidgets.QRadioButton(self.Box_options)
        self.radio_custom.setGeometry(QtCore.QRect(20, 120, 121, 26))
        self.radio_custom.setObjectName("radio_custom")
        self.output_format.addButton(self.radio_custom)

        self.label_output = QtWidgets.QLabel(self.Box_options)
        self.label_output.setGeometry(QtCore.QRect(20, 30, 141, 22))
        self.label_output.setObjectName("label_output")

        self.custom = QtWidgets.QLineEdit(self.Box_options)
        self.custom.setGeometry(QtCore.QRect(145, 120, 101, 32))
        self.custom.setMaxLength(9)
        self.custom.setObjectName("custom")
        self.label_pix = QtWidgets.QLabel(self.Box_options)
        self.label_pix.setGeometry(QtCore.QRect(260, 120, 41, 32))
        self.label_pix.setObjectName("label_pix")

        self.label_mon1 = QtWidgets.QLabel(self.Box_options)
        self.label_mon1.setGeometry(QtCore.QRect(42, 160, 121, 32))
        self.label_mon1.setObjectName("label_mon1")
        self.size_monitors = QtWidgets.QLineEdit(self.Box_options)
        self.size_monitors.setGeometry(QtCore.QRect(167, 160, 61, 32))
        self.size_monitors.setMaxLength(5)
        self.size_monitors.setObjectName("size_monitors")
        self.label_m = QtWidgets.QLabel(self.Box_options)
        self.label_m.setGeometry(QtCore.QRect(237, 160, 61, 32))
        self.label_m.setObjectName("label_m")

        self.label_ar = QtWidgets.QLabel(self.Box_options)
        self.label_ar.setGeometry(QtCore.QRect(42, 240, 121, 31))
        self.label_ar.setObjectName("label_ar")
        self.resolution = QtWidgets.QLineEdit(self.Box_options)
        self.resolution.setGeometry(QtCore.QRect(167, 240, 101, 32))
        self.resolution.setMaxLength(9)
        self.resolution.setObjectName("resolution")
        self.label_pix2 = QtWidgets.QLabel(self.Box_options)
        self.label_pix2.setGeometry(QtCore.QRect(277, 240, 41, 32))
        self.label_pix2.setObjectName("label_pix2")

        self.label_gap = QtWidgets.QLabel(self.Box_options)
        self.label_gap.setGeometry(QtCore.QRect(42, 200, 121, 32))
        self.label_gap.setObjectName("label_gap")
        self.size_gap = QtWidgets.QLineEdit(self.Box_options)
        self.size_gap.setGeometry(QtCore.QRect(167, 200, 61, 32))
        self.size_gap.setMaxLength(4)
        self.size_gap.setObjectName("size_gap")
        self.label_m2 = QtWidgets.QLabel(self.Box_options)
        self.label_m2.setGeometry(QtCore.QRect(237, 200, 61, 32))
        self.label_m2.setObjectName("label_m2")

        self.checkBox_dualMonitor = QtWidgets.QCheckBox(self.Box_options)
        self.checkBox_dualMonitor.setGeometry(QtCore.QRect(290, 120, 121, 31))
        self.checkBox_dualMonitor.setObjectName("checkBox_dualMonitor")

        self.rec_size = QtWidgets.QSlider(self.Box_options)
        self.rec_size.setGeometry(QtCore.QRect(585, 30, 40, 190))
        self.rec_size.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.rec_size.setMinimum(10)
        self.rec_size.setMaximum(100)
        self.rec_size.setProperty("value", 100)
        self.rec_size.setOrientation(QtCore.Qt.Vertical)
        self.rec_size.setInvertedAppearance(False)
        self.rec_size.setInvertedControls(False)
        self.rec_size.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.rec_size.setTickInterval(10)
        self.rec_size.setObjectName("rec_size")
        self.label_recSize = QtWidgets.QLabel(self.Box_options)
        self.label_recSize.setGeometry(QtCore.QRect(480, 20, 100, 41))
        self.label_recSize.setObjectName("label_recSize")
        self.label_instr = QtWidgets.QLabel(self.Box_options)
        self.label_instr.setGeometry(QtCore.QRect(465, 80, 120, 100))
        self.label_instr.setObjectName("label_instr")
        self.label_recSizeValue = QtWidgets.QLabel(self.Box_options)
        self.label_recSizeValue.setGeometry(QtCore.QRect(510, 50, 111, 41))
        self.label_recSizeValue.setObjectName("label_recSizeValue")
        self.Button_refresh = QtWidgets.QPushButton(self.Box_options)
        self.Button_refresh.setGeometry(QtCore.QRect(480, 240, 141, 32))
        self.Button_refresh.setObjectName("Button_refresh")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Advanced +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        self.Box_advanced = QtWidgets.QGroupBox(self)
        self.Box_advanced.setGeometry(QtCore.QRect(10, 10, 490, 751))
        self.Box_advanced.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Box_advanced.setObjectName("Box_advanced")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.files = QtWidgets.QListWidget(self.Box_advanced)
        self.files.setGeometry(QtCore.QRect(10, 240, 470, 420))
        self.files.setObjectName("listview")
        self.files.setFont(font)
        self.files.setStyleSheet("QListView::Item { height: 20px }")
        path = QtCore.QDir.rootPath()
        self.directories = QtWidgets.QTreeView(self.Box_advanced)
        self.directories.setGeometry(QtCore.QRect(10, 30, 470, 200))
        self.directories.setFont(font)
        self.directories.setStyleSheet("QTreeView::Item { height: 18px }")
        self.directories.header().setFont(font)
        self.directories.setObjectName("treeview")
        self.dirModel = MyDirectories()
        self.dirModel.setRootPath(path)
        self.dirModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
        self.directories.setModel(self.dirModel)
        for i in range(1, self.directories.model().columnCount()):
            self.directories.header().hideSection(i)
        self.directories.setRootIndex(self.dirModel.index(path))

        self.saveDir = QtWidgets.QLineEdit(self.Box_advanced)
        self.saveDir.setGeometry(QtCore.QRect(10, 670, 340, 32))
        self.saveDir.setObjectName("saveDir")
        self.saveDir.setEnabled(False)
        self.saveDir.setText('Same as original, or choose new folder →')
        self.Button_openDir = QtWidgets.QPushButton(self.Box_advanced)
        self.Button_openDir.setGeometry(QtCore.QRect(360, 670, 121, 32))
        self.Button_openDir.setObjectName("Button_openDir")

        self.Button_prev = QtWidgets.QPushButton(self.Box_advanced)
        self.Button_prev.setGeometry(QtCore.QRect(10, 710, 90, 32))
        self.Button_prev.setObjectName("Button_prev")
        self.Button_fastSave = QtWidgets.QPushButton(self.Box_advanced)
        self.Button_fastSave.setGeometry(QtCore.QRect(175, 710, 141, 32))
        self.Button_fastSave.setObjectName("Button_fastSave")
        self.Button_next = QtWidgets.QPushButton(self.Box_advanced)
        self.Button_next.setGeometry(QtCore.QRect(390, 710, 90, 32))
        self.Button_next.setObjectName("Button_next")

        self.Box_advanced.setVisible(False)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Buttons +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.Button_advanced = QtWidgets.QPushButton(self)
        self.Button_advanced.setGeometry(QtCore.QRect(10, 770, 141, 32))
        self.Button_advanced.setObjectName("Button_advanced")
        self.Button_open = QtWidgets.QPushButton(self)
        self.Button_open.setGeometry(QtCore.QRect(660, 770, 141, 32))
        self.Button_open.setObjectName("Button_open")
        self.Button_saveWallpaper = QtWidgets.QPushButton(self)
        self.Button_saveWallpaper.setGeometry(QtCore.QRect(810, 770, 141, 32))
        self.Button_saveWallpaper.setObjectName("Button_saveWallpaper")
        self.Button_about = QtWidgets.QPushButton(self)
        self.Button_about.setGeometry(QtCore.QRect(985, 770, 141, 32))
        self.Button_about.setObjectName("Button_about")
        self.Button_quit = QtWidgets.QPushButton(self)
        self.Button_quit.setGeometry(QtCore.QRect(1160, 770, 141, 32))
        self.Button_quit.setObjectName("Button_quit")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Setting Text, etc. ++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        self.Button_openDir.setText("Select Folder")
        self.Button_fastSave.setText("FastSave")
        self.Button_next.setText("Next >")
        self.Button_prev.setText("< Prev")
        self.Box_advanced.setTitle("Files")
        self.Box_original.setTitle("Original")
        self.Box_wallpaper.setTitle("Result")
        self.Box_options.setTitle("Settings")
        self.Box_info.setTitle("Information")
        self.original.setText("")
        self.wallpaper.setText("")
        self.Button_advanced.setText("<< Advanced")
        self.Button_open.setText("Open")
        self.Button_refresh.setText("Refresh")
        self.Button_saveWallpaper.setText("Save as")
        self.Button_about.setText("About")
        self.Button_quit.setText("Quit")
        self.radio_fullHD.setText("FullHD - 16:9 - 1920x1080px")
        self.radio_dual.setText("Dual Monitor - FullHD - 32:9 - 3840x1080px")
        self.radio_custom.setText("Custom size")
        self.label_output.setText("Output format :")

        self.label_mon1.setText("Screen Diagonal")
        self.label_m.setText("cm/inch")
        self.label_m2.setText("cm/inch")
        self.label_pix.setText("px")
        self.label_pix2.setText("px")
        self.label_gap.setText("Screen Gap")
        self.label_ar.setText("Mon. Resolution")
        self.checkBox_dualMonitor.setText("Dual Monitor")
        self.label_recSize.setText("Clipping size")
        self.label_instr.setWordWrap(True)
        self.label_instr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_instr.setText('Click & hold right mouse button to move selection')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Signals & Slots +++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        self.Button_openDir.clicked.connect(self.open_Folder)
        self.Button_quit.clicked.connect(self.close)
        self.Button_saveWallpaper.clicked.connect(self.save_pic)
        self.Button_advanced.clicked.connect(self.set_advanced)
        self.Button_open.clicked.connect(self.open_pic)
        self.Button_refresh.clicked.connect(self.refresh)
        self.Button_about.clicked.connect(self.showAbout)
        self.rec_size.valueChanged.connect(self.show_rectangles)

        self.resolution.textChanged.connect(self.refresh)
        self.size_gap.textChanged.connect(self.refresh)
        self.size_monitors.textChanged.connect(self.refresh)

        self.radio_fullHD.toggled.connect(self.set_fullHD)
        self.radio_dual.toggled.connect(self.set_dual)
        self.radio_custom.toggled.connect(self.set_custom)
        self.checkBox_dualMonitor.stateChanged.connect(self.set_custom)
        self.directories.clicked.connect(self.on_treeviewClicked)
        self.files.clicked.connect(self.on_listviewClicked)
        self.Button_fastSave.clicked.connect(self.FaseSave)
        self.Button_next.clicked.connect(self.set_Next)
        self.Button_prev.clicked.connect(self.set_Prev)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Initialize ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        self.show()
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            if Path(filename).exists():
                self.image = filename
                self.set_image()
                self.set_original()
                self.show_original()
        self.size_monitors.setText('59.7')
        self.size_gap.setText('4.0')
        self.set_fullHD()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : Set Image +++++++++++++++++++++++++++++++++++++++++++++++++++ #
    def set_image(self):
        self.pixmap = QtGui.QPixmap(self.image)
        self.setWindowTitle('b-Trim  -  '+str(Path(self.image).name)+'  -  ©2020 Alexander Mielke')

    def refresh_settings(self):
        self.dualx, self.dualy, self. dualspan, self.dualgpx = 0, 0, 0, 0
        self.lastx, self.lasty = 0, 0
        self.startx, self.starty = 0, 0
        self.difx, self.dify = 0, 0
        self.max_width, self.max_height = 0, 0
        self.pixmap = None
        self.new_pic = None
        self.dim = Dimensions()
        self.rec = Dimensions()
        self.last_dir = ''

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : File Dialogs /About +++++++++++++++++++++++++++++++++++++++++ #

    def set_advanced(self):
        if not self.isAdvanced:
            self.resize(1812, 810)
            self.Box_original.setGeometry(QtCore.QRect(510, 10, 641, 451))
            self.Box_wallpaper.setGeometry(QtCore.QRect(1160, 10, 641, 451))
            self.Box_info.setGeometry(QtCore.QRect(1160, 470, 641, 291))
            self.Box_options.setGeometry(QtCore.QRect(510, 470, 641, 291))
            self.Button_advanced.setGeometry(QtCore.QRect(10, 770, 141, 32))
            self.Button_open.setGeometry(QtCore.QRect(1160, 770, 141, 32))
            self.Button_saveWallpaper.setGeometry(QtCore.QRect(1310, 770, 141, 32))
            self.Button_about.setGeometry(QtCore.QRect(1485, 770, 141, 32))
            self.Button_quit.setGeometry(QtCore.QRect(1660, 770, 141, 32))
            self.isAdvanced = True
            self.Button_advanced.setText("Advanced >>")
            self.Box_advanced.setVisible(True)

        else:
            self.resize(1312, 810)
            self.Box_original.setGeometry(QtCore.QRect(10, 10, 641, 451))
            self.Box_wallpaper.setGeometry(QtCore.QRect(660, 10, 641, 451))
            self.Box_info.setGeometry(QtCore.QRect(660, 470, 641, 291))
            self.Box_options.setGeometry(QtCore.QRect(10, 470, 641, 291))
            self.Button_advanced.setGeometry(QtCore.QRect(10, 770, 141, 32))
            self.Button_open.setGeometry(QtCore.QRect(660, 770, 141, 32))
            self.Button_saveWallpaper.setGeometry(QtCore.QRect(810, 770, 141, 32))
            self.Button_about.setGeometry(QtCore.QRect(985, 770, 141, 32))
            self.Button_quit.setGeometry(QtCore.QRect(1160, 770, 141, 32))
            self.isAdvanced = False
            self.Button_advanced.setText("<< Advanced")
            self.Box_advanced.setVisible(False)

    def on_treeviewClicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        p = Path(path).glob('*.*')
        files = [x for x in p if (x.is_file()) and (x.suffix in ['.jpg', '.png', '.bmp', '.jpeg', '.gif', '.pbm', '.pgm', '.ppm', '.xbm', '.xpm'])]
        self.files.clear()
        self.fileList = []
        for file in files:
            self.fileList.append(str(file))
        self.fileList.sort(key=str.casefold)
        self.refresh_listview()
        self.fileIndex = -10 if len(self.fileList) == 0 else -1

    def on_listviewClicked(self, index):
        self.image = str(self.fileList[index.row()])
        self.refresh_settings()
        self.set_image()
        self.set_original()
        self.show_original()
        self.refresh()
        self.last_dir = str(Path(self.image).parent)
        self.fileIndex = index.row()

    def refresh_listview(self):
        self.files.clear()
        for file in self.fileList:
            if file in self.workedList:
                item = QtWidgets.QListWidgetItem(str(Path(file).name))
                font = QtGui.QFont()
                font.setStyle(QtGui.QFont.StyleItalic)
                font.setBold(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor(52, 203, 60)))
                self.files.addItem(item)
            else:
                self.files.addItem(QtWidgets.QListWidgetItem(str(Path(file).name)))

    def set_Next(self):
        if self.fileIndex >= -1 and self.fileIndex < len(self.fileList)-1:
            self.fileIndex += 1
            self.files.setCurrentRow(self.fileIndex)
            self.image = str(self.fileList[self.fileIndex])
            self.refresh_settings()
            self.set_image()
            self.set_original()
            self.show_original()
            self.refresh()
            self.last_dir = str(Path(self.image).parent)

    def set_Prev(self):
        if self.fileIndex > 0:
            self.fileIndex -= 1
            self.files.setCurrentRow(self.fileIndex)
            self.image = str(self.fileList[self.fileIndex])
            self.refresh_settings()
            self.set_image()
            self.set_original()
            self.show_original()
            self.refresh()
            self.last_dir = str(Path(self.image).parent)

    def showAbout(self):
        about.show()

    def open_Folder(self):
        dir = self.last_dir if self.last_dir != '' else str(Path.cwd())
        foldername = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open FastSave Folder', dir, options=QtWidgets.QFileDialog.ShowDirsOnly)
        fname = str(foldername)
        if fname != '':
            self.saveDir.setText(fname)
            self.last_dir = fname

    def FaseSave(self):
        if self.new_pic:
            foldername = str(Path(self.image).parent) if not Path(self.saveDir.text()).is_dir() else str(Path(self.saveDir.text()))
            foldername += '/'
            filename = str(Path(self.image).name)
            filename = '(cut) '+filename
            savename = foldername+filename
            img_format = str(Path(self.image).suffix).upper()
            img_format = img_format[1:]
            try:
                self.new_pic.save(savename, img_format)
                self.workedList.append(self.image)
                self.refresh_listview()
                self.files.setCurrentRow(self.fileIndex)
            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Error: Could not save file!")
                msg.setText(str(sys.exc_info()))
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                dummie = msg.exec_()

    def open_pic(self):
        dir = self.last_dir if self.last_dir != '' else str(Path.cwd())
        filter = 'Windows Bitmap (*.bmp);;Graphic Interchange Format (*.gif);;Joint Photographic Experts Group (*.jpg);;Joint Photographic Experts Group (*.jpeg);;Portable Network Graphics (*.png);;Portable Bitmap (*.pbm);;Portable Graymap (*.pgm);;Portable Pixmap (*.ppm);;X11 Bitmap (*.xbm);;X11 Bitmap (*.xpm)'
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Imagefile', dir, filter, 'Joint Photographic Experts Group (*.jpg)', options=QtWidgets.QFileDialog.DontUseNativeDialog)
        fname = filename[0]
        if fname != '':
            self.image = fname
            try:
                self.refresh_settings()
                self.set_image()
                self.set_original()
                self.show_original()
                self.refresh()
                self.last_dir = str(Path(self.image).parent)
            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Error: Could not open file!")
                msg.setText(str(sys.exc_info()))
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                dummie = msg.exec_()
                self.image = ''

    def save_pic(self):
        if self.new_pic:
            dir = self.last_dir if self.last_dir != '' else str(Path.cwd())
            filter = 'Windows Bitmap (*.bmp);;Joint Photographic Experts Group (*.jpg);;Joint Photographic Experts Group (*.jpeg);;Portable Network Graphics (*.png);;Portable Pixmap (*.ppm);;X11 Bitmap (*.xbm);;X11 Bitmap (*.xpm)'
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Einkaufszettel speichern...', dir, filter, 'Joint Photographic Experts Group (*.jpg)')
            fname = filename[0]
            if fname:
                if 'bmp' in filename[1]:
                    img_format = 'BMP'
                if 'jpg' in filename[1]:
                    img_format = 'JPG'
                if 'jpeg' in filename[1]:
                    img_format = 'JPEG'
                if 'png' in filename[1]:
                    img_format = 'PNG'
                if 'ppm' in filename[1]:
                    img_format = 'PPM'
                if 'xbm' in filename[1]:
                    img_format = 'XBM'
                if 'xpm' in filename[1]:
                    img_format = 'XPM'
                ending = '.' + img_format.lower()
                dummy = Path(fname)
                if dummy.suffix != ending:
                    fname += ending
                try:
                    self.new_pic.save(fname, img_format)
                    self.last_dir = str(dummy.parent)
                except:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setWindowTitle("Error: Could not save file!")
                    msg.setText(str(sys.exc_info()))
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    dummie = msg.exec_()
                    self.last_dir = ''


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : Mouse Events ++++++++++++++++++++++++++++++++++++++++++++++++ #


    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton and self.image != '':
            leftx = self.dim.startx+510 if self.isAdvanced else self.dim.startx+10
            rightx = self.dim.startx+510+self.dim.width if self.isAdvanced else self.dim.startx+10+self.dim.width
            topy = self.dim.starty+30
            bottomy = self.dim.starty+30+self.dim.height

            if (event.x() in range(leftx, rightx)) and (event.y() in range(topy, bottomy)):
                self.rec.startx = int(self.rec.startx + (event.x()-self.lastx-self.dim.startx*2)*self.difx)
                self.rec.starty = int(self.rec.starty + (event.y()-self.lasty-self.dim.starty*2)*self.dify)
                if self.rec.startx < 0:
                    self.rec.startx = 0
                if self.rec.starty < 0:
                    self.rec.starty = 0
                if self.rec.startx > (self.pixmap.width()-self.rec.width):
                    self.rec.startx = (self.pixmap.width()-self.rec.width)
                if self.rec.starty > (self.pixmap.height()-self.rec.height):
                    self.rec.starty = (self.pixmap.height()-self.rec.height)
                self.show_rectangles()
                self.lastx = event.x()-self.dim.startx*2
                self.lasty = event.y()-self.dim.starty*2

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.lastx = event.x()-self.dim.startx*2
            self.lasty = event.y()-self.dim.starty*2

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : Set Resolution ++++++++++++++++++++++++++++++++++++++++++++++ #

    def refresh(self):
        if self.radio_fullHD.isChecked():
            self.set_fullHD()
        if self.radio_dual.isChecked():
            self.set_dual()
        if self.radio_custom.isChecked():
            self.set_custom()
        self.show_information()

    def set_fullHD(self):
        self.new_pic = None
        self.label_gap.setVisible(False)
        self.label_mon1.setVisible(False)
        self.size_monitors.setVisible(False)
        self.label_ar.setVisible(False)
        self.resolution.setVisible(False)
        self.size_gap.setVisible(False)
        self.custom.setVisible(False)
        self.label_m.setVisible(False)
        self.label_m2.setVisible(False)
        self.label_pix.setVisible(False)
        self.label_pix2.setVisible(False)
        self.checkBox_dualMonitor.setVisible(False)
        self.checkBox_dualMonitor.setChecked(False)
        if self.set_maxSliderValue():
            self.show_rectangles()
        elif self.image != '':
            self.show_original()
        self.show_information()

    def set_dual(self):
        self.new_pic = None
        self.label_gap.setVisible(True)
        self.label_mon1.setVisible(True)
        self.size_monitors.setVisible(True)
        self.size_gap.setVisible(True)
        self.label_ar.setVisible(False)
        self.resolution.setVisible(False)
        self.custom.setVisible(False)
        self.label_m.setVisible(True)
        self.label_m2.setVisible(True)
        self.label_pix.setVisible(False)
        self.label_pix2.setVisible(False)
        self.checkBox_dualMonitor.setVisible(False)
        self.checkBox_dualMonitor.setChecked(False)
        if self.set_maxSliderValue():
            self.show_rectangles()
        elif self.image != '':
            self.show_original()
        self.show_information()

    def set_custom(self):
        self.new_pic = None
        if self.radio_custom.isChecked():
            self.custom.setVisible(True)
            self.label_pix.setVisible(True)
            self.checkBox_dualMonitor.setVisible(True)
            if self.checkBox_dualMonitor.isChecked():
                self.custom.setVisible(False)
                self.label_pix.setVisible(False)
                self.label_mon1.setVisible(True)
                self.label_m.setVisible(True)
                self.label_m2.setVisible(True)
                self.size_monitors.setVisible(True)
                self.label_ar.setVisible(True)
                self.resolution.setVisible(True)
                self.label_gap.setVisible(True)
                self.size_gap.setVisible(True)
                self.label_pix2.setVisible(True)
            else:
                self.custom.setVisible(True)
                self.label_pix.setVisible(True)
                self.label_gap.setVisible(False)
                self.label_m.setVisible(False)
                self.label_m2.setVisible(False)
                self.label_mon1.setVisible(False)
                self.size_monitors.setVisible(False)
                self.label_ar.setVisible(False)
                self.resolution.setVisible(False)
                self.size_gap.setVisible(False)
                self.label_pix2.setVisible(False)
        if self.set_maxSliderValue():
            self.show_rectangles()
        elif self.image != '':
            self.show_original()
        self.show_information()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : Calculations ++++++++++++++++++++++++++++++++++++++++++++++++ #

    def calc_dual(self):
        success = False
        if self.radio_dual.isChecked():
            self.dualx = 1920
            self.dualy = 1080
            check1, d = is_number(self.size_monitors.text())
            check2, gap = is_number(self.size_gap.text())
            if check1 and check2:
                a = d*math.sqrt(1 / (1 + (self.dualy/self.dualx)**2))
                self.dualgpx = int((self.dualx / a)*gap)
                self.dualspan = self.dualx*2 + self.dualgpx
                success = True
        if self.radio_custom.isChecked() and self.checkBox_dualMonitor.isChecked():
            check1, self.dualx, self.dualy = is_resolution(self.resolution.text())
            check2, d = is_number(self.size_monitors.text())
            check3, gap = is_number(self.size_gap.text())
            if check1 and check2 and check3:
                a = d*math.sqrt(1 / (1 + (self.dualy/self.dualx)**2))
                self.dualgpx = int((self.dualx / a)*gap)
                self.dualspan = self.dualx*2 + self.dualgpx
                success = True
                print(self.dualx, self.dualy, self.dualspan, self.dualgpx)
        return success

    def set_max(self):
        success = False
        if self.radio_fullHD.isChecked():
            self.max_width = 1920
            self.max_height = 1080
            success = True
        if self.radio_dual.isChecked() and self.calc_dual():
            self.max_width = self.dualspan
            self.max_height = self.dualy
            success = True
        check, w, h = is_resolution(self.custom.text())
        if self.radio_custom.isChecked() and check:
            self.max_width = w
            self.max_height = h
            success = True
        if self.radio_custom.isChecked() and self.calc_dual():
            self.max_width = self.dualspan
            self.max_height = self.dualy
            success = True
        return success

    def set_maxSliderValue(self):
        self.rec_size.blockSignals(True)
        self.rec_size.setMinimum(0)
        self.rec_size.setMaximum(0)
        self.rec_size.setEnabled(False)
        success = False
        if self.image != '' and self.set_max():
            self.rec_size.setMinimum(10)
            self.rec_size.setEnabled(True)
            pw = self.pixmap.width()
            ph = self.pixmap.height()
            mw = self.max_width
            mh = self.max_height
            vw = pw/mw
            vh = ph/mh
            if (vw == 1.0 and vh == 1.0) or (vw >= 1.0 and vh > 1.0) or (vw > 1.0 and vh >= 1.0):
                self.rec_size.setMaximum(int(vh*100)) if vw >= vh else self.rec_size.setMaximum(int(vw*100))
                self.rec_size.setValue(100)
                success = True
            if (vw < 1.0 and vh < 1.0) or (vw <= 1.0 and vh < 1.0) or (vw < 1.0 and vh <= 1.0):
                self.rec_size.setMaximum(int(vh*100)) if vh < vw else self.rec_size.setMaximum(int(vw*100))
                self.rec_size.setValue(self.rec_size.maximum())
                success = True
            if (vw < 1.0 and vh > 1.0) or (vw < 1.0 and vh > 1.0) or (vw <= 1.0 and vh > 1.0):
                self.rec_size.setMaximum(int(vw*100))
                self.rec_size.setValue(self.rec_size.maximum())
                success = True
            if (vw > 1.0 and vh < 1.0) or (vw > 1.0 and vh <= 1.0) or (vw >= 1.0 and vh < 1.0):
                self.rec_size.setMaximum(int(vh*100))
                self.rec_size.setValue(self.rec_size.maximum())
                success = True
        self.rec_size.blockSignals(False)
        return success

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : Show Images +++++++++++++++++++++++++++++++++++++++++++++++++ #

    def set_original(self):
        if self.image != '':
            self.set_image()
            startx = self.dim.startx
            starty = self.dim.starty
            lw = self.dim.width
            lh = self.dim.height
            ph = self.pixmap.height()
            pw = self.pixmap.width()
            if pw < lw and ph < lh:
                startx = (lw//2 + 10) - (pw//2)
                starty = (lh//2 + 30) - (ph//2)
                lh = ph
                lw = pw
            elif pw > lw and ph < lh:
                new_height = (lw*ph)//pw
                starty = (lh//2 + 30) - (new_height//2)
                lh = new_height
            elif pw < lw and ph > lh:
                new_width = (lh*pw)//ph
                startx = (lw//2 + 10) - (new_width//2)
                lw = new_width
            elif pw > lw and ph > lh:
                if not (pw/lw) == (ph/lh):
                    if (pw/lw) > (ph/lh):
                        v = pw/lw
                        new_height = int(ph/v)
                        starty = (lh//2 + 30) - (new_height//2)
                        lh = new_height
                    else:
                        v = ph/lh
                        new_width = int(pw/v)
                        startx = (lw//2 + 10) - (new_width//2)
                        lw = new_width
            self.dim.startx = startx
            self.dim.starty = starty
            self.dim.width = lw
            self.dim.height = lh
            self.rec.startx = 0
            self.rec.starty = 0
            self.difx = self.pixmap.width()/self.dim.width
            self.dify = self.pixmap.width()/self.dim.width

    def show_original(self):
        self.wallpaper.clear()
        self.original.setGeometry(QtCore.QRect(self.dim.startx, self.dim.starty, self.dim.width, self.dim.height))
        self.original.setPixmap(self.pixmap)

    def show_wallpaper(self):
        self.set_image()
        startx = 10
        starty = 30
        lw = 620
        lh = 410
        if self.radio_fullHD.isChecked():
            self.new_pic = self.pixmap.copy(self.rec.startx, self.rec.starty, self.rec.width, self.rec.height)
            self.new_pic = self.new_pic.scaled(self.max_width, self.max_height, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        elif self.radio_dual.isChecked():
            p = self.rec.width/(self.dualspan)
            width1 = int(p*self.dualx)
            start2 = int(self.rec.startx+width1+p*self.dualgpx)
            pic1 = self.pixmap.copy(self.rec.startx, self.rec.starty, width1, self.rec.height)
            pic2 = self.pixmap.copy(start2, self.rec.starty, width1, self.rec.height)
            pic1 = pic1.scaled(self.dualx, self.dualy, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            pic2 = pic2.scaled(self.dualx, self.dualy, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.new_pic = QtGui.QPixmap(self.dualx*2, self.dualy)
            painter = QtGui.QPainter(self.new_pic)
            painter.drawPixmap(0, 0, pic1, 0, 0, self.dualx, self.dualy)
            painter.drawPixmap(self.dualx, 0, pic2, 0, 0, self.dualx, self.dualy)
            painter.end()
        elif self.radio_custom.isChecked() and not self.checkBox_dualMonitor.isChecked():
            self.new_pic = self.pixmap.copy(self.rec.startx, self.rec.starty, self.rec.width, self.rec.height)
            self.new_pic = self.new_pic.scaled(self.max_width, self.max_height, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        elif self.radio_custom.isChecked() and self.checkBox_dualMonitor.isChecked():
            p = self.rec.width/(self.dualspan)
            width1 = int(p*self.dualx)
            start2 = int(self.rec.startx+width1+p*self.dualgpx)
            pic1 = self.pixmap.copy(self.rec.startx, self.rec.starty, width1, self.rec.height)
            pic2 = self.pixmap.copy(start2, self.rec.starty, width1, self.rec.height)
            pic1 = pic1.scaled(self.dualx, self.dualy, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            pic2 = pic2.scaled(self.dualx, self.dualy, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.new_pic = QtGui.QPixmap(self.dualx*2, self.dualy)
            painter = QtGui.QPainter(self.new_pic)
            painter.drawPixmap(0, 0, pic1, 0, 0, self.dualx, self.dualy)
            painter.drawPixmap(self.dualx, 0, pic2, 0, 0, self.dualx, self.dualy)
            painter.end()
        ph = self.new_pic.height()
        pw = self.new_pic.width()
        if pw < lw and ph < lh:
            pass
        elif pw > lw and ph < lh:
            new_height = (lw*ph)//pw
            starty = int((lh/2 + 30) - (new_height/2))
            lh = new_height
        elif pw < lw and ph > lh:
            new_width = (lh*pw)//ph
            startx = int((lw/2 + 10) - (new_width/2))
            lw = new_width
        elif pw > lw and ph > lh:
            if not (pw/lw) == (ph/lh):
                if (pw/lw) > (ph/lh):
                    v = pw/lw
                    new_height = int(ph/v)
                    starty = int((lh/2 + 30) - (new_height/2))
                    lh = new_height
                else:
                    v = ph/lh
                    new_width = int(pw/v)
                    startx = int((lw/2 + 10) - (new_width/2))
                    lw = new_width
        self.wallpaper.setGeometry(QtCore.QRect(startx, starty, lw, lh))
        self.wallpaper.setPixmap(self.new_pic)
        self.show_information()

    def show_rectangles(self):
        self.set_image()
        self.label_recSizeValue.setText(str(self.rec_size.value())+' %')
        self.painterInstance = QtGui.QPainter(self.pixmap)
        self.penRectangle = QtGui.QPen(QtCore.Qt.darkRed)
        self.penRectangle.setWidth(int(10*(self.pixmap.width()/self.max_width))+2)
        self.painterInstance.setPen(self.penRectangle)
        vfaktor = (self.rec_size.value()/self.rec_size.maximum())
        if self.pixmap.width() >= self.max_width and self.pixmap.height() >= self.max_height:
            self.rec.width = int(self.max_width*self.rec_size.value()/100)
            self.rec.height = int(self.max_height*self.rec_size.value()/100)
        elif self.pixmap.width() > self.max_width and self.pixmap.height() < self.max_height:
            self.rec.width = int((self.pixmap.height()*self.max_width*vfaktor) / self.max_height)
            self.rec.height = int(self.pixmap.height()*vfaktor)
        elif self.pixmap.width() < self.max_width and self.pixmap.height() > self.max_height:
            self.rec.width = int(self.pixmap.width()*vfaktor)
            self.rec.height = int((self.pixmap.width()*self.max_height*vfaktor) / self.max_width)
        elif self.pixmap.width() <= self.max_width and self.pixmap.height() <= self.max_height:
            vx = self.pixmap.width()/self.max_width
            vy = self.pixmap.height()/self.max_height
            if vx == vy:
                self.rec.width = int(self.pixmap.width()*vfaktor)
                self.rec.height = int(self.pixmap.height()*vfaktor)
            if vx < vy:
                self.rec.width = int(self.pixmap.width()*vfaktor)
                self.rec.height = int(self.pixmap.width()*(self.max_height/self.max_width)*vfaktor)
            if vx > vy:
                self.rec.width = int(self.pixmap.height()*vfaktor*(self.max_width/self.max_height))
                self.rec.height = int(self.pixmap.height()*vfaktor)
        if (self.rec.startx+self.rec.width) >= self.pixmap.width():
            b = self.pixmap.width() - self.rec.startx
            a = self.pixmap.width() - b
            c = self.rec.width - b
            self.rec.startx -= c
        if (self.rec.starty+self.rec.height) >= self.pixmap.height():
            b = self.pixmap.height() - self.rec.starty
            a = self.pixmap.height() - b
            c = self.rec.height - b
            self.rec.starty -= c

        if self.radio_fullHD.isChecked():
            self.painterInstance.drawRect(self.rec.startx, self.rec.starty, self.rec.width, self.rec.height)
            self.painterInstance.end()
        elif self.radio_dual.isChecked():
            p = self.rec.width/(self.dualspan)
            width1 = int(p*self.dualx)
            start2 = int(self.rec.startx+width1+p*self.dualgpx)
            self.painterInstance.drawRect(self.rec.startx, self.rec.starty, width1, self.rec.height)
            self.painterInstance.drawRect(start2, self.rec.starty, width1, self.rec.height)
            self.painterInstance.end()
        elif self.radio_custom.isChecked() and not self.checkBox_dualMonitor.isChecked():
            self.painterInstance.drawRect(self.rec.startx, self.rec.starty, self.rec.width, self.rec.height)
            self.painterInstance.end()
        elif self.radio_custom.isChecked() and self.checkBox_dualMonitor.isChecked():
            p = self.rec.width/(self.dualspan)
            width1 = int(p*self.dualx)
            start2 = int(self.rec.startx+width1+p*self.dualgpx)
            self.painterInstance.drawRect(self.rec.startx, self.rec.starty, width1, self.rec.height)
            self.painterInstance.drawRect(start2, self.rec.starty, width1, self.rec.height)
            self.painterInstance.end()

        self.original.setPixmap(self.pixmap)
        self.original.show()
        self.show_wallpaper()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Methods : Show Information +++++++++++++++++++++++++++++++++++++++++++++++++ #

    def get_infoList(self):
        infolist = []

        if self.pixmap:
            infolist.append(['Original File', ''])
            infolist.append(['Filename', str(Path(self.image).name)])
            infolist.append(['Resolution', str(self.pixmap.width())+' x '+str(self.pixmap.height())+' x '+str(self.pixmap.depth())+'bit'])
            infolist.append(['Logical / Physical DPI', str(self.pixmap.logicalDpiX())+'x'+str(self.pixmap.logicalDpiY())+' / '+str(self.pixmap.physicalDpiX())+'x'+str(self.pixmap.physicalDpiY())])
            ram = convert2beauty(self.pixmap.width()*self.pixmap.height()*self.pixmap.depth()/8/1024)
            fmem = convert2beauty(Path(self.image).stat().st_size/1024)
            infolist.append(['Size in memory / file', ram+' / '+fmem])

            check_d = self.checkBox_dualMonitor.isChecked()
            check0, i, j = is_resolution(self.custom.text())
            check1, i, j = is_resolution(self.resolution.text())
            check2, i = is_number(self.size_monitors.text())
            check3, j = is_number(self.size_gap.text())

        if self.new_pic:
            if self.radio_fullHD.isChecked() or (self.radio_custom.isChecked() and check0 and not check_d):
                infolist.append(['Clip', ''])
                scale = self.rec_size.value()
                infolist.append(['Scaling', str(scale)+' %']) if scale > 99 else infolist.append(['Scaling', str(scale)+' %  (Quality loss)'])
                infolist.append(['Resolution', str(self.rec.width)+' x '+str(self.rec.height)+' px'])

            elif (self.radio_dual.isChecked() and check2 and check3) or (self.radio_custom.isChecked() and check_d and check1 and check2 and check3):
                infolist.append(['Clip', ''])
                scale = self.rec_size.value()
                infolist.append(['Scaling', str(scale)+' %']) if scale > 99 else infolist.append(['Scaling', str(scale)+' %  (Quality loss)'])
                width = int((self.rec.width/self.dualspan)*self.dualx)
                infolist.append(['Resolution', ('2 x '+str(width)+' x '+str(self.rec.height)+' px')])
                gap = self.rec.width-2*width
                infolist.append(['Gap', str(gap)+' px'])

        if self.new_pic:
            if self.radio_fullHD.isChecked() or (self.radio_custom.isChecked() and self.custom.text != '' and not self.checkBox_dualMonitor.isChecked()) or self.calc_dual():
                infolist.append(['Wallpaper', ''])
                infolist.append(['Resolution', str(self.new_pic.width())+' x '+str(self.new_pic.height())+' x '+str(self.new_pic.depth())+'bit'])
                infolist.append(['Logical / Physical DPI', str(self.new_pic.logicalDpiX())+'x'+str(self.new_pic.logicalDpiY()) +
                                 ' / '+str(self.new_pic.physicalDpiX())+'x'+str(self.new_pic.physicalDpiY())])
                ram = convert2beauty(self.new_pic.width()*self.new_pic.height()*self.new_pic.depth()/8/1024)
                infolist.append(['Size in memory', ram])

        return infolist

    def show_information(self):
        list = self.get_infoList()
        self.information.setRowCount(0)
        for index, line in enumerate(list):
            self.information.insertRow(index)
            if line[0] != '' and line[1] == '':
                item = QtWidgets.QTableWidgetItem(line[0])
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setUnderline(True)
                font.setItalic(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor(192, 101, 21)))
                self.information.setItem(index, 0, item)
            else:
                self.information.setItem(index, 0, QtWidgets.QTableWidgetItem(line[0]))
                self.information.setItem(index, 1, QtWidgets.QTableWidgetItem(line[1]))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ About Dialog ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class AboutDialog(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        self.setObjectName("AboutDialog")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(570, 458)
        self.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(50, 420, 471, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 10, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: darkRed")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 551, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /></head><body>\n"
                                 "<p style=\" text-align: center;font-size:16px;\"><br />A tool for trimming images to desktop <br /> wallpapers for single or dual monitors.</p>\n"
                                 "<p style=\" text-align: center;font-size:14px;\">Written in Python 3.8.6 <br />with PyQt5 (5.15.1)<br />as only 3rd party module</p>\n"
                                 "<p style=\" text-align: center;font-size:14px;\">Other modules used: sys, math, pathlib</p>\n"
                                 "<p style=\" text-align: center;font-size:14px;\">(c) 2020 Alexander Mielke (<a href=\"mailto:alexandermielke@t-online.de\"><span style=\" text-decoration: underline; color:#2eb8e6;\">alexandermielke@t-online.de</span></a>)</p>\n"
                                 "<p style=\" text-align: center;font-size:14px;\"><a href=\"https://github.com/AlexMielke/bTrim\"><span style=\" text-decoration: underline; color:#2eb8e6;\">GitHub-Repository</span></a></p>\n"
                                 "<p style=\" text-align: center;font-size:12px;\">Licence MIT Licence (see Licence file)</p></body></html>")
        self.setWindowTitle(QtCore.QCoreApplication.translate("self", "About"))
        self.label.setText(QtCore.QCoreApplication.translate("self", "bTrim"))
        self.buttonBox.accepted.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Main ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle('Fusion')
    # darkmode()
    ui = bTrim()
    about = AboutDialog()

    sys.exit(app.exec_())
