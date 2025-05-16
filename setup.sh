#!/usr/bin/env bash
# setup.sh – bootstrap env for résumé‑to‑industry predictor

set -e

# 1. Ensure Python 3 is available (via Homebrew if missing)
if ! command -v python3 >/dev/null 2>&1 ; then
  echo "Installing Python 3 via Homebrew…"
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install python@3.11
fi

# 2. Create and enter virtual‑env
ENV_DIR="orange_env"
python3 -m venv "$ENV_DIR"
source "$ENV_DIR/bin/activate"

# 3. Install run‑time deps
pip install --upgrade pip
pip install orange3 orange3-text PyQt5==5.15.10 scikit-learn==1.5.2  # ← NEW lines

# 4. Tiny launcher
cat <<'EOF' >"$ENV_DIR/bin/resume2industry"
#!/usr/bin/env bash
DIR=$(cd "$(dirname "$0")/.." && pwd)
source "$DIR/orange_env/bin/activate"
export ORANGE_NO_GUI=1                # ← Tell Orange to stay headless
python "$DIR/predict_industry.py" "$@"
EOF
chmod +x "$ENV_DIR/bin/resume2industry"

echo "✔ Environment ready.  Use:  source $ENV_DIR/bin/activate"
echo "✔ Predict with:       resume2industry resume.txt"
