from PyQt6.QtCore import QProcess
import os


class CommandRunner:
    def __init__(self, output_widget):
        self.process = QProcess()
        self.output_widget = output_widget

        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.on_finished)

    # 🔥 MAIN RUN FUNCTION
    def run(self, command, working_dir=None):
        # ✅ Kill previous process first
        if self.process.state() != QProcess.ProcessState.NotRunning:
            self.output_widget.append("\n🛑 Stopping previous process...\n")
            self.process.kill()
            self.process.waitForFinished(2000)

        self.output_widget.append(f"\n🚀 Running: {command}\n")

        if working_dir:
            self.process.setWorkingDirectory(working_dir)

        # ✅ Environment fixes
        env = self.process.processEnvironment()
        home = os.path.expanduser("~")

        env.insert("HOME", home)
        env.insert("USERPROFILE", home)
        env.insert("PYTHONIOENCODING", "utf-8")

        self.process.setProcessEnvironment(env)

        # ✅ UTF-8 terminal
        full_command = f"chcp 65001 > nul && {command}"

        self.process.start("cmd.exe", ["/c", full_command])

    # ================= HANDLERS =================

    def handle_stdout(self):
        data = bytes(self.process.readAllStandardOutput()).decode("utf-8", errors="ignore")
        self.output_widget.append(data)

    def handle_stderr(self):
        data = bytes(self.process.readAllStandardError()).decode("utf-8", errors="ignore")
        self.output_widget.append(f"<span style='color:red;'>{data}</span>")

    def on_finished(self):
        self.output_widget.append("\n✅ Process Finished\n")