INTRO_ADAPTIVE_CARD_CONTENT = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.0",
    "backgroundImage": "https://terralfletcher.com/wp-content/uploads/2014/01/light-repeat-bg.jpg",
    "fillMode": "repeatHorizontally",
    "body": [
        {
            "speak": "Welcome Steve Smith",
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 3,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Welcome"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Steve Smith",
                            "color": "accent",
                            "weight": "bolder",
                            "size": "extraLarge",
                            "spacing": "none"
                        },
                        {
                            "type": "TextBlock",
                            "text": "We are here to provide support.",
                            "isSubtle": True,
                            "spacing": "none"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Please select one the option below",
                            "spacing": "none"
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": 1,
                    "items": [
                        {
                            "type": "Image",
                            "url": "https://www.cricbuzz.com/a/img/v1/152x152/i1/c170624/steven-smith.jpg",
                            "size": "auto",
                            "height": "100px"
                        }
                    ]
                }
            ]
        }
    ],
    "actions": [

        {
            "type": "Action.ShowCard",
            "title": "Account Balance",
            "displayText": "AccountBalance",
            "card": {
                "type": "AdaptiveCard",
                "body": [
                    {
                        "type": "TextBlock",
                        "text": "Account Balance"
                    }
                ]
            }
        },
        {
            "type": "Action.OpenUrl",
            "title": "Credit Card",
            "url": "https://www.cricbuzz.com/a/img/v1/152x152/i1/c170624/steven-smith.jpg"
        },
        {
            "type": "Action.OpenUrl",
            "title": "Customer Support",
            "url": "https://www.cricbuzz.com/a/img/v1/152x152/i1/c170624/steven-smith.jpg"
        }
    ],

}
