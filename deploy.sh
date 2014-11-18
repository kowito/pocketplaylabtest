virtualenv pocket_playlab_env
source pocket_playlab_env/bin/activate
pip install -r requirement.txt 
python pocket_playlab_test.py 
deactivate 
rm -rf pocket_playlab_env/
cat output.txt
