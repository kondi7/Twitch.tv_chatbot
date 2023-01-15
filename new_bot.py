from twitchio.ext import commands
from params import settings
from keyboard import is_pressed
import asyncio
import random


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=settings.TOKEN,
            prefix='!',
            initial_channels=[settings.CHANNEL]
        )

    # Bot upon joining the channel prints bot's nickname and user_id
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        self.loop.create_task(self.hotkey_task())  # Needed to check if button is pressed

    @commands.command()
    # Bot sends message to the chat upon calling the !custom_command2
    async def custom_command2(self, ctx: commands.Context):
        random_number1 = random.randint(0, 50)
        if 0 <= random_number1 < 15:
            await ctx.send(f'message {random_number1} {ctx.author.name} ')
        else:
            await ctx.send(f'message {random_number1} {ctx.author.name} ')

    @commands.command()
    # Bot sends message to the chat upon calling the !custom_command
    async def custom_command(self, ctx: commands.Context):
        random_number = random.randint(0, 200)
        if random_number < 50:
            await ctx.send(f'message {random_number}% {ctx.author.name}')
        elif 50 < random_number < 100:
            await ctx.send(f'message {random_number}% {ctx.author.name}')
        elif random_number == 200:
            await ctx.send(f'message {random_number}% {ctx.author.name}')
        else:
            await ctx.send(f'message {random_number}% {ctx.author.name}')

    @commands.command()
    #Bot sends message to the chat upon calling the !custom_command1
    async def custom_command1(self, ctx: commands.Context):
        await ctx.send(f'message {ctx.author.name} ')

    # Bot sends custom message to the chat upon pressing certain button
    async def hotkey_task(self):
        message = self.get_channel(settings.CHANNEL).send
        while True:
            if is_pressed('F7'):
                await message("message")
            elif is_pressed('F11'):
                await message("message")
            elif is_pressed('F10'):
                await message("message")
            elif is_pressed('F9'):
                await message("message")
            elif is_pressed('F8'):
                await message("message")
            await asyncio.sleep(0.1)


# Run the bot
bot = Bot()
bot.run()
