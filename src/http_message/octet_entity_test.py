from .octet_entity import ascii_byte, ascii_bytes, enumerate_segments, OctetEntity, segment_dump, split_buffer


def test_short_bytes():
    entity = OctetEntity(bytes.fromhex('deadbeef'))
    assert list(entity.lines()) == [
        'deadbeef                            | ....',
    ]


def test_bytes_shorter_than_limit__for_equal_segments():
    entity = OctetEntity(bytes((i % 256 for i in range(64))))
    assert list(entity.lines(8)) == [
        '00010203 04050607 08090a0b 0c0d0e0f | .... .... .... ....',
        '10111213 14151617 18191a1b 1c1d1e1f | .... .... .... ....',
        '20212223 24252627 28292a2b 2c2d2e2f |  !"# $%&\' ()*+ ,-./',
        '30313233 34353637 38393a3b 3c3d3e3f | 0123 4567 89:; <=>?',
    ]


def test_bytes_shorter_than_limit__for_short_final_segments():
    entity = OctetEntity(bytes((i % 256 for i in range(63))))
    assert list(entity.lines(8)) == [
        '00010203 04050607 08090a0b 0c0d0e0f | .... .... .... ....',
        '10111213 14151617 18191a1b 1c1d1e1f | .... .... .... ....',
        '20212223 24252627 28292a2b 2c2d2e2f |  !"# $%&\' ()*+ ,-./',
        '30313233 34353637 38393a3b 3c3d3e   | 0123 4567 89:; <=>',
    ]


def test_long_bytes():
    entity = OctetEntity(bytes((i % 256 for i in range(512))))
    assert list(entity.lines(8)) == [
        '00010203 04050607 08090a0b 0c0d0e0f | .... .... .... ....',
        '10111213 14151617 18191a1b 1c1d1e1f | .... .... .... ....',
        '20212223 24252627 28292a2b 2c2d2e2f |  !"# $%&\' ()*+ ,-./',
        '30313233 34353637 38393a3b 3c3d3e3f | 0123 4567 89:; <=>?',
        '40414243 44454647 48494a4b 4c4d4e4f | @ABC DEFG HIJK LMNO',
        '50515253 54555657 58595a5b 5c5d5e5f | PQRS TUVW XYZ[ \\]^_',
        '60616263 64656667 68696a6b 6c6d6e6f | `abc defg hijk lmno',
        '... (512 bytes total)',
    ]


def test_ascii_byte():
    assert ascii_byte(0x1f) == '.'
    assert ascii_byte(0x20) == ' '
    assert ascii_byte(0x41) == 'A'
    assert ascii_byte(0x61) == 'a'
    assert ascii_byte(0x7e) == '~'
    assert ascii_byte(0x7f) == '.'


def test_ascii_bytes():
    buffer = bytes(range(0, 16))
    assert ''.join(ascii_bytes(buffer)) == '.... .... .... ....'
    assert ''.join(ascii_bytes(buffer, sep='|')) == '....|....|....|....'
    assert (
            ''.join(ascii_bytes(buffer, sep='|', bytes_per_sep=6))
            == '......|......|....'
    )

    buffer = bytes(range(32, 48))
    assert ''.join(ascii_bytes(buffer)) == ' !"# $%&\' ()*+ ,-./'

    buffer = bytes(range(64, 80))
    assert ''.join(ascii_bytes(buffer)) == '@ABC DEFG HIJK LMNO'

    buffer = bytes(range(112, 128))
    assert ''.join(ascii_bytes(buffer)) == 'pqrs tuvw xyz{ |}~.'


def test_enumerate_segments():
    buffer = bytes((i % 256 for i in range(512)))
    segments = list(enumerate_segments(buffer, segment_count=8))

    assert len(segments) == 8
    assert segments[0] == (0, bytes(range(16)))
    assert segments[-1] == (7, bytes(range(112, 128)))


def test_enumerate_segments_for_small_final_segment():
    buffer = bytes(range(20))
    segments = list(enumerate_segments(buffer))

    assert len(segments) == 2
    assert segments[0] == (0, bytes(range(16)))
    assert segments[-1] == (1, bytes(range(16, 20)))


def test_segment_dump():
    segment = bytes(range(64, 80))
    assert segment_dump(segment) == (
        '40414243 44454647 48494a4b 4c4d4e4f | @ABC DEFG HIJK LMNO'
    )


def test_segment_dump_for_short_segment():
    segment = bytes.fromhex('deadbeef')
    assert segment_dump(segment) == (
        'deadbeef                            | ....'
    )


def test_split_buffer():
    buffer = bytes((i % 256 for i in range(512)))
    segments = list(split_buffer(buffer))

    assert len(segments) == 32
    assert len(segments[0]) == 16
    assert segments[0].hex(' ', -4) == (
        '00010203 04050607 08090a0b 0c0d0e0f'
    )
    assert segments[-1].hex(' ', -4) == (
        'f0f1f2f3 f4f5f6f7 f8f9fafb fcfdfeff'
    )


def test_split_buffer_with_segment_size():
    buffer = bytes((i % 256 for i in range(512)))
    segments = list(split_buffer(buffer, segment_size=8))

    assert len(segments) == 64
    assert len(segments[0]) == 8
    assert segments[0].hex(' ', -4) == '00010203 04050607'
    assert segments[-1].hex(' ', -4) == 'f8f9fafb fcfdfeff'


def test_split_buffer_for_empty_buffer():
    buffer = bytes()
    segments = list(split_buffer(buffer))

    assert len(segments) == 0


def test_split_buffer_for_small_single_segment():
    buffer = bytes(range(14))
    segments = list(split_buffer(buffer))

    assert len(segments) == 1
    assert len(segments[0]) == 14
    assert segments[0].hex(' ', -4) == (
        '00010203 04050607 08090a0b 0c0d'
    )


def test_split_buffer_for_small_final_segment():
    buffer = bytes(range(20))
    segments = list(split_buffer(buffer))

    assert len(segments) == 2

    assert len(segments[0]) == 16
    assert segments[0].hex(' ', -4) == (
        '00010203 04050607 08090a0b 0c0d0e0f'
    )

    assert len(segments[1]) == 4
    assert segments[1].hex(' ', -4) == '10111213'
