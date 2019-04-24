#! /usr/bin/env python3

import re

Name = "Katherine went to the concert to see her favorite band, Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend, Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friends, Kathrin and katharine."

line = Name.split()

for name in line:
    name = name.rstrip(".").rstrip(",").rstrip("s").rstrip("")
    if re.search("(ka|Ca.*(r.*))", name,re.I):
        print(name)


