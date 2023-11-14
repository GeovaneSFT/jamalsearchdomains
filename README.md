# Domain Checker

This Python script checks the existence of a given name on various top-level domains (TLDs). It combines the name with each TLD and attempts to make a request to the resulting URL. If the response status code is 200 (OK), it assumes the domain exists.

## Usage

1. **Install Dependencies:**

    ```bash
    pip install requests beautifulsoup4
    ```

2. **Run the Script:**

    ```bash
    python jamal.py
    ```

3. **Modify Configuration:**

    - Update the `name` variable in the script to the name you want to check.
    - Set the `op` variable to `True` if you want to open the URLs in a web browser.

## Configuration

- `name`: The name to be checked on different TLDs.
- `op`: Set to `True` if you want to open the URLs in a web browser.

## Dependencies

- [Requests](https://docs.python-requests.org/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

