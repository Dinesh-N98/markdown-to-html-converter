# 1. CodeHilite Extension Demo

To use code highlighting, you can specify the language after the opening backticks. The codehilite extension applies CSS classes to colorize the code.

```python
import os

def check_file(filename):
    if os.path.exists(filename):
        return f"{filename} exists!"
    return "File not found."
```

```javascript
const user = {
  name: "Alex",
  role: "Developer"
};
console.log(user.name);
```
