# Bump the version number first.
rm rf dist
python3 -m build
twine upload dist/*
