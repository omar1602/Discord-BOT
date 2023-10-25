from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 487341179688583202  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

# Exo 1
@bot.command()
async def name(ctx):
    user_name = ctx.author.name
    await ctx.send(f"Ton Blaze : {user_name}")

# Exo 2
@bot.command()
async def d6(ctx):
    random_value = random.randint(1, 6)
    await ctx.send(f'Tentes ta chance chef : {random_value}')

# Exo 3
@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul")
        await message.channel.send(f"{message.author.mention}")

# Exo 4
@bot.command()
async def admin(ctx, member: discord.Member):
    admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
    if not admin_role:
        admin_role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions.all())

    await member.add_roles(admin_role)
    await ctx.send(f"{member.mention} is now an Admin!")

# Exo 5
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=""):
    if not reason:
        funny_catchphrases = [
            "Juste comme ça.",
            "Pas de raison.",
            "Blagues racistes.",
            ".",
            "J'ai oublié pourquoi.",
        ]
        reason = random.choice(funny_catchphrases)

    await ctx.guild.ban(member, reason=reason)
    await ctx.send(f"{member.mention} dehors pour la raison suivante : {reason}")

# Exo 6
@bot.command()
async def xkcd(ctx):
    response = requests.get("https://xkcd.com/info.0.json")
    response = requests.get("https://xkcd.com")
    if response.status_code == 200:
        comic_data = response.json()
        comic_url = comic_data["img"]
        comic_alt_text = comic_data["alt"]
        await ctx.send(f"Voici un comic XKCD aléatoire ;) {comic_url}")
        await ctx.send(f"Texte  : {comic_alt_text}")
    else:
        await ctx.send("Sorry Broski, y'a rien à gratter ici")

token = ""
bot.run(token)  # Starts the bot