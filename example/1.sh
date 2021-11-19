#/bin/bash

data=$1
if [ $data == 'a' ];then
    echo "1"
    exit 1
  else
    echo "2"
    exit 2
fi