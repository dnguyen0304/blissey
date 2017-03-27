# Blissey Python Buildtime

## Getting Started
### Building
Get a local copy of the repository and then build the image.
```
# NOTE: Remember to replace the `<tag>` placeholder.

git clone https://github.com/dnguyen0304/blissey.git
cd blissey/python-buildtime
git checkout tags/<tag>

sudo docker build --file Dockerfile --tag dnguyen0304/python-2.7-buildtime:<tag> .
```

### Pushing
Push the image.
```
# NOTE: Remember to replace the `<tag>` placeholder.

sudo docker push dnguyen0304/python-2.7-buildtime:<tag>
```
