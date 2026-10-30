"""Standalone Gradio app for the Decision Tree Classifier.

Run:  python app.py
"""
from pathlib import Path

import gradio as gr
import joblib
import pandas as pd

HERE = Path(__file__).parent
model = joblib.load(HERE / "model" / "decision_tree_model.joblib")

FEATURES = ["outlook", "temperature", "humidity", "wind"]
CHOICES = {
    "outlook": ["overcast", "rain", "sunny"],
    "temperature": ["cool", "hot", "mild"],
    "humidity": ["high", "normal"],
    "wind": ["strong", "weak"],
}


def predict_play(outlook, temperature, humidity, wind):
    row = pd.DataFrame([{"outlook": outlook, "temperature": temperature, "humidity": humidity, "wind": wind}])
    proba = dict(zip(model.classes_, model.predict_proba(row)[0]))
    return {"Play (yes)": float(proba["yes"]), "Don't play (no)": float(proba["no"])}


demo = gr.Interface(
    fn=predict_play,
    inputs=[gr.Dropdown(CHOICES[f], value=CHOICES[f][0], label=f.capitalize()) for f in FEATURES],
    outputs=gr.Label(num_top_classes=2, label="Prediction"),
    examples=[["sunny", "hot", "high", "weak"], ["overcast", "cool", "normal", "strong"], ["rain", "mild", "high", "strong"]],
    title="Decision Tree Classifier: play tennis?",
    description="Pick the weather conditions and the model predicts whether to play.",
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
