# SoloParser

A solo.to API parser made in Python using PyQt6. This application allows you to fetch and display data from the solo.to API by entering a username.

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
pip install requests pyqt6
```

## Usage

To start the application, run the following command:

```bash
python main.py
```

In the application window, enter a solo.to username and click "Fetch Data". If the username is valid, a new window will open displaying the fetched data.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[GNU](LICENSE)
