import volatility.plugins.taskmods as taskmods

p = taskmods.PSList(config)

for process in p.calculate():
  if str(process.ImageFileName) == "calc.exe":
    print "[*] Found calc.exe with PID %d" % process.UniqueProcessId
    print "[*] Hunting for physical offsets...please wait."
    address_space = process.get_process_address_space()
    pages = address_space.get_available_pages()
