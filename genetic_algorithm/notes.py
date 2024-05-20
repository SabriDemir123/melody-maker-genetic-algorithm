building_blocks = [
    # Beethoven's fragments
    (('e4', 8), ('f#4', 8), ('g4*', 4), ('f#4', 8), ('e4', 8), ('d#4*', 4), ('e4', 8), ('f#4', 8)),  # Beethoven's Symphony No. 5
    (('g4', 8), ('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('a3', 8), ('g3', 8)),  # Beethoven's Für Elise
    (('e4', 8), ('g#4', 8), ('b4', 8), ('e5', 8), ('b4', 8), ('g#4', 8), ('e4', 8), ('g#4', 8)),  # Beethoven's Moonlight Sonata
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8)),  # Beethoven's Ode to Joy
    (('d4', 8), ('c#4', 8), ('d4', 8), ('f4', 8), ('d4', 8), ('c#4', 8), ('d4', 8), ('f4', 8)),  # Beethoven's Sonata Pathétique
    (('a4', 8), ('c#5', 8), ('e5', 8), ('a5', 8), ('e5', 8), ('c#5', 8), ('a4', 8), ('c#5', 8)),  # Beethoven's Appassionata Sonata
    (('g4', 8), ('a4', 8), ('g4', 8), ('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('d4', 8)),  # Beethoven's Symphony No. 6 "Pastoral"
    (('f#4', 8), ('e4', 8), ('f#4', 8), ('g#4', 8), ('f#4', 8), ('e4', 8), ('f#4', 8), ('g#4', 8)),  # Beethoven's Piano Sonata No. 14 "Moonlight"

    # Mozart's fragments
    (('g4', 8), ('a4', 8), ('b4', 8), ('a4', 8), ('g4', 8), ('f#4', 8), ('e4', 8), ('f#4', 8)),  # Mozart's Symphony No. 40
    (('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('a3', 8), ('b3', 8), ('c4', 8), ('d4', 8)),  # Mozart's Eine kleine Nachtmusik
    (('d4', 8), ('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c#5', 8), ('d5', 8)),  # Mozart's Turkish March
    (('c4', 8), ('b3', 8), ('a3', 8), ('g3', 8), ('f3', 8), ('e3', 8), ('d3', 8), ('c3', 8)),  # Mozart's Symphony No. 25
    (('e4', 8), ('f#4', 8), ('g#4', 8), ('a4', 8), ('b4', 8), ('c#5', 8), ('d5', 8), ('e5', 8)),  # Mozart's Sonata in C Major
    (('c4', 8), ('d4', 8), ('e4', 8), ('f4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8)),  # Mozart's Symphony No. 41 "Jupiter"
    (('f4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c5', 8), ('d5', 8), ('e5', 8), ('f5', 8)),  # Mozart's Piano Sonata No. 16 "Sonata facile"
    (('b3', 8), ('c#4', 8), ('d#4', 8), ('e4', 8), ('f#4', 8), ('g#4', 8), ('a#4', 8), ('b4', 8)),  # Mozart's Symphony No. 41 "Jupiter" (second theme)

    # Bach's fragments
    (('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('c4', 8), ('d4', 8), ('e4', 8)),  # Bach's Air on the G String
    (('d4', 8), ('f#4', 8), ('a4', 8), ('d5', 8), ('a4', 8), ('f#4', 8), ('d4', 8), ('f#4', 8)),  # Bach's Brandenburg Concerto No. 3
    (('g4', 8), ('b4', 8), ('d5', 8), ('f5', 8), ('d5', 8), ('b4', 8), ('g4', 8), ('b4', 8)),  # Bach's Jesu, Joy of Man's Desiring
    (('f4', 8), ('e4', 8), ('d4', 8), ('c4', 8), ('b3', 8), ('a3', 8), ('g#3', 8), ('a3', 8)),  # Bach's Toccata and Fugue in D minor
    (('d4', 8), ('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8), ('b4', 8), ('c#5', 8), ('d5', 8)),  # Bach's Prelude and Fugue in C Major
    (('e3', 8), ('f#3', 8), ('g#3', 8), ('a3', 8), ('b3', 8), ('c#4', 8), ('d#4', 8), ('e4', 8)),  # Bach's Prelude in E Major
    (('e4', 8), ('d4', 8), ('c#4', 8), ('d4', 8), ('e4', 8), ('f#4', 8), ('g4', 8), ('a4', 8)),  # Bach's Prelude in C Major
    (('g#3', 8), ('b3', 8), ('c#4', 8), ('e4', 8), ('c#4', 8), ('b3', 8), ('g#3', 8), ('e4', 8)),  # Bach's Prelude in C# minor

    # Chopin's fragments
    (('c#4', 8), ('e4', 8), ('g#4', 8), ('c#5', 8), ('g#4', 8), ('e4', 8), ('c#4', 8), ('e4', 8)),  # Chopin's Revolutionary Étude
    (('e4', 8), ('g#4', 8), ('b4', 8), ('e5', 8), ('b4', 8), ('g#4', 8), ('e4', 8), ('g#4', 8)),  # Chopin's Nocturne Op. 9 No. 2
    (('c#3', 8), ('e3', 8), ('g#3', 8), ('c#4', 8), ('g#3', 8), ('e3', 8), ('c#3', 8), ('e3', 8)),  # Chopin's Étude Op. 10 No. 4
    (('e5', 8), ('g#5', 8), ('b5', 8), ('e6', 8), ('b5', 8), ('g#5', 8), ('e5', 8), ('g#5', 8)),   # Chopin's Ballade No. 1 in G minor
    (('d#4', 8), ('f4', 8), ('g#4', 8), ('c5', 8), ('g#4', 8), ('f4', 8), ('d#4', 8), ('f4', 8)),  # Chopin's Prelude Op. 28 No. 8
    (('a3', 8), ('c#4', 8), ('e4', 8), ('a4', 8), ('e4', 8), ('c#4', 8), ('a3', 8), ('e4', 8)),  # Chopin's Nocturne Op. 27 No. 2
    (('g4', 8), ('b4', 8), ('d5', 8), ('f5', 8), ('a5', 8), ('f5', 8), ('d5', 8), ('b4', 8)),  # Chopin's Polonaise in A-flat Major "Heroic"
    (('d#4', 8), ('f#4', 8), ('a4', 8), ('c#5', 8), ('e5', 8), ('c#5', 8), ('a4', 8), ('f#4', 8)),  # Chopin's Fantaisie-Impromptu
]

c_major_scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

random_note = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
random_duration = [1, 2, 4, 8]