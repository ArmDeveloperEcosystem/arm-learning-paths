if file -b --mime-type $1 | grep -q md; then
   pip install -r tools/requirements.txt
   tools/maintenance.py -i $1
else
   echo "Not an .md file, skipping"
fi