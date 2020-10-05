from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

def intro_card():
    card = HeroCard(
        title="Welcome Steve!",
        text="Hope you are doing good. How can we help you today. Let's start with one of the options from below.",

        images=[CardImage(
            url="http://bsmedia.business-standard.com/_media/bs/img/article/2015-08/28/full/1440706704-1419.jpg")],
        buttons=[
            CardAction(
                type=ActionTypes.im_back,
                title="Account",
                text="Account Balance",
                display_text="Account",
                value="Account Balance",
            ),
            CardAction(
                type=ActionTypes.im_back,
                title="Credit Card",
                text="Credit Card",
                display_text="Credit Card",
                value="Credit Card",
            ),

            CardAction(
                type=ActionTypes.im_back,
                title="Service Requests",
                text="Service Requests",
                display_text="Service Requests",
                value="Service Requests",
            ),
        ],
    )

    return card

