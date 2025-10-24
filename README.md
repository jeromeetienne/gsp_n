# gsp_n

## Overview
This repository contains an attempts `.pyi` typed declaration of the GSP api.
The goal is to 'see what's missing' compared to the Google Drive document we have been working with up to now.

It also contains 2 attempts to have a specification of GSP protocol.
- one using protobufs (in the `./tmp/protobuf` folder)
- one using pydantic's dataclasses with type hints (in the `./tmp/dataclasses` folder)

## Installation

Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . 
```

## Files

### GSP .pyi typed declaration
- [gsp_n/gsp_api.pyi](gsp_n/gsp_api.pyi) is the .pyi typed declaration of the GSP api.
- [./examples/images-2d.py](./examples/images-2d.py) is an example script using the GSP api for 2D images.
- [./examples/pixels-3d.py](./examples/pixels-3d.py) is an example script using the GSP api for 3D pixels.

It is rather complete.

### Protobuf specification
- [./tmp/protobuf/GSP.proto](./tmp/protobuf/GSP.proto) is the Protobuf specification for the GSP API.
  - [./tmp/protobuf/NOTES.md](./tmp/protobuf/NOTES.md) notes i tooks while working on the protobuf specification.
- [./tmp/protobuf/Makefile](./tmp/protobuf/Makefile) is a Makefile to generate python code from the protobuf specification. 
- [./tmp/protobuf/sample.py](./tmp/protobuf/sample.py) is a usage example of the generated protobuf code.



### Pydantic dataclasses specification
- [./tmp/dataclasses/gsp_dataclasses.py](./tmp/dataclasses/gsp_dataclasses.py) is the Pydantic dataclasses specification for the GSP API.
- [./tmp/dataclasses/sample.py](./tmp/dataclasses/sample.py) is a usage example of the Pydantic dataclasses specification.