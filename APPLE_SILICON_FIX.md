# Fixing Slow PyTorch Import on Apple Silicon

## Problem

If you're on Apple Silicon (M1/M2/M3) but Python reports `x86_64`, your conda environment is running under Rosetta 2 emulation, which makes PyTorch imports very slow.

**Check your architecture:**
```bash
uname -m  # Should show: arm64
python -c "import platform; print(platform.machine())"  # Currently shows: x86_64 (BAD!)
```

## Solution: Recreate Environment with Native arm64 Python

### Step 1: Remove the Old Environment

```bash
conda deactivate
conda env remove -n d2l -y
```

### Step 2: Ensure You're Using Native Conda

Make sure you're using a native arm64 conda installation:

**Check conda architecture:**
```bash
conda info
# Look for "platform" - should show "osx-arm64" not "osx-64"
```

**If you see "osx-64", you need to install native arm64 Miniforge:**

### Option A: Install Miniforge Directly (Recommended)

1. **Remove the x86_64 miniforge** (if installed):
   ```bash
   rm -rf ~/miniforge3
   ```

2. **Download and install native arm64 Miniforge:**
   ```bash
   # Download the arm64 installer
   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh"
   
   # Make it executable
   chmod +x Miniforge3-MacOSX-arm64.sh
   
   # Install (follow prompts, say yes to initialize)
   ./Miniforge3-MacOSX-arm64.sh -b -p ~/miniforge3
   
   # Clean up
   rm Miniforge3-MacOSX-arm64.sh
   ```

3. **Initialize Miniforge:**
   ```bash
   ~/miniforge3/bin/conda init zsh
   ```

4. **Restart your terminal** or reload:
   ```bash
   source ~/.zshrc
   ```

5. **Verify it's arm64:**
   ```bash
   conda info | grep platform  # Should show: osx-arm64 ✅
   ~/miniforge3/bin/python -c "import platform; print(platform.machine())"  # Should show: arm64 ✅
   ```

### Option B: Fix Homebrew Installation

If you installed via Homebrew and got x86_64:

1. **Check if Homebrew is running under Rosetta:**
   ```bash
   arch  # Should show: arm64 (not i386)
   which brew  # Check location
   file $(which brew)  # Should show arm64
   ```

2. **If Homebrew is x86_64, reinstall Homebrew natively:**
   ```bash
   # Remove old Homebrew
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
   
   # Install native arm64 Homebrew
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Then install miniforge:**
   ```bash
   brew install miniforge
   ```

### Update ~/.zshrc

After installing native miniforge, make sure your `~/.zshrc` prioritizes miniforge:

1. **Remove or comment out anaconda3** from PATH (if present):
   ```bash
   # Comment out lines like:
   # export PATH=$HOME/anaconda3/bin:$PATH
   ```

2. **Ensure miniforge comes first:**
   ```bash
   # Add this line (if not already there from conda init):
   export PATH="$HOME/miniforge3/bin:$PATH"
   ```

3. **Reload:**
   ```bash
   source ~/.zshrc
   ```

### Step 3: Create New Environment with Native Python

```bash
# Make sure you're using native conda
conda create --name d2l python=3.9 -y

# Activate it
conda activate d2l

# Verify it's native
python -c "import platform; print(platform.machine())"  # Should show: arm64 ✅
```

### Step 4: Install Packages

```bash
conda activate d2l
cd <dir>/d2l-en

# Install scientific packages via conda
conda install -c conda-forge numpy=1.23.5 matplotlib=3.7.2 pandas=2.0.3 scipy=1.10.1 ipykernel -y

# Install pip packages
pip install jupyter==1.0.0 matplotlib-inline==0.1.6 requests==2.31.0
pip install mu-notedown d2lbook autopep8

# Install PyTorch for Apple Silicon (native, fast!)
pip install torch torchvision

# Install d2l library
pip install -e .

# Register as Jupyter kernel
python -m ipykernel install --user --name d2l --display-name "Python (d2l)"
```

### Step 5: Verify It's Working

```bash
conda activate d2l
python -c "import platform; print('Architecture:', platform.machine())"  # Should be arm64
python -c "import torch; print('PyTorch version:', torch.__version__); print('MPS available:', torch.backends.mps.is_available())"
```

**Expected output:**
- Architecture: `arm64` ✅
- PyTorch should import quickly
- MPS (Metal Performance Shaders) should be available for GPU acceleration

## Alternative: Use environment.yml with Native Conda

If your conda is already native (arm64), you can use the environment.yml:

```bash
conda env create -f environment.yml
conda activate d2l
pip install -e .
python -m ipykernel install --user --name d2l --display-name "Python (d2l)"
```

But make sure PyTorch installs the arm64 version:
```bash
pip install torch torchvision  # This should automatically get arm64 version
```

## Why This Happens

- **x86_64 Python on Apple Silicon:** Runs through Rosetta 2 emulation → Very slow
- **arm64 Python on Apple Silicon:** Native execution → Fast!

## Benefits of Native arm64

✅ **Much faster PyTorch imports** (seconds instead of minutes)
✅ **Can use MPS (Metal)** for GPU acceleration on Apple Silicon
✅ **Better performance** overall
✅ **Lower power consumption**

## Quick Check Script

```bash
#!/bin/bash
echo "System architecture: $(uname -m)"
echo "Python architecture: $(python -c 'import platform; print(platform.machine())')"
if [ "$(uname -m)" = "arm64" ] && [ "$(python -c 'import platform; print(platform.machine())')" = "x86_64" ]; then
    echo "⚠️  WARNING: You're running x86_64 Python on Apple Silicon!"
    echo "   This will be very slow. Recreate your environment with native arm64 Python."
else
    echo "✅ Architecture looks good!"
fi
```

## Summary

**The issue:** x86_64 Python on Apple Silicon = slow PyTorch
**The fix:** Use native arm64 Python = fast PyTorch

After recreating the environment with native Python, PyTorch imports should be much faster!

