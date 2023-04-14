from os import environ
class Config(object):
    API_ID = environ.get("API_ID", None)
    API_HASH = environ.get("API_HASH", None)
    BOT_TOKEN = environ.get("BOT_TOKEN", "2089413356:AAGs97YYJvzoTCM20k6HqyT4qKP9r0nNZyw")
    STRING_SESSION = environ.get("STRING", "1BVtsOIMBu8CvA-FQ76T3oFeBLAd-Vz4YhH_hL-9xhRXxHIfJqqBvB2Eti7KxMAYX3OX-pFFvM4lbgXBBLMzAyQeLeccgAdNghYRq3-63ZrDQunxat0xJGqvP8vSHdSeOOHZovMCbPtqzX5ZWdh0zbL6_RrraXC1WhjxBtlIj4cIG_6ek65Pdy298xsBvL3-1Gexqq4qt4mj_7YfkrKJpX-EReKHDtVWRP--0WU30OnFkB8lxQ89lBLmHYMoWX5ckYVKf6rpTPMbSusKhKPpPgPk2uYVVFRUpzxthdvRDsV-53SswRxH0U0t6krUuVCYwc9EYwwksU_o216sxHSILUwG8Tu-fqj0=")
    SUDO_USERS = environ.get("SUDO_USERS", "1908563535")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
