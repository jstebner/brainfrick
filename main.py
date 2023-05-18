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
            # FIXME: currently, all this does is mark start of loop, 
            #        so its basically a 'do{...}while(mem[mp]!=0);'
            #        instead of 'while(mem[mp]!=0){...}'
            #        which is not pog !
            loop_stack.append(ip)
            
            if mem[mp] == 0:
                # do something
                pass
            else:
                # do something else ?
                pass
            
        case ']': # end loop
            # FIXME: rmv 0 check here since its handled by start bracket ig
            ip = (lambda loop_idx: ip if mem[mp] == 0 else loop_idx - 1)(loop_stack.pop())
            
        case ',': # input character
            mem[ip] = ord(input()[0]) % 256
            
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
            open('./data/helloworld.bf', 'r').read()
            )
        )
    ip = 0
    
    loop_stack = list()
    
    while ip < len(instr):
        mem, mp, ip, loop_stack = parse_instr(instr, MEM_SIZE, mem, mp, ip, loop_stack)

if __name__ == '__main__':
    main()