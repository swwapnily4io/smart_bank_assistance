LOGIN_OTP_CARD_CONTENT = {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2",
    "body": [
        {
            "type": "RichTextBlock",
            "inlines": [
                {
                    "type": "TextRun",
                    "text": "Login"
                }
            ]
        },
        {
            "type": "Input.Text",
            "placeholder": "Customer ID",
            "label": "Customer ID",
            "isRequired": True,
            "maxLength": 10,
            "spacing": "Large",
            "errorMessage": "Please enter valid customer ID",
            "id": "customerId",
            "separator": True
        },
        {
            "type": "Input.Text",
            "placeholder": "Password",
            "id": "password",
            "spacing": "Medium",
            "label": "Password",
            "isRequired": True,
            "errorMessage": "Please enter Password."
        },
        {
            "type": "Input.Toggle",
            "title": "I accept the Terms & Conditions",
            "id": "terms",
            "spacing": "Medium"
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.Submit",
                    "data": {
                            "type": "Login"
                    },
                    "title": "Login",
                }
            ]
        }
    ],
    "backgroundImage": {
        "url": "Publish Adaptive Card Schema"
    }
}
