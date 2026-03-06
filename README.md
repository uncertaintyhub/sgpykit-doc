# Documentation

Files to generate documentation for [sgpykit](https://github.com/uncertaintyhub/sgpykit).

```
git clone --recurse-submodules https://github.com/uncertaintyhub/sgpykit-doc
cd sgpykit-doc/doc

# if needed
python -m venv --system-site-packages .venv
source .venv/bin/activate
pip install sphinx numpydoc sphinx-rtd-theme

make clean; make html
```


The initial spartial checkout workflow:

```
git clone https://github.com/uncertaintyhub/sgpykit-doc.git sgpykit-doc
cd sgpykit-doc
git submodule add https://github.com/uncertaintyhub/sgpykit sgpykit
git submodule update --init sgpykit
cd sgpykit
git sparse-checkout init --no-cone
git sparse-checkout set "sgpykit/*"
git checkout .
```
