#!/bin/bash
# Script to upload package to TestPyPI using twine and API token

# Ensure twine is installed
pip install --upgrade twine

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# When prompted:
# Username: SlockAhuja
# Password: pypi-AgENdGVzdC5weXBpLm9yZwIkZTg5NWIzZDQtNTdjNi00MTViLTg3MjgtNDg4NmJjZDgxZmRlAAIqWzMsImQ1OTg2ZWI1LTBlNGItNDI3OC04YmQ4LTYwZTY3NTkyZGE3OCJdAAAGIKij1wm9jjrGEq34HOXNQmQSEw7MriF5K2oVkwkri-Mj
