import pickle
from sklearn.linear_model import LogisticRegression

# Train a simple model
model = LogisticRegression()
model.fit([[0, 0], [1, 1]], [0, 1])  # Simple binary classification

# Save it
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl created successfully!")
