from move import movement, unpack_t

movement_seq = {
    "m1": {
        1: [[93.59, 0, -16.324, 'arm1'], [93.59, 0, -16.324, 'arm3']],
        2: [[93.59, 10, 16.324, 'arm2'], [93.59, 0, 16.324, 'arm4']]
    },
    'm2': {
        1: [[93.59, 10, 16.324, 'arm1'], [93.59, 10, 16.324, 'arm3']],
        2: [[93.59, 0, -16.324, 'arm2'], [93.59, 0, -16.324, 'arm4']]
    },
    "m3": {
        1: [[93.59, 0, 16.324, 'arm1'], [93.59, 0, 16.324, 'arm3']],
        2: [[93.59, 0, -16.324, 'arm2'], [93.59, 0, -16.324, 'arm4']]
    },
    "m4": {
        1: [[93.59, 0, -16.324, 'arm1'], [93.59, 0, -16.324, 'arm3']],
        2: [[93.59, 10, 16.324, 'arm2'], [93.59, 10, 16.324, 'arm4']]
    }
}

for i in movement_seq:
    for j in movement_seq[i]:
        x, y, z, arm = unpack_t(movement_seq[i][j])
        movement([], x, y, z, arm)
