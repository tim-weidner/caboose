@command("help", man = "Displays list of commands. Usage: {leader}{command}")
def help(bot, line):
    line.conn.privmsg(line.args[0], "Available commands: {}".format(", ".join(key for key 
        in bot.COMMANDS if (key != "__builtins__" and bot.COMMANDS[key].visible))))
    #Add functionality to display ** after command if it's disabled (footnote after explaining so)