# Updating the D2L Environment

This guide explains how to update your conda environment without reinstalling everything.

## Quick Reference

```bash
# Activate the environment first
conda activate d2l

# Update from environment.yml (when file changes)
conda env update -f environment.yml --prune

# Update specific conda packages
conda update numpy matplotlib pandas scipy

# Update specific pip packages
pip install --upgrade d2lbook mu-notedown

# Update deep learning framework
pip install --upgrade torch torchvision  # or tensorflow, mxnet, jax, etc.
```

## Detailed Methods

### Method 1: Update from environment.yml

**When to use:** When `environment.yml` has been modified (packages added/removed/version changed)

```bash
conda activate d2l
cd <dir>/d2l-en
conda env update -f environment.yml --prune
```

**What it does:**
- Adds new packages listed in `environment.yml`
- Updates packages to versions specified in `environment.yml`
- Removes packages no longer in `environment.yml` (due to `--prune` flag)
- Keeps packages not listed in `environment.yml` (like your deep learning framework)

**⚠️ Note:** This can be slow because conda re-solves all dependencies every time, even if packages are already installed. For a single missing package, use Method 2 instead.

**Example:** If you add `tensorflow` to `environment.yml`, it will install it. If you remove `pandas`, it will uninstall it.

### Method 2: Install/Update Individual Packages (Fastest)

**When to use:** When you need to install a missing package or update specific packages. **This is much faster** than `conda env update` for single packages.

**Install a missing package:**
```bash
conda activate d2l
pip install autopep8  # Fast! Just installs what's missing
```

**Update conda packages:**
```bash
conda activate d2l
conda update numpy matplotlib pandas scipy
```

**Update pip packages:**
```bash
conda activate d2l
pip install --upgrade d2lbook
pip install --upgrade mu-notedown
pip install --upgrade jupyter
```

**Why this is faster:** It only installs/updates the specific package without re-solving the entire environment.

**Update deep learning framework:**
```bash
conda activate d2l
# PyTorch
pip install --upgrade torch torchvision

# TensorFlow
pip install --upgrade tensorflow

# MXNet
pip install --upgrade mxnet

# JAX
pip install --upgrade jax jaxlib flax
```

### Method 3: Update All Packages (Use with Caution)

**When to use:** When you want the latest versions of everything (may break compatibility)

```bash
conda activate d2l

# Update all conda packages
conda update --all

# Check which pip packages are outdated
pip list --outdated

# Update all outdated pip packages
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

**⚠️ Warning:** This may update packages to versions incompatible with the book's code. The book was tested with specific versions.

### Method 4: Update the d2l Library

**When to use:** When you've modified the d2l source code or pulled updates from git

```bash
conda activate d2l
cd <dir>/d2l-en
pip install -e . --upgrade
```

## Common Update Scenarios

### Scenario 1: Install a missing package (e.g., autopep8)

**Fast way (recommended):**
```bash
conda activate d2l
pip install autopep8
```

**Slow way (only if you need to sync everything):**
```bash
conda activate d2l
conda env update -f environment.yml --prune
```

### Scenario 2: Update d2lbook to latest version

```bash
conda activate d2l
pip install --upgrade d2lbook
```

### Scenario 2: Update PyTorch to latest version

```bash
conda activate d2l
pip install --upgrade torch torchvision
```

### Scenario 3: Add a new package to the environment

```bash
conda activate d2l
# For conda packages
conda install package-name

# For pip packages
pip install package-name
```

### Scenario 4: Update environment.yml and sync

1. Edit `environment.yml` to add/remove/update packages
2. Run:
   ```bash
   conda activate d2l
   conda env update -f environment.yml --prune
   ```

### Scenario 5: Check what's outdated

```bash
conda activate d2l

# Check conda packages
conda list --outdated

# Check pip packages
pip list --outdated
```

## Best Practices

1. **Use direct install for single packages:** Instead of `conda env update`, use `pip install package-name` for faster installation
2. **Only use `conda env update` when:** You've made multiple changes to `environment.yml` and want to sync everything at once
3. **Regular updates:** Update packages periodically to get bug fixes and security patches
4. **Test after updates:** Run a few notebook cells after updating to ensure everything still works
5. **Version pinning:** If something breaks, you can pin versions in `environment.yml` to prevent future updates
6. **Backup:** Before major updates, consider exporting your environment:
   ```bash
   conda env export > environment_backup.yml
   ```

## Why is `conda env update` slow?

`conda env update` can be slow because:
- It re-solves **all** dependencies every time, even if packages are already installed
- It checks for updates and compatibility across the entire environment
- The dependency solver can take time to find optimal solutions
- Network checks for package availability

**Solution:** For installing a single missing package (like `autopep8`), use:
```bash
pip install autopep8  # Much faster!
```

Only use `conda env update` when you need to sync multiple changes from `environment.yml`.

## Troubleshooting

### If an update breaks something

**Option 1: Revert to environment.yml**
```bash
conda activate d2l
conda env update -f environment.yml --prune
```

**Option 2: Reinstall specific package**
```bash
conda activate d2l
pip install --force-reinstall package-name==specific-version
```

**Option 3: Recreate environment (last resort)**
```bash
conda env remove -n d2l
conda env create -f environment.yml
conda activate d2l
pip install -e .
pip install torch torchvision  # Reinstall your framework
```

### If conda update is slow

Conda can be slow. For faster updates, you can:
- Use `mamba` (faster conda alternative): `mamba env update -f environment.yml --prune`
- Update only what you need instead of everything

## Summary

| Task | Command |
|------|---------|
| Update from environment.yml | `conda env update -f environment.yml --prune` |
| Update specific conda package | `conda update package-name` |
| Update specific pip package | `pip install --upgrade package-name` |
| Update all conda packages | `conda update --all` |
| Check outdated packages | `conda list --outdated` and `pip list --outdated` |
| Export environment | `conda env export > environment_backup.yml` |

