from .buffer import Buffer
from ..transforms.transform_chain import TransformChain


TransBuf = Buffer | TransformChain
