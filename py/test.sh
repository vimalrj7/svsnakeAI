#!/bin/bash
# Tested using bash version 4.1.5
for ((i=1;i<=250;i++)); 
do 
   py data_tester.py
   echo $i
   sleep 1
done