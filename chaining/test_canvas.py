# Different Canvas loading example
# Manifest is subclassed in schema_extension
# Canvas is subclassed in schema_extension
# When instantiated directly, the extended Canvas class is used and the extension property is available
# When instantiated by the Pydantic load, the original prezi3_schema class is used, and so errors if you try to access the extension property

from schema_extension import Manifest, Canvas
from example_objects import example_manifest, example_canvas

c = Canvas(**example_canvas)
print("Canvas instantiated directly from class imported via schema_extension.py")
print("-----")
print("Canvas class:", c.__class__)
print("Extension property:", c.extraCanvasProperty)
print("-----")
print()

m = Manifest(**example_manifest)
c = m.items[0]
print("Canvas instantiated by Pydantic as part of a manifest load - this will error")
print("-----")
print("Manifest class:", m.__class__)
print("Canvas class:", c.__class__)
print("Attempting to access extension property - error incoming...")
print()
print("Canvas property:", c.extraCanvasProperty)
