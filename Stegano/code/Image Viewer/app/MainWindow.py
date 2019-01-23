import os
import re

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QMainWindow, QAction, 
    qApp, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QFileDialog, QLabel)

class MainWindow( QMainWindow ):

    def __init__( self ):
        super( MainWindow, self ).__init__()
        
        self.init_ui()
        
        
    def init_ui( self ):   
        self.ui_menubar()
        self.ui_layout()

        self.setGeometry(200, 100, 900, 600)
        self.setWindowTitle('Orlo - Image Viewer')    
        self.show()            
        

    def ui_menubar( self ):
        exit_act = QAction( '&Quit', self )
        exit_act.setShortcut( 'Ctrl+Q' )
        exit_act.triggered.connect( qApp.quit )

        import_act = QAction( 'I&mport Directory', self )
        import_act.triggered.connect( self.import_dir_clicked )

        about_act = QAction( 'About', self )
        about_act.triggered.connect( qApp.quit )
        
        menubar = self.menuBar()

        file_menu = menubar.addMenu( '&File' )
        file_menu.addAction( import_act )
        file_menu.addAction( exit_act )

        help_menu = menubar.addMenu( '&Help' )
        help_menu.addAction( about_act )


    def ui_layout( self ):
        # Image Display
        img_layout = QHBoxLayout()

        self.img_label = QLabel()
        self.img_label.setFixedSize( QSize(860, 500) )

        img_layout.addStretch( 1 )
        img_layout.addWidget( self.img_label )
        img_layout.addStretch( 1 )

        # Sliding Controls
        control_layout = QHBoxLayout()

        left_btn = QPushButton( "<" )
        left_btn.setFixedSize(QSize(48, 48))
        left_btn.clicked.connect( self.load_prev_img )

        right_btn = QPushButton( ">" )
        right_btn.setFixedSize(QSize(48, 48))
        right_btn.clicked.connect( self.load_next_img )
        
        control_layout.addStretch( 1 )
        control_layout.addWidget( left_btn )
        control_layout.addWidget( right_btn )
        control_layout.addStretch( 1 )

        # Main layout
        prime_VBox = QVBoxLayout()

        prime_VBox.addLayout( img_layout )
        prime_VBox.addLayout( control_layout )

        main_wid = QWidget()
        self.setCentralWidget( main_wid )
        main_wid.setLayout( prime_VBox )


    def import_dir_clicked( self ):
        dir_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        self.img_files = []
        self.curr_img = -1

        for f in os.listdir( dir_path ):
            if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', '.png'):
                self.img_files.append( os.path.join( dir_path, f ) )

        self.load_next_img()


    def load_next_img( self ):
        if self.img_files:
            self.curr_img = (self.curr_img + 1) % len( self.img_files ) 
            curr_img_path = self.img_files[ self.curr_img ]
            self.img_label.setPixmap( QPixmap( curr_img_path ).scaledToWidth( 860 ) )


    def load_prev_img( self ):
        if self.img_files:
            self.curr_img = (self.curr_img - 1) % len( self.img_files ) 
            curr_img_path = self.img_files[ self.curr_img ]
            self.img_label.setPixmap( QPixmap( curr_img_path ).scaledToWidth( 860 ) )

