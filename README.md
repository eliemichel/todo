    Welcome to TODO!

TODO is a simple utility to store ideas on the fly.


Basic usage
-----------

Just type `todo add "A wonderful idea"` and todo will remember your idea!
Todo ideas are stored in a `.todo` file in your home. This file has a really
simple format since each single line is an idea, its index and its tags, like so:

    index: tag1,tag2: A wonderful idea

You can directly edit this file, there's no problem with that. But if two lines
have the same index, the behavior is undefined.

To list existing ideas, call `todo list`, or even `todo ls`. If you want to see
ideas with a specific tag, say 'foo', type `todo list foo`.

To specify status when adding a new idea, type
`todo add "A new idea" status1 status2`.

You can `todo update 42 "Changed idea"` to change the idea at index 42.
After `update`, you can either give an index or a part of an idea. In the
latter case, you will be prompted if some abiguity is spotted.

You can also `todo tag add 42 foo` to add tag `foo` to idea at index 42. Once
again, it is possible to replace the index by an idea message.

Finally, you can `todo rm 42`, or `todo tag rm 42 foo` to remove respectively
ideas or tags.

Restrictions on tag names:

 * The following tags are PROHIBITED: `and`, `or`.
 * The following characters CAN NOT be used in tag names: `:`, `,`, `!`, `(`, `)`.
 * Tags beginning with an underscore (`_`) are system tags. Some of them may
   be used by internal mechanisms so read the documentation carefully before
   using them.


Advanced usage
--------------

If you want to store project related ideas, you can add a `.todo` file at your
project root. Then, when calling TODO from a subdirectory of your project,
ideas will be append to that file instead of the `.todo` from your home.

It is actually recommanded to use `todo init` instead of manually adding the
`.todo` file since the mechanism of TODO may change one day but not its syntaxe
(or at least in a major version).

When TODO deal with such a `.todo` file, it add a line to the main `.todo` file
(in your home) taged with `_subtodo` with the absolute path to that file.
Actually the path can even specify a remote host (ssh-style, e.g.
`me@mymachine:/path/to/my/.todo`) but you must add it manually.

If the `.todo` file is not found (because it has been moved or deleted), this
line is simply dropped from the file.

You can use advanced views with `todo list`. Instead of specifying a simple tag
name to filter results, you can give a boolean expression according to the
following grammar:

    expr ::= tagname | (expr) | !expr | expr and expr | expr or expr

The semantic is what you can expect it is: If the expression is reduced to a
single tag name, the expression is true if and only if the idea has the given
tag. In other cases, this is a usual boolean expression, where `!` denotes the
logical negation. Note that `or` is applyed before `and`.


Full documentation
------------------

[[TODO]]

add force id

