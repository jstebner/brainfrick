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
                loop_stack.append(ip)
            case ']': # end loop
                if mem[mp] != 0:
                    ip = loop_stack.pop() - 1
                else:
                    loop_stack.pop()
            case ',': # input character
                mem[ip] = ord(input()[0]) % 256
            case '.': # output character
                print(chr(mem[mp]), end='')
        
        ip += 1

if __name__ == '__main__':
    main()