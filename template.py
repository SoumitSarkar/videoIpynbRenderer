import os
from pathlib import Path
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s] %(message)s"
)


while True:
    project_name = input("Enter the Project Name: ")
    if project_name:
        break


logging.info(f"Create Project By Name: {project_name}")


# list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory @: {filedir} for file: {filename}")
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating file {filename} @ path: {filepath}")
    else:
        logging.info("file is already present @ {path}".format(path=filepath))







