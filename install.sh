echo "starting installation ..."
sleep 2 
pkg install python -y 
clear
pip install colorama 
clear
pip install tqdm 
clear
echo "The installation is complete."
var1="1"
echo "done script"
echo "1) Yes"
echo "2) Exit"
read -p ">> " resp
if [ "$resp" == "$var1" ]
then
python pirate.sec.py
else
echo "to start the script you must write: python3 piratesec_DDOS.py "
echo ":D"
fi 
