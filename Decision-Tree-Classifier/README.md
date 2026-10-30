# Decision Tree Classifier

Predict whether to play tennis from the weather, and learn exactly how a decision tree picks its questions.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/notjustavibe/Machine-Learning/blob/main/Decision-Tree-Classifier/decision_tree.ipynb)

## What you will learn

- Entropy, Gini impurity and information gain, computed by hand
- The ID3 algorithm built from scratch in about 15 lines
- Preprocessing categorical data with a scikit-learn `Pipeline` (one-hot encoding)
- Why a single test score on tiny data is unreliable, and how cross-validation and a baseline help
- Overfitting and `max_depth`
- Visualizing the tree, saving the model with `joblib`, and building a Gradio UI

## Files

| File | Purpose |
|------|---------|
| `decision_tree.ipynb` | The step-by-step tutorial |
| `app.py` | Standalone Gradio app (`python app.py`) |
| `data/decisiontree.csv` | The 14-row "play tennis" dataset (read by the notebook) |
| `data/decisiontree.xlsx` | The same data in its original Excel form |
| `model/decision_tree_model.joblib` | Saved pipeline (encoder + tree), created by the notebook |

## Run it

```bash
pip install -r ../requirements.txt
jupyter notebook decision_tree.ipynb
python app.py        # opens http://127.0.0.1:7860
```

> The saved model must be loaded with the same scikit-learn version that created it. If `app.py` complains, just re-run the notebook to regenerate `model/decision_tree_model.joblib`. Only load model files you trust.

## Deploy for free on Hugging Face Spaces

Create a new Gradio Space and upload `app.py`, the `model/` folder and a `requirements.txt` containing `scikit-learn`, `pandas`, `joblib` and `gradio`.
