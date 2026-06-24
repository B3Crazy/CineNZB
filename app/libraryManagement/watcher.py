import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from libraryManagement.importer import import_nzbs
from libraryManagement.scanner import scan_library

class NZBFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        if str(event.src_path).endswith('.nzb'):
            print(f"New NZB file detected: {event.src_path}")
            nzb_list = scan_library()
            import_nzbs(nzb_list)

def start_watcher():
    library_path = os.environ.get('LIBRARY_PATH', '/nzbs')  # Default path if not set
    handler = NZBFileHandler()
    observer = Observer()
    observer.schedule(handler, path=library_path, recursive=True)
    observer.start()
    print(f"Started watching for NZB files in: {library_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()