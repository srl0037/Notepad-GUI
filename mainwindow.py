from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QToolBar, QToolButton, QMenu, QComboBox
from PySide6.QtCore import QSize
from textedit import TextEdit
from PySide6.QtGui import QFont, QColor

# from menubar import MenuBar


'''
the plan is to have a toolbar at the top that allows you to do the button
things like copy/paste/undo/redo

then, want to have an area for text editing

then, want to have a status bar at the bottom that updates with the 
widget that is being hovered over? maybe the one that was clicked?
'''

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Notepad")

        self.widget = TextEdit()
        self.setCentralWidget(self.widget)

        # menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # file menu
        file_menu = menu_bar.addMenu("File")

        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.current_text_button)

        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        # edit menu
        edit_menu = menu_bar.addMenu("Edit")

        copy_action = edit_menu.addAction("Copy")
        copy_action.triggered.connect(self.widget.text_edit.copy)

        cut_action = edit_menu.addAction("Cut")
        cut_action.triggered.connect(self.widget.text_edit.cut)

        paste_action = edit_menu.addAction("Paste")
        paste_action.triggered.connect(self.widget.text_edit.paste)

        undo_action = edit_menu.addAction("Undo")
        undo_action.triggered.connect(self.widget.text_edit.undo)

        redo_action = edit_menu.addAction("Redo")
        redo_action.triggered.connect(self.widget.text_edit.redo)

        set_plain_text_action = edit_menu.addAction("Set Plain Text")
        set_plain_text_action.triggered.connect(self.set_plain_text)

        set_plain_text_action = edit_menu.addAction("Set HMTL")
        set_plain_text_action.triggered.connect(self.set_html)

        clear_action = edit_menu.addAction("Clear")
        clear_action.triggered.connect(self.widget.text_edit.clear)

        # view menu
        view_menu = menu_bar.addMenu("View")

        zoom_in_action = view_menu.addAction("Zoom In")
        zoom_in_action.triggered.connect(self.widget.text_edit.zoomIn)

        zoom_out_action = view_menu.addAction("Zoom Out")
        zoom_out_action.triggered.connect(self.widget.text_edit.zoomOut)

        # make a toolbar that has formatting options
        toolbar = QToolBar()
        # toolbar.setMinimumSize(QSize(300,300))
        self.addToolBar(toolbar)

        bold = toolbar.addAction("Bold")
        bold.triggered.connect(self.set_bold)

        italic = toolbar.addAction("Italicize")
        italic.triggered.connect(self.set_italic)

        underline = toolbar.addAction("Underline")
        underline.triggered.connect(self.set_underline)


        # maybe want to make a combo box for all of the fonts
        # let's read some documentation (slay)
        self.combo_box = QComboBox()
        self.combo_box.setPlaceholderText("Font Size")
        self.combo_box.addItem("12 pt", userData=12)
        self.combo_box.addItem("16 pt", userData=16)
        self.combo_box.addItem("20 pt", userData=20)
        self.combo_box.addItem("24 pt", userData=24)
        self.combo_box.addItem("32 pt", userData=32)
        self.combo_box.addItem("48 pt", userData=48)
        self.combo_box.addItem("86 pt", userData=86)
        self.combo_box.addItem("104 pt", userData=104)
        self.combo_box.setCurrentIndex(-1) # this is to see the placehodler text
        self.combo_box.activated.connect(self.on_combo_box_activation)
    
        toolbar.addWidget(self.combo_box)

        # new combo box for fonts
        self.font_box = QComboBox()
        self.font_box.setPlaceholderText("Font Family")
        self.font_box.addItem("Arial", userData="Arial")
        self.font_box.addItem("Times New Roman", userData="Times")
        self.font_box.addItem("Courier", userData="Courier")
        self.font_box.activated.connect(self.on_font_box_activation)

        toolbar.addWidget(self.font_box)

        # another combo box for text color
        self.color_box = QComboBox()
        self.color_box.setPlaceholderText("Text Color")
        self.color_box.addItem("Black", userData=[0,0,0])
        self.color_box.addItem("White", userData=[255,255,255])
        self.color_box.addItem("Red", userData=[255,5,5])
        self.color_box.addItem("Orange", userData=[255,161,5])
        self.color_box.addItem("Yellow", userData=[255,247,5])
        self.color_box.addItem("Green", userData=[0,200,0])
        self.color_box.addItem("Blue", userData=[0,123,240])
        self.color_box.addItem("Purple", userData=[176,0,240])
        self.color_box.addItem("Pink", userData=[240,0,149])
        self.color_box.activated.connect(self.on_color_box_activation)

        toolbar.addWidget(self.color_box)


    # class functions
    def quit_app(self):
        self.app.quit()

    def set_plain_text(self, widget):
        self.widget.text_edit.setPlainText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus id velit leo. Cras non luctus sem, ac fringilla urna. Sed ac erat at mauris feugiat lobortis vitae eu nisi. Pellentesque tempor ipsum sed arcu bibendum, vitae iaculis neque pulvinar. Pellentesque vitae ullamcorper diam. Etiam diam risus, ullamcorper a augue et, porttitor luctus risus. Integer a nunc et metus sollicitudin convallis. Morbi a mauris eget odio dapibus mattis quis vitae lacus. Mauris elementum accumsan justo, sit amet mattis nulla tincidunt eu.")

    def set_html(self, widget):
        self.widget.text_edit.setHtml("<h1>This is basic HTML</h1><p>This is used to show how we can use basic HTML</p><br>This is the last thing I want to write</br>")

    def current_text_button(self, widget):
        print(self.widget.text_edit.toPlainText())

    def set_bold(self, widget):
        is_bold = self.widget.text_edit.fontWeight()
        if is_bold == QFont.Weight.Normal:
            self.widget.text_edit.setFontWeight(QFont.Weight.Bold)
        else:
            self.widget.text_edit.setFontWeight(QFont.Weight.Normal)

    def set_italic(self, widget):
        is_italic = self.widget.text_edit.fontItalic()
        self.widget.text_edit.setFontItalic(not is_italic)

    def set_underline(self, widget):
        is_underline = self.widget.text_edit.fontUnderline()
        self.widget.text_edit.setFontUnderline(not is_underline)

    def on_combo_box_activation(self, index):
        font_size = self.combo_box.itemData(index)
        if font_size:
            self.pt_action(font_size)
        else:
            print("placeholder was not a font size")

    def pt_action(self, size):
        print (f"Action triggered for font size {size} pt")
        font = QFont("Arial", size)
        self.widget.text_edit.setFont(font)

    def on_font_box_activation(self, index):
        font_family = self.font_box.itemText(index) # font_family is then a string

        if font_family:
            # passing in a string
            self.font_action(font_family)
        else:
            print("placeholder was not a font family")

    def font_action(self, family):
        print(f"action triggered for font family {family}")
        font = QFont(family)
        self.widget.text_edit.setFont(font)



    def on_color_box_activation(self, index):
        text_color = self.color_box.itemData(index)

        if text_color:
            self.color_action(text_color)
        else:
            print("placeholder was not a text color")
    
    def color_action(self, color):
        print(f"action triggered for text color{color}")
        color_one = color[0]
        color_two = color[1]
        color_three = color[2]
        self.widget.text_edit.setTextColor(QColor(color_one,color_two,color_three))