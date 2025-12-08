---
domain: scripting
concept: collections
version: 1.14+
requires: [scopes, triggers_core]
relates: [effects, triggers_specialized, script_concepts]
---

# Collections

Collections are iterable sets of scoped objects (countries, states, characters, MIOs, etc.) used in triggers/effects and scripted localization.

## Inputs

- Built-ins: `game:all_countries`, `game:all_possible_countries`, `game:all_states`, `game:scope` (current scope), plus DLC/system-specific sets.
- Named collections: Define reusable sets in script; keep naming consistent and documented.
- Constants: Use to seed collections for deterministic iteration; avoid mixing incompatible scope types.

## Operators

- `collection_size`: Returns count of elements.
- `every_collection_element`: Iterates collection; use `limit` to filter during iteration.
- Common operators: `faction_members`, `owned_states`, `controlled_states`, `country_and_all_subjects`, `all_mios`, etc.
- Localization behavior: Iteration order is deterministic; avoid relying on implicit ordering for UI text.

## Usage Tips

- Scope safety: Ensure collection element scope matches the consuming trigger/effect.
- Performance: Filter early (`limit`) and keep collections small where possible.
- Debugging: Combine with `effect_docs`/`trigger_docs` to validate collection contents during development.

## Referencing Collections

To reference a collection, simply write its name in the form `prefix:name`,
like in the following example:

```
some_property = game:all_countries # All countries in the game!
```

## Creating Collections

To create a new collection, pick a unique name and put the following script in any
script file in "common/collections":

```
my_awesome_collection = {

	input = prefix:another_collection # A reference to another collection that will be used as input

	limit = {
		# Optional
		#
		# A trigger that can be used to make the new collection only contain elements of the input
		# that match certain criteria.
		#
		# SCOPE = element of the input collection
		# PREV = previous scope, defined by the context in which the collection is used
		# ROOT = PREV.ROOT
		# FROM = PREV.FROM
		#
		# NOTE : the scope structure above mimics the scope structure of other every_xxx effects
	}
}
```

To reference the newly created collection in script, use the *collection:* prefix:

```
some_property = collection:my_awesome_collection
```

## Anonymous Collections

Collections can be defined directly in the place where they are used. Such collections
are called *anonymous*, because they have no name and therefore cannot be referenced
elsewhere.

The syntax used to define an anonymous collection is the same that is used to define
a named collection, except for the fact that anonymous collections can occur anywhere
in script, where a collection reference is expected.

```
some_property = {
	# The scripting of the collection goes here (see above for the detailed info)
}
```

## Built-In Collections

There is a variety of collections that are already built into the game. These built-in
collections can be used directly in script, or serve as inputs when creating other collections.

### game:

Scope: ANY

- *game:empty* - an empty collection
- *game:all_countries* - all currently existing countries in the game
- *game:all_possible_countries* - all possible countries in the game
- *game:all_states* - all states in the game

### country:

Scope: COUNTRY

- *country:faction_members* - all members of the country's faction if any, otherwise - empty collection

## Triggers and Effects

### List of Collection-Related Triggers

- *collection_size* - compares size of a collection with a number or a variable

### List of Collection-Related Effects

- *every_collection_element* - iterates over elements of a collection and applies effects to every element
