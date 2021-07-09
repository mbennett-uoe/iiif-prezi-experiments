from schema_extension import Manifest, Canvas
from example_objects import example_manifest, example_canvas

c = Canvas(**example_canvas)
print("Canvas instantiated directly from class imported via schema_extension.py")
print("-----")
print("Canvas class:", c.__class__)
print("Canvas ID:", c.id)
print("Canvas property:", c.extraCanvasProperty)
print()

m = Manifest(**example_manifest)
c = m.items[0]
print("Canvas instantiated as part of a manifest - this will error")
print("-----")
print("Manifest class:", m.__class__)
print("Canvas class:", c.__class__)
print("Canvas ID:", c.id)
print("Canvas property:", c.extraCanvasProperty)
