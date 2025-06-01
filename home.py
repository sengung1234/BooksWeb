# 1 Import the Flask class from the flask module
from flask import Flask,render_template
# 2 Create an instance of the Flask class
app = Flask(__name__);
# 3 # Define a route for the home page ('/') and associate it with a view function
@app.route('/')
def index():
    """
    View function for the home page.
    It renders and returns the 'index.html' template.
    """
    return render_template('index.html', fname = 'Larry', lname='Smith')

# 4 # Run the app only if this script is executed directly (not imported as a module)
# if __name__ == '__main__':
    """
      Enable debug mode so changes are 
      auto-reloaded and errors are shown in browser
     """
#    app.run(debug=True)
    