# Machine Learning, Step by Step

Beginner-friendly Jupyter notebooks that explain **how each machine learning algorithm really works**, then finish by turning the trained model into a **web app with [Gradio](https://www.gradio.app)** in a few lines of code.

Every notebook follows the same path: intuition, maths, a from-scratch version, scikit-learn, evaluation, saving the model, and a UI.

## Algorithms

| # | Algorithm | Notebook | Open in Colab |
|---|-----------|----------|---------------|
| 1 | Decision Tree Classifier | [Decision-Tree-Classifier](Decision-Tree-Classifier/) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/notjustavibe/Machine-Learning/blob/main/Decision-Tree-Classifier/decision_tree.ipynb) |

More coming soon.

## Repository layout

```
Machine-Learning/
├── README.md
├── requirements.txt
├── _template/                      # blank notebook skeleton for new algorithms
│   └── algorithm_template.ipynb
└── Decision-Tree-Classifier/
    ├── README.md
    ├── decision_tree.ipynb         # the step-by-step tutorial
    ├── app.py                      # standalone Gradio app
    ├── data/                       # datasets (csv + original xlsx)
    └── model/                      # saved model (joblib)
```

## Quick start

```bash
git clone https://github.com/notjustavibe/Machine-Learning.git
cd Machine-Learning
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cd Decision-Tree-Classifier
jupyter notebook decision_tree.ipynb          # follow the tutorial
python app.py                                 # or just launch the web app
```

## Adding a new algorithm

1. Create a folder named `Algorithm-Name/` with `data/`, `model/`, `app.py` and a `README.md`.
2. Copy `_template/algorithm_template.ipynb` into it and fill in each step.
3. Add a row to the table above.

## About

Created by **Muhammad Qasim Ashfaq** at *Qasim's Academy*. Issues and suggestions are welcome.
