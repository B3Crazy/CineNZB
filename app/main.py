from flask import Flask, jsonify, render_template, send_file
from libraryManagement.database import Base, engine
from libraryManagement.models import NZB
import os

Base.metadata.create_all(engine)
app = Flask(__name__)

# Route to check the health of the application
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Route to serve the home page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route to list all NZBs in the database
@app.route('/nzbs', methods=['GET'])
def list_nzbs():
    from libraryManagement.queries import get_all

    nzbs = get_all()
    return render_template('nzbs.html', nzbs=nzbs)

# Route to trigger the scanning and importing of NZBs
@app.route('/scan', methods=['GET'])
def scan():
    from libraryManagement.scanner import scan_library
    from libraryManagement.importer import import_nzbs

    nzb_list = scan_library()
    import_nzbs(nzb_list)
    return jsonify({'message': 'Library scanned and NZBs imported successfully.'}), 200

# Route to download a specific NZB file by its path
@app.route('/download/<path:nzb_path>', methods=['GET'])
def download_nzb(nzb_path):

    full_path = os.path.join(os.environ.get('LIBRARY_PATH', '/nzbs'), nzb_path)
    if os.path.exists(full_path):
        return send_file(full_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2160)