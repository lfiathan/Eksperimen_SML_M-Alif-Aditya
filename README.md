# MLOps-RedWine-Dashboard

MLOps-RedWine-Dashboard — preprocessing and simple experiments for the UCI/Kaggle Red Wine Quality dataset.

## What this repo contains

- **Dataset:** `winequality-red.csv` (raw)
- **Preprocessing:** `preprocessing/automate_Muhammad-Alif-Aditya.py` and output `preprocessing/winequality_preprocessed.csv`
- **Experiments / notebooks:** `Eksperimen_SML_Nama-siswa/` and `preprocessing/Experimen_Muhammad-Alif-Aditya.ipynb`
- **Dependencies:** `requirements.txt`

## Dataset source

- Original dataset: UCI / Kaggle "Red Wine Quality" (Cortez et al., 2009). The raw CSV is stored at the repository root as `winequality-red.csv`.

## Requirements

- Python 3.12.7
- See `requirements.txt` for exact Python packages.

## Quick setup (recommended: venv)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Conda setup (optional)

If you prefer conda, create an environment in the repo (accept conda TOS if prompted):

```bash
# accept conda TOS if required
conda create --yes --prefix .conda python=3.12
conda activate ./.conda
pip install -r requirements.txt
```

## Preprocessing

Run the preprocessing script from the repository root (it resolves paths reliably):

```bash
python preprocessing/automate_Muhammad-Alif-Aditya.py
```

This will read `winequality-red.csv` and write `preprocessing/winequality_preprocessed.csv`.

## Notebooks & experiments

- Open the notebooks in `Eksperimen_SML_Nama-siswa/` or `preprocessing/` to explore models and visualizations.
- If running notebooks outside the repo root, ensure working directory or input paths are set correctly.

## Troubleshooting

- Matplotlib backend errors in notebooks: unset `MPLBACKEND` or set a backend in code (e.g. `matplotlib.use("Agg")`) before importing `pyplot`.
- `AttributeError: module 'matplotlib' has no attribute 'colors'`: make sure there is no local `matplotlib.py` shadowing the package and reinstall matplotlib:

```bash
find . -name "matplotlib.py" -o -name "matplotlib" -type d
find . -name "*.pyc" -delete
pip install --upgrade --force-reinstall matplotlib
```

## Repository structure

- `winequality-red.csv` — raw dataset
- `preprocessing/` — preprocessing scripts and preprocessed CSV
- `Eksperimen_SML_Nama-siswa/` — experiment notebook templates
- `requirements.txt` — Python dependencies
- `README.md` — this file

## Contributing

- Fork, create a feature branch, and open a pull request. Keep changes small and include a short description of purpose.

## License & Contact

- Add a license and maintainer contact information here (e.g., MIT, your GitHub handle).

---
If you want, I can also add a small `Makefile` or GitHub Actions workflow to run the preprocessing automatically.
