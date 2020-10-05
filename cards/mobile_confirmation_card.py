from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

def mobile_confirmation_card():
    card = ThumbnailCard(
                title="",
                text="Please confirm if you want to pay the bill now?",

                images=[CardImage(url="https://images.app.goo.gl/voWF7ZpTWzJocoUw5")],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="Confirm",
                        text="Confirm",
                        display_text="Confirm",
                        value="Confirm",
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