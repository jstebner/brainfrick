creates msg (backwards)
>++++++++[<+++++++>-]<[>+>+>+>+<<<<-]
+++++[>+>+>+<<<-]>+++++++>>>

creates pswd (backwards)
>>++++++++++[<++++++++++>-]<+++++++
[>>+>>+>>+>>+<<<<<<<<-]
>>---->>+++>>++++>>-

rolling msg check
[
    <,>[<->-]<  input chr; get diff
    [>+<[+]]+<  if nonzero; add 1 to r and flush l
]

sum flags
>[->[>>+<<-]>]>

replace msg w beep character if any flags procd
[[-]+[<[>-]>[-<+>]<]<[[-]<]>+++++++>]

move left til hit
+[<[>-]>[-<+>]<]

print and clear
<[.[-]<]