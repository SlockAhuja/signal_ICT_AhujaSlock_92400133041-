#!/bin/bash
# Script to upload package to PyPI using twine and API token

# Ensure twine is installed
pip install --upgrade twine

# Upload to PyPI
twine upload dist/* --username __token__ --password pypi-AgENdGVzdC5weXBpLm9yZwIkNDVkMzdmYjMtYjk2OC00ZTRlLTliMTAtMDIzODc1NjdlMDA3AAIqWzMsImQ1OTg2ZWI1LTBlNGItNDI3OC04YmQ4LTYwZTY3NTkyZGE3OCJdAAAGIAqu7QiLSQkOvwsPN59ooEWhHcS85lRoj6AbEg149AMC

