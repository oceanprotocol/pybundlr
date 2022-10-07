
### Release Process

Find the current version number at [pypi](https://pypi.org/project/pybundlr/).

Open `pyproject.toml` in an editor, and update the value in `"version" = x.y.z`.

In terminal:

```console
#go to root of directory
cd ~/code/pybundlr

#ensure repo is up-to-date
git commit -am "Release x.y.z"
git push

#turn off virtual env't
deactivate

#ensure `dist/` folder is empty
rm -rf dist

#generate distribution archives: create `dist` folder with two files 
python -m build
```

OPTIONAL: test the library, via test.pypi.org. In terminal:
```
#run twine to upload `dist` files to *test* pypi
python3 -m twine upload --repository testpypi dist/*
```

OPTIONAL cont'd: open a different terminal, and:
```console
python -m venv venv
source venv/bin/activate
pip install -i https://test.pypi.org/simple/ pybundlr==<x.y.z>

#Then: go through "Using Pybundlr Library" section above
```

Once you're satisfied, we can distribute to main pypi. In terminal:
```console
#run twine to upload `dist` files *main* pypi
python -m twine upload dist/*

# -when prompted, give username: __token__
# -when prompted, given password: <pypi API token>
```

Done! The updated package will be [at pypi](https://pypi.org/project/pybundlr/).

Notes: this section is based on [packaging.python.org tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).