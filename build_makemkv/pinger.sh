#!/bin/bash
version=""
keepRunning=true
echo "-> Finding newest makemkv version..."
while :
do
  for f in $(seq 1 10)
  do
    for s in $(seq 12 100)
    do
      for t in $(seq 1 10)
      do
        #echo "$f.$s.$t"
        if [ $keepRunning == true ]
        then
          curl -s --head http://www.makemkv.com/download/makemkv-oss-$f.$s.$t.tar.gz | head -n 1 | grep "HTTP/1.[01] [23].." > /dev/null
        else
          break
        fi
        if [ $? == 0 ]
        then
          version="$f.$s.$t"
          keepRunning=false
          break
        fi
      done
    done
  done
  curl -s --head http://www.makemkv.com/download/makemkv-oss-$version.tar.gz | head -n 1 | grep "HTTP/1.[01] [23].." > /dev/null
  if [ $? == 0 ] 
  then
    break
  elif [ $? == 1 ]
  then
    echo "One"
  fi
done
echo "Version: $version"
wget http://www.makemkv.com/download/makemkv-oss-$version.tar.gz
mv makemkv-oss-$version.tar.gz /src/makemkv-oss.tar.gz
wget http://www.makemkv.com/download/makemkv-bin-$version.tar.gz
mv makemkv-bin-$version.tar.gz /src/makemkv-bin.tar.gz
