#!/bin/bash
# Tested using bash version 4.1.5
for ((i=1;i<=200;i++)); 
do 
   py data_tester.py
   echo $i
done