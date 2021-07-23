# Multiple Extension Example
# Manifest is subclassed in schema_extension _and again_ in schema_second_extension
# Canvas is subclassed _only_ schema_extension and imported via the `import *` in schema_second_extension
# Annotation is imported from prezi3_schema via the `import *` statements in schema_extension and then schema_second_extension
from schema_second_extension import Manifest, Canvas,  Annotation
from example_objects import example_manifest, example_canvas, example_annotation

m = Manifest(**example_manifest)
print("Manifest loaded through schema_second_extension.py")
print("-----")
print("Manifest class:", m.__class__)
print("Extension property:", m.extraManifestProperty)
print("Second extension property:", m.secondExtensionProperty)
print("-----")
print()

c = Canvas(**example_canvas)
print("Canvas loaded from schema_extension.py chained through schema_second_extension.py")
print("-----")
print("Canvas class:", c.__class__)
print("Extension property:", c.extraCanvasProperty)
print("-----")
print()

a = Annotation(**example_annotation)
print("Annotation loaded from prezi3_schema.py chained through schema_extension.py and then schema_second_extension.py")
print("-----")
print("Annotation class:", a.__class__)