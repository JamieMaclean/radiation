## Setup virtual env

Once you have python installed go to the project in your teminal. In the `radiation` directory run the command 

```bash
python -m venv .venv
```

This will create a folder called .env in the project. This will be ignored by git. IT is the local python environment that you will use only for this project.
All libraries that you install will only be installed in this version of python NOT the general python you have on your machine.

### Activate virtual environment

Before you do any coding ensure that you have actiavted your python virtual environment. You can do this by running the following command:

```bash
.\venv\Scripts\activate.bat
```

More advice can be found here: https://docs.python.org/3/library/venv.html#how-venvs-work

To deactivate the venv you can type `deactivate`

## Run the main function

```bash
python src/main.py
```

## Run tests

```bash
python -m unittest discover tests
```