UI Feedback Analysis (Dockerized Flask API)

This project is a Flask-based API that analyzes user feedback on UI and categorizes it as useful or generic. It is fully containerized with Docker to ensure portability and easy integration into other projects like Apomind.

🚀 Features

📌 Flask API to collect and analyze UI feedback

🔥 Dockerized backend for easy deployment

🧠 Basic NLP filtering to detect performance/design issues

🛠️ Future Integration: This backend will be incorporated into Apomind

🛠️ Setup & Run

1️⃣ Build & Run the Docker Container

git clone https://github.com/your-username/ui-feedback-analysis.git
cd ui-feedback-analysis
docker build -t ui-feedback-api .
docker run -p 5000:5000 ui-feedback-api

2️⃣ Test API with curl

Submit UI Feedback

curl -X POST http://localhost:5000/submit-feedback \
     -H "Content-Type: application/json" \
     -d '{"feedback": "The UI is slow"}'

📌 Expected Output:

{"message":"UI performance issue detected.","useful":true}

Test with Generic Feedback

curl -X POST http://localhost:5000/submit-feedback \
     -H "Content-Type: application/json" \
     -d '{"feedback": "It is good"}'

📌 Expected Output:

{"message":"Thank you for your feedback!","useful":true}

🖼️ Screenshots

(Add API response screenshots here)

🚀 Why Docker?

This backend is containerized with Docker to make it easily reusable across multiple projects.

✅ Portability: Works the same on any system.
✅ Scalability: Can be deployed independently or as part of Apomind.
✅ Integration-Ready: This will be used in other Apomind projects for deeper analysis.
