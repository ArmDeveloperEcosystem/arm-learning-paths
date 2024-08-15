if [[ $1 == *.md ]]; then
   pip install -r tools/requirements.txt
   tools/maintenance.py -i $1
else
   echo "Not an .md file, skipping"
fi