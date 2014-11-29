Sublime Text Day/Night Theme Changing
=======================

I got bored and made this to learn the Sublime API. Works with Windows, Linux, and OSX... hopefully. The idea of this is nobody likes being blinded in the middle of the night with some bright theme. This just makes it quicker to change between them. Yes I'm that lazy.

### Shortcuts ###
`ALT + SHIFT + N` will set the theme to the selected night theme.  
`ALT + SHIFT + D` will set the theme to the selected day theme.

### Automatic Changing ###
(There will be an option to disable once I am more bored)  

Checks hour every 60 seconds, if between 8PM and 6AM it'll use night theme otherwise it'll use day theme. If you change the theme manually using Sublime's builtin change; the system will ignore and won't change it. Once a better option is added it will overwrite only when enabled.

### Installing ###
Drop files of zip (this repo) into a folder called "NightDay" in your SL 2/3 Packages folder.

### Options ###
"night" - Set the path from root sublime app data directory to the theme (e.g: Packages/MyThemes/HelloKitty.tmTheme)  
"day" - Same as above but for a lighter/brighter theme.

### ToDo ###
- Better settings
- Override ability
