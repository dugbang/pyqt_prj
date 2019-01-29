## pyqt 학습용 프로젝트

* 그냥 여기저기 사이트의 예제를 실행해 볼 목적으로 작성
** tetris 디렉토리; zetcode Tetris 예제 학습용

* [PyQt5 tutorial](http://zetcode.com/gui/pyqt5/)
    1. [사용할 이미지 다운받은 곳](https://github.com/AlexandreCarlos/PyQt_Tutorial/tree/master/image)
        - 전체가 있는 것이 아님.
        - 아이콘을 다운받아 사용할 수 있는 방법을 확인하는 것이 좋겠음.
    1. [Custom widgets in PyQt5](http://zetcode.com/gui/pyqt5/customwidgets/)
        1. t10_customwidget.py
    1. [Painting in PyQt5](http://zetcode.com/gui/pyqt5/painting/)
        1. t09_beziercurve.py
        1. t09_brushes.py
        1. t09_pens.py
        1. t09_colours.py; pen 은 brush 의 라인을 그리는 역활
        1. t09_points.py
        1. t09_drawingtext.py
    1. [Drag and drop in PyQt5](http://zetcode.com/gui/pyqt5/dragdrop/)
        1. t08_dragbutton.py
        1. t08_simpledragdrop.py
    1. [PyQt5 widgets 2](http://zetcode.com/gui/pyqt5/widgets2/)
        1. t07_combobox.py
        1. t07_splitter.py
        1. t07_lineedit.py
        1. t07_pixmap.py
    1. [PyQt5 widgets](http://zetcode.com/gui/pyqt5/widgets/)
        1. t06_calendar.py
        1. t06_progressbar.py
            - timer id 확인하는 부분이 필요.
        1. t06_slider.py
        1. t06_togglebutton.py
            - "redb.clicked[bool].connect(self.setColor)":https://stackoverflow.com/questions/26316879/difference-between-qtgui-qpushbutton-clickedbool-and-qtgui-qpushbutton-clicked
            - 다른 예제에서는 타입에 따라 함수를 구분했는데 답변을 보면 그렇게하지 않아도 될 듯함.
        1. t06_checkbox.py
    1. [Dialogs in PyQt5](http://zetcode.com/gui/pyqt5/dialogs/)
        1. t05_filedialog.py
        1. t05_fontdialog.py
        1. t05_colordialog.py; setStyleSheet 사용
        1. t05_inputdialog.py
    1. [Events and signals in PyQt5](http://zetcode.com/gui/pyqt5/eventssignals/)
        1. t04_customsignal.py
        1. t04_eventsource.py; 이벤트 발생 객체 확인하기
        1. t04_eventobject.py; mouseMoveEvent, self.setMouseTracking(True)
        1. t04_escape.py; keyPressEvent
        1. t04_sigslot.py
    1. [Layout management in PyQt5](http://zetcode.com/gui/pyqt5/layout/)
        1. t03_review.py
        1. t03_calculator.py; QGridLayout, 이전에 경험하지 못한 새로운 코딩 스타일 확인
        1. t03_buttons.py
        1. t03_absolute.py
    1. [Menus and toolbars in PyQt5](http://zetcode.com/gui/pyqt5/menustoolbars/)
        1. t02_mainwindow.py
        1. t02_toolbar.py
        1. t02_contextmenu.py
        1. t02_checkmenu.py
        1. t02_submenu.py
        1. t02_simplemenu.py
        1. t02_statusbar.py
    1. [First programs in PyQt5](http://zetcode.com/gui/pyqt5/firstprograms/)
        1. t01_center.py
        1. t01_messagebox.py
        1. t01_quitbutton.py
        1. t01_tooltip.py
        1. t01_icon.py
        1. t01_simple.py

* [예제로 배우는 PyQt](https://opentutorials.org/module/544)  opentutor
    1. **ui 파일 없이 동작하는 코드**
        1. sample08_LayoutWidget; [다양한 레이아웃 위젯 사용](https://opentutorials.org/module/544/18664)
        1. sample07_QWidgetLayer; [겹쳐진 위젯의 순서 변경](https://opentutorials.org/module/544/18658)
            - 위젯 투명도 설정 부분도 추가
        1. sample06_PaintEvent; [Paint Event 사용](https://opentutorials.org/module/544/18655)
            - update() 함수 호출시 실행되는 함수; paintEvent
        1. sample05; [Signal 과 Slot 사용자정의 슬롯 만들기](https://opentutorials.org/module/544/18979)
            - 현재 버전에서는 pyqtSlot 데코레이터 를 명시하지 않아도 동작함.
            - 이후 있는 Signal 과 Slot 에 대한 예제는 스킵함 _예제의 목적을 이해하지 못함...ㅠ_
        1. sample04; [Signal 과 Slot 사용자정의 시그널 반환 값 타입](https://opentutorials.org/module/544/18978)
            - 시그널의 name 필드를 사용하지 않고 그냥 시그널 선언 자체를 사용할 수 있음
        1. sample03; Signal 과 Slot 사용자정의 시그널 만들기
        1. sample02; Signal 과 Slot 람다 함수를 이용하여 값 처리 및 전달
        1. sample01; Signal 과 slot 연결 기본
    1. tutor02; Qt Designer를 이용하여 폼 제작 후, 시그널 슬롯 연결하기
    1. tutor01; Qt Designer를 이용하여 폼 제작

* [PyQt를 이용한 GUI 프로그래밍](https://wikidocs.net/5218) wikidocs
    1. qt_gui_QDialogCommunicate; [메인 윈도우와 다이얼로그의 상호 작용](https://wikidocs.net/5249)
        - 모달리스 다이얼로그와 사용할 때는 슬롯과 시그널을 이용하여야 할 듯
    1. qt_gui_QInputDialog; [QInputDialog](https://wikidocs.net/5248)
    1. qt_gui_QFileDialog; [QFileDialog](https://wikidocs.net/5247)
    1. qt_gui_QLayoutLayer; [레이아웃 중첩](https://wikidocs.net/5245)
    1. qt_gui_QGridLayout; [QGridLayout](https://wikidocs.net/5244)
    1. qt_gui_QHBoxLayout; [QHBoxLayout](https://wikidocs.net/5243)
    1. qt_gui_QVBoxLayout; [QVBoxLayout](https://wikidocs.net/5242)
    1. qt_gui_QTableWidget; [QTableWidget](https://wikidocs.net/5240)
    1. qt_gui_QSpinBox; [QSpinBox](https://wikidocs.net/5239)
    1. qt_gui_QCheckBox; [QCheckBox](https://wikidocs.net/5238)
    1. qt_gui_QRadioButtonQGroupBox; [QRadioButton과 QGroupBox](https://wikidocs.net/5237)
        - 그룹박스와 라디오 버튼을 매칭시키는 부분을 찾지 못함.
    1. qt_gui_QLineEditQStatusBar; [QLineEdit 와 QStatusBar](https://wikidocs.net/5236)
    1. qt_gui_QLabel; [QLabel](https://wikidocs.net/5231)
    1. qt_gui_QPushButton; [QPushButton](https://wikidocs.net/5230)
    1. qt_gui01; [이벤트 처리하기](https://wikidocs.net/5228)

## 팁정리
* [메인윈도에서 다이얼로그를 사용하는 방법](https://ruriro.tistory.com/10?category=631468)
    1. 모달(modal)로 다이얼로그를 사용하기
        dialog = SaveDialog(self)
        dialog.exec_()
    1. 모덜리스(modeless)로 다이얼로그를 사용하기
        if (not self.search_dialog):
            self.search_dialog = SearchDialog(self)
        self.search_dialog.show()
        self.search_dialog.raise()
        self.search_dialog.activateWindow()

