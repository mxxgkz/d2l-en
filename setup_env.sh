#!/bin/bash
# Setup script for D2L environment
# This creates a conda environment that can both build the book and run code

set -e

echo "=========================================="
echo "D2L Environment Setup"
echo "=========================================="

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Error: conda is not installed."
    echo "Please install Miniconda or Anaconda first:"
    echo "  https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo ""
echo "Step 1: Creating conda environment 'd2l'..."
conda env create -f environment.yml

echo ""
echo "Step 2: Activating environment..."
echo "Note: You'll need to activate this environment manually:"
echo "  conda activate d2l"

echo ""
echo "Step 3: Installing d2l library from source..."
echo "Run this after activating the environment:"
echo "  cd $SCRIPT_DIR"
echo "  pip install -e ."

echo ""
echo "Step 4: Configuring Jupyter for markdown files..."
echo "Run this after activating the environment:"
echo "  jupyter notebook --generate-config"
echo "  echo \"c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'\" >> ~/.jupyter/jupyter_notebook_config.py"

echo ""
echo "=========================================="
echo "Next steps:"
echo "=========================================="
echo "1. Activate the environment:"
echo "   conda activate d2l"
echo ""
echo "2. Install the d2l library:"
echo "   cd $SCRIPT_DIR"
echo "   pip install -e ."
echo ""
echo "3. Install a deep learning framework (choose one):"
echo "   # For PyTorch:"
echo "   pip install torch torchvision"
echo ""
echo "   # For TensorFlow:"
echo "   pip install tensorflow"
echo ""
echo "   # For MXNet:"
echo "   pip install mxnet"
echo ""
echo "   # For JAX:"
echo "   pip install jax jaxlib flax"
echo ""
echo "4. Register environment as Jupyter kernel:"
echo "   python -m ipykernel install --user --name d2l --display-name \"d2l\""
echo ""
echo "5. Configure Jupyter (one-time setup):"
echo "   jupyter notebook --generate-config"
echo "   echo \"c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'\" >> ~/.jupyter/jupyter_notebook_config.py"
echo ""
echo "6. Start Jupyter Notebook:"
echo "   jupyter notebook"
echo ""
echo "7. Or build the HTML book:"
echo "   d2lbook build html"
echo "=========================================="

