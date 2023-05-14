import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.bing.com/?setlang=en&cc=ae&cc=AE'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        def update_url(q):
            self.url_bar.setText(q.toString())

        self.browser.urlChanged.connect(update_url)

        def navigate_to_url():
            url = self.url_bar.text()
            self.browser.setUrl(QUrl(url))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(navigate_to_url)
        navbar.addWidget(self.url_bar)

        def navigate_home():
            self.browser.setUrl(QUrl('https://www.bing.com/?setlang=en&cc=ae&cc=AE'))

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(navigate_home)
        navbar.addAction(home_btn)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_T:
            self.browser.page().action(QWebEnginePage.AddTab).trigger()

app = QApplication(sys.argv)
QApplication.setApplicationName("SuperStyleBrowser")
window = MainWindow()
window.show()
app.exec_()
