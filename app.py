from flask import Flask, render_template, request, jsonify
from googlesearch import search    # pip install googlesearch-python

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def osint_search():
    data = request.get_json()
    query = data.get('query', '').strip()
    results = []
    if query:
        try:
            # perform Google search
            for url in search(query, num_results=10, lang='ru'):
                results.append(url)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
