from schema_second_extension import Manifest, Canvas,  Annotation
from example_objects import example_manifest, example_canvas, example_annotation

m = Manifest(**example_manifest)
print("Manifest loaded through schema_second_extension.py")
print("-----")
print("Manifest class:", m.__class__)
print("Manifest ID:", m.id)
print("Extension property:", m.extraManifestProperty)
print("Second extension:", m.secondExtensionProperty)
print()

c = Canvas(**example_canvas)
print("Canvas loaded from schema_extension.py chained through schema_second_extension.py")
print("-----")
print("Canvas class:", c.__class__)
print("Canvas extension:", c.extraCanvasProperty)
print()

a = Annotation(**example_annotation)
print("Annotation loaded from prezi3_schema.py chained through schema_second_extension.py and schema_extension.py")
print("-----")
print("Annotation class:", a.__class__)
print("Annotation ID:", a.id)