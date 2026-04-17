from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    try:
        return float(a) + float(b)
    except (ValueError, TypeError):
        return None

# كود الـ HTML الخاص بالواجهة
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Addition App</title>
</head>
<body>
    <h1>Simple Addition Web App</h1>
    <form method="POST">
        <p>First number: <input type="text" name="num1"></p>
        <p>Second number: <input type="text" name="num2"></p>
        <button type="submit">Add</button>
    </form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        # الحصول على الأرقام من مربعات النص في الواجهة
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        result = add_numbers(num1, num2)
    
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)