# FedEx

## Install

```PowerShell
# Install pyenv-win
pip install pyenv-win --target "$HOME\.pyenv"

# Install and set Python version globally
pyenv install 3.15.0a5
pyenv global 3.15.0a5

# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r .\requirements.txt

# Create config file from template
copy config-template.json config.json
```

## Usage

```PowerShell
# Run the script
python .
```
