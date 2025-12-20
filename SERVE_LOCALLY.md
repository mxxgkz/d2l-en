# How to Serve D2L Book Locally

This guide explains how to serve the Dive into Deep Learning book on your local computer.

## 🎯 Recommended: Create a Dedicated Python Environment

**Best for:** Building the book AND running code examples

This creates a complete environment that can both build the book and execute all code examples.

### Option A: Using Conda (Recommended)

1. **Create the environment:**
   ```bash
   cd /Users/karlzhang/Library/CloudStorage/OneDrive-Personal/Other/Live_Courses/BitTiger/Alg_Practice/Ind_Proj/d2l-en
   conda env create -f environment.yml
   ```

2. **Activate the environment:**
   ```bash
   conda activate d2l
   ```

3. **Install the d2l library:**
   ```bash
   pip install -e .
   ```

4. **Install a deep learning framework (choose one):**
   ```bash
   # PyTorch (most common)
   pip install torch torchvision
   
   # Or TensorFlow
   pip install tensorflow
   
   # Or MXNet
   pip install mxnet
   
   # Or JAX
   pip install jax jaxlib flax
   ```

5. **Register environment as Jupyter kernel:**
   ```bash
   python -m ipykernel install --user --name d2l --display-name "d2l"
   ```
   This makes "d2l" available as a kernel in Jupyter Notebook/Lab.

6. **Configure Jupyter (one-time setup):**
   ```bash
   jupyter notebook --generate-config
   echo "c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'" >> ~/.jupyter/jupyter_notebook_config.py
   ```

7. **You're ready! Now you can:**
   - **View and run notebooks:** `jupyter notebook` (select "d2l" kernel)
   - **Use in JupyterLab:** `jupyter lab` (select "d2l" kernel)
   - **Build HTML book:** `d2lbook build html`
   - **Build PDF:** `d2lbook build pdf`

### Option B: Using Python venv

If you prefer Python's built-in virtual environment:

```bash
# Create virtual environment
python3 -m venv d2l-env

# Activate it
source d2l-env/bin/activate  # On macOS/Linux
# or: d2l-env\Scripts\activate  # On Windows

# Install all dependencies
pip install jupyter==1.0.0 numpy==1.23.5 matplotlib==3.7.2 matplotlib-inline==0.1.6 requests==2.31.0 pandas==2.0.3 scipy==1.10.1
pip install mu-notedown d2lbook
pip install torch torchvision  # or your preferred framework
pip install -e .  # Install d2l library

# Configure Jupyter
jupyter notebook --generate-config
echo "c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'" >> ~/.jupyter/jupyter_notebook_config.py
```

---

## Option 1: Jupyter Notebook (Simplest - Recommended)

This allows you to view and run the markdown files as interactive notebooks.

### Prerequisites
1. Python 3.8+ (you have Python 3.10.12 ✓)
2. pip

### Steps

1. **Install required packages:**
   ```bash
   pip install jupyter notedown
   pip install -e .  # Install the d2l library from source
   ```

2. **Configure Jupyter to read markdown files:**
   ```bash
   jupyter notebook --generate-config
   echo "c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'" >> ~/.jupyter/jupyter_notebook_config.py
   ```

3. **Start Jupyter Notebook:**
   ```bash
   cd /Users/karlzhang/Library/CloudStorage/OneDrive-Personal/Other/Live_Courses/BitTiger/Alg_Practice/Ind_Proj/d2l-en
   jupyter notebook
   ```

4. **Access the book:**
   - Your browser should automatically open to `http://localhost:8888`
   - If not, manually open that URL
   - Navigate through the chapter folders to view the markdown files as notebooks

### Note
- You can edit and run code cells directly in the notebooks
- The markdown files (`.md`) will appear as notebooks in Jupyter

---

## Option 2: Build HTML Website

This builds a full HTML website version of the book (like the online version).

### Prerequisites
1. Python 3.8+
2. pip
3. `d2lbook` package

### Steps

1. **Install d2lbook:**
   ```bash
   pip install d2lbook
   ```

2. **Install the d2l library:**
   ```bash
   pip install -e .
   ```

3. **Build the HTML version:**
   ```bash
   cd /Users/karlzhang/Library/CloudStorage/OneDrive-Personal/Other/Live_Courses/BitTiger/Alg_Practice/Ind_Proj/d2l-en
   d2lbook build html
   ```
   
   **Note:** This may take a while as it evaluates all notebooks. To skip evaluation (faster build):
   - Edit `config.ini` and change `eval_notebook = True` to `eval_notebook = False`
   - Then run `d2lbook build html` again

4. **Serve the built HTML:**
   
   The HTML files will be in `_build/html/`. You can serve them using Python's built-in HTTP server:
   
   ```bash
   cd _build/html
   python3 -m http.server 8000
   ```
   
   Or using Python 2 (if you have it):
   ```bash
   python -m SimpleHTTPServer 8000
   ```

5. **Access the book:**
   - Open your browser and go to `http://localhost:8000`
   - You'll see the full website version of the book

---

## Quick Start (Fastest)

If you just want to get started quickly without a dedicated environment:

```bash
# Install dependencies
pip install jupyter mu-notedown

# Install d2l library
pip install -e .

# Register as Jupyter kernel
python -m ipykernel install --user --name d2l --display-name "d2l"

# Configure Jupyter (one-time setup)
jupyter notebook --generate-config
echo "c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'" >> ~/.jupyter/jupyter_notebook_config.py

# Start Jupyter
jupyter notebook
```

Then open `http://localhost:8888` in your browser. When creating a new notebook, select "d2l" as the kernel.

**Note:** For a complete setup that can both build and run code, use the "Recommended: Create a Dedicated Python Environment" section above.

---

## Troubleshooting

- **If Jupyter doesn't recognize markdown files:** 
  - Make sure `mu-notedown` (or `notedown`) is installed
  - Check that the config file is set up correctly: `cat ~/.jupyter/jupyter_notebook_config.py | grep notedown`
  - Try using `mu-notedown` instead of `notedown` if you have issues
  
- **If build fails:** 
  - Try setting `eval_notebook = False` in `config.ini` to skip code evaluation
  - Make sure `d2lbook` is installed: `pip install d2lbook`
  
- **If port 8888 is in use:** Jupyter will automatically try the next available port (8889, 8890, etc.)
  
- **If you get import errors when running code:**
  - Make sure you've installed a deep learning framework (PyTorch, TensorFlow, etc.)
  - Make sure the d2l library is installed: `pip install -e .`
  - Check that you're in the correct conda/virtual environment

- **To update the environment later:**
  
  **Update from environment.yml (when the file changes):**
  ```bash
  conda activate d2l
  conda env update -f environment.yml --prune
  ```
  The `--prune` flag removes packages no longer in the file.
  
  **Update specific packages:**
  ```bash
  conda activate d2l
  conda update numpy matplotlib  # Update conda packages
  pip install --upgrade d2lbook  # Update pip packages
  ```
  
  **Update everything (use with caution):**
  ```bash
  conda activate d2l
  conda update --all
  pip list --outdated  # Check outdated pip packages
  ```

**Installation failure**
- Use `environment-base.yml` to install basic libaries first. Can use `mamba`.
- Then install `torch` and `torchvision` separately.
- Install several packages from conda-forge to avoid `_control_lock` error.
      - `conda activate d2l`
      - `python -m pip uninstall -y jupyterlab jupyterlab-server jupyterlab-pygments jupyterlab-widgets notebook notebook-shim`
      - `conda install -c conda-forge -y jupyterlab notebook jupyterlab_server jupyterlab_widgets -v`
      