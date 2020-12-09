## Personal remix

This is an experiment in rearranging the syntax highlight colors in the built-in Dark+ theme according to personal taste and supplementing it with some additional colors while preserving the general subdued feel. No guarantees are made about quality, support or anything else about this extension.  

## Three themes in a trenchcoat

The interface colors only receive a couple of tweaks (the status bar, the current line highlight), almost all of the remixing applies to the syntax highlighting in the editor.

The basic foreground/background are kept from the Dark+ itself and then the syntax colors are supplemented by colors from other subdued looking themes and arranged according to my own conceptions about what should be which kind of color. 

One variant takes all common semantic colors from the Nord theme, and another mixes semantic colors from Dark+ with a number of colors from One Dark theme. Both variants also use a few colors from the Solarized theme for less common stuff like annotations. The One Dark variant is reasonably subdued, and the Nord variant is extra pale, possibly too pale. The example image shows the Nord variant.

![Example (Nord Variant)](https://raw.githubusercontent.com/daydev/vscode-dark-remix/master/screen-nord.png)

## Color Specification

Not a strict technical specification, but a general idea of what kinds of color go where with their placeholder IDs as used in the theme template:

- Text and local variables: offwhite (#white)
- Background: offblack (#black)
- Hints and invisible characters: dark grey (#grey-)
- Punctuation and operators: light grey (#grey+)
- Keywords: #violet
- Constants (except strings): magenta (#magenta)
- Strings: #cyan
- String inserts (interpolation, escape): #teal
- Functions and tags: #yellow
- Parameters, options and attributes: pale red (#red)
- Built-ins and predefs: #orange
- Comments and docstrings: medium grey (#grey)
- Annotations and decorators: #olive 
- Classes and types: light green (#green)
- Fields and properties: dark blue (#blue)

### Terminal colors

The above doesn't quite fit into the 16 terminal colors, so some colors are not used and a few others are added just for the terminal:

1. Black: #black
2. Black bright: #grey-
3. White: #white
4. White bright: brighter white (#white+)
5. Red: #red
6. Red bright: brighter red (#red+)
7. Blue: #blue
8. Blue bright: brighter blue (#blue+)
9. Green: #green
10. Green bright: brighter green (#green+)
11. Yellow: #yellow
12. Yellow bright: #olive
13. Cyan: #teal
14. Cyan bright: #cyan
15. Magenta: #violet
16. Magenta bright: #magenta


## Actual Colors

### Nord Variant


- #black: #1e1e1e from Dark+, 
- #white: #d4d4d4 from Dark+,
- #white+: #fdf6e3 from Solarized,
- #grey: #4c566a from Nord,
- #grey-: #2e3440 from Nord,
- #grey+: #93A1A1 from Solarized,
- #red: #bf616a from Nord,
- #red+: #dc322f from Solarized,
- #green: #a3be8c from Nord,
- #green+: #50fa7b from Dracula,
- #blue: #5e81ac from Nord,
- #blue+: #268bd2 from Solarized,
- #orange: #d08770 from Nord,
- #olive: #859900 from Solarized,
- #yellow: #ebcb8b from Nord,
- #teal: #2aa198 from Solarized,
- #cyan: #88c0d0 from Nord,
- #violet: #b48ead from Nord,
- #magenta: #d33682 from Solarized

### One Dark Variant

- #black: #1e1e1e from Dark+,
- #white: #d4d4d4 from Dark+,
- #white+: #fdf6e3 from Solarized,
- #grey: #7F848E from One Dark,
- #grey-: #002b36 from Solarized,
- #grey+: #93A1A1 from Solarized,
- #red: #E06C75 from One Dark,
- #red+: #dc322f from Solarized,
- #green: #98C379 from One Dark,
- #green+: #50fa7b from Dracula,
- #blue: #569CD6 from Dark+,
- #blue+: #268bd2 from Solarized,
- #orange: #CE9178 from Dark+,
- #olive: #859900 from Solarized,
- #yellow: #e5c07b from One Dark,
- #teal: #2aa198 from Solarized,
- #cyan: #9CDCFE from Dark+,
- #violet: #C586C0 from Dark+,
- #magenta: #d33682 from Solarized

## References

- [Nord Theme for VS Code](https://github.com/arcticicestudio/nord-visual-studio-code)
- [One Dark Pro Theme for VS Code](https://github.com/Binaryify/OneDark-Pro)
- [Solarized Color Palette](https://ethanschoonover.com/solarized/)
- [Dracula Theme for VS Code](https://github.com/dracula/visual-studio-code)