JSONDict = dict[str, 'JSONType']

JSONList = list['JSONType'] | tuple['JSONType', ...]

JSONType = JSONDict | JSONList | str | int | float | bool | None
