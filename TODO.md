# TODO

## DHCPD

* [ ] Make match and spawn classes. The main philosophy behind this rebuild is after all - everything thay is not a clear key/value parameter should be a seperate object.
* [ ] Complete Mixin Classes
* [ ] Remodel build_tree to take a object as the first node (currently Global). That way one could possibly resuse it for include statement parsing.
* [ ] Save the line number for all scopes/declarations. Main reason or this is that it might be vital to preserve order of the scopes. At the very least it is in the case of include statements.
* [ ] Make a cleaner method of the build_tree method. Currently there is one bif if/else statement and this could possbibly hurt readability. Also perhaps rename method to construct_object_tree or something similar for clarity.
* [ ] The Include node should contain a parsed tree of the included file and the ablity to write back to that specific file.
