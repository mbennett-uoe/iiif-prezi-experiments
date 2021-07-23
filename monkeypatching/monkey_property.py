from prezi3_schema import Canvas

class CanvasExtension:
    extraCanvasProperty = "New Canvas Property added in monkey_property.py"


print("Monkeypatching in monkey_property.py triggered")
print("-----")
print("Canvas class bases before monkeypatch:", Canvas.__bases__)
canvas_bases = list(Canvas.__bases__)
canvas_bases.append(CanvasExtension)
Canvas.__bases__ = tuple(canvas_bases)
print("Canvas class bases after monkeypatch:", Canvas.__bases__)
print("-----")
print()
