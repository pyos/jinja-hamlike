## hamlike

A minimalistic indentation-sensitive markup preprocessor for
[Jinja2](http://jinja.pocoo.org/docs/).

### Usage

#### With Jinja2

```python
from hamlike import HamlikeExtension

environment.add_extension(HamlikeExtension)
```

where `environment` is an [Environment](http://jinja.pocoo.org/docs/api/#high-level-api) instance
(e.g. `jinja_env` attribute of [Flask](http://flask.pocoo.org/docs/api/#application-object) objects.)

After you do that, any file with the `.hamlike` extension will automatically
get preprocessed!

#### Stand-alone

```python
from hamlike import Hamlike

h = Hamlike('%h1 -> Hello, World!', 'filename')
print(h.block.data)
```

#### CLI

```sh
python -m dg -m hamlike < input_file > output_file
```

### Syntax

```
// Lines that start with `//` are comments.
// Tags are created with `%`.
%!doctype html
%html
  // Their contents are indentation-sensitive.
  %head
    // Tags use standard HTML syntax for attributes.
    %meta charset="utf-8"
    // Everything until the end of the line OR the next `->` is an attribute.
    // An arrow is equivalent to a line break and a 2-space indent.
    %title -> A simple page
    // `-` starts a Jinja control statement;
    // `=` is a Jinja expression.
    -block styles
      -set style = "normal.css"
      // You can use standard Jinja syntax in tags and content, too.
      %link rel="stylesheet" href="/css/{{ style }}"
  %body
    // Control statements are also indentation-sensitive.
    -if 1 > 0
      -set greeting = "Hello, World!"
    -else
      -set greeting = "Oh crap."
    %h1 -> =greeting
    // If you want a literal line starting with any of the special
    // characters, prefix it with `\`.
    \- is a literal dash.
    \\ this applies to <code>\</code> itself, too.
    // Oh, and inline HTML is allowed, too.
    %footer class="text-muted"
      That's all!
```
