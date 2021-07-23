# Subclassing the schema (a.k.a the 'reverse' approach) 

## Overview
* Extensions _don't_ subclass the main schema
* Instead, the main Pydantic schema imports and subclasses the extensions against the appropriate classes
* Client imports models from the main schema as normal

### Pros
* Multiple helper classes / model extensions can exist independently of one another
* All changes are "in the code", so can be introspected by IDEs / linters etc
* Classes instantiated indirectly (i.e by parent model) use the extended classes

### Cons
* Requires modifying the main Pydantic schema - hampers ability to regenerate on demand
* Extensions don't know in advance which classes they will be attached to, so don't have write-time introspection of parent
class properties when used in IDEs

## Demo
### `test_reverse.py`
The `Manifest` and `Canvas` classes in `prezi3_extended_schema.py` have been modified to subclass the extensions from
`schema_extesion_reverse.py`. These modified classes are then imported in the demo, and used to demonstrate that both
directly and indirectly instantiated instances on `Canvas` have access to the extension's properties