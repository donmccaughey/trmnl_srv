from .octet_entity import ascii_bytes, enumerate_segments, segment_preview, split_buffer


def test_ascii_bytes():
    buffer = bytes(range(0, 16))
    assert ascii_bytes(buffer) == '.... .... .... ....'

    buffer = bytes(range(32, 48))
    assert ascii_bytes(buffer) == ' !"# $%&\' ()*+ ,-./'

    buffer = bytes(range(64, 80))
    assert ascii_bytes(buffer) == '@ABC DEFG HIJK LMNO'

    buffer = bytes(range(112, 128))
    assert ascii_bytes(buffer) == 'pqrs tuvw xyz{ |}~.'


def test_enumerate_segments():
    buffer = bytes((i % 256 for i in range(512)))
    segments = list(enumerate_segments(buffer))

    assert len(segments) == 8
    assert segments[0] == (0, bytes(range(16)))
    assert segments[-1] == (7, bytes(range(112, 128)))


def test_enumerate_segments_for_small_final_segment():
    buffer = bytes(range(20))
    segments = list(enumerate_segments(buffer))

    assert len(segments) == 2
    assert segments[0] == (0, bytes(range(16)))
    assert segments[-1] == (1, bytes(range(16, 20)))


def test_segment_preview():
    segment = bytes(range(64, 80))
    assert segment_preview(segment) == (
        '40414243 44454647 48494a4b 4c4d4e4f | @ABC DEFG HIJK LMNO'
    )


def test_segment_preview_for_short_segment():
    segment = bytes.fromhex('deadbeef')
    assert segment_preview(segment) == (
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
