# TCM

An AI program that using Kinect camera and shows netural network and human skeleton.

![python_version](https://img.shields.io/badge/python-3.11%2B-blue)
![workstation](https://img.shields.io/badge/works%20on-my%20machine-brightgreen)
[![code_style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/index.html)
[![code_lint](https://img.shields.io/badge/code%20lint-flake8-2980B9.svg)](https://flake8.pycqa.org/en/latest/)

## Installnation

Install scaffold:

```bash
pip install --upgrade poetry
```

Install independencies:

```bash
poetry install
```

If you have some troubles above command, please try to reinstall the problematic package by `pip`. Exapmle:

```bash
pip install --upgrade pyqt5
```

If you still have troubles, try to install all dependencies with `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Run the code

```bash
poetry run python ./main.py
```

## UI Design Scheme

| Name                    | Value                        |
| ----------------------- | ---------------------------- |
| Logo                    | ![logo](./res/logo_mini.png) |
| Main color              | #1DE9B6                      |
| Background color        | #31363B                      |
| Deeper background color | #232629                      |
| Border color            | #515558                      |
| Border radius           | 7px                          |
| Font                    | Microsoft YaHei UI           |
