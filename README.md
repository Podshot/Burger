# Burger
Burger is a "framework" for automatically extracting data
from the Minecraft game for the purpose of writing the protocol
specification, interoperability, and other neat uses.

## The Idea
Burger is made up of *toppings*, which can provide and satisfy
simple dependencies, and which can be run all-together or just
a few specifically. Each topping is then aggregated by
`munch.py` into the whole and output as a JSON dictionary.

## Usage
The simplest way to use Burger is to pass the `-d` or `--download`
flag, which will download the minecraft client for you.

    $ python munch.py --download

Alternatively, you can specify the client JAR by passing it as an argument.

    $ python munch.py 1.8.jar

You can redirect the output from the default `stdout` by passing
`-o <path>` or `--output <path>`.
    
    $ python munch.py -d --output output.json

You can see what toppings are available by passing `-l` or `--list`.

    $ python munch.py --list

You can also run specific toppings by passing a comma-delimited list
to `-t` or `--toppings`. If a topping cannot be used because it's
missing a dependency, it will output an error telling you what 
also needs to be included.  Toppings will generally automatically load
their dependencies, however.

    $ python munch.py -d --toppings language,stats

The above example would only extract the language information, as
well as the stats and achievements (both part of `stats`).
