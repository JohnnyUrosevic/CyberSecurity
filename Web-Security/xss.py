from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet_user():
    name = request.args.get('name')

    if name is None:
       greeting = ''
    else:
        greeting = f'<p>Hello {name}!</p>'
    
    html = """
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <form method=GET>
            <label for="name">Enter your name:</label><br>
            <input type="text" id="name" name="name" value="John">
            <input type="submit" value="Submit">
        </form>
        """

    return html + greeting

def clean_input(name):
    """
    Cleans the user input to make sure that no XSS occurs
    """

    # TODO: return the cleaned version of the user input
    return name
