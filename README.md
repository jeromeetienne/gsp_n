# gsp_n


## Files

- `./pyi`: a typed declaration of GSP api
    - see [pyi/gsp_n/sample.py](pyi/gsp_n/sample.py) for an example of usage
- `./protobuf`: an experimental implementation of GSP on top of protobufs
  - see [GSP.proto](protobuf/GSP.proto) for the protobuf definition
  - see [protobuf/output/sample.py](protobuf/output/sample.py) for an example of usage
  - use `make compile` to compile the protobuf files in .py and .pyi

## Installation

Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
```

```
pip install -e . 
```