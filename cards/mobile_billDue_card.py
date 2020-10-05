from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

def mobile_billDue_card():
    card = ThumbnailCard(
        title="Bill Payment Reminder",
        text="Hey Steve, I found your Vodafone post paid bill for XXXXXXXX90 which is due in next 2 days.\n\n Would you like to pay it now?",

        images=[CardImage(url="https://images.app.goo.gl/voWF7ZpTWzJocoUw5")],
        buttons=[
            CardAction(
                type=ActionTypes.im_back,
                title="Yes",
                text="Yes",
                display_text="Yes",
                value="Yes, pay my mobile bill",
            ),
            CardAction(
                type=ActionTypes.im_back,
                title="No",
                text="No",
                display_text="No",
                value="No not now.",
            ),
        ],
    )
    return card