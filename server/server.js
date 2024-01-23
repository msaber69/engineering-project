const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const {
    calculateAsrsScoreOld,
    calculateAsrsScoreNew,
    calculateDsm5Score,
    calculateQidsSr16Score
} = require('./scoring_logic');

const app = express();
const port = 3001;

app.use(cors());
app.use(bodyParser.json());

app.post('/submitTest', (req, res) => {
    const testType = req.body.testType;
    const responses = req.body.responses;

    let result;

    switch (testType) {
        case 'asrs_old':
            result = calculateAsrsScoreOld(responses);
            break;
        case 'asrs_new':
            result = calculateAsrsScoreNew(responses);
            break;
        case 'dsm5':
            result = calculateDsm5Score(responses);
            break;
        case 'qids_sr16':
            result = calculateQidsSr16Score(responses);
            break;
        case 'test1':
            // Mock response for testing purposes
            result = { test1Score: 42 };
            break;
        default:
            result = { error: 'Invalid test type' };
    }

    res.json({ result });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
