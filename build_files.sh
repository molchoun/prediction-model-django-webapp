echo "BUILD START"
python3.9 pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
python3.9 prediction_project/manage.py collectstatic --no-input --clear
echo "BUILD END"