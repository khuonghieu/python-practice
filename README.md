# Problem #1: The Basics/ String/ Dictionary

## Given

A string as the following: 

> I completed **{number_of_sessions}** sessions and I rated my expert **{number_of_stars}** stars

while:
- `number_of_sessions` is any number in `[1, 2, ...9]`

- `number_of_stars` is any text in `[one, two, three, four, five]`

## Then

- Convert `number_of_sessions` from number to text.

- Convert `number_of_stars` from text to number.

- Using dictionaries and string methods.

## Expected output

For example, with `number_of_sessions` = `2` and `number_of_stars` = `five`, the original string will be:

> I completed **2** sessions and I rated my expert **five** stars

The result after conversion:

> I completed **two** sessions and I rated my expert **5** stars


# Problem #2: Object-Oriented Programming/ Exceptions

## Given

- Existing code from Problem #1.

## Then

- Create a class `Step` contains:

  - Instance variables:
    - `number_of_sessions: int`

    - `number_of_stars: int`

  - Methods:
    - `__init__(number_of_sessions: int, number_of_stars: string)`
  
    - `make_step(self)`

- Move your code logic into the method `make_step`. 
  
  Then you should be able to call your method as `Step(2, 'five').make_step()`.

--

- In module `enums`, create a model entities `Session`, it should contain all of your constants as its *class variables*.

- The constants should be accessible via `enums.Session`.
  
  Remember update your `make_step` to use the enums you just defined.

  ```python
  # enums.py
  class Session(object):
      NUMBER_TO_TEXT_MAP: dict

  # other.py
  from enums import Session
  Session.NUMBER_TO_TEXT_MAP
  ```

--

- Create an exeption called `InvalidValueException`:

  - Instance variables:
    - `message: string`

  - Methods:
    - `__init__(message: string)`

- Create an exception `InvalidValueException` extends from `Exception`.

  Then you can raise the exception as the following: `raise InvalidValueException("Invalid number of sessions")`.

--

- When `Step` be created with invalid `number_of_session` or `number_of_stars`, it should raise an `InvalidValueException` exception with the corresponding message. 
  
  Try to catch and print out the message using `try`, `except`.

## Expected output

- `Step`, `Session` and `Exception` should have their own modules.

- Expected result:
  ```python
  Step(2, "five").make_step()
  # > I completed two sessions and I rated my expert 5 stars
  ```

  ```python
  Step(0, "five").make_step()
  # > Invalid number of sessions
  ```

  ```python
  Step(2, "ten").make_step()
  # > Invalid number of stars
  ```


# Problem #3: Advanced Data Types

## Given

A list, a tuple and a set of numbers:
```python
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}
```

## Then

- Decide if `a`, `b`, `c` all contain the same set of numbers.


## Expected output

The result should be `true`.


# Problem #4: Files/ JSON/ Dictionary/ Algorithm

## Given

A file `data.json` with the following content:

```json
{
  "expiration_time": 300,
  "id": 0,
  "product": "xchat",
  "storefront": {
      "banner_enabled": true,
      "banner_text": "Dynamic offer banner",
      "description": "",
      "enabled": true,
      "purchase_options": [
          {
              "button_text": "Dynamic offer - button_text",
              "description": "Dynamic offer - description",
              "id": "",
              "price": "7.99",
              "price_text": "price_text",
              "session_count": "3",
              "subtitle": "Dynamic offer - subtitle",
              "title": "Dynamic offer - title",
              "suffix": "Dynamic offer - suffix",
              "trial_duration": 0,
              "min_member_count": 1,
              "max_member_count": 1,
              "action": "purchase",
              "frequency_view": "monthly",
              "free_learning_subscription": false,
              "team_type": "personal",
              "frequency": null,
          }
      ],
  },
  "utm_campaign": "19203420349",
  "utm_source": "",
}
```

An object `modify_data` with the following content:

```python
modify_data = {
  "expiration_time": 200,
  "product": "qchat",
  "utm_campaign": str(time.time()),
  "storefront": {
    "banner_enabled": False,
    "purchase_options": [
          {
              "button_text": "Dynamic offer 1 - button_text",
              "description": "Dynamic offer 1 - description",
              "id": "",
              "price": "99.99",
              "price_text": "price_text",
              "session_count": "0",
              "subtitle": "Dynamic offer - subtitle",
              "title": "Dynamic offer - title",
              "suffix": "Dynamic offer - suffix",
              "trial_duration": 0,
              "min_member_count": 1,
              "max_member_count": 1,
              "action": "purchase",
              "frequency_view": "monthly",
              "free_learning_subscription": False,
              "team_type": "personal",
              "frequency": None,
          }
      ]
  }
}

```

## Then

- Create class model entities `StorefrontConfig`:

  - Methods:

    - `__init__(data: object)`

    - `update(modify_data: object)`: Write an algorithm to update data of the object using the dictionary provided (**not using direct variable assignment**).

- Create class `FileController`: 

  - Static Methods:

    - `read_file(file_name: string): StorefrontConfig`: To read a json with name `file_name`, it should return a `StorefrontConfig` object with the data in the text file.

    - `write_file(object: StorefrontConfig, file_name: string)`: To write the `StorefrontConfig` object down to file `file_name` as text.

- The result should be written to file `result.json`.

## Expected output

```python
file_controller = FileController()
config = file_controller.read_file("data.json")
config.update(modify_data)
file_controller.write_file(config, "result.json")
```

A new file `result.json` should be created with the following content:

```json
{
    "expiration_time": 200,
    "id": 0,
    "product": "qchat",
    "storefront": {
        "banner_enabled": false,
        "banner_text": "Dynamic offer banner",
        "description": "",
        "enabled": true,
        "purchase_options": [
            {
                "button_text": "Dynamic offer 1 - button_text",
                "description": "Dynamic offer 1 - description",
                "id": "",
                "price": "99.99",
                "price_text": "price_text",
                "session_count": "0",
                "subtitle": "Dynamic offer - subtitle",
                "title": "Dynamic offer - title",
                "suffix": "Dynamic offer - suffix",
                "trial_duration": 0,
                "min_member_count": 1,
                "max_member_count": 1,
                "action": "purchase",
                "frequency_view": "monthly",
                "free_learning_subscription": false,
                "team_type": "personal",
                "frequency": null
            }
        ]
    },
    "utm_campaign": "updated_timestamp",
    "utm_source": ""
}
```

