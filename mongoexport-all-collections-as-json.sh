#!/bin/bash

DB=$1
COLLECTIONS=$(mongo localhost:27017/$DB --quiet --eval "db.getCollectionNames()" | sed 's/,/ /g')

for collection in $COLLECTIONS; do
    echo "Exporting $DB/$collection ..."
    mongoexport -d newtickettoolDB -c $collection -o $collection.json
done
