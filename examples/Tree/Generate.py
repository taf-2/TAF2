import Taf

myTaf = Taf.CLI()

# myTaf.do_display("all")
# myTaf.help_parse_template()
myTaf.auto=True
myTaf.do_overwrite()
myTaf.do_parse_template()
myTaf.do_generate()


