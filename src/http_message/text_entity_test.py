from .text_entity import TextEntity


def test_short_text():
    entity = TextEntity('This is a test message')
    assert list(entity.lines()) == [
        'This is a test message',
    ]


def test_long_text():
    entity = TextEntity(
        'This is a test message with many lines:\n'
        'Line 2: Apple\n'
        'Line 3: Banana\n'
        'Line 4: Carrot\n'
        'Line 5: Dates\n'
        'Line 6: Eggplant\n'
        'Line 7: Figs\n'
        'Line 8: Ginger\n'
        'Line 9: Horseradish\n'
        'Line 10: Iceberg lettuce\n'
    )
    assert list(entity.lines(8)) == [
        'This is a test message with many lines:',
        'Line 2: Apple',
        'Line 3: Banana',
        'Line 4: Carrot',
        'Line 5: Dates',
        'Line 6: Eggplant',
        'Line 7: Figs',
        '... (3 lines omitted)',
    ]
    assert list(entity.lines()) == [
        'This is a test message with many lines:',
        'Line 2: Apple',
        'Line 3: Banana',
        'Line 4: Carrot',
        'Line 5: Dates',
        'Line 6: Eggplant',
        'Line 7: Figs',
        'Line 8: Ginger',
        'Line 9: Horseradish',
        'Line 10: Iceberg lettuce',
    ]


def test_short_json():
    entity = TextEntity(
        '{"foo":"bar","baz":42}', content_type='application/json'
    )
    assert list(entity.lines(8)) == [
        '{',
        '    "baz": 42,',
        '    "foo": "bar"',
        '}',
    ]


def test_long_json():
    entity = TextEntity(
        '{"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8}',
        content_type='application/json',
    )
    assert list(entity.lines(8)) == [
        '{',
        '    "1": 1,',
        '    "2": 2,',
        '    "3": 3,',
        '    "4": 4,',
        '    "5": 5,',
        '    ... (3 lines omitted)',
        '}',
    ]
    assert list(entity.lines()) == [
        '{',
        '    "1": 1,',
        '    "2": 2,',
        '    "3": 3,',
        '    "4": 4,',
        '    "5": 5,',
        '    "6": 6,',
        '    "7": 7,',
        '    "8": 8',
        '}',
    ]
