# Reverse subclass example
# Extensions from schema_extension_reversed are subclassed onto the appropriate models in prezi3_extended_schema
# Extended attributes are available in objects instantiated directly _and_ indirectly

from prezi3_extended_schema import Manifest, Canvas
from example_objects import example_manifest, example_canvas

c = Canvas(**example_canvas)
print("Canvas instantiated directly")
print("-----")
print("Canvas class:", c.__class__)
print("Extension property:", c.extraCanvasProperty)
print("-----")
print()

m = Manifest(**example_manifest)
c = m.items[0]
print("Canvas instantiated as part of a manifest")
print("-----")
print("Manifest class:", m.__class__)
print("Canvas class:", c.__class__)
print("Extension property:", c.extraCanvasProperty)
