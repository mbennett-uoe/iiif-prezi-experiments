# Monkeypatching the schema - now with added chaining!

## Overview
* Extensions _don't_ subclass the main schema, but are standalone
* Monkeypatching is used to dynamically modify the schema to subclass from extension objects
* One dedicated "helpers" class that also imports the schema, allowing the client to chain import schema objects

### Pros
* No modification of generated schema required - all changes are made at runtime
* Dedicated helper class means 99% of the time, we can guarantee that the monkeypatching code will run

### Cons
* If client imports directly from the schema instead of through the helpers class, the monkeypatching code is not run

## Demo
### `test_helpers.py`
Monkeypatches the `Canvas` class in `monkey_property.py` and demonstrates that the patch applies both to directly and
indirectly instantiated objects.
#### Further notes
In order for the monkeypatch code to run, the file containing it must be included in the client class. This is currently
accomplished simply by importing the `CanvasExtension` object, without actually using it. Because the monkeypatch code is
outside of the class, python runs it when _anything_ from the file is imported elsewhere.

The inherent danger of this approach is that some IDEs or linters may remove the import as "unused", which would obviously
prevent the monkeypatching from happening. There are a couple of potential approaches:
1) Leave the code as is and push the responsibility for maintaining the import to the client
2) Wrap the monkeypatch code in a function, then require the client to import and run that:
   
   ```python
   from prezi3_schema import Manifest
   from monkey_property import patch_classes   
   
   patch_classes()
   m = Manifest(**manifest_data)
   ```
3) Basically the same as #1 but chain the schema objects so that the client can import things it will actually use, and 
still trigger the monkeypatching, dodging the "unused import" issue. This approach can be seen in the `monkeypatching-with-chaining` folder