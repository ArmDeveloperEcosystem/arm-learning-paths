echo "HELLO WORLD"
pip install -r $1/tools/requirements.txt
./tools/maintenance.py -i $1/content/install-guides/cmake.md