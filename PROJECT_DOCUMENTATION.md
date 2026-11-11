# SMS SPAM DETECTION SYSTEM USING MACHINE LEARNING

**Student:** Rhed Gantia  
**Course:** Computer Engineering  
**Project Type:** Applied Machine Learning and Software Development

## 1. Project Overview

The SMS Spam Detection System is a machine learning-based application designed to classify text messages as Spam or Ham (Legitimate). It helps users identify potentially unwanted or suspicious messages through an automated classification process.

The system uses Natural Language Processing and Logistic Regression to analyze SMS messages and generate predictions. A Streamlit web application was developed so users can enter messages and view the classification results.

## 2. Problem Statement

Spam messages are a common problem for mobile phone users. These messages may contain unwanted advertisements, misleading offers, and suspicious links. Some users have difficulty identifying whether a message is legitimate or spam.

This project aims to develop a machine learning-based system that can automatically classify SMS messages and help users recognize potentially unwanted messages.

## 3. Project Objectives

- Develop a machine learning model that classifies SMS messages as Spam or Ham.
- Prepare and clean an SMS dataset for machine learning.
- Train and compare different machine learning algorithms.
- Evaluate the models using accuracy, precision, recall, F1-score, and a confusion matrix.
- Develop a functional web application that uses the trained model to generate actual predictions.

## 4. Dataset Description

**Dataset Name:** SMS Spam Collection  
**Source:** UCI Machine Learning Repository  
**Original loaded records:** 5,572  
**Columns:** 2

The dataset contains SMS messages labeled as either Ham or Spam.

| Column | Description |
|---|---|
| label | Classification of the message |
| message | Actual SMS text |

### Dataset Cleaning

The original loaded dataset contained 5,572 records. During inspection, 403 duplicate records were identified and removed.

| Cleaning information | Result |
|---|---:|
| Original records | 5,572 |
| Duplicate records removed | 403 |
| Remaining records | 5,169 |
| Missing values remaining | 0 |
| Duplicate records remaining | 0 |

### Final Class Distribution

| Category | Number of messages |
|---|---:|
| Ham | 4,516 |
| Spam | 653 |
| Total | 5,169 |

## 5. Machine Learning Methodology

### 5.1 Data Preparation

The dataset was loaded using Pandas. Duplicate messages were removed, and the cleaned dataset was used for model development.

### 5.2 TF-IDF Vectorization

Term Frequency–Inverse Document Frequency (TF-IDF) was used to convert text messages into numerical features that machine learning algorithms could process.

### 5.3 Training and Testing

The dataset was divided into:

- 80% training data
- 20% testing data

Stratified splitting was applied to maintain the class distribution in both sets.

### 5.4 Machine Learning Algorithms

Three models were trained and compared:

1. Dummy Classifier – used as the baseline model.
2. Multinomial Naive Bayes – used for text classification.
3. Logistic Regression – used as an alternative classification algorithm.

## 6. Model Evaluation and Comparison

The models were evaluated using the testing dataset.

| Model | Accuracy |
|---|---:|
| Dummy Classifier | 87.33% |
| Multinomial Naive Bayes | 95.26% |
| Logistic Regression | 96.42% |

Logistic Regression achieved the highest accuracy among the three models.

### Logistic Regression Classification Results

| Metric | Ham | Spam |
|---|---:|---:|
| Precision | 0.96 | 0.96 |
| Recall | 1.00 | 0.75 |
| F1-score | 0.98 | 0.84 |

The confusion matrix showed that:

- 899 legitimate messages were correctly classified.
- 4 legitimate messages were incorrectly classified as spam.
- 98 spam messages were correctly detected.
- 33 spam messages were incorrectly classified as legitimate.

Based on these results, Logistic Regression was selected as the final model because it achieved the highest accuracy and better spam recall than Naive Bayes.

## 7. Software Application Development

The application was developed using Python and Streamlit. The trained Logistic Regression model, including its TF-IDF vectorizer, was saved and integrated into the application.

### Application Features

1. SMS Message Input – Users can enter or paste a text message.
2. Message Classification – The trained model predicts whether the message is Spam or Ham.
3. Prediction Confidence – The application displays the model's predicted class probability.
4. Input Validation – The application displays a warning when the user submits an empty message.

### Technologies Used

- Python
- Google Colab
- Visual Studio Code
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Git and GitHub

## 8. Application Testing and Results

The application was tested using different SMS messages and an empty input.

| Test | Expected Result | Actual Result |
|---|---|---|
| Promotional prize message | Spam | Spam |
| Assignment thank-you message | Ham | Ham |
| Cash reward message | Spam | Spam |
| School meeting message | Ham | Ham |
| Empty message | Warning | Warning displayed |

All five test scenarios produced the expected results.

The application successfully accepted user input, generated predictions through the trained model, displayed prediction confidence, and handled empty input.

## 9. Project Outcome

The project successfully demonstrated the use of machine learning and software development to create an SMS spam detection application.

The Logistic Regression model achieved 96.42% accuracy on the test dataset. The trained model was integrated into a working Streamlit application that can classify messages as Spam or Ham.

The project also demonstrated how text preprocessing, machine learning algorithms, and a software interface can be combined to address a real-world problem.

## 10. Limitations and Future Improvements

Although the application performed well during initial testing, it still has limitations. The Logistic Regression model achieved 75% recall for spam messages, meaning some spam messages were not detected during evaluation.

Future improvements may include:

- Increasing the variety of training messages.
- Improving the detection of spam messages.
- Testing additional machine learning algorithms.
- Improving the application's interface.
- Adding message history and prediction reports.

## 11. Conclusion

The SMS Spam Detection System successfully combined machine learning and software development into a functional web application. Through dataset cleaning, TF-IDF vectorization, model training, and evaluation, Logistic Regression was selected as the final model.

The application demonstrated that machine learning can help identify potentially unwanted SMS messages and provide useful classification results to users.

This project also improved my understanding of data preparation, machine learning, model evaluation, Python programming, and software application development.