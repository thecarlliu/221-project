const eloCalc = {
    calculateSingle: function(playerData) {

    },
    calculateMultiple: function(listOfPlayerData) {

    }
};

const queueGenerator = {
    createQueue: function() {
        
    }
};

//A single player should have the following data which is a simplified representation of the data needed when a player queues up for a match and what gets affected post-match:
examplePlayer = {
    name: "", //the player's in-game name
    currentRank: "", //the player's rank this season
    lastSeasonRank: "", //the player's rank last season
    overallWR: "", //the player's overall winrate percentage
    currentMMR: "", //determined by the eloCalc,
    currentGain: "", //how much elo a player gains when a match is won, determined by eloCalc
    currentLoss: "", //how much elo a player loses when a match is lost, determined by eloCalc
    rolePreference: [], //list of roles that the player prefers to play
    matchHistory: [] //array of objects, each object representing a match
};