// Anything that is written after a double front slash is a comment.
// A comment is a line that is ignored when running the script.
// comments are useful for explaining your code to others and
// more importantly, your future self.

// writing comments is a good habit because it helps you understand your
// own code better.
// you will see comments widely used in this guide, to explain almost
// every bit of code that you see

// do note though, that even though commenting is a good practise,
// over commenting code is a worse thing to do. Only comment stuff
// that really needs commenting!

/* Anything enclosed by a front slash
and asterisk pair is a
multi line comment */

// // Here, you are creating a function that is called 'main'.
// void main() {
//     // this line says that you have an integer called 'a' that has a value of 10.
//     // note that almost every statement in XS is ended with a semi colon,
//     // just like in english we use periods to indicate the end of a sentence.
//     int a = 10;
//     int b = 20;

//     // this line says that you make a new integer called 'c' and it is the sum of 'a' and 'b'.
//     int c = a+b;

//     // this line will show in the game chat the value of 'c'. This shows '30' in chat.
//     xsChatData(""+c);
// }


// void custom_func1(){
//     int a = 10;
//     int b = 40;

//     // this line says that you make a new integer called 'c' and it is the sum of 'a' and 'b'.
//     int c = a+b;

//     // this line will show in the game chat the value of 'c'. This shows '30' in chat.
//     xsChatData(""+c);  
// }

// Global Variables
int heroUnitID = -1;  // Store Hero's ID
int spawnX = 50;
int spawnY = 50;  // Define spawn location

// Function to spawn the hero
void spawnHero() {
    int playerID = 1; // Player 1
    int heroType = 90; // Example: William Wallace (Replace with correct hero ID)

    // Spawn the hero at the defined coordinates
    heroUnitID = xsCreateObject(playerID, heroType, spawnX, spawnY, 0);
    
    // Announce to the player
    xsChatMessage(playerID, "A hero has appeared!");

    // Start monitoring the hero's status
    xsEnableRule("checkHeroDeath");
}

// Function to check if the hero is dead
void checkHeroDeath() {
    if (xsGetUnitHP(heroUnitID) <= 0) {
        xsChatMessage(1, "Your hero has fallen! Respawning in 2 minutes...");

        // Disable this rule until the hero respawns
        xsDisableRule("checkHeroDeath");

        // Schedule respawn after 2 minutes (120 seconds)
        xsScheduleFunction("spawnHero", 120);
    }
}

// Main function (called when the game starts)
void main() {
    // Initial hero spawn
    spawnHero();
}
