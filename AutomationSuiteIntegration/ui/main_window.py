from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QScrollArea, QTextEdit
)

from backend.runner import CommandRunner
from ui.components import create_button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automation Suite")
        self.setGeometry(100, 100, 1400, 800)

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()

        # LEFT: BUTTON PANEL
        left_panel = self.create_button_panel()

        # RIGHT: TERMINAL PANEL
        right_panel = self.create_terminal_panel()

        main_layout.addWidget(left_panel, 2)
        main_layout.addWidget(right_panel, 3)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ================= BUTTON PANEL =================

    def create_button_panel(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        self.layout = QVBoxLayout()

        self.layout.setSpacing(8)
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.layout.addWidget(QLabel("🚀 Automation Suite Dashboard"))

        # Initialize runner AFTER terminal created
        # (will assign later)
        self.container = container
        container.setLayout(self.layout)
        scroll.setWidget(container)

        return scroll

    # ================= TERMINAL PANEL =================

    def create_terminal_panel(self):
        layout = QVBoxLayout()

        label = QLabel("🖥️ Terminal Output")

        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)

        # Terminal styling
        self.terminal.setStyleSheet("""
            QTextEdit {
                background-color: #0d1117;
                color: #00ff9c;
                font-family: Consolas;
                font-size: 13px;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        layout.addWidget(label)
        layout.addWidget(self.terminal)

        container = QWidget()
        container.setLayout(layout)

        # Initialize runner here
        self.runner = CommandRunner(self.terminal)

        # NOW add buttons after runner exists
        self.populate_buttons()

        return container

    # ================= BUTTONS =================

    def populate_buttons(self):
        add = self.layout.addWidget

        add(create_button(
            "Bulk Email Sender",
            lambda: self.runner.run(
                "python send_emails.py",
                r"D:\AutomationScripting\bulk_email_sender"
            )
        ))

        add(create_button(
            "Email Scheduler",
            lambda: self.runner.run(
                "python automated_email_schedule.py",
                r"D:\AutomationScripting\bulk_email_sender"
            )
        ))

        add(create_button(
            "NetPulse Speedometer",
            lambda: self.runner.run(
                "streamlit run app.py",
                r"D:\AutomationScripting\netpulse_speedometer"
            )
        ))

        add(create_button(
            "Stock Notifier",
            lambda: self.runner.run(
                "streamlit run app.py",
                r"D:\AutomationScripting\stock_notifier"
            )
        ))

        add(create_button(
            "SMS Automation",
            lambda: self.runner.run(
                "python app.py",
                r"D:\AutomationScripting\sms_automation"
            )
        ))

        add(create_button(
            "WhatsApp Automation",
            lambda: self.runner.run(
                "python bulk_message.py",
                r"D:\AutomationScripting\whatsapp_automation"
            )
        ))

        

        add(create_button(
            "System Resource Monitor",
            lambda: self.runner.run(
                "streamlit run app.py",
                r"D:\AutomationScripting\system_resource_monitor"
            )
        ))

        add(create_button(
            "File System Automation",
            lambda: self.runner.run(
                "python gui_app.py",
                r"D:\AutomationScripting\file-system-automation"
            )
        ))

        

        

        self.layout.addStretch()