# ESWEB - An Eternal Sovereign DKP Website

## About the project

This project is for an EverQuest guild on the Bertoxxulous server.  Its goals are:

- Roster
- DKP System
- Integration with phpbb3
- API for use with our desktop app to assist in handling DKP

## Progress

I'm using this as a tool to learn Django programming and generally flex my mental muscles when I'm not working and being a sysadmin.  So, progress may be slow, or non-existent.

## Contributing

I welcome any contributions folks want to bring to the table.  I would love to make this generic and configurable so any guild could use it, and use our DKP system as wanted.  While there is already a great EQDKP project, it doesn't have the interface and rules flexibility we wanted.  Please fork and send me a pull request with your code.  I ask that you make sure all unit tests pass and that you don't skimp on writing your own tests as needed.

### Formatting

All python in this project is auto-formatted using `black` with a line length of 100.  If you use VSCode, you can configure that as follows in your `settings.json`:

```json
{
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "/usr/local/bin/black",
    "python.formatting.blackArgs": [
        "--line-length=100"
    ],
}
```

Adjust your `blackPath` as necessary.

## Requirements

I develop on a Mac, but this stuff should all work on any operating system that can run docker and docker-compose.

## Running tests

If you're using docker-compose for local development, the following commands should work out of the box

```sh
# Run the stack so mysql is available
docker-compose up -d

# Run the tests
docker-compose exec web bash -c 'python manage.py test'
```

The Django test framework tries to make a `test_esdkp` database, so MySQL is provided a startup script in `local-init.sql` that will add the needed permissions to the user specified in `localdev.env` so that Django's test framework can run.

## Seeding Fixture Data

EQ has a bunch of rarely changing data that I've made available to seed your database with as fixtures.

```sh
docker-compose exec web bash -c 'python manage.py loaddata classes events expansions races servers'
```

This should load:
- Classes
- Races
- Servers
- Expansions (through TOV)
- Raid Events (EOK, ROS, TBL, and TOV)

There are also some example item fixtures as well.  Add `items` to the above command to install those as well.

## Specification

So, what does this API need to do?  It will have two consumers, itself as an informational website, and the ESDKP desktop client.

### ESDKP Client Actions

The ESDKP client needs to able to do the following things as of the current version:

1. Retrieve DKP and Attendance for a player
2. Create a raid event
3. Pull a list of loot and their values
4. Load an existing raid event
5. Update an existing raid event
6. Generate a raid report (to be deprecated with the website)

Features that will need to be added to work with the new model layout:

1. Understanding the difference of an event and a raid - no more arbitrary event names.

Eventual features might include:

1. Knowing the context of a raid (expansion, specific event) to filter loot

We need to provide API endpoints to do the following

### Plan of action

To keep things simple, the ESDKP client will only interact with a few models - a full raid model, events, characters, and items.

In this way, we can keep the logic of segregating a "character" versus understanding a raid attendee, for example, without precluding adding more advanced logic at a future date.

In essence

### Planned API endpoints

#### `GET /raids/{id}`

`id` - an integer id of a specific raid event, optional

Returns a JSON representation of a raid including the raid details, attendees, and loots.  With no {id}, returns a list of known raids.

#### `POST /raids/{id}`

This endpoint expects JSON data for required `Raid` model attributes.

Will create a new raid if no `id` is given, otherwise will overwrite the details for the given raid id, if valid.

#### `GET /characters/{id}`

Returns a JSON representation of a specific character given an `id`, or returns a list of known characters.

#### `POST /characters/{id}`

Expects a JSON representation of a character as data, and will create a new character if no `id` is given, or update a character given a valid `id`.

#### `GET /items/{id}`

Returns a JSON representation of a specific item, given an `id`, or returns a list of known items.

#### `POST /items/{id}`

Expects a JSON representation of a character as data, and will create a new character if no `id` given, or update a character given a valid `id`

#### `GET /events/`

Returns a JSON list of known events.
