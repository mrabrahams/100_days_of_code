# list of states by order they joined the union
states_in_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland',
                     'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island',
                     'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois',
                     'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin',
                     'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado',
                     'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma',
                     'New Mexico', 'Arizona', 'Alaska', 'Hawaii']


# print the states and their order of joining the union
def print_states(states):
    i = 1
    for state in states:
        print(f'{state} was the {i} state to join the union')
        i += 1
    return None


def main():
    print_states(states_in_america)


if __name__ == '__main__':
    main()
