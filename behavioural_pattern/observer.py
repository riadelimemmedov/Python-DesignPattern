from abc import ABC, abstractmethod


"""
    An Observer Pattern says that "just define a one-to-one dependency so that when one object changes state, all its dependents are notified and updated automatically". 
    The observer pattern is also known as Dependents or Publish-Subscribe.
"""


#!EventListener
class EventListener(ABC):
    @abstractmethod
    def update(self, event_type: str, file):
        pass


#!EventListener
class EventManager:
    def __init__(self, operations):
        self.operations = operations
        self.listeners = {}
        for op in operations:
            self.listeners[op] = []

    def subscribe(self, event_type: str, listener: EventListener):
        users = self.listeners[event_type]
        users.append(listener)

    def unsubscribe(self, event_type: str, listener: EventListener):
        users = self.listeners[event_type]
        users.remove(listener)

    def notify(self, event_type: str, file):
        users = self.listeners[event_type]
        [u.update(event_type, file) for u in users]


#!Editor
class Editor:
    events = EventManager(['open', 'save'])
    file = None

    def open_file(self, file):
        self.file = file
        print(f"Editor : opening file {file}")
        self.events.notify('open', file)

    def save_file(self):
        print(f"Editor: saving file {self.file}")
        self.events.notify('save', self.file)


#!EmailNotificationListener
class EmailNotificationListener(EventListener):
    def __init__(self, email):
        self.email = email

    def update(self, event_type: str, file):
        print(f"Email to {self.email}: Someone has performed {event_type} operation on the file {file}")


#!LogOpenListener
class LogOpenListener(EventListener):
    def __init__(self, log_file):
        self.log_file = log_file

    def update(self, event_type: str, file):
        print(f"Save to log {self.log_file}: Someone has performed {event_type} operation on the file {file}")


#__name__ == __main__
if __name__ == "__main__":
    editor = Editor()

    email_listener = EmailNotificationListener('test@gmail.com')
    log_listener = LogOpenListener('path/to/log/file.txt')

    editor.events.subscribe('open', log_listener)
    editor.events.subscribe('save', log_listener)
    editor.events.subscribe('save', email_listener)

    editor.open_file('test.txt')
    editor.save_file()
