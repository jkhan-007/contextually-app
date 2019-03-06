from PyQt5.QtCore import QThreadPool


class WorkerPool:
    thread_pool = QThreadPool()

    def schedule(self, worker):
        self.thread_pool.start(worker)

    def shutdown(self):
        self.thread_pool.clear()


pool = WorkerPool()