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