from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ThumbnailCard,
    ActionTypes,
)

def accountbalance_card():
    card = ThumbnailCard(
        title="Account Details",
        text="Please select an account to see last 10 transaction details",

        # images=[CardImage(url="https://www.iconfinder.com/data/icons/infographic-bar-16/512/17-512.png")],
        buttons=[
            CardAction(
                type=ActionTypes.im_back,
                title="Savings Account xxxxxxxxx4567 \n Opened date: 05/10/2010 \n Balance is $112.02",
                text="Balance is $112.02",
                display_text="Balance is $112.02",
                value="xxxxxxxxx4567",
            ),
            CardAction(
                type=ActionTypes.im_back,
                title="Current Account xxxxxxxxx4566 \n Opened date: 05/10/2012 \n Balance is $0.00",
                text="Balance is $0.00",
                display_text="Balance is $0.00",
                value="xxxxxxxxx4566",
            ),
        ],
    )

    return card