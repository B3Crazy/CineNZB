import os

def scan_library():
    library_path = os.environ.get('LIBRARY_PATH', '/nzbs')  # Default path if not set
    nzb_files = []

    for root, dirs, files in os.walk(library_path):
        for file in files:
            if file.endswith('.nzb'):
                rel_path = os.path.relpath(os.path.join(root, file), library_path)
                filename = os.path.splitext(file)[0]  # Remove the .nzb extension
                nzb_files.append({
                    'filename': filename,
                    'path': rel_path
                })
    return nzb_files