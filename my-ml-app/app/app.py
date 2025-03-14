from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to analyze feedback
def analyze_feedback(feedback):
    generic_words = {"good", "fine", "ok", "nice", "decent"}
    feedback_words = set(feedback.lower().split())

    if feedback_words.issubset(generic_words):
        return {"message": "Generic feedback ignored.", "useful": False}
    
    if "slow" in feedback or "lag" in feedback:
        return {"message": "UI performance issue detected.", "useful": True}
    if "confusing" in feedback or "complex" in feedback:
        return {"message": "UI design improvement needed.", "useful": True}
    
    return {"message": "Thank you for your feedback!", "useful": True}

@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    data = request.json
    feedback = data.get("feedback", "").strip()

    if not feedback:
        return jsonify({"error": "No feedback provided"}), 400

    analysis = analyze_feedback(feedback)
    return jsonify(analysis)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


