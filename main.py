from pyrogram import Client, filters


API_ID = "18401114"
API_HASH = "e9105cffc9ef49b4011dfeb843acb091"
BOT_TOKEN = "5691494843:AAF_iYfZHfFTZToJn2hU33Ywc-N9yTllu1w"


SIJITH = Client(
    name="filetolinkbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("Bot Was Started")


SIJITH.run()
