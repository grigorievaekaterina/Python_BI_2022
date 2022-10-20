## Operation system

These commands were written for MacOS Monterey 12.4.

## Python version

These commands were written for Python 3.10.8.

## Step-by-step instruction

* If you do not have brew, install it using the command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

If you have already had brew, just update brew:

```bash
brew update
```

* Download wget using brew:

```bash
brew install wget
```

* Update your Python up to 3.11 version following the link "https://www.python.org/ftp/python/3.11.0/python-3.11.0rc2-macos11.pkg" and given instructions. Close the shell and open a new one.

* Create and activate a virtual environment using commands:

```bash
$ python3 -m venv PATH_TO_ENVIRONMENT/ENVIRONMENT_NAME
$ source PATH_TO_ENVIRONMENT/ENVIRONMENT_NAME/bin/activate
```

* Check your Python version in the virtual environment:

```bash
cd PATH_TO_ENVIRONMENT/ENVIRONMENT_NAME/
python3 --version
```

It should be Python 3.11.

* Upload the python file and the requirements text file from Github using wget:

```bash
wget "https://raw.githubusercontent.com/grigorievaekaterina/Python_BI_2022/Modules_VEnvs/ultraviolence.py"
wget "https://raw.githubusercontent.com/grigorievaekaterina/Python_BI_2022/Modules_VEnvs/requirements.txt"
```

* Install packages from requirements.txt:

```bash
python3 -m pip install -r requirements.txt
```

* Rename google package:

```bash
cd lib/python3.11/site-packages/
mv google-3.0.0.dist-info google
```

* Change the code in pandas module to avoid error with indexes using vim text editor:

```bash
vim pandas/core/frame.py
```

In vim editor press `/` and find the next: `index cannot be a set`

Using insert mode (press `i`) delete the following `raise ValueError("index cannot be a set")`

Write the following `index = list(index)` at the same place accoding to tabulation.

Press `ESC` to quit insert mode. Close the file typing `:wq`.

* Now you are ready to open the python file:

```bash
cd PATH_TO_ENVIRONMENT/ENVIRONMENT_NAME/
python3 ultraviolence.py
```
