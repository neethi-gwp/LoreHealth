# Test Framework

I opted for the combination of BDD & Data driven approach. I chose Python, Selenium & BehaveX (wrapper on top of Python Behave). I have used the page object design pattern to separate page specific code and test code. The framework right now only supports chromedriver on all major Operating Systems(Mac, Win, Linux).


## Installation

```bash  
python3  -m  venv  venv
source  venv/bin/activate
cd <LoreHealth_directory>
pip install -r requirements
```

## Run Tests


```bash  
behavex
```

## Reporting

- Reports are automatically generated and saved under an "output" folder in the LoreHealth folder. 
- Open the html report in a browser.

# Test Plan Considerations

 - Main user story for this exercise is part of the End2End Automation test suite. 
 - Elaborate test cases for the interactions are in their own test suites namely - Signup, Login, Add to cart and Shipping.  


## Potential enhancements to current framework

For the purpose of this assignment the framework used is a barebones one. Ideally, the following improvements need to be incorporated:

 - Docstrings for all methods
 - Better Logging
 - Screenshots on failures
 - Automated retries of potentially flaky tests
 - Lint checks
 - Support for cross browser testing
