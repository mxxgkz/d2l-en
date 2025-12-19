# Making the D2L Environment Usable in Jupyter

This guide shows how to make your `d2l` conda environment available as a kernel in Jupyter Notebook and JupyterLab.

## Quick Setup

After creating and activating your environment:

```bash
conda activate d2l
python -m ipykernel install --user --name d2l --display-name "d2l"
```

That's it! Now "d2l" will appear in your Jupyter kernel list.

## Detailed Steps

### Step 1: Ensure ipykernel is Installed

The `environment.yml` already includes `ipykernel`, but if you need to install it manually:

```bash
conda activate d2l
conda install ipykernel
# or
pip install ipykernel
```

### Step 2: Register the Kernel

```bash
conda activate d2l
python -m ipykernel install --user --name d2l --display-name "d2l"
```

**What this does:**
- Creates a kernel specification in `~/.local/share/jupyter/kernels/d2l/`
- Makes "d2l" appear in Jupyter's kernel list
- Links the kernel to your `d2l` conda environment

### Step 3: Verify Installation

List all available kernels:
```bash
jupyter kernelspec list
```

You should see `d2l` in the list.

### Step 4: Use in Jupyter

**Jupyter Notebook:**
```bash
jupyter notebook
```
- Click "New" → "d2l" to create a new notebook
- For existing notebooks: "Kernel" → "Change Kernel" → "d2l"

**JupyterLab:**
```bash
jupyter lab
```
- Click the kernel name in the top right
- Select "d2l" from the dropdown

**VS Code:**
- Open a `.ipynb` file
- Click the kernel selector in the top right
- Choose "d2l" or "Python 3.x.x ('d2l': conda)"

## Using the Kernel

### Create a New Notebook with d2l Kernel

1. Start Jupyter: `jupyter notebook` or `jupyter lab`
2. Click "New" → "d2l"
3. Your notebook will use the d2l environment with all packages available

### Change Kernel of Existing Notebook

1. Open your notebook in Jupyter
2. Go to "Kernel" → "Change Kernel" → "d2l"
3. The notebook will now use the d2l environment

### Verify It's Working

Run this in a cell to verify:
```python
import sys
print(sys.executable)  # Should show path to d2l environment
import d2l
print("d2l imported successfully!")
import torch  # or your framework
print("Framework imported successfully!")
```

## Troubleshooting

### Kernel Not Appearing

**Check if kernel is registered:**
```bash
jupyter kernelspec list
```

**Re-register the kernel:**
```bash
conda activate d2l
python -m ipykernel install --user --name d2l --display-name "d2l" --force
```

### Kernel Fails to Start

**Check ipykernel is installed:**
```bash
conda activate d2l
python -c "import ipykernel; print(ipykernel.__version__)"
```

**Reinstall ipykernel:**
```bash
conda activate d2l
conda install ipykernel --force-reinstall
# or
pip install --force-reinstall ipykernel
```

### Wrong Python Path

If the kernel uses the wrong Python:

**Remove and re-register:**
```bash
jupyter kernelspec uninstall d2l
conda activate d2l
python -m ipykernel install --user --name d2l --display-name "d2l"
```

### Kernel Can't Find Packages

**Verify you're in the right environment:**
```bash
conda activate d2l
which python
python -c "import d2l; print('OK')"
```

**Reinstall packages:**
```bash
conda activate d2l
pip install -e .  # Reinstall d2l library
```

## Advanced: Multiple Kernel Names

You can create multiple kernel names pointing to the same environment:

```bash
conda activate d2l
python -m ipykernel install --user --name d2l-pytorch --display-name "D2L (PyTorch)"
python -m ipykernel install --user --name d2l-tensorflow --display-name "D2L (TensorFlow)"
```

## Removing the Kernel

If you want to remove the kernel:

```bash
jupyter kernelspec uninstall d2l
```

## Summary

✅ **One command to register:**
```bash
python -m ipykernel install --user --name d2l --display-name "d2l"
```

✅ **Available in:**
- Jupyter Notebook
- JupyterLab
- VS Code
- Any Jupyter-compatible IDE

✅ **Benefits:**
- Use the d2l environment in any notebook
- All packages (d2l, PyTorch, etc.) available automatically
- Isolated from system Python

