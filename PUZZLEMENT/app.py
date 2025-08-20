from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Question, correct answer, and hint
qa_data = {
    "Which one is the longest ?": {
        "answer": "February",
        "hint": "Consider the words."
    },
    "Scissor has to win.": {
        "answer": "paper rock paper rock scissor",
        "hint": "Consider the rules for simple Rock Paper Scissor game."
    },
    "8 = 3,57 = 201,5 = 11,3 = ?": {
        "answer": "8",
        "hint": "Just mind the symbols."
    },
    "2 + 7 × 7 - 5 = ?": {
        "answer": "46",
        "hint": "Follow the rules of math. DMAS."
    },
    "A + B = 11,B = 5,Á + B + B = ?": {
        "answer": "19",
        "hint": "Carefully see the pictures."
    },
    "Where dose bee honey came from ?": {
        "answer": "bee",
        "hint": "Focus on words only."
    },
    "1 + 5 = 8,7 + 6 = 2,9 + 4 = 3,8 + 4 = ?": {
        "answer": "12",
        "hint": "Ignore above calculations."
    },
    "Get the biggest number possible.": {
        "answer": "999",
        "hint": "Ignore above calculations."
    },
    "My friend is single. He has two brothers, both of whom are married and have at least one child. My friend is the uncle of four children. What is the minimum number of plates that need to be arranged for dinner ?": {
        "answer": "10",
        "hint": "Also count the speaker."
    },
    "Hit this !!": {
        "answer": "this",
        "hint": "Consider words only."
    }
}

# ✅ Missing route added here
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/q2")
def q2():
    return render_template("Q2.html")
@app.route("/q3")
def q3():
    return render_template("Q3.html")
@app.route("/q4")
def q4():
    return render_template("Q4.html")
@app.route("/q5")
def q5():
    return render_template("Q5.html")
@app.route("/q6")
def q6():
    return render_template("Q6.html")
@app.route("/q7")
def q7():
    return render_template("Q7.html")
@app.route("/q8")
def q8():
    return render_template("Q8.html")
@app.route("/q9")
def q9():
    return render_template("Q9.html")
@app.route("/q10")
def q10():
    return render_template("Q10.html")
@app.route("/final")
def final():
    return render_template("final.html")

@app.route('/button-click', methods=['POST'])
def button_click():
    data = request.json
    question = data.get('question')
    answer = data.get('answer')

    if question not in qa_data:
        return jsonify({"correct": False, "hint": "Question not found"})

    correct_answer = qa_data[question]["answer"]

    if answer == correct_answer:
        return jsonify({"correct": True})

    elif answer.strip().lower() == correct_answer.lower():
        return jsonify({"correct": True})

    else:
        return jsonify({"correct": False, "hint": qa_data[question]["hint"]})


if __name__ == '__main__':
    app.run(debug=True)
