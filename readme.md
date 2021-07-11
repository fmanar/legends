# Legends

## Random Legend Picker

### Randomly choose legends to keep things fresh.
<br/>
This script chooses random legends for a whole squad. Player names can be
supplied as command line arguments, and legends will be matched to them.

Invocation:

    $ python legends.py [PLAYER]...

Examples:
    Without arguments the script picks three legends:

        $ python legends.py
        Random legends! Loba! Horizon! Octane!
        
With arguments the script picks legends for each player supplied:

        $ python legends.py Frodo Sam
        Random legends!
        Frodo plays Mirage!
        Sam plays Gibraltar!

### Notes:
If Skyler is playing, Crypto is removed from the legend pool. 
