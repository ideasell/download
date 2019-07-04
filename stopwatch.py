from datetime import datetime


class Stopwatch:
    def __init__(self):
        self.start = datetime.now()

    def start(self):
        self.start = datetime.now()

    def stop(self, message=''):
        self.end = datetime.now()
        self.elpsed = self.end - self.start

        elapsed_time = "소요시간 {:0>.6f}".format((self.elpsed.seconds * 1000000 + self.elpsed.microseconds) / 1000000)
        if message == '':
            return "{}".format(elapsed_time)
        else:
            return "{}: {}".format(elapsed_time, message)

    def stopStart(self, message=''):
        self.end = datetime.now()
        self.elpsed = self.end - self.start
        self.start = datetime.now()

        elapsed_time = "소요시간 {:0>.6f}".format((self.elpsed.seconds * 1000000 + self.elpsed.microseconds) / 1000000)
        if message == '':
            return "{}".format(elapsed_time)
        else:
            return "{}, {}".format(message, elapsed_time)


if __name__ == '__main__':
    pass
