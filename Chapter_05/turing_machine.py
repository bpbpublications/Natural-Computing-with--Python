def print_state(tm, tape, state):
    # Note: this function breaks for state symbols that are not 2 characters
    pretty_head = ''
    pretty_tape = ''
    length = len(tape[1])
    
    for i in range(length):
        if i == tape[0]: # If head is at this index
            pretty_head += ' V' # Print the head
            pretty_tape += ' ' + str(tape[1][i]) # Print the tape
        else:
            pretty_head += '  '
            pretty_tape += ' ' + str(tape[1][i])
    print ('    ' + pretty_head)
    print (state + ': ' + pretty_tape)
    print (' ')


def move_machine(tm, tape, state):
    print_state(tm, tape, state)  
    head_pos  = tape[0] # head_pos is the index of the head position
    head_sym  = tape[1][head_pos] # head_sym is the symbol being read by the head
    new_state = '00'
    new_tape  = tape
    key       = []
    
    try: 
        key = tm[state][head_sym]
        head_sym  = key[0] # head_sym is changed according to TM instructions
        new_state = key[1] # new_state is as well 
    except KeyError:
        head_sym  = 'HALT' # If the TM doesn't have a matching entry, start to HALT
        new_state = 'XX'
        
    if head_sym == 'HALT':
        print_state(tm, tape, new_state) # HALT: No recursion call
    elif head_sym == 'R':
        new_tape = ((head_pos + 1), tape[1]) # Move the head right
        move_machine(tm, new_tape, key[1]) # Recursion call
    elif head_sym == 'L':
        new_tape = ((head_pos - 1), tape[1]) # Move the head left
        move_machine(tm, new_tape, key[1]) # Recursion call
    else:
        new_tape[1][head_pos] = head_sym # Overwrites the symbol being read according to TM instructions
        move_machine(tm, new_tape, key[1]) # Recursion call

"""
tm1 = {'q1': {'1': ('b', 'q2'),
              '0': ('a', 'q2')},
       'q2': {'1': ('R', 'q1'),
              'b': ('R', 'q1')}
      }

in1 = (1,['#','a','a','a','a','b','#'])
in2 = (1,['#','a','a','a','a','a','a','a','#'])
in3 = (1,['#','a','#'])

move_machine(tm1, in3, 'q1')
"""
tm2 = {'q1': {'a': ('R', 'q1'),
              'b': ('R', 'q2')
             },
       'q2': {'a': ('R', 'q1'),
              'b': ('R', 'q3')
             },
       'q3': {'a': ('L', 'q4'),
              'b': ('R', 'q3'),
              '#': ('L', 'q4')
             },
       'q4': {'a': ('R', 'q1'),
              'b': ('a', 'q5'),
              '#': ('R', 'q1')
             },
       'q5': {'a': ('L', 'q4'),
             }
      }

in1 = (1, ['#','a','#'])
in2 = (1, ['#','b','#'])
in3 = (1, ['#','b','b','#'])
in4 = (1, ['#','b','b','b','b','b','#'])
in5 = (1, list('#aabbbababbb#'))
in6 = (1, list('#bbaaaaabbb#'))

move_machine(tm2, in3, 'q1')


