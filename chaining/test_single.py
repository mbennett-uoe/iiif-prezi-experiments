# Single Extension Example
# Manifest is subclassed in schema_extension
# Annotation is imported from prezi3_schema via the `import *` statement in schema_extension
from schema_extension import Manifest, Annotation
from example_objects import example_manifest, example_annotation

m = Manifest(**example_manifest)
print("Manifest loaded through schema_extension.py")
print("-----")
print("Manifest class:", m.__class__)
print("Manifest ID:", m.id)
print("Extension property:", m.extraManifestProperty)
print()
print()

a = Annotation(**example_annotation)
print("Annotation loaded from prezi3_schema.py chained through schema_extension.py")
print("-----")
print("Annotation class: ", a.__class__)