#!/usr/bin/env bash

set -eu

namespace="blissey"
component_1="blissey"

cd $(dirname $0)

build_root=$(pwd)

if [ -d build ]; then
    rm -r build
fi
mkdir build


# Include Blissey.
cd blissey

docker pull dnguyen0304/${namespace}-${component_1}-buildtime:latest
docker run --rm \
           --volume $(pwd):/tmp/build \
           dnguyen0304/${namespace}-${component_1}-buildtime:latest

cp build/* ${build_root}/build
cd ${build_root}


environments=( "development" "production" )
counter=${#environments[@]}

for (( i=0; i<${counter}; i++ ));
do
    docker build --file Dockerfile \
                 --tag dnguyen0304/${namespace}-latest:${environments[$i]} \
                 --build-arg NAMESPACE=${namespace} \
                 --build-arg COMPONENT_1=${component_1} \
                 --build-arg BLISSEY_CONFIGURATION_FILE_NAME="${component_1}.${environments[$i]}.config" \
                 .
done
