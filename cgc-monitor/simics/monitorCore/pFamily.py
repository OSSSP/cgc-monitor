from simics import *
import memUtils
from genMonitor import Prec
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

class Pfamily():
    def __init__(self, target, param, cell_config, mem_utils, task_utils, lgr):
        self.cell_config = cell_config
        self.target = target
        self.param = param
        self.mem_utils = mem_utils
        self.task_utils = task_utils
        self.prev_parent = None
        self.prev_tabs = ''
        self.lgr = lgr
        self.report_fh = None

    def getPfamily(self):
        retval = []
        cpu, comm, pid = self.task_utils.curProc()
        retval.append(Prec(cpu, comm, pid))
        tasks = self.task_utils.getTaskStructs()
        tabs = ''
        while pid != 0:
            parent_pid, parent_comm, parent_parent = self.parentInfo(pid, tasks)
            if parent_pid != 0:
                retval.append(Prec(cpu, parent_comm, parent_pid))
            pid = parent_pid
        return retval

    def parentInfo(self, pid, tasks):
        for t in tasks:
            if tasks[t].pid == pid:
                prec_addr = tasks[t].parent
                return tasks[prec_addr].pid, tasks[prec_addr].comm, tasks[prec_addr].parent

    def execveHap(self, hap_cpu, third, forth, memory):
        cpu = SIM_current_processor()
        if cpu != hap_cpu:
            self.lgr.debug('execveHap, wrong cpu %s %s' % (cpu.name, hap_cpu.name))
        cpu, comm, pid = self.task_utils.curProc() 
        prog_string, arg_string_list = self.task_utils.getProcArgsFromStack(pid, None, cpu)
        nargs = min(4, len(arg_string_list))
        arg_string = ''
        for i in range(nargs):
            if is_ascii(arg_string_list[i]):
                arg_string += arg_string_list[i]+' '
            else:
                break
        pfamily = self.getPfamily()
        dumb = pfamily.pop(0)
        flen = len(pfamily)
        if flen > 0:
            self.lgr.debug('flen is %d, parent_pid is %d  prev %s' % (flen, pfamily[0].pid, str(self.prev_parent)))
            if pfamily[0].pid != self.prev_parent:
                tabs = ''
                while len(pfamily) > 0:
                    prec = pfamily.pop()
                    self.report_fh.write('%s%5d  %s\n' % (tabs, prec.pid, prec.proc))
                    tabs += '\t'
                    self.prev_parent = prec.pid
                self.report_fh.write('%s%5d  %s %s\n' % (tabs, pid, prog_string, arg_string))
                self.prev_tabs = tabs
            else:
                self.report_fh.write('%s%5d  %s %s\n' % (self.prev_tabs, pid, prog_string, arg_string))
        else:
            self.report_fh.write('%s %s\n' % (prog_string, arg_string))
            self.prev_parent = None
            self.prev_tabs = ''
         
        #print('execve from %d (%s) prog_string %s' % (pid, comm, prog_string))
        #for arg in arg_string_list:
        #    print(arg)
         

    def traceExecve(self):
        cpu = self.cell_config.cpuFromCell(self.target)
        cell = self.cell_config.cell_context[self.target]
        self.lgr.debug('toExecve set break at 0x%x' % self.param.execve)
        proc_break = SIM_breakpoint(cell, Sim_Break_Linear, Sim_Access_Execute, self.param.execve, self.mem_utils.WORD_SIZE, 0)
        proc_hap = SIM_hap_add_callback_index("Core_Breakpoint_Memop", self.execveHap, cpu, proc_break)
        self.report_fh = open('/tmp/pfamily.txt', 'w')
