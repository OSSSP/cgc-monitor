class SyscallNumbers():
    def __init__(self, params):
        self.syscalls = {}
        self.callnums = {}
        hackvals = {}
        fpath = params.unistd
        with open(fpath) as fh:
            for line in fh:
                if '__NR_' in line:
                    parts = line.split()
                    if parts[0] != '#define':
                        continue
                    nr = parts[1][5:]
                    try:
                        callnum = int(parts[2])
                        hackvals[parts[1]] = callnum
                    except:
                        #print('failed to handle %s' % line)
                        s = parts[2]
                        express = s[s.find("(")+1:s.find(")")]
                        sym, offset = express.split('+')
                        base = hackvals[sym]
                        callnum = base + int(offset)
                    self.syscalls[callnum] = nr
                    self.callnums[nr] = callnum
                     
