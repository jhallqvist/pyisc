# TODO

## DHCPD

* [ ] Make match and spawn classes. The main philosophy behind this rebuild is after all - everything that is not a clear key/value parameter should be a seperate object.
* [ ] Complete Mixin Classes
* [ ] Detach sorting function from the to_isc in Global class and allow it as a parameter for all to_isc methods. That way users can supply their own sorting if they wish. Sorting order should be: Parameters, Options, Includes, Keys, Zones, Failover, Subnets, Shared Networks, Classes, Subclasses, Hosts and Groups.
* [ ] Remodel build_tree to take a object as the first node (currently Global). That way one could possibly resuse it for include statement parsing.
* [ ] Save the line number for all scopes/declarations. Main reason or this is that it might be vital to preserve order of the scopes. At the very least it is in the case of include statements.
* [ ] Make a cleaner method of the build_tree method. Currently there is one big if/else statement and this could possbibly hurt readability. Also perhaps rename method to construct_object_tree or something similar for clarity.
* [ ] The Include node should contain a parsed tree of the included file and the ablity to write back to that specific file.
* [ ] Create new tests and remove the old ones.
* [ ] Possibility to reduce repeated code in parsing. For all declarations - create a switcher class where the functions add the correct object and also use getattr with a dict mapping to determine the method that must be used to add the object.
* [ ] Alternate idea is that instead of the Global object there is a DhcpdConf object that is initiated with the file given to it. That could be a simple way to keep track of the files involved.
