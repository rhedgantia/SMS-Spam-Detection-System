
import streamlit as st
import joblib
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="🛡️",
    layout="centered"
)

# Load trained model
MODEL_PATH = Path(__file__).parent / "models" / "sms_spam_model_improved.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

# Application interface
st.title("🛡️ SMS Spam Detection System")

st.write(
    "Enter an SMS message below to check whether "
    "it is Spam or a legitimate message."
)

try:
    model = load_model()

    message = st.text_area(
        "Enter your SMS message:",
        placeholder="Type or paste your message here..."
    )

    if st.button("Check Message", type="primary"):

        if not message.strip():
            st.warning("Please enter a message first.")

        else:
            prediction = model.predict([message])[0]

            probabilities = model.predict_proba([message])[0]
            confidence = max(probabilities) * 100

            st.subheader("Prediction Result")

            if prediction == "spam":
                st.error("🚨 This message is classified as SPAM.")

            else:
                st.success("✅ This message is classified as HAM (Legitimate).")

            st.metric(
                "Model Confidence",
                f"{confidence:.2f}%"
            )

            st.caption(
                "This is an automated prediction, not a guarantee "
                "that a message is safe or harmful."
            )

except FileNotFoundError:
    st.error("Trained model not found. Check your models folder.")

except Exception as e:
    st.error(f"Unable to load or use the model: {e}")
