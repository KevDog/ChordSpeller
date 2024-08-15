def get_altered_notes(key, alterations, start_degree=1):
  """
  Calculates altered notes based on the given key and alterations.

  Args:
    key: The base key (e.g., 'C', 'G', 'Db').
    alterations: A list of tuples, where each tuple contains an alteration ('b' or '#') and a degree (1-7).

  Returns:
    A list of altered notes.
  """

  # Dictionary mapping key signatures to accidental patterns
  key_signatures = {
      'C': [],
      'G': ['#'],
      'D': ['#', '#'],
      'A': ['#', '#', '#'],
      'E': ['#', '#', '#', '#'],
      'B': ['#', '#', '#', '#', '#'],
      'F#': ['#', '#', '#', '#', '#', '#'],
      'C#': ['#', '#', '#', '#', '#', '#', '#'],
      'F': ['b'],
      'Bb': ['b', 'b'],
      'Eb': ['b', 'b', 'b'],
      'Ab': ['b', 'b', 'b', 'b'],
      'Db': ['b', 'b', 'b', 'b', 'b'],
      'Gb': ['b', 'b', 'b', 'b', 'b', 'b'],
      'Cb': ['b', 'b', 'b', 'b', 'b', 'b', 'b']
  }

  def get_base_notes(key):
    scale_degrees = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    accidentals = key_signatures.get(key, [])
    for i, accidental in enumerate(accidentals):
      scale_degrees[i] = accidental + scale_degrees[i]
    return scale_degrees

#   def apply_alteration(note, alt):
#     if alt == 'b':
#       return note + 'b'
#     elif alt == '#':
#       return note + '#'
#     else:
#       return note
  def apply_alteration(note, alt, scale_degrees):
    index = scale_degrees.index(note)
    if alt == 'b':
        index -= 1
    elif alt == '#':
        index += 1
    return scale_degrees[index % 7]

  scale_degrees = get_base_notes(key)
  altered_notes = scale_degrees.copy()

  for alt, degree in alterations:
    altered_notes[int(degree) - 1] = apply_alteration(altered_notes[int(degree) - 1], alt,scale_degrees)
  altered_notes = altered_notes[start_degree - 1:] + altered_notes[:start_degree - 1]
  return altered_notes

