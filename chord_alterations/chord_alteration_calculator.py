 # Dictionary mapping key signatures to accidental patterns
key_signatures = {
        'C': [],
        'G': ['F#'],
        'D': ['F#', 'C#'],
        'A': ['F#', 'C#', 'G#'],
        'E': ['F#', 'C#', 'G#', 'D#'],
        'B': ['F#', 'C#', 'G#', 'D#', 'A#'],
        'F#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#'],
        'C#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'],
        'F': ['Bb'],
        'Bb': ['Bb', 'Eb'],
        'Eb': ['Bb', 'Eb', 'Ab'],
        'Ab': ['Bb', 'Eb', 'Ab', 'Db'],
        'Db': ['Bb', 'Eb', 'Ab', 'Db', 'Gb'],
        'Gb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'],
        'Cb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb']
    }
scale_degrees = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Dictionary mapping chord symbols to scale degrees (as strings)
chord_spellings = {
    "Maj": ["1", "3", "5"],
    "Maj7": ["1", "3", "5", "7"],
    "min": ["1", "b3", "5"],
    "min7": ["1", "b3", "5", "b7"],
    "7": ["1", "3", "5", "b7"],
    "m7b5": ["1", "b3", "b5", "b7"],
    "dom7": ["1", "3", "5", "b7"],
    "sus4": ["1", "4", "5"],
    "sus2": ["1", "2", "5"],
    "add9": ["1", "3", "5", "9"],
    "add11": ["1", "3", "5", "9", "11"],
    "add13": ["1", "3", "5", "9", "11", "13"],
    "6": ["1", "3", "5", "6"],
    "6/9": ["1", "3", "5", "6", "9"],
    "9sus4": ["1", "4", "5", "9"]
}

def get_altered_notes(key, alterations, start_degree=1):
    """
    Calculates altered notes based on the given key and alterations.

    Args:
        key: The base key (e.g., 'C', 'G', 'Db').
        alterations: A list of tuples, where each tuple contains an alteration ('b' or '#') and a degree (1-7).
        start_degree: The degree to start the scale from (default is 1).

    Returns:
        A list of altered notes.
    """

    def get_base_notes(key):
        accidentals = key_signatures.get(key, [])
        
        # Find the starting note index
        start_note = key[0]
        start_index = scale_degrees.index(start_note)
        
        # Rotate the scale degrees to start from the key note
        rotated_scale = scale_degrees[start_index:] + scale_degrees[:start_index]
        
        # Apply accidentals
        for accidental in accidentals:
            note = accidental[0]  # Get the note part (e.g., 'F' from 'F#')
            if note in rotated_scale:
                index = rotated_scale.index(note)
                rotated_scale[index] = accidental  # Apply the accidental
        
        return rotated_scale

    def apply_alteration(note, alt):
        if alt == 'b':
            if note.endswith('#'):
                return note[0]  # Remove the sharp
            elif note.endswith('b'):
                return note + 'b'  # Add another flat
            else:
                return note + 'b'
        elif alt == '#':
            if note.endswith('b'):
                return note[0]  # Remove the flat
            elif note.endswith('#'):
                return note + '#'  # Add another sharp
            else:
                return note + '#'
        else:
            return note

    base_notes = get_base_notes(key)
    altered_notes = base_notes[:]
    for alt, degree in alterations:
        note = base_notes[(degree - 1) % 7]
        altered_note = apply_alteration(note, alt)
        altered_notes[(degree - 1) % 7] = altered_note
    
    rotated_notes = altered_notes[start_degree - 1:] + altered_notes[:start_degree - 1]
    return rotated_notes

def spell_chord(chord, key='C'):
  """
  Returns a list of notes for a given chord in a specified key.

  Args:
    chord: The chord symbol (e.g., "Cmaj7").
    key: The base key (e.g., "C").

  Returns:
    A list of notes in the chord.
  """
  # Get the chord's scale degrees
  chord_scale_degrees = chord_spellings[chord]

  # Get the base notes for the key
  base_notes = get_base_notes(key)

  # Apply the chord's scale degrees to the base notes
  chord_notes = [base_notes[get_note_index(note, base_notes)] for note in map_scale_degrees_to_notes(chord_scale_degrees, base_notes)]

  return chord_notes
def get_note_index(note, base_notes):
    """
    Gets the index of a note in the base notes list, handling alterations.

    Args:
        note: The note string, possibly with alterations.
        base_notes: The list of base notes.

    Returns:
        The index of the note in the base notes list.
    """
    if note in base_notes:
        return base_notes.index(note)
    elif note.endswith('b'):
        return base_notes.index(note[0]) - 1
    elif note.endswith('#'):
        return base_notes.index(note[0]) + 1
    else:
        raise ValueError(f"Note {note} is not in the base notes list")

def get_base_notes(key):
  accidentals = key_signatures.get(key, [])

  # Find the starting note index
  start_note = key[0]
  start_index = scale_degrees.index(start_note)

  # Rotate the scale degrees to start from the key note
  rotated_scale = scale_degrees[start_index:] + scale_degrees[:start_index]

  # Apply accidentals
  for accidental in accidentals:
    note = accidental[0]  # Get the note part (e.g., 'F' from 'F#')
    index = rotated_scale.index(note)
    if note in rotated_scale[index]:  # Check if accidental already exists
      rotated_scale[index] = accidental + rotated_scale[index]  # Add the accidental
    else:
      rotated_scale[index] = accidental

  return rotated_scale

def map_scale_degrees_to_notes(scale_degrees, base_notes):
    """
    Maps scale degrees to corresponding notes in the base notes list.

    Args:
        scale_degrees: List of scale degrees (e.g., ['1', '2', '3', '4', '5', '6', '7']).
        base_notes: List of base notes in the key.

    Returns:
        List of notes corresponding to the scale degrees.
    """
    degree_to_note = {
        '1': base_notes[0],
        '2': base_notes[1],
        '3': base_notes[2],
        '4': base_notes[3],
        '5': base_notes[4],
        '6': base_notes[5],
        '7': base_notes[6]
    }
    return [degree_to_note[degree] for degree in scale_degrees]
