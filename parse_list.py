#!/usr/bin/env python

def ip_prefix(addr):
    return addr[:addr.rfind('.', 0, addr.rfind('.'))]

def get_ips(line):
    if not line.strip(): return []
    name, numbers = line.split('\t')
    options = numbers.split(',')
    prefix = ip_prefix(options[0].strip())
    ips = [options[0].strip()]
    for addr in options[1:]:
        addr = addr.strip()
        if addr.count('.') == 1:
            ips.append(prefix + '.' + addr)
        else:
            ips.append(addr.strip())
            prefix = ip_prefix(addr)
    return ips

def add(a, b): return a + b

def all_ips(lines):
    return list(set(x for x in reduce(add, map(get_ips, lines)) if x))

if __name__ == '__main__':
    print ' '.join(all_ips(open('list.txt').read().split('\n')))

# vim: et sw=4 sts=4
