# Blissey
A personal relationship management (PRM) platform.

Getting Started
---------------
### General
```
$ git clone https://github.com/dnguyen0304/blissey.git
$ cd blissey
$ git checkout tags/latest
```

```
$ cd scripts/setup
$ sudo ./set_up_blissey
```

Configuration
-------------
### Shell Environment
When building from source or outside a Docker container, to set the environment variables for the current and all future shell sessions, from the terminal run
```
$ echo 'export BLISSEY_CONFIGURATION_FILE_PATH=/opt/blissey/configuration/blissey.development.config"' >> ~/.bashrc
$ source ~/.bashrc
```
