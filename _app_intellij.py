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
                       CompoundRule)

import lib.format

grammarCfg = Config("Intellij Typescript edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # navigation
        # next/prev brace
        # next/prev matching selection
        "down method <n>": Key("a-down:%(n)d"),
        "go to column <n>": Key("c-g/25") + Text(":%(n)d") + Key("enter"),
        "go to line <n>": Key("c-g/25") + Text("%(n)d") + Key("enter"),
        "go to line <n> column <m>": Key("c-g/25") + Text("%(n)d:%(m)d") + Key("enter"),
        "left word <n>": Key("c-left:%(n)d"),
        "right word <n>": Key("c-right:%(n)d"),
        "select word <n>": Key("c-w:%(n)d"),
        "up method <n>": Key("a-up:%(n)d"),

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
        "paren": Text("("),
        "private": Text("private "),
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

        # symbols
        # plus,minus,and dot etc

        # editing
        # For writing words that would otherwise be characters or commands.
        # Ex: "period", tab", "left", "right", "home", select word
        "dictate <text>": Text("%(text)s"),
        "escape": Key("escape"),
        "format": Key("csa-p"),
        "save": Key("c-s"),
        "undo": Key("c-z"),
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


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

sequence = Repetition(single_action, min=1, max=16, name="sequence")


class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = "<sequence> [[[and] repeat [that]] <n> times]"
    extras = [
        sequence,  # Sequence of actions defined above.
        IntegerRef("n", 1, 100),  # Times to repeat the sequence.
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
#         "class <text>": Text("class ") + Function(lib.format.pascal_case_text) + Text(" {") + Key("enter"),
#         "const <text>": Text("const ") + Function(lib.format.camel_case_text),
#         "enum <text>": Text("enum ") + Function(lib.format.pascal_case_text) + Text(" {") + Key("enter"),
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
