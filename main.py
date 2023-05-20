def find_end(idx, instr):
    count = 1
    while idx < len(instr)-1:
        if instr[idx+1] == '[':
            count += 1
        if instr[idx+1] == ']':
            count -= 1
            
        if count == 0:
            return idx+1
        
        idx += 1

def parse_instr(instr, MEM_SIZE, mem, mp, ip, loop_stack):
    match instr[ip]:
        case '>': # inc mp
            mp = (mp + 1) % MEM_SIZE
            
        case '<': # dec mp
            mp = (mp - 1) % MEM_SIZE
            
        case '+': # inc curr mem
            mem[mp] = (mem[mp] + 1) % 256
            
        case '-': # dec curr mem
            mem[mp] = (mem[mp] - 1) % 256
            
        case '[': # start loop
            if mem[mp] == 0:
                ip = find_end(ip, instr)
            else:
                loop_stack.append(ip)
                
        case ']': # end loop
            ip = loop_stack.pop() - 1
            
        case ',': # input character
            mem[mp] = ord(input()[0]) % 256
            
        case '.': # output character
            print(chr(mem[mp]), end='')
            
    ip += 1
    return mem, mp, ip, loop_stack

def main():
    MEM_SIZE = 30_000
    mem = [0] * MEM_SIZE
    mp = 0
    
    instr = list(
        filter(
            lambda x: x in '><+-[],.', 
            # open('./data/helloworld.bf', 'r').read()
            # open('./data/0123.bf', 'r').read()
            open('./data/password.bf', 'r').read()
            # open('./data/cat.bf', 'r').read()
            )
        )
    ip = 0
    
    loop_stack = list()
    
    while ip < len(instr):
        mem, mp, ip, loop_stack = parse_instr(instr, MEM_SIZE, mem, mp, ip, loop_stack)

if __name__ == '__main__':
    main()