#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sIo tmp.txt 0.0.0.0:5000 && sed -n '/Content-Length/p' tmp.txt | awk '{print $2}' && rm tmp.txt
