# Blissey
A personal relationship management (PRM) platform.

## Getting Started
### Installing
Get a local copy of the repository and then install the package.
```
# NOTE: Remember to replace the <tag> placeholder.

git clone https://github.com/dnguyen0304/blissey.git
cd blissey/blissey
git checkout tags/<tag>

python setup.py install
```

### Configuring
Set the environment variables for the current and all future shell sessions.
```
# NOTE: Remember to replace the <environment> placeholder.

echo 'export BLISSEY_CONFIGURATION_FILE_PATH=/opt/blissey/configuration/blissey.<environment>.config"' >> ~/.bashrc
source ~/.bashrc
```

### Running
Run an example.
```
# Remember to replace the <first_name> and <last_name> placeholders.

from blissey import services

blissey_service = services.BlisseyService()
blissey_service.add_note(message='set <first_name> <last_name> Hello, World!')
```

### Building
Update the configuration files in the `configuration` directory and then build the package.
```
# NOTE: Remember to replace the <tag> placeholder.

sudo docker build --file Dockerfile \
                  --tag dnguyen0304/blissey-blissey-buildtime:<tag> \
                  .
sudo docker run --rm \
                --volume $(pwd):/tmp/build \
                dnguyen0304/blissey-blissey-buildtime:<tag>
```

### Pushing
Push the buildtime image.
```
# NOTE: Remember to replace the <tag> placeholder.

sudo docker push dnguyen0304/blissey-blissey-buildtime:<tag>
```
