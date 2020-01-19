import os
from application import app, db


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8080.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

