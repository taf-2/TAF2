import sys
sys.path.append('../../src')
import Taf
import time

start = time.time()

myTaf = Taf.CLI()

myTaf.do_display("all")
myTaf.help_parse_template()
myTaf.do_parse_template(None)
myTaf.do_generate(None)

end = time.time()
with open("time", "a") as f:
	f.write(str(end-start) + "\n")
	print("time: " + str(end-start))