# Monkeypatching the schema

## Overview
* Extensions _don't_ subclass the main schema, but are standalone
* Monkeypatching is used to dynamically modify the schema to subclass from extension objects

### Pros
* No modification of generated schema required - all changes are made at runtime
* Multiple helper classes / model extensions can exist independently of one another
* Classes instantiated indirectly (i.e by parent model) correctly use the extended classes

### Cons
* Extensions don't know in advance which classes they will be attached to, so don't have write-time introspection of parent
class properties when used in IDEs
* There might be clashes with multiple extensions adding the same properties (although this would happen with write-time multi-inheritance too)
* Need to ensure the monkeypatching code is run - see further discussion in the Demo section

## Demo
### `test_property.py`
Monkeypatches the `Manifest` and `Canvas` classes in `prezi3_helpers.py` and demonstrates that the patch applies both to directly and
indirectly instantiated objects, and is run by virtue of the `Manifest` class being chained through the `import *` approach