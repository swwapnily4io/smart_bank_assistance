INVOICE_ADAPTIVE_CARD = {
  "type": "AdaptiveCard",
  "body": [
    {
      "type": "Container",
      "style": "emphasis",
      "items": [
        {
          "type": "ColumnSet",
          "columns": [
            {
              "type": "Column",
              "items": [
                {
                  "type": "TextBlock",
                  "size": "Medium",
                  "weight": "Bolder",
                  "text": "**Your VodafoneIdea Bill**"
                }
              ],
              "width": "stretch"
            },
            {
              "type": "Column",
              "items": [
              ],
              "width": "auto"
            }
          ]
        }
      ],
      "bleed": True
    },
    {
      "type": "Container",
      "items": [
        {
          "type": "ColumnSet",
          "columns": [
            {
              "type": "Column",
              "items": [
              ],
              "width": "stretch"
            },
            {
              "type": "Column",
              "items": [
                {
                  "type": "ActionSet",
                  "actions": [
                    {
                      "type": "Action.OpenUrl",
                      "title": "EXPORT AS PDF",
                      "url": "https://adaptivecards.io"
                    }
                  ]
                }
              ],
              "width": "auto"
            }
          ]
        },
        {
          "type": "FactSet",
          "spacing": "Medium",
          "facts": [
            {
              "title": "Relationship No: ",
              "value": "1144553"
            },
            {
              "title": "No. of connections:",
              "value": "xxxxxxxx90"
            },
            {
              "title": "Amount Due",
              "value": "100$"
            },
            {
              "title": "Due date",
              "value": "26/09/2020"
            },
            {
              "title": "Late payment fee:",
              "value": "10$"
            }
          ]
        }
      ]
    },

  ],
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.2",
  "fallbackText": "This card requires Adaptive Cards v1.2 support to be rendered properly."
}
