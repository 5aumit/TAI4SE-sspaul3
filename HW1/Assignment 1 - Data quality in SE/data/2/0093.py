from threading import Thread
from queue import Queue
__all__ = ['ThreadPool', 'season_map', 'Course', 'CSCurriculumKey', 'ISCurriculumKey']

class CSCurriculumKey:
    INTRODUCTORY = 0
    FOUNDATION = 1
    SOFTWARE_AND_SYSTEMS_DEVELOPMENT = 2
    THEORY = 3
    DATA_SCIENCE = 4
    DATABASE_SYSTEMS = 5
    ARTIFICIAL_INTELLIGENCE = 6
    SOFTWARE_ENGINEERING = 7
    MULTIMEDIA = 8
    RESEARCH_COLLOQUIUM = 9
    MASTERS_RESEARCH = 10
    MASTERS_THESIS = 11
    GRADUATE_INTERNSHIP = 12
    AREAS = 13
    RESEARCH_AND_THESIS_OPTIONS = 14


class ISCurriculumKey:
    INTRODUCTORY = 0
    FOUNDATION = 1
    ADVANCED = 2
    MAJOR_ELECTIVES = 3
    CAPSTONE = 4
    # extra cdm elective


season_map = {
    "Fall 2015-2016": "AuE",
    "Winter 2015-2016": "WiE",
    "Spring 2015-2016": "SpE",
    "Summer 10 week 2015-2016": "S0E",
    "Summer I 2015-2016": "S1E",
    "Summer II 2015-2016": "S2E",
    "Fall 2016-2017": "AuO",
    "Winter 2016-2017": "WiO",
    "Spring 2016-2017": "SpO",
    "Summer 10 week 2016-2017": "S0O",
    "Summer I 2016-2017": "S1O",
    "Summer II 2016-2017": "S2O"
}


class Course:
    __slots__ = 'subject', 'num', 'name', 'prerequisites', 'history', 'description', 'priority'

    def __init__(self, subject=None, num=None, name=None):
        self.subject = subject
        self.num = num
        self.name = name
        self.description = None
        self.prerequisites = None
        self.history = None
        self.priority = None

    def __repr__(self):
        return "<Course subject={}, num={}, name={}, prerequisites={}, history={}>"\
            .format(self.subject, self.num, self.name, self.prerequisites, self.history)

    def __str__(self):
        return "({} {})".format(self.subject, self.num)


class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """ Add a task to the queue """
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()