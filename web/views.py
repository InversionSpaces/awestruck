from web import app

@app.route("/", methods=["GET", "POST"])
def main():
    return "Hello"
