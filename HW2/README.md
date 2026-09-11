# Code Clone Embeddings with CodeBERT and t-SNE

This submission samples 10 code snippets as five pairs from the CodeXGLUE
clone-detection benchmark, embeds them with CodeBERT, and visualizes the
embeddings in two dimensions with t-SNE.

## Contents

- `code-embeddings.ipynb` - data sampling, CodeBERT embeddings, and t-SNE plot
- `tsne.png` - generated visualization
- `requirements.txt` - Python dependencies

## Run

Use Python 3 or Google Colab, then install the dependencies and run the
notebook from top to bottom:

```bash
pip install -r requirements.txt
```

The notebook downloads the CodeXGLUE dataset and the `microsoft/codebert-base`
model, so an internet connection is required.

## Observation

All five sampled pairs are labeled as semantic clones in CodeXGLUE. Their
CodeBERT embeddings do not consistently appear close together after the 2D
t-SNE projection: P1 and P3 are relatively close, while P2, P4, and P5 are
more widely separated. This suggests that semantic equivalence is not always
preserved as proximity in this two-dimensional visualization.
