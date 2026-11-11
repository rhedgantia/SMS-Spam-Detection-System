
# SMS Spam Detection System

## Project Description
The SMS Spam Detection System is a machine learning-based application that classifies text messages as Spam or Ham (Legitimate).

It uses Natural Language Processing and Machine Learning to analyze SMS messages and provide predictions.

## Objectives
- Identify potentially unwanted SMS messages.
- Train and evaluate machine learning models.
- Develop a working web application for SMS classification.

## Dataset
- **Name:** SMS Spam Collection
- **Source:** UCI Machine Learning Repository
- **Original downloaded records:** 5,572
- **Records after removing duplicates:** 5,169
- **Features:** Message text
- **Target:** Ham or Spam

## Machine Learning Methods
- TF-IDF Vectorization
- Dummy Classifier (Baseline)
- Multinomial Naive Bayes
- Logistic Regression

## Model Evaluation

| Model | Accuracy |
|---|---:|
| Dummy Classifier | 87.33% |
| Naive Bayes | 95.26% |
| Logistic Regression | 96.42% |

Logistic Regression was selected as the final model based on its performance on the test dataset.

## Application Features
1. SMS message input.
2. Spam and legitimate message classification.
3. Prediction confidence display.
4. Empty input validation.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF
- Streamlit
- Git and GitHub

## How to Run the Application

1. Install the required Python libraries.
2. Make sure the trained model is inside the `models` folder.
3. Open the project folder in VS Code.
4. Run:

```bash
python -m streamlit run app.py
```

5. Open the local address displayed in your terminal.

## Disclaimer
The system provides automated predictions and is not a guarantee that a message is safe or harmful.

## Developer
Rhed Gantia

Computer Engineering
