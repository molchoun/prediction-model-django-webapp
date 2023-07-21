echo "BUILD START"
python3.9 pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
echo "Make migrations..."
python3.9 prediction_project/manage.py makemigrations
python3.9 prediction_project/manage.py migrate
echo "Collect static"
python3.9 prediction_project/manage.py collectstatic --no-input --clear
echo "BUILD END"