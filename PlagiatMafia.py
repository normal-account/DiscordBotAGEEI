import discord

TOKEN = 'YOUR_TOKEN_HERE'


client = discord.Client(self_client=True)


def prepare_embed(permalink, user, reporter, content):
    embed = discord.Embed(title="Nouveau message signalé")
    embed.add_field(name="Lien du message", value=permalink, inline=False)
    embed.add_field(name="Auteur du message", value=user, inline=False)
    embed.add_field(name="Utilisateur ayant signalé le message", value=reporter, inline=False)
    embed.add_field(name="Contenu du message", value=content, inline=False)
    return embed


@client.event
async def on_raw_reaction_add(reaction):
    guild_id = reaction.guild_id
    guild = client.get_guild(guild_id)
    member = guild.get_member(reaction.user_id)
    channel = client.get_channel(reaction.channel_id)
    msg = await channel.fetch_message(reaction.message_id)
    try:
        if str(reaction.emoji.id) == "963093427388579890":
                    user = await client.fetch_user(reaction.user_id)
                    await msg.remove_reaction(reaction.emoji, user)
                    ### The 2 following lines are server and channel specific !!!
                    REVIEWchannel = client.get_channel(962858870676521020)
                    await REVIEWchannel.send(embed=prepare_embed("https://discord.com/channels/755106635885838477/" + str(msg.channel.id) + "/" + str(msg.id), msg.author, user, msg.content))
                    await user.send("Le message en question a bien été signalé aux modérateurs du serveur. Merci pour votre aide.")

    except discord.errors.Forbidden as e:
        print("You didn't give me enough permissions : " + e)
    except discord.errors.NotFound as e:
        print("I'm getting a 404 error : " + e)
    except discord.errors.InvalidData as e:
        print(e)
    except discord.errors.InvalidArgument as e:
        print(e)
    except discord.errors.ConnectionClosed as e:
        print(e)
    except discord.errors.HTTPException as e:
        print(e)
    except discord.errors.DiscordException as e:
        print(e)
print("Bot has been started.")
client.run(TOKEN)
