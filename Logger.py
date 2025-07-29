from datetime import datetime

class Logger:
    def __init__(self, file="log.txt"):
        self.file = file

    def log(self, txt, append=True):
        now = datetime.now().strftime("[%Y-%m-%d %H:%M] ")
        mode = "a" if append else "w"
        with open(self.file, mode, encoding="utf-8") as log:
            log.write(now + txt + "\n")

    def get_logs(self, num_lines=10):
        try:
            with open(self.file, "r", encoding="utf-8") as log:
                lines = log.readlines()
                return [line.strip() for line in lines[-num_lines:]]
        except FileNotFoundError:
            return ["Log file not found."]
