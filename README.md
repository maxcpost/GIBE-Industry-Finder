# GIBE-Industry-Finder

A machine learning tool that analyzes resumes and predicts the most suitable industry for a candidate based on their resume content.

## Overview

This tool uses the Orange data mining framework with text processing capabilities to analyze resume text and predict which industry would be the best fit. It provides both the top industry recommendation and a probability distribution across all possible industries.

## Features

- Process a single resume or batch process multiple resumes
- Display predicted industry with confidence scores
- Simple command-line interface
- Easy setup with automated environment configuration

## Requirements

- Python 3.x
- Mac OS with Homebrew (for automatic installation) or manual Python installation
- Disk space for dependencies

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/resume-industry-predictor.git
   cd resume-industry-predictor
   ```

2. Run the setup script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

The setup script will:
- Ensure Python 3 is installed (using Homebrew if needed)
- Create a virtual environment (`orange_env`)
- Install all necessary dependencies
- Set up a convenient command-line tool

## Usage

### Activate the environment

```bash
source orange_env/bin/activate
```

### Process a single resume

```bash
resume2industry path/to/resume.txt
```

### Process all resumes in the default directory

```bash
resume2industry -all
```

This will process all `.txt` files in the `resume/` directory.

## Output Example

```
================ resume.txt → Industry ================
Recommended industry:  Technology
Class probabilities:
  Technology             75.25%
  Healthcare             12.10%
  Finance                 6.45%
  Education               4.12%
  Manufacturing           2.08%
====================================================
```

## Project Structure

- `predict_industry.py`: Main script for processing resumes and making predictions
- `setup.sh`: Environment setup script
- `orange-model.pkcls`: Pre-trained classification model (must be provided separately)
- `resume/`: Default directory for batch processing resumes

## How It Works

The tool uses a pre-trained Orange text classification model that has been trained on resume data. The model:

1. Processes the input resume text
2. Converts text to features using NLP techniques
3. Applies the classification model to predict the most suitable industry
4. Calculates confidence scores for each possible industry class

## Model Training

This repository includes only the prediction scripts. The model file (`orange-model.pkcls`) needs to be generated separately through the Orange Canvas interface or using Orange's Python API with a labeled dataset of resumes.

## License

[Add your preferred license here]
