# python-via

This is a local annotator service modified from [VGG Annotator](https://www.robots.ox.ac.uk/~vgg/software/via/) version 2.x.y.

## Install

```
$ pip install git+https://github.com/ShihHsuanChen/python-via.git
```

## Usage

### Run Service

```
$ via --host 127.0.0.1 --port 8000
```

### Show help
```
$ via --help
usage: via [-h] [--host HOST] [--port PORT]

Local VGG Annotator with Uvicorn server

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Bind socket to this host. (default: 127.0.0.1)
  --port PORT  Bind socket to this port. If 0, an available port will be picked. (default: 8000)
```

