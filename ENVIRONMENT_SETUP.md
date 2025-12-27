# Complete Environment Setup Guide

This guide shows you how to create a Python environment that can **both build the book AND run all code examples**.

## 🎯 Quick Start with Conda (Recommended)

### Step 1: Create the Environment

```bash
cd <dir>/d2l-en
conda env create -f environment.yml
```

Or use the automated setup script:
```bash
./setup_env.sh
```

### Step 2: Activate the Environment

```bash
conda activate d2l
```

### Step 3: Install the d2l Library

```bash
pip install -e .
```

This installs the `d2l` package in development mode, so you can edit the source code if needed.

### Step 4: Install a Deep Learning Framework

Choose **one** framework based on your preference:

#### PyTorch (Most Popular)
```bash
pip install torch torchvision
```

#### TensorFlow
```bash
pip install tensorflow==2.12.0 tensorflow-probability==0.20.0
```

#### MXNet
```bash
# CPU version
pip install mxnet==1.9.1

# GPU version (if you have CUDA)
pip install mxnet-cu112==1.9.1
```

#### JAX
```bash
# CPU version
pip install "jax[cpu]==0.4.13" flax==0.7.0

# GPU version (if you have CUDA)
pip install "jax[cuda11_pip]==0.4.13" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html flax==0.7.0
```

### Step 5: Register Environment as Jupyter Kernel

This makes the `d2l` environment available as a kernel in Jupyter Notebook/Lab:

```bash
conda activate d2l
python -m ipykernel install --user --name d2l --display-name "d2l"
```

Now when you create a new notebook, you can select "d2l" as the kernel.

### Step 6: Configure Jupyter (One-time Setup)

```bash
jupyter notebook --generate-config
echo "c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'" >> ~/.jupyter/jupyter_notebook_config.py
```

### Step 7: You're Ready!

Now you can:

**View and run notebooks:**
```bash
jupyter notebook
```
Then open `http://localhost:8888` in your browser.

**Or use JupyterLab:**
```bash
jupyter lab
```

**In Jupyter, select the kernel:**
- When creating a new notebook, click "New" → "d2l"
- For existing notebooks, go to "Kernel" → "Change Kernel" → "d2l"

**Build the HTML book:**
```bash
d2lbook build html
cd _build/html
python3 -m http.server 8000
```

**Build the PDF:**
```bash
d2lbook build pdf
```

---

## Alternative: Python venv

If you prefer Python's built-in virtual environment:

```bash
# Create virtual environment
python3 -m venv d2l-env

# Activate it
source d2l-env/bin/activate  # macOS/Linux
# d2l-env\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Install a deep learning framework (choose one)
pip install torch torchvision  # or tensorflow, mxnet, jax, etc.

# Install d2l library
pip install -e .

# Configure Jupyter
jupyter notebook --generate-config
echo "c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'" >> ~/.jupyter/jupyter_notebook_config.py
```

---

## What's Included in the Environment?

The environment includes:

✅ **Core Dependencies:**
- Jupyter Notebook for interactive coding
- NumPy, Matplotlib, Pandas, SciPy for data science
- Requests for downloading datasets

✅ **Book Building Tools:**
- `d2lbook` - Builds HTML, PDF, and other formats
- `mu-notedown` - Allows Jupyter to read markdown files
- `autopep8` - Code formatting (required by d2lbook)
- `pandoc` - Document converter (required for building HTML/PDF) - **Must be installed separately**

✅ **Deep Learning Framework:**
- You choose: PyTorch, TensorFlow, MXNet, or JAX

✅ **D2L Library:**
- The `d2l` package with helper functions used throughout the book

---

## Daily Usage

Once set up, your daily workflow is:

1. **Activate the environment:**
   ```bash
   conda activate d2l
   ```

2. **Navigate to the book directory:**
   ```bash
   cd <dir>/d2l-en
   ```

3. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

4. **Or build the book:**
   ```bash
   d2lbook build html
   ```

---

## Troubleshooting

### Environment Issues

**If conda command not found:**
- Install Miniconda: https://docs.conda.io/en/latest/miniconda.html
- Or use the Python venv method instead

**If environment creation fails:**
- Make sure you have Python 3.8+ installed
- Try updating conda: `conda update conda`

### Import Errors

**If `import d2l` fails:**
- Make sure you've run `pip install -e .` in the d2l-en directory
- Verify you're in the correct environment: `conda info --envs`

**If framework import fails (torch, tensorflow, etc.):**
- Make sure you've installed at least one framework
- Check installation: `python -c "import torch"` (or your framework)

### Jupyter Issues

**If markdown files don't open:**
- Verify notedown is installed: `pip list | grep notedown`
- Check Jupyter config: `cat ~/.jupyter/jupyter_notebook_config.py | grep notedown`
- Try using `mu-notedown` instead of `notedown`

### Build Issues

**If `d2lbook` command not found:**
- Install it: `pip install d2lbook`
- Make sure you're in the activated environment

**If build is too slow:**
- Edit `config.ini` and set `eval_notebook = False` to skip code evaluation

---

## Updating the Environment

### Update from environment.yml

To update the environment when `environment.yml` changes (adds/removes packages):

```bash
conda activate d2l
conda env update -f environment.yml --prune
```

The `--prune` flag removes packages that are no longer listed in `environment.yml`.

### Update specific packages

**Update conda packages:**
```bash
conda activate d2l
conda update numpy matplotlib pandas scipy  # Update specific packages
conda update --all  # Update all conda packages (use with caution)
```

**Update pip packages:**
```bash
conda activate d2l
pip install --upgrade d2lbook mu-notedown jupyter
pip install --upgrade torch torchvision  # Update your deep learning framework
```

**Update the d2l library (if you've modified the source):**
```bash
conda activate d2l
cd <dir>/d2l-en
pip install -e . --upgrade
```

### Update everything

To update all packages to their latest compatible versions:

```bash
conda activate d2l
conda update --all
pip list --outdated  # Check for outdated pip packages
pip install --upgrade $(pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1)
```

**Note:** Be careful with `conda update --all` as it might update packages to versions that break compatibility with the book's code.

---

## Summary

✅ **One environment** for everything:
- ✅ View and edit notebooks
- ✅ Run all code examples
- ✅ Build HTML book
- ✅ Build PDF book
- ✅ All dependencies isolated

This keeps your system Python clean and makes it easy to manage dependencies!

