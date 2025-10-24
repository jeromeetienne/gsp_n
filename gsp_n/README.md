## Principles
- this API is the python API definition for the Graphics Server Protocol

## User target
- In the scientific visualization domain, the GSP protocol API can be viewed as a low-level 3D graphics API, similar to a "matplotlib backend"
    - It is not designed to be used directly by scientists who want to visualize their data
    - It is designed for developers who want to implement visualization tools (and these visualization tools will, in turn, be used by scientists)
- So the API is designed 
    - to be unambiguous (hence the use of typing and pyi files)
    - to be complete (hence the presence of low-level constructs such as buffers, matrices, etc)
    - to be efficient (hence the presence of constructs such as buffers, matrices, etc)
- What it MUST NOT be:
    - no syntaxic sugar: if somebody wants sugar it can build it on top of this API. Occam Razor principle.
    - no black magic: everything must be clear and explicit

