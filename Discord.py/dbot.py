import discord
from discord.ext import commands
import discordai

# config stores the sensitive data such as api keys
import config

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='!')


def call_openai(message: str, mention: str) -> str:
    return discordai.prompt(message, mention)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def nathan(ctx, message: int):
    try:
        msg_obj = await ctx.fetch_message(message)
        msg = msg_obj.content
        mention = msg_obj.author.mention
        print(mention)
        await ctx.send("Fixing, please wait...")    
        response = call_openai(msg, mention)
        await ctx.send(f'{response}')
    except discord.NotFound:
        await ctx.send("Must be a valid message ID from THIS channel!")
    except:
        await ctx.send("Something went wrong; make sure your message ID is correct, or reply to the message you would like to fix with '!fixthis'!")


@bot.command()
async def fixthis(ctx):
    try:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await ctx.send("Fixing, please wait...")
        response = call_openai(message.content, message.author.mention)
        await ctx.reply(response)
    except AttributeError:
        await ctx.send("Must reply to message you would like to fix!")
    except:
        await ctx.send("Something went wrong; try again, or type the command !nathan followed by the message ID of the message you would like to fix!")

if __name__ == "__main__":
    bot.run(config.bot_token)
