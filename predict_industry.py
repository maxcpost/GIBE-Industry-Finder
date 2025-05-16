#!/usr/bin/env python3

# ── 0.  Keep Orange from touching Qt / GUI layers ────────────────────────────
import os
os.environ["ORANGE_NO_GUI"] = "1"           # also set in the launcher for safety

# ── 1.  Standard imports ─────────────────────────────────────────────────────
import sys
import pickle
from pathlib import Path
from Orange.data import Domain, Table
from orangecontrib.text.corpus import Corpus

# ── 2.  Configuration ────────────────────────────────────────────────────────
MODEL_FILE = "orange-model.pkcls"
RESUME_DIR = "resume"

# ── 3.  Load the trained Orange model ────────────────────────────────────────
try:
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    sys.exit(f"❌  Model file {MODEL_FILE} not found in {Path.cwd()}")

# ── 4.  Helper functions ──────────────────────────────────────────────────────
def process_resume(resume_path):
    """Process a single resume file and print predictions"""
    if not resume_path.is_file():
        print(f"❌  Résumé file {resume_path} not found")
        return
    
    resume_txt = resume_path.read_text(encoding="utf8")
    
    # Re‑use the *exact* StringVariable stored as the first meta variable
    try:
        text_var = model.domain.metas[0]
    except IndexError:
        sys.exit("❌  The loaded model does not contain a text meta variable")
    
    input_domain = Domain([], metas=[text_var])          # StringVariable must be meta
    data = Table.from_list(input_domain, [[resume_txt]])
    # Convert to Corpus for text preprocessing
    data = Corpus.from_table(input_domain, data)
    
    # Predict label and probabilities
    pred_idx = model(data)[0]                            # numeric class index
    pred_label = model.domain.class_var.values[int(pred_idx)]
    probs = model(data, model.Probs)[0]                  # probability vector
    
    # Pretty output
    print(f"\n================ {resume_path.name} → Industry ================")
    print(f"Recommended industry:  {pred_label}")
    print("Class probabilities:")
    for lbl, p in zip(model.domain.class_var.values, probs):
        print(f"  {lbl:<22s} {p:6.2%}")
    print("====================================================\n")

# ── 5.  Main script flow ──────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python predict_industry.py resume.txt OR python predict_industry.py -all")
    
    # Check if we should process all resumes
    if sys.argv[1] == "-all":
        resume_dir = Path(RESUME_DIR)
        if not resume_dir.is_dir():
            sys.exit(f"❌  Resume directory {RESUME_DIR} not found")
        
        resume_files = list(resume_dir.glob("*.txt"))
        if not resume_files:
            sys.exit(f"❌  No resume files (*.txt) found in {RESUME_DIR} directory")
        
        print(f"Processing {len(resume_files)} resumes from {RESUME_DIR}/ directory...")
        for resume_path in resume_files:
            process_resume(resume_path)
    else:
        # Process a single resume
        resume_path = Path(sys.argv[1])
        process_resume(resume_path)
