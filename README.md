📂 Project – Reply Classification (SvaraAI Internship Assignment)

This project classifies email replies into three categories:

Positive → Interested in meeting/demo

Negative → Not interested / rejection

Neutral → Non-committal or irrelevant

The pipeline includes data preprocessing, model training, fine-tuning DistilBERT, and deployment via Flask API.

🚀 Project Structure
├── reply_classification_dataset              
├── notebook.ipynb        
├── saved_model/         
├── app.py                
├── answers.md            
├── README.md             

🧩 Part A – ML/NLP Pipeline

Preprocessed text (cleaning, lowercasing, removing noise).

Baseline: Logistic Regression.

Fine-tuned: DistilBERT using Hugging Face Transformers.

Evaluation metrics: Accuracy & F1-score.

Best model saved in saved_model/.

🧩 Part B – Deployment

Deployed best model with Flask.

Run locally:

# Install dependencies
pip install -r requirements.txt

# Start API
python app.py


API Endpoint:

URL: http://127.0.0.1:5000/predict

Method: POST

Input (JSON):

{"text": "Looking forward to the demo!"}


Output (JSON):

{"label": "positive", "confidence": 0.87}

🧩 Part C – Reasoning

See answers.md
 for short responses to:

Improving performance with only 200 labeled samples.

Ensuring fairness & safety in production.

Designing prompts for personalized cold email openers.

📦 Requirements

Python 3.8+

Transformers (Hugging Face)

TensorFlow / PyTorch

Flask

scikit-learn

pandas, numpy

Install with:

pip install -r requirements.txt

📽️ Demo Video

A short video explanation is included as per the assignment instructions.
