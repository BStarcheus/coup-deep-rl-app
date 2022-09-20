from components import *

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()

        self.lbl = QLabel('New Game', self)
        self.layout.addRow(self.lbl)
        self.layout.setAlignment(self.lbl, Qt.AlignmentFlag.AlignCenter)

        self.create_new_checkbox = QCheckBox('Create New Opponent Agent')
        self.create_new_checkbox.stateChanged.connect(self.create_new_changed)
        self.layout.addRow(self.create_new_checkbox)
        self.layout.setAlignment(self.create_new_checkbox, Qt.AlignmentFlag.AlignCenter)

        # Pages for whether creating new or not
        self.agent_info_stack = QStackedWidget()

        # Select existing RL agent opponent
        stack_page_1 = QWidget()
        sub = QVBoxLayout()
        self.select_btn = QPushButton('Select Existing File', self)
        self.select_btn.clicked.connect(self.select_agent)
        sub.addWidget(self.select_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        stack_page_1.setLayout(sub)
        self.agent_info_stack.addWidget(stack_page_1)

        # Form data for a new agent. Display if checkbox above is checked
        stack_page_2 = QWidget()
        sub = QVBoxLayout()

        sub2 = QHBoxLayout()
        sub2.addWidget(QLabel('Learning Rate:'))
        self.lr = QDoubleSpinBox()
        self.lr.setDecimals(3)
        self.lr.setRange(0.001, 1)
        self.lr.setSingleStep(0.001)
        self.lr.setValue(0.5)
        sub2.addWidget(self.lr)
        sub.addLayout(sub2)

        sub2 = QHBoxLayout()
        sub2.addWidget(QLabel('Discount Factor:'))
        self.df = QDoubleSpinBox()
        self.df.setDecimals(3)
        self.df.setRange(0, 1)
        self.df.setSingleStep(0.001)
        self.df.setValue(0.5)
        sub2.addWidget(self.df)
        sub.addLayout(sub2)

        sub2 = QHBoxLayout()
        sub2.addWidget(QLabel('Epsilon (% Exploration):'))
        self.eps = QDoubleSpinBox()
        self.eps.setDecimals(3)
        self.eps.setRange(0, 1)
        self.eps.setSingleStep(0.001)
        self.eps.setValue(0.5)
        sub2.addWidget(self.eps)
        sub.addLayout(sub2)

        # Name a new file
        self.create_btn = QPushButton('Select New File Location', self)
        self.create_btn.clicked.connect(self.create_agent)
        sub.addWidget(self.create_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        stack_page_2.setLayout(sub)
        self.agent_info_stack.addWidget(stack_page_2)

        self.layout.addRow(self.agent_info_stack)

        # Display selected file name
        self.file_name = QLineEdit('', self)
        self.file_name.setReadOnly(True)
        self.file_name.setMinimumWidth(200)
        self.layout.addRow(self.file_name)
        self.layout.setAlignment(self.file_name, Qt.AlignmentFlag.AlignCenter)

        self.train_checkbox = QCheckBox('Train the agent')
        self.layout.addRow(self.train_checkbox)
        self.layout.setAlignment(self.train_checkbox, Qt.AlignmentFlag.AlignCenter)
        
        self.first_turn_checkbox = QCheckBox('Opponent goes first')
        self.layout.addRow(self.first_turn_checkbox)
        self.layout.setAlignment(self.first_turn_checkbox, Qt.AlignmentFlag.AlignCenter)

        self.start_btn = QPushButton('Start', self)
        self.start_btn.setEnabled(False)
        self.layout.addRow(self.start_btn)
        self.layout.setAlignment(self.start_btn, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)

    def get_form_data(self):
        c = self.create_new_checkbox.isChecked()
        return (
            self.first_turn_checkbox.isChecked(),
            self.file_name.text(),
            self.train_checkbox.isChecked(),
            self.lr.value() if c else None,
            self.df.value() if c else None,
            self.eps.value() if c else None
        )

    def create_new_changed(self):
        ind = int(self.create_new_checkbox.isChecked())
        self.file_name.setText('')
        self.start_btn.setEnabled(False)
        self.agent_info_stack.setCurrentIndex(ind)

    def select_agent(self):
        dialog = QFileDialog(self)
        self.agent_file(dialog)

    def create_agent(self):
        dialog = QFileDialog(self)
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        self.agent_file(dialog)

    def agent_file(self, dialog):
        dialog.setNameFilter('*.npz')
        if dialog.exec():
            self.file_name.setText(dialog.selectedFiles()[0])
            self.start_btn.setEnabled(True)
        else:
            if not len(self.file_name.text()):
                self.start_btn.setEnabled(False)
