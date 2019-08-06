# Problem #1

## Given

A string as the following: 

> I completed **{number_of_sessions}** sessions and I rated my expert **{number_of_stars}** stars

while:
- `number_of_sessions` is any number in `[0, 1, ...9]`
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


# Problem #2

## Given

- Problem #1.

## Then

- Move your code logic into a function that takes 2 parameters `make_step(number_of_sessions, number_of_stars)`. 
  
  Then you should be able to call your function as `make_step(2, 'five')`.

- Move your dictionary maps into a class `Session` in a module called `enums`.
  
  It should be accessible via `enums.Session`. And update your `make_step`.

- Create an exception `InvalidValueException` extends from `Exception`.

  It takes a message as the following: `InvalidValueException('Invalid number of sessions')`.

- When `make_step` be called with invalid parameter(s), it should throw an `InvalidValueException` exception. 
  
  Try to catch and print out the message.

## Expected output

- `Enums` and `Exception` should have their own modules.
- Expected result:
  ```
  make_step(2, 'five')
  > I completed two sessions and I rated my expert 5 stars
  ```

  ```
  make_step(0, 'five')
  > Invalid number of sessions
  ```

  ```
  make_step(2, 'ten')
  > Invalid number of stars
  ```


# Problem #3

## Given

A list, a tuple and a set of numbers:
```
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}
```

## Then

- Decide if `a`, `b`, `c` contain the same set of numbers.


## Expected output

The result should be `true`.


# Problem #4

## Given

A file `data.json` with the following content:

```json
{
  "expiration_time": 300,
  "id": 0,
  "product": "excelchat",
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

An object with the following content (**yes, you can copy & paste**):

```python
modify_data = {
  "expiration_time": 200,
  "product": "querychat",
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

- Come up with an algorithm to update data in file `data.json` with the object provided **without using direct object/ variable assignment**.
- The result should be written to file `result.json`.

## Expected output

A new file `data2.json` should be created with the following content:

```json
{
    "expiration_time": 200,
    "id": 0,
    "product": "querychat",
    "storefront": {
        "banner_enabled": false,
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

