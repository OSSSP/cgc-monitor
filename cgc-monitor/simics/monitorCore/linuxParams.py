'''
 * This software was created by United States Government employees
 * and may not be copyrighted.
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
'''

'''
Instead of simics-style .params file.  Hardcode limited number of offsets.
'''
class linuxParams():
    kernel_base = 3221225472
    ram_base = 0
    stack_size = 8192
    os32bit  = True
    #ts_next = 236
    ts_next = 196
    ts_prev = 200
    ts_comm = 504
    ts_pid = 256
    ts_parent = 272
    ts_real_parent = 268
    ts_state = None
    ts_active_mm = 228
    ts_mm = 224
    ts_binfmt = None
    ts_tgid = 260
    ts_group_leader = None
    ts_children_list_head = 276
    ts_sibling_list_head = 284
    ts_thread_group_list_head = 352
    ts_next_relative = True
    current_task = 0xc2001454
    # int80 vectors here
    sys_entry = 0xc10028a4
    # sysenter instruction vectors here
    sysenter = 0xc1002800
    # where the call jump table computation occurs
    syscall_compute = 0xc10028e9
    # if int80 is execve, we compute a call to here
    execve = 0xc1002a48
    # from symbol table
    # NOT GOOD execve = 0xc01019f0
    # page fault exception vectors here
    page_fault = 0xc12406e8
    # call edi goes to
    #page_fault = 0xc1241e2a
    # not symbol, instruct before ret to user; get emperically
    sys_exit = 0xc10028a2
    # kallsym
    do_exit = 0xc1028dd4

    # constant used in syscall jump table calculation
    syscall_jump = 0x3edb9f00

    unistd = '/mnt/ubuntu_img/linux-2.6.32/linux-2.6.32/arch/x86/include/asm/unistd_32.h'
    root_prefix = '/mnt/vdr_img/rootfs'


#['linux_tracker', {'version_string': 'Linux', 'ts_indirect': True, 'ts_next_relative': True, 'kernel_base': 3221225472, 'ram_base': 0, 'stack_size': 8192, 'os32bit': True, 'ts_offsets': {'mm': 264, 'active_mm': 268, 'parent': 328, 'sibling_list_head': 340, 'tgid': 320, 'group_leader': 348, 'pid': 316, 'next': 236, 'real_parent': 324, 'state': 0, 'children_list_head': 332, 'comm': 532, 'thread_group_list_head': 404, 'prev': 240}, 'tracker_version': 4582}]
