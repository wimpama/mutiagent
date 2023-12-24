# filename: check_install_yfinance.py

try:
    import yfinance as yf
    print("yfinance is installed.")
except ImportError:
    print("yfinance is not installed. Please run 'pip install yfinance' to install it.")