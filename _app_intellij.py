#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it 
#   under the terms of the GNU Lesser General Public License as published 
#   by the Free Software Foundation, either version 3 of the License, or 
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but 
#   WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public 
#   License along with Dragonfly.  If not, see 
#   <http://www.gnu.org/licenses/>.
#

"""
    This module is a simple example of Dragonfly use.
    It shows how to use Dragonfly's Grammar, AppContext, and MappingRule
    classes.  This module can be activated in the same way as other
    Natlink macros by placing it in the "My Documents\Natlink folder" or
    "Program Files\NetLink/MacroSystem".
"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text, IntegerRef, Function, Config, Section, Item, RuleRef, Alternative, Repetition,
                       CompoundRule, Choice)

import lib.format

formatMap = {
    "camel case": lib.format.FormatTypes.camelCase,
    "pascal case": lib.format.FormatTypes.pascalCase,
    "snake case": lib.format.FormatTypes.snakeCase,
    "uppercase": lib.format.FormatTypes.upperCase,
    "lowercase": lib.format.FormatTypes.lowerCase,
    "squash": lib.format.FormatTypes.squash,
    "lowercase squash": [lib.format.FormatTypes.squash, lib.format.FormatTypes.lowerCase],
    "uppercase squash": [lib.format.FormatTypes.squash, lib.format.FormatTypes.upperCase],
    "squash lowercase": [lib.format.FormatTypes.squash, lib.format.FormatTypes.lowerCase],
    "squash uppercase": [lib.format.FormatTypes.squash, lib.format.FormatTypes.upperCase],
    "dashify": lib.format.FormatTypes.dashify,
    "lowercase dashify": [lib.format.FormatTypes.dashify, lib.format.FormatTypes.lowerCase],
    "uppercase dashify": [lib.format.FormatTypes.dashify, lib.format.FormatTypes.upperCase],
    "dashify lowercase": [lib.format.FormatTypes.dashify, lib.format.FormatTypes.lowerCase],
    "dashify uppercase": [lib.format.FormatTypes.dashify, lib.format.FormatTypes.upperCase],
    "dotify": lib.format.FormatTypes.dotify,
    "lowercase dotify": [lib.format.FormatTypes.dotify, lib.format.FormatTypes.lowerCase],
    "uppercase dotify": [lib.format.FormatTypes.dotify, lib.format.FormatTypes.upperCase],
    "dotify lowercase": [lib.format.FormatTypes.dotify, lib.format.FormatTypes.lowerCase],
    "dotify uppercase": [lib.format.FormatTypes.dotify, lib.format.FormatTypes.upperCase],
    "say": lib.format.FormatTypes.spokenForm,
    "environment variable": [lib.format.FormatTypes.snakeCase, lib.format.FormatTypes.upperCase],
}

grammarCfg = Config("Intellij Typescript edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # navigation
        # next/prev brace
        # next/prev matching selection
        "down [<n>]": Key("down:%(n)d"),
        "down block": Key("c-rbracket"),
        "down method [<n>]": Key("a-down:%(n)d"),
        "down page [<n>]": Key("pgdown:%(n)d"),

        "doc end": Key("c-end"),
        "doc start": Key("c-home"),

        "go to column <n>": Key("c-g/25") + Text(":%(n)d") + Key("enter"),
        "go to declaration": Key("c-b"),
        "go to implemetation": Key("sc-b"),
        "go to line <n>": Key("c-g/25") + Text("%(n)d") + Key("enter"),
        "go to line <n> column <m>": Key("c-g/25") + Text("%(n)d:%(m)d") + Key("enter"),

        "left [<n>]": Key("left:%(n)d"),
        "left <n> (word|words)": Key("c-left:%(n)d"),

        "line end": Key("end"),
        "line start": Key("home"),

        "matching brace": Key("cs-m"),

        "next error": Key("f2"),
        "next position": Key("ca-right"),
        "previous error": Key("s-f2"),
        "previous position": Key("ca-left"),

        "right [<n>]": Key("right:%(n)d"),
        "right word [<n>]": Key("c-right:%(n)d"),

        "up [<n>]": Key("up:%(n)d"),
        "up block": Key("c-lbracket"),
        "up method [<n>]": Key("a-up:%(n)d"),
        "up page [<n>]": Key("pgup:%(n)d"),
        "up word [<n>]": Key("c-left:%(n)d"),

        # Searching
        "find in file": Key("c-f"),
        "find in path": Key("cs-f"),
        "find usage": Key("a-f7"),
        "find next": Key("f3"),
        "find previous": Key("s-f3"),
        "find word": Key("c-f3"),

        "replace in file": Key("c-r"),
        "replace in pat": Key("sc-r"),
        "select word <n>": Key("c-w:%(n)d"),

        # function keys
        "F one": Key("f1"),
        "F two": Key("f2"),
        "F three": Key("f3"),
        "F four": Key("f4"),
        "F five": Key("f5"),
        "F six": Key("f6"),
        "F Seven": Key("f7"),
        "F eight": Key("f8"),
        "F nine": Key("f9"),
        "F ten": Key("f10"),
        "F eleven": Key("f11"),
        "F 12": Key("f12"),

        # letters
        "(A|alpha)": Text("a"),
        "(B|bravo) ": Text("b"),
        "(C|charlie) ": Text("c"),
        "(D|delta) ": Text("d"),
        "(E|echo) ": Text("e"),
        "(F|foxtrot) ": Text("f"),
        "(G|golf) ": Text("g"),
        "(H|hotel) ": Text("h"),
        "(I|india|indigo) ": Text("i"),
        "(J|juliet) ": Text("j"),
        "(K|kilo) ": Text("k"),
        "(L|lima) ": Text("l"),
        "(M|mike) ": Text("m"),
        "(N|november) ": Text("n"),
        "(O|oscar) ": Text("o"),
        "(P|papa|poppa) ": Text("p"),
        "(Q|quebec|quiche) ": Text("q"),
        "(R|romeo) ": Text("r"),
        "(S|sierra) ": Text("s"),
        "(T|tango) ": Text("t"),
        "(U|uniform) ": Text("u"),
        "(V|victor) ": Text("v"),
        "(W|whiskey) ": Text("w"),
        "(X|x-ray) ": Text("x"),
        "(Y|yankee) ": Text("y"),
        "(Z|zulu) ": Text("z"),

        # Typescript keywords, defined as commands so case etc is correct
        "abstract": Text("abstract "),
        "as": Text("as "),
        "async": Text("async "),
        "await": Text("await "),
        "break": Text("break") + Key("enter"),
        "case": Text("case :") + Key("left"),
        "catch": Text("catch(err) {") + Key("enter"),
        "class <text>": Text("class ") + Function(lib.format.pascal_case_text) + Text(" {") + Key("enter"),
        "const <text>": Text("const ") + Function(lib.format.camel_case_text),
        "constructor": Text("constructor () {") + Key("left:3"),
        "continue": Text("continue") + Key("enter"),
        "declare": Text("declare "),
        "default": Text("default "),
        "delete <text>": Text("delete ") + Function(lib.format.camel_case_text),
        "do": Text("do "),
        "else": Text(" else {") + Key("enter"),
        "enum <text>": Text("enum ") + Function(lib.format.pascal_case_text) + Text(" {") + Key("enter"),
        "export": Text("export "),
        "extends <text>": Text("extends ") + Function(lib.format.pascal_case_text),
        "false": Text("false"),
        "finally": Text("finally {") + Key("enter"),
        "for of <text>": Text("for (const elem of ") + Function(lib.format.pascal_case_text) + Text("){"),
        "for in <text>": Text("for (const key of ") + Function(lib.format.pascal_case_text) + Text("){"),
        "function <text>": Text("function ") + Function(lib.format.pascal_case_text) + Text("() {") + Key("enter") + Key("cs-m") + Key("left:2"),
        "from": Text("from ''") + Key("left"),
        "get <text>": Text("get ") + Function(lib.format.camel_case_text) + Text("() {") + Key("enter") + Text("return "),
        "if": Text("if () {") + Key("enter") + Key("cs-m") + Key("left"),
        "implements <text>": Text("implements ") + Function(lib.format.pascal_case_text),
        "import": Text("import "),
        "in": Text("in "),
        "interface <text>": Text("interface ") + Function(lib.format.pascal_case_text) + Text(" {") + Key("enter"),
        "instance of": Text("instanceof "),
        "let <text>": Text("let ") + Function(lib.format.camel_case_text),
        "new": Text("new "),
        "null": Text("null "),
        "package": Text("package "),
        "private <text>": Text("private ") + Function(lib.format.camel_case_text),
        "protected": Text("protected "),
        "public": Text("public "),
        "read only": Text("readonly "),
        "return": Text("return "),
        "set <text>": Text("set ") + Function(lib.format.camel_case_text) + Text("() {") + Key("enter") + Key("cs-m") + Key("left:2"),
        "static": Text("static "),
        "super": Text("super("),
        "switch": Text("switch () {") + Key("enter") + Text("case :") + Key("enter") + Text("break") + Key("cs-m") + Key("left:2"),
        "this": Text("this"),
        "true": Text("true"),
        "try": Text("try {") + Key("enter") + Key("down:2") + Text("catch (err) {") + Key("enter") + Key("cs-m") + Key("up"),
        "type": Text("type "),
        "type of": Text("typeof"),
        "undefined": Text("undefined"),
        "void": Text("void"),
        "while": Text("while () {") + Key("enter") + Key("cs-m") + Key("left:2"),

        # common  methods
        "log": Text("console.log(\""),

        # common types
        "any": Text("any"),
        "boolean": Text("boolean"),
        "map": Text("Map"),
        "number": Text("number"),
        "new map": Text("Map<>(") + Key("left:2"),
        "string": Text("string"),

        # symbols, puncuation etc
        "bar": Text(" | "),
        "equal to": Text(" === "),
        "equals": Text(" = "),
        "greater than": Text(" > "),
        "greater than or equal 2": Text(" >= "),
        "less than": Text(" < "),
        "less than or equal 2": Text(" <= "),
        "not equal to": Text(" !== "),
        "angle bracket": Key("langle"),
        "close angle bracket": Key("rangle"),
        "square bracket": Text("["),
        "close square bracket": Text("]"),
        "brace": Key("lbrace"),
        "close brace": Key("rbrace"),
        "paren": Key("lparen"),
        "close paren": Key("rparen"),
        "quote": Key("dquote"),
        "single quote": Key("squote"),
        "colon [<n>]": Key("colon:%(n)d"),
        "semi-colon [<n>]": Key("semicolon:%(n)d"),
        "comma [<n>]": Key("comma:%(n)d"),
        "dot [<n>]": Key("dot:%(n)d"),
        "(dash|hyphen|minus) [<n>]": Key("hyphen:%(n)d"),
        "underscore [<n>]": Key("underscore:%(n)d"),
        "plus": Text(" + "),
        "bang": Text("!"),
        "at": Text("@"),

        # Formatting <n> words to the left of the cursor.
        "camel case <n>": Function(lib.format.camel_case_count),
        "camel case <text>": Function(lib.format.camel_case_text),
        "pascal case <n>": Function(lib.format.pascal_case_count),
        "pascal case <text>": Function(lib.format.pascal_case_text),
        "snake case <n>": Function(lib.format.snake_case_count),
        "snake case <text>": Function(lib.format.snake_case_text),
        "squash <n>": Function(lib.format.squash_count),
        "expand <n>": Function(lib.format.expand_count),
        "uppercase <n>": Function(lib.format.uppercase_count),
        "uppercase <text>": Function(lib.format.uppercase_text),
        "lowercase <n>": Function(lib.format.lowercase_count),
        "lowercase <text>": Function(lib.format.lowercase_text),
        # Format dictated words. See the formatMap for all available types.
        # Ex: "camel case my new variable" -> "myNewVariable"
        # Ex: "snake case my new variable" -> "my_new_variable"
        # Ex: "uppercase squash my new hyphen variable" -> "MYNEW-VARIABLE"
        # "<formatType> <text>": Function(lib.format.format_text),

        # editing
        # For writing words that would otherwise be characters or commands.
        # Ex: "period", tab", "left", "right", "home", select word
        "cut": Key("c-x"),
        "dictate <text>": Text("%(text)s"),
        "duplicate line": Key("c-d"),
        "escape": Key("escape"),
        "format": Key("csa-p"),
        "paste": Key("c-v"),
        "save": Key("c-s"),
        "undo": Key("c-z"),
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)
#
class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 1000),
        IntegerRef("m", 1, 1000),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {
        "n": 1,
    }

alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
single_action = Alternative(alternatives)

sequence = Repetition(single_action, min=1, max=8, name="sequence")


class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = "<sequence> [[[and] repeat [that]] <n> times]"
    extras = [
        sequence,  # Sequence of actions defined above.
        IntegerRef("n", 1, 1000),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
    }

    def _process_recognition(self, node, extras):  # @UnusedVariable
        sequence = extras["sequence"]  # A sequence of actions.
        count = extras["n"]  # An integer repeat count.
        for i in range(count):  # @UnusedVariable
            for action in sequence:
                action.execute()

grammar = Grammar("IntelliJ Typescript edit", context=AppContext(executable="idea64"))
grammar.add_rule(RepeatRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.


# ---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

# grammar_context = AppContext(executable="idea64")
# grammar = Grammar("idea", context=grammar_context)

# ---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

# idea_rule = MappingRule(
#     name="IntelliJ",  # The name of the rule.
#     mapping={  # The mapping dict: spec -> action.
#         # file
#         "save [file]": Key("c-s"),
#
#         # navigation
#         "go to column <n>": Key("c-g/25") + Text(":%(n)d") + Key("enter"),
#         "go to line <n>": Key("c-g/25") + Text("%(n)d") + Key("enter"),
#         "go to line <n> column <m>": Key("c-g/25") + Text("%(n)d:%(m)d") + Key("enter"),
#
#         # code
#         "brace": Text("{"),
#         "class <text>": Text("class ") + Function(lib.format.FormatTypes.pascal_case_text) + Text(" {") + Key("enter"),
#         "const <text>": Text("const ") + Function(lib.format.FormatTypes.camel_case_text),
#         "enum <text>": Text("enum ") + Function(lib.format.FormatTypes.pascal_case_text) + Text(" {") + Key("enter"),
#         "export": Text("export "),
#         "from": Text("from ''") + Key("left"),
#         "import": Text("import "),
#         "paren": Text("("),
#         "read only": Text("readonly "),
#
#         # editing
#         # For writing words that would otherwise be characters or commands.
#         # Ex: "period", tab", "left", "right", "home".
#         "undo": Key("c-z"),
#     },
#     extras=[  # Special elements in the specs of the mapping.
#         Dictation("text"),
#         IntegerRef("m", 1, 50000),
#         IntegerRef("n", 1, 50000),
#     ],
# )

# Add the action rule to the grammar instance.
# grammar.add_rule(idea_rule)

# ---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

# grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
