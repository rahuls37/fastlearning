Keep in mind that ```JSON``` only supports ```str``` as keys.

But Pydantic has automatic data conversion.

This means that, even though your API clients can only send strings as keys, as long as those strings contain pure integers, Pydantic will convert them and validate them.

And the dict you receive as weights will actually have ```int``` keys and ```float``` values.