# Monkeypatched helpers test
# Helpers for Manifest and Canvas classes are in prezi3_helpers and are monkeypatched in there outside of the class definition
# The import of the Manifest object causes the monkeypatching code to run, even though this class comes from the schema

from prezi3_helpers import Manifest, Canvas
from example_objects import example_manifest, example_canvas

c = Canvas(**example_canvas)
print("Canvas instantiated directly")
print("-----")
print("Canvas class:", c.__class__)
print("Helper function:", c.helper_function())
print("-----")
print()

m = Manifest(**example_manifest)
c = m.items[0]
print("Canvas instantiated as part of a manifest")
print("-----")
print("Manifest class:", m.__class__)
print("Manifest helper:", m.widest_canvas())
print("Canvas class:", c.__class__)
print("Canvas helper:", c.helper_function())
