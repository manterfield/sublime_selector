# Selector - Sublime Text 2 plugin providing extra text selection options.

## Features
- **Google**: search the selected text on Google (opens in default browser)

- **Stack Overflow**: search the selected text on SO (opens in default browser)

- **URL Encode**: URL Encode the selected text (also known as percent encoding)

- **URL Decode**: URL Decode the selected string

- **Slugify**: slugify the selected text

- **Wrap**: wrap selected text in whatever tags with a couple of clicks,
		    you can add tags yourself in the settings (decribed below)

- **Alphanumeric**: Strip non alphanumeric characters from the selected text

- **Title**: Convert selected text to title case

- **Class**: Convert selected text to a class name
		 (strip non alphanumerics and convert to camelcase)


### Installation

Install 'Selector' via package control or download this repo and save it to your Packages directory.

### Adding your own wrapper tags

Create a file in your Packages directory named Context.sublime-menu
the content of the file should be in the structure below:

```json
[
    {
        "id": "Wrapper",
        "children":
        [
            {
                "caption": "%%",
                "command": "selector",
                "args": {
                    "command": "wrap",
                    "open_tag": "%",
                    "close_tag": "%"
                }
            }
        ]
    }
]
```

Above is the example for the percent wrap function. The caption option is what you would like this to display as in the right-click menu, open_tag and close_tag are what they sound like. Everything else should remain the same.

To add multiple it would look like this:

```json
[
    {
        "id": "Wrapper",
        "children":
        [
            {
                "caption": "%%",
                "command": "selector",
                "args": {
                    "command": "wrap",
                    "open_tag": "%",
                    "close_tag": "%"
                }
            },
            {
                "caption": "Foo tags",
                "command": "selector",
                "args": {
                    "command": "wrap",
                    "open_tag": "<foo>",
                    "close_tag": "</foo>"
                }
            }
        ]
    }
]
```

and so on.

###Contribution

Any contribution is welcome. If you are adding commands, make sure they are covered by tests.

Make sure to write your code as if it is going to be read by humans. Pretty much every programmer I have met so far has been human, so it is a pretty good rule of thumb.
