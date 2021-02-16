WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_well_done(desired_state):
    return desired_state == 'well-done'

def is_medium(desired_state):
    return desired_state == 'medium'

def cooked_well_done(time, temperature, pressure):
    return time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE

def cooked_medium(time, temperature, pressure):
    return time * temperature * pressure * COOKED_CONSTANT >= MEDIUM

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    if is_well_done(desired_state) and cooked_well_done(time, temperature, pressure):
        return True
    if is_medium(desired_state) and cooked_medium(time, temperature, pressure):
        return True
    return False
