# Monkeypatched property test
# Canvas Extension is in monkey_property.py and is monkeypatched in there outside of the class definition
# The import of the CanvasExtension object causes the monkeypatching code to run, even though the imported object is not used in this file

from prezi3_schema import Manifest, Canvas
from monkey_property import CanvasExtension
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
print("Canvas property:", c.extraCanvasProperty)
