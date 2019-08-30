# Corrections

Determine corrections to be made in a section of text, given a user's context.

Each word within a given piece of text will be compared against a users context using the [Jaro-Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) and where an error is determined, the word will be replaced with the proper word as given by the context. 
