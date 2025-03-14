import { useState } from "react";

function FeedbackForm() {
  const [feedback, setFeedback] = useState("");
  const [result, setResult] = useState(null);

  const submitFeedback = async () => {
    const response = await fetch("http://127.0.0.1:5000/submit-feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ feedback }),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div>
      <textarea
        value={feedback}
        onChange={(e) => setFeedback(e.target.value)}
        placeholder="Enter your UI feedback..."
      />
      <button onClick={submitFeedback}>Submit</button>

      {result && (
        <div>
          <h3>Analysis Result:</h3>
          <p>{result.message}</p>
        </div>
      )}
    </div>
  );
}

export default FeedbackForm;
