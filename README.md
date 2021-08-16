# bebbot

A discord bot for World of Warships utility commands, written in Python. 

## Commands List

| Command                                   | Usage
| ----------------------------------------- | --------------------------------------------------------------------- |
| .help                                     | displays the available command list                                   |
| .ct [clan] [ship]                         | displays the top performers of the specified ship in the clan         |
| .pr [ship] [damage] [frags] [winrate]     | calculates the PR for the specified ship with the given results       |
| .ballistics [ship]                        | displays a ballistics graph of a ships AP performance                 |
| .history [ship]                           | displays a graph of a player's stat history for a specific ship       |
| .leaderboard [ship]                       | displays the top 10 leaderboard of a specified ship                   |

## How to set up

Create a `config.json` file with the following variables:

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| bot_prefix                | The prefix(es) of the bot                                             |
| token                     | The discord token of the bot                                          |
| application_id            | The discord application ID of the bot                                 |
| wgdev_id                  | The WG developer application ID                                       |
| db_pass                   | The MariaDB root password                                             |
| owners                    | The user ID of all the bot owners                                     |


## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows)
.

Before running the bot you will need to install all the requirements with this command:

```
pip install -r requirements.txt
```

Use the following command to start the bot:

```
python3 bot.py
```

## Issues or Questions

If you have any issues or questions, you can contact @beb#1789.

## Built With

* [Python 3.9](https://www.python.org/)
