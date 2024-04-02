import sys
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/dell/Downloads"

class FileMovementHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"{event.src_path} has been created")
    
    def on_deleted(self, event):
        print(f"{event.src_path} has been deleted")
    
    def on_modified(self, event):
        print(f"{event.src_path} has been modified")
    
    def on_moved(self, event):
        print(f"{event.src_path} has been moved")
        
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()