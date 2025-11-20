#!/bin/bash

echo "File Management Script"
read -p "Enter 1.Create  2.Delete  3.Move File : " fms

case $fms in

1)  read -p "Name the file to be created: " c
    touch "$c"
    echo "File '$c' created."
    ;;

2)  read -p "Name the file to be deleted: " d
    if [ -f "$d" ]; then
        rm "$d"
        echo "File deleted."
    else
        echo "File not found."
    fi
    ;;

3)  echo "MOVE FILE"
    read -p "Enter source file name: " src
    read -p "Enter destination path: " dest

    if [ -f "$src" ]; then
        mv "$src" "$dest"
        echo "File moved successfully."
    else
        echo "Source file not found."
    fi
    ;;

*)  echo "Invalid option."
    ;;
esac

