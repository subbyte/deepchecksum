#!/usr/bin/env bash

if [[ "$#" -ne 1 ]]
then
    echo "Usage: ./check_directory.sh directory"
else
    if [[ -x "/usr/bin/sha1deep" ]]
    then
        if [[ -d "$1" ]]
        then
            hash_file_old="$1.sha1"
            if [[ -f "$hash_file_old" ]]
            then
                hash_file_new="$(mktemp)"
                sha1deep -r $1 > $hash_file_new
                python3 compare_hashes.py $hash_file_old $hash_file_new
            else
                echo "[ERR] The target sha1 file \"$1.sha1\" does not exist."
            fi
        else
            echo "[ERR] The target directory \"$1\" does not exist."
        fi
    else
        echo "[ERR] Please install \"sha1deep\" (\"hashdeep\" package) first."
    fi
fi
