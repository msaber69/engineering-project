// scoring_logic.js

function calculateAsrsScoreOld(responses) {
    const inattentiveItems = [1, 2, 3, 7, 8, 9, 10, 11];
    const hyperactiveMotorItems = [5, 6, 12, 13, 14];
    const hyperactiveVerbalItems = [15, 16, 17, 18];

    const inattentiveScore = calculateSubscaleScore(responses, inattentiveItems, 2);
    const hyperactiveMotorScore = calculateSubscaleScore(responses, hyperactiveMotorItems, 3);
    const hyperactiveVerbalScore = calculateSubscaleScore(responses, hyperactiveVerbalItems, 3);

    return {
        inattentiveScore,
        hyperactiveMotorScore,
        hyperactiveVerbalScore,
    };
}

function calculateSubscaleScore(responses, items, threshold) {
    return items.reduce((score, item) => score + (responses[item - 1] > threshold ? 1 : 0), 0);
}

function calculateAsrsScoreNew(responses) {
    const inattentionItems = [7, 8, 9, 1, 2, 4, 10, 11, 3];
    const hyperactivityItems = [5, 12, 13, 14, 6, 15, 16, 17, 18];

    const inattentionScore = calculateSubscaleScore(responses, inattentionItems, 3);
    const hyperactivityScore = calculateSubscaleScore(responses, hyperactivityItems, 3);

    return {
        inattentionScore,
        hyperactivityScore,
    };
}

function calculateDsm5Score(scale, responses) {
    const totalScore = responses.reduce((sum, response) => sum + response, 0);

    switch (scale) {
        case 'Depression':
        case 'Anger':
        case 'Anxiety':
        case 'SomaticSymptoms':
            return totalScore;
        case 'Mania':
            return totalScore >= 2 ? 1 : 0;
        case 'Suicidal':
        case 'Psychosis':
        case 'Dissociation':
        case 'SubstanceUse':
            return totalScore;
        default:
            return null;
    }
}

function calculateQidsSr16Score(responses) {
    const sleepItems = [1, 2, 3, 4];
    const appetiteWeightItems = [6, 7, 8, 9];
    const psychomotorItems = [15, 16];

    const sleepScore = Math.max(...sleepItems.map(item => responses[item - 1]));
    const appetiteWeightScore = Math.max(...appetiteWeightItems.map(item => responses[item - 1]));
    const psychomotorScore = Math.max(...psychomotorItems.map(item => responses[item - 1]));

    const totalScore = responses.reduce((sum, response) => sum + response, 0)
        - Math.min(...responses.slice(5, 14))
        + sleepScore + appetiteWeightScore + psychomotorScore;

    return totalScore;
}

module.exports = {
    calculateAsrsScoreOld,
    calculateAsrsScoreNew,
    calculateDsm5Score,
    calculateQidsSr16Score
};


// Example usage:
const asrsOldResponses = [2, 3, 4, 1, 0, 2, 1, 3, 4, 1, 0, 2, 3, 0, 1, 4, 0, 3];
const asrsNewResponses = [2, 3, 4, 1, 0, 2, 1, 3, 4, 1, 0, 2, 3, 0, 1, 4, 0, 3];
const dsm5DepressionResponses = [1, 2];
const qidsSr16Responses = [2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2];

const asrsOldScores = calculateAsrsScoreOld(asrsOldResponses);
const asrsNewScores = calculateAsrsScoreNew(asrsNewResponses);
const dsm5DepressionScore = calculateDsm5Score('Depression', dsm5DepressionResponses);
const qidsSr16Score = calculateQidsSr16Score(qidsSr16Responses);

console.log("ASRS Old Scores:", asrsOldScores);
console.log("ASRS New Scores:", asrsNewScores);
console.log("DSM-5 Depression Score:", dsm5DepressionScore);
console.log("QIDS-SR16 Score:", qidsSr16Score);
