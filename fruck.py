from hikkatl.types import Message
from hikkatl import utils
from .. import loader
import time

@loader.tds
class FruckModule(loader.Module):
    """Fruck module"""

    def __init__(self):
        self.name = "FruckModule"
        self.all_commands = self.commands

    @loader.command
    async def fruck(self, message: Message):
        """
        Usage: .fruck @username or person's ID 10s
        Sends a delayed message and then deletes it after a specified delay.
        """
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, "Please provide a user mention or ID and a delay.")
            return

        try:
            user_input, delay_str = args.split(" ", 1)
            user_id = await utils.get_user_id(message.client, user_input)
            delay = float(delay_str[:-1])
        except ValueError:
            await utils.answer(message, "Invalid input format. Please use '.fruck @username or person's ID 10s'.")
            return

        initial_message = await utils.answer(message, f"Frucking {user_input} in {delay} seconds...")
        time.sleep(delay)

        await utils.delete_messages(message.client, message.chat_id, [initial_message.id])

        follow_up_message = f"You're a cool person {user_input}!"
        await utils.answer(message, follow_up_message)

# Optional: Add any additional commands or aliases
