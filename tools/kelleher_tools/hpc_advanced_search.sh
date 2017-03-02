#!/bin/sh
#sleep 5
echo MZML ONE $1
echo FLAT FILES TWO $2
echo REGEX THREE $3
echo OUTPUT1 FOUR $4
echo OUTPUT2 FIVE $5
echo OUTPUT3 SIX $6
echo WORKING FOLDER SEVEN $7
echo EIGHT $8
echo EMAIL NINE $9
echo JOB ID TEN ${10}
echo 11 ${11}
echo 12 ${12}

REGEX=$3

if [ -z "$3" ]; then
   REGEX=none
fi

ENV_PATH=/projects/b1035/shared/${11}
#echo $ENV_PATH

var1=$(echo ${10} | cut -f1 -d'_')
var2=$(echo ${10} | cut -f2 -d'_')
DB_NAME=$(echo $var2 | cut -f1 -d'.')
DB=$(echo $var2 | cut -f1 -d'.').db
var4=$(echo $var2 | cut -f2 -d'.')

WORKING_DIR=$7
USER_EMAIL=$9
parent=`dirname $4`

#echo $4
#echo ${10}

#echo jobId${10}

inputPathAll=$parent/inputs/*
inputPath=$parent/inputs
tLen=${#inputPathAll[@]}

#echo $tLen

#echo $inputPath

var=0

for f in $inputPathAll
do
  ((var++))
#  cat $f >> /projects/d20657/shared/GalaxyHPCSearch/NtoNto1.txt
done

#echo $var

grandparent=`dirname $parent`

#echo parent $parent
#echo grandparent $grandparent
JOB_ID=`basename $grandparent`

#echo metadata
#python $ENV_PATH/GalaxyHPCSearch/hpc_echo_sysargv.py $WORKING_DIR ${10} $USER_EMAIL
python $ENV_PATH/GalaxyHPCSearch/hpc_create_metadata.py $WORKING_DIR ${10} $USER_EMAIL

#echo monitor
#python $ENV_PATH/GalaxyHPCSearch/hpc_echo_sysargv.py $ENV_PATH $WORKING_DIR $JOB_ID ${10}
python $ENV_PATH/GalaxyHPCSearch/hpc_monitor.py $ENV_PATH $WORKING_DIR $JOB_ID ${10} &

echo create
python $ENV_PATH/GalaxyHPCSearch/hpc_echo_sysargv.py $ENV_PATH $2 $DB_NAME  $JOB_ID
python $ENV_PATH/GalaxyHPCSearch/hpc_create_database.py $ENV_PATH $2 $DB_NAME $JOB_ID false

echo copy
python $ENV_PATH/GalaxyHPCSearch/hpc_echo_sysargv.py $ENV_PATH $DB $WORKING_DIR $JOB_ID $USER_EMAIL
python $ENV_PATH/GalaxyHPCSearch/hpc_copy_database.py $ENV_PATH $DB $WORKING_DIR $JOB_ID $USER_EMAIL ${12}


echo prepare
python $ENV_PATH/GalaxyHPCSearch/hpc_echo_sysargv.py $ENV_PATH $1 $WORKING_DIR $JOB_ID $USER_EMAIL
python $ENV_PATH/GalaxyHPCSearch/hpc_prepare.py $ENV_PATH $1 $WORKING_DIR $JOB_ID $USER_EMAIL

echo queue
python $ENV_PATH/GalaxyHPCSearch/hpc_echo_sysargv.py $ENV_PATH $var $DB $WORKING_DIR $JOB_ID $USER_EMAIL
python $ENV_PATH/GalaxyHPCSearch/hpc_queue_array.py $ENV_PATH $var $DB $WORKING_DIR $JOB_ID $USER_EMAIL

#sleep 300

echo generate
python $ENV_PATH/GalaxyHPCSearch/hpc_echo_sysargv.py $ENV_PATH $REGEX $4 $5 $6 $WORKING_DIR $JOB_ID $USER_EMAIL
python $ENV_PATH/GalaxyHPCSearch/hpc_generate_reports.py $ENV_PATH $REGEX $4 $5 $6 $WORKING_DIR $JOB_ID $USER_EMAIL

#echo "Done" >> $WORKING_DIR/done.txt

