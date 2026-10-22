"""Give your companion pictures (README Step 6): edit her fixed reference
image with Wavespeed Qwen, optionally applying a style LoRA.

Usage:
    export WAVESPEED_API_KEY=...
    python examples/image_edit.py ./assets/her.png "her in a summer dress, soft light"
"""

import os
import sys

from xfriend.modules.wavespeed import WavespeedImage

base = sys.argv[1] if len(sys.argv) > 1 else "./assets/her.png"
prompt = sys.argv[2] if len(sys.argv) > 2 else "her wearing a glowing crown"

image = WavespeedImage(
    api_key=os.environ.get("WAVESPEED_API_KEY"),
    base_image=base,
)
result = image.generate(prompt=prompt, images=[base])
print("outputs:", result.outputs)