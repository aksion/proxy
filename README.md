# Proxy

This is a simple project demonstrating how a proxy server can work. Pages will be displayed and function correctly, just like the original ones, with the exception of modified text.

## Install

To run this project, you need to have Python 3.9+ installed.

1. Clone this repository.
2. Navigate to the project folder.

3. Run this command to install requirements:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

Create a `.env` file and set up your proxy server.

### Example .env

 ```ini
 PROXY_HOST = "127.0.0.1"
 PROXY_PORT = 8232
 BASE_URL = "https://news.ycombinator.com"
 SYMBOL = "™"
 ```

Edit the values in the `.env` file according to your requirements.

## Run

Run the proxy server using the following command:

 ```bash
 python3 proxy.py
 ```

## Use

Make sure the proxy server is running before you use it.
By default, call [http://127.0.0.1:8232](http://127.0.0.1:8232) page in browser.
