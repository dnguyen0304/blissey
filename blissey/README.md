# Blissey
A personal relationship management (PRM) platform.

## Getting Started
### Installation
Get a local copy of the repository.
```
# Remember to replace the `<tag>` placeholder.

git clone https://github.com/dnguyen0304/blissey.git
cd blissey/blissey
git checkout tags/<tag>
```

Update the configuration files in the `configuration` directory. Then build Blissey.
```
sudo docker build --file Dockerfile .
sudo docker run --rm --volume $(pwd):/tmp/build <images_id>
```

Configuration
-------------
### Shell Environment
When building from source or outside a Docker container, to set the environment variables for the current and all future shell sessions, from the terminal run
```
$ echo 'export BLISSEY_CONFIGURATION_FILE_PATH=/opt/blissey/configuration/blissey.development.config"' >> ~/.bashrc
$ source ~/.bashrc
```
