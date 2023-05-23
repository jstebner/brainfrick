
# EXAMPLE:
# s_src = '>++++>+>+>+[<]>[[>]<+[<]>-]'
#
# # parse out looped instrs to rec fella
# s_new = '>++++>+>+>+0>1'
# subrt = {
#   0: '<',
#   1: '2<+3>-',
#   2: '>',
#   3: '<'
# }
#
# # maybe cleanup redundant fellas
# # (this might also just be done during initial subrt creation)
# s_new = '>++++>+>+>+0>1'
# subrt = {
#   0: '<',
#   1: '2<+0>-',
#   2: '>'
# }

def main():
    pass


if __name__ == '__main__':
    import sys
    main()