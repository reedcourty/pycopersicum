import datetime
import threading
import time

class TimerThread(threading.Thread):
        
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
        self.session = args
    
    def run(self):
        while (self.session.remaining_time>datetime.timedelta(seconds=0)):
            self.session.set_remaining_time()
            time.sleep(0.01)

class SessionTimer():
    def __init__(self, session_length):
        self.start_time = None
        self.stop_time = None
        self.suspended = False
        self.remaining_time = datetime.timedelta(seconds=session_length)
        self.session_length = datetime.timedelta(seconds=session_length)
        self.timerthread = TimerThread(args=(self))
    
    def get_remaining_time(self):
        return self.remaining_time
        
    def set_remaining_time(self):
        if not self.suspended:
            self.remaining_time = self.stop_time - datetime.datetime.now()
    
    def start_session(self):
        self.start_time = datetime.datetime.now()
        self.stop_time = self.start_time + self.session_length
        self.timerthread.start()
        
    def stop_session(self):
        self.stop_time = datetime.datetime.now()
        self.remaining_time = datetime.timedelta(seconds=0)

    def suspend_session(self):
        self.suspended = True

    def restart_session(self):
        self.suspended = False
   
if __name__ == "__main__":
    pass
        