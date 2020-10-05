from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

def billPaymentConfirmation_card():
    card = ThumbnailCard(
        title="Payment Confirmation",
        text="Please confirm bill payment of 100$ to VodafoneIdea ?",

        images=[CardImage(url="https://images.app.goo.gl/voWF7ZpTWzJocoUw5")],
        buttons=[
            CardAction(
                type=ActionTypes.im_back,
                title="Confirm",
                text="Confirm",
                display_text="Confirm",
                value="Confirmed pay 100$ to VodafoneIdea",
            ),
            CardAction(
                type=ActionTypes.im_back,
                title="Cancel",
                text="Cancel",
                display_text="Cancel",
                value="Cancel",
            ),
        ],
    )

    return  card