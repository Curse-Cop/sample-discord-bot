# Curse Cop Sample Discord Bot

## Getting Started
1. To start using this Discord bot, you first must create an account at Curse Cop and purchase at least the Mini Package [Sign Up Here](https://cursecop.davidcromptonapps.com/client-signup/)
2. Clone/Download this repository
3. Login To [Discord Developer](https://discord.com/login?redirect_to=/developers) and create a new Application
4. Under the Settings options select the Bot option, create a bot user for your newly created application and copy the Token provided
5. Open Settings.py and replace the variables `CuseCopUsername` with your Curse Cop Email Address, `CurseCopPassword` Curse Cop Password and `DiscordBotToken` with your Discord Bot Token from the previous step
6. Download the requirements for the repository using the following command
```
pip3 install -r requirements.txt
```
7. Once the required packaged are installed, start the bot using the command  ```python3 -m main```
8. Invite the Discord Bot to your server using this link to generate [this URL](https://discordapi.com/permissions.html#8192) with the correct permissions 