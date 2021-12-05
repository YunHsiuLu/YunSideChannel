echo
now="Now: `date +%F%t%T` in $USER"
echo $now
echo
if [ -z $1 ]; then
	echo "You have to input a .py file!!!"
	echo "No program is running..............."
else
	c=$1
	str=$(echo $c | awk -F'.' '{print$1}')
	logstr="logfile/`date +%H%M%S_%Y%m%d`_$str.log"

	echo "$1 is Runing.............."
	echo
	python3 $1 | tee $logstr
	echo
	echo "$1 is Finished............"
fi
