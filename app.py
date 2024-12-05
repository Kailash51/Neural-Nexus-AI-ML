from app.__init__ import create_app
from waitress import serve

# Create the application instance
application = create_app()
# Add this line to make it work with gunicorn
app = application

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
