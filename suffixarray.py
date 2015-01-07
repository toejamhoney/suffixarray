import sys
from array import array
from collections import OrderedDict


l_type = -1
s_type = 1


def define_types_ptrs(string, types, lms_ptrs, buckets):
    types[-1] = s_type
    for idx in range(len(string)-2, -1, -1):
        if string[idx] < string[idx + 1] or \
                (string[idx] == string[idx + 1] and types[idx + 1] is s_type):
            # S type
            types[idx] = s_type
        elif string[idx] > string[idx + 1] or \
                (string[idx] == string[idx + 1] and types[idx + 1] is l_type):
            # L type
            types[idx] = l_type
            if types[idx + 1] is s_type:
                # LMS Character at idx + 1
                lms_ptrs.append(idx + 1)

        buckets[string[idx]] += 1

    for ch in string:
        print chr(ch),
    print

    for t in types:
        if t is l_type:
            print "L",
        if t is s_type:
            print "S",
    print 

    lastidx = 0
    for ptr in reversed(ptrs):
        sys.stdout.write("%s* " % ('  ' * (ptr - lastidx)))
        lastidx = ptr + 1
    print 


def sais_step1(string, types, ptrs, sa):
    for lms_char in ptrs: 
        sa[string[lms_char]]['pre'].append(lms_char)
    
    print "Step 1:"
    for bucket in sa.keys():
        if bucket > 0:
            print chr(bucket),
        else:
            print '$',
    print

    for bucket in sa.values():
        print '{',bucket['suf'], bucket['pre'],'}',
    print


def sais_step2(string, types, ptrs, sa):
    for bucket in sa.values():
        for idx in bucket['suf']:
            if types[idx-1] is l_type:
                sa[string[idx - 1]]['suf'].append(idx - 1)
        for idx in bucket['pre']:
            if types[idx-1] is l_type:
                sa[string[idx - 1]]['suf'].append(idx - 1)

    for bucket in sa.values():
        print '{',bucket['suf'], bucket['pre'],'}',
    print


def sais_step3(string, types, ptrs, sa):
    tail_ptrs = dict(zip(sa.keys(), [-1 for i in range(len(sa))]))
    
    for bucket in sa.items():
        pre_len = 
    
    for key, bucket in reversed(sa.items()):

        for idx in reversed(bucket['pre']):
            print idx
            if types[idx - 1] is s_type:
                tail = tail_ptrs.get(string[idx - 1])
                print sa[string[idx - 1]]['pre']
                try:
                    sa[string[idx - 1]]['pre'][tail] =  idx - 1
                    tail -= 1
                except IndexError:
                    sa[string[idx - 1]]['pre'].insert(0, idx - 1)
                    tail -= 1
                print sa[string[idx - 1]]['pre']
                tail_ptrs[string[idx-1]] = tail

        for idx in reversed(bucket['suf']):
            print idx,
            if types[idx - 1] is s_type:
                tail = tail_ptrs.get(string[idx - 1])
                print sa[string[idx - 1]]['pre']
                try:
                    sa[string[idx - 1]]['pre'][tail] =  idx - 1
                    tail -= 1
                except IndexError:
                    sa[string[idx - 1]]['pre'].insert(0, idx - 1)
                    tail -= 1
                print sa[string[idx - 1]]['pre']
                tail_ptrs[string[idx-1]] = tail


    for bucket in sa.values():
        print '{',bucket['suf'], bucket['pre'],'}',
    print


def sais(byte_str, sa):
    """
    (t)ypes: array [0...n-1] bool
    S1: array [0...n1-1] int
    (P1)ptrs: array [0...n1-1] int
    (b)uckets: array [0...||sigma(s)||-1] int
    """
    ptrs = []
    types = array('b', [0] * len(byte_str))
    buckets = array('i', [0] * 255)

    define_types_ptrs(byte_str, types, ptrs)

    sais_step1(byte_str, types, ptrs, sa)
    sais_step2(byte_str, types, ptrs, sa)
    sais_step3(byte_str, types, ptrs, sa)

def construct_sa(byte_str):
    sa = array('i', [-1] * (len(byte_str) + 1))
    sais(byte_str += chr(0), sa)
    return []

def main(byte_str):
    suff_arr = construct_sa(byte_str)
    for str_idx in suff_arr:
        print byte_str[str_idx:]

if __name__ == "__main__":
    try:
        argv_str = bytearray(sys.argv[1])
    except IndexError:
        sys.exit(1)
    else:
        main(argv_str)

