# weblogic_server_config_decoder

this code is to extract server related configuration information from the config.xml of weblogic. In between the server tags of the file

`<server>
.....
.....
....
....
</server>`


# what versions of weblogic does it work ?

Tested with 9 and 10.3 (11g). should also work in 12c

# how to execute it.

Execute the script with two startup arguments.

1) Fully qualified location of your config.xml file
2) Hostname where this domain is running (In cases where there is not hostname mentioned within the config.xml. Provided hostname would be considered)

`` ./config_xml_extractor.py config.xml `hostname` ``

