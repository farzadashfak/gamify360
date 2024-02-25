from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route('/set_search_term')
def set_search_term():
    search_term = request.args.get('search_term', '')
    with open('search_term.txt', 'w') as f:
        f.write(search_term)
    return redirect("http://localhost:8501")

if __name__ == '__main__':
    app.run(port=5001)
