from datetime import datetime

class Logger:
    def __init__(self, file="log.txt"):
        self.file = file

    def log(self, txt,level="INFO", append=True):
        now = datetime.now().strftime("[%Y-%m-%d %H:%M] ")
        mode = "a" if append else "w"
        message = f"{now}{level} - {txt}\n"
        with open(self.file, mode, encoding="utf-8") as log:
            log.write(message)

    def get_logs(self, num_lines=10):
        try:
            with open(self.file, "r") as log:
                lines = log.readlines()
                return [line.strip() for line in lines[-num_lines:]]
        except FileNotFoundError:
            return ["Log file not found."]
