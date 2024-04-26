# SoloParser

A solo.to API parser made in Python using PyQt6. This application allows you to fetch and display data from the solo.to API by entering a username.

Sample:

![Sample](https://user-images.githubusercontent.com/68476516/134805013-3f3b3b7b-3b7b-4b7b-8b7b-3b7b3b7b3b7b.png)

## Requirements

- Python 3.8 or higher
- [requests](https://pypi.org/project/requests/)
- [PyQt6](https://pypi.org/project/PyQt6/)

## Installation

<details><summary>Install a virtual environment</summary>

```bash
python -m venv .venv
source .venv/bin/activate # Linux
.venv\Scripts\activate # Windows
```

</details>

```bash
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```bash
python main.py
```

In the application window, enter a solo.to username and click "Submit". If the username is valid, a new window will open displaying the fetched data.

## Contributing
- CodeByAidan (@CodeByAidan)

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[GNU](LICENSE)
