## IIIF Prezi experiments

Some different approaches to adding extra properties and functions to classes after the JSON schema has been through Pydantic

### Chaining
First approach - subclassing schema objects and using a mixture of those and objects from the schema.

Doesn't allow for child objects to access the extensions and a bit fiddly for multiple extensions.
Probably not worth pursuing.

### Subclass schema
Second approach - adding extra classes to the objects in the schema file after generation.

Allows for child object access, and multiple extensions, but requires editing schema file.
Worth pursuing if we decide monkeypatching is too risky.

### Monkeypatching
Third approach - monkeypatch the extension properties into the schema at runtime

Allows for child object access, and multiple extensions, with no editing of the schema file. Some downsides which are
discussed further in the README file in the directory.

### Monkeypatching with Chaining
Third approach, take two - using a dedicated helpers class to effectively "force" the monkeypatching to happen

This is probably the most useful / functional approach, but still has some drawbacks re: introspection, code risk etc